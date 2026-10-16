---
tags:
  - Windows
  - Memory Imaging
---
> This article was copied from the Rekall Forensics blog, posted by
> [Michael Cohen](michael_cohen.md) on 2014-03-10.
> Copied with permission for historical preservation.

## How to stop memory acquisition by changing one byte

In a recent paper \[published at DFRWS 2013], we
examined memory acquisition in details and tested a bunch of tools.
Memory acquisition tools have to achieve two tasks to be useful:

1. They need to be able to map a region of physical memory into the virtual
   address space, so it can be read by the tool.
2. They need to know where in the physical address space it is safe to
   read. Reading a DMA mapped region will typically crash the system
   (BSOD).

Since PCI devices are able to map DMA buffers into the physical address
space, it is not safe to read these buffers. When a read operation
occurs on the memory bus for these addresses, the device might become
activated and cause a system crash or worse. The memory acquisition tool
needs to be able to avoid these DMA mapped regions in order to safely
acquire the memory.

Let us see what occurs when one loads the memory acquisition driver.
Since our goal is to play around with memory modification, we will
enable write support for the winpmem acquisition tool (This example uses
a Windows 7 AMD64 VM):

In [2]:

```cmd
!c:/Users/mic/winpmem_write_1.5.5.exe -l -w
```

```text
Enabling write mode.
Driver Unloaded.
Loaded Driver C:\Users\mic\AppData\Local\Temp\pmeE820.tmp.
Write mode enabled! Hope you know what you are doing.
CR3: 0x0000187000
 2 memory ranges:
Start 0x00001000 - Length 0x0009E000
Start 0x00100000 - Length 0x7CEF0000
Acquisition mode PTE Remapping
```

We see that winpmem extracts its driver to a temporary location, and
loads it into the kernel. It then reports the value of the Control
Register CR3 (This is the kernel's Directory Table Base - or DTB).

Next we see that the driver is reporting the ranges of physical memory
available on this system. There are two ranges on this system with a gap
in between. To understand why this is let's consider the boot process:

* When the system boots, the BIOS configures the initial physical memory
  map. The RAM in the system is literally installed at various ranges in
  the physical address space by the BIOS.
* The operating system is booted in Real mode, at which point a BIOS
  service interrupt is issued to query this physical memory configuration.
  It is only possible to issue this interrupt in Real mode.
* During the OS boot sequence, the processor is switched to protected mode
  and the operating system continues booting.
* The OS configures PCI devices by talking to the PCI controller and
  mapping each PCI device's DMA buffer (plug and play) into one of the
  gaps in the physical address space. Note that these gaps may not
  actually be backed by any RAM chips at all (which means that a write to
  that location will simply not stick - reading it back will produce 0).

The important thing to take from this is that the physical memory
configuration is done by the machine BIOS on its own (independent of the
running operating system). The OS kernel needs to live with whatever
configuration the hardware boots with. The hardware will typically
install some gaps in the physical address range so that PCI devices can
be mapped inside them (Some PCI devices can only address 4GB so there
must be sufficient space in the lower 4GB of physical address space for
these.).

Since the operating system can only query the physical memory map when
running in real mode, but needs to use it to configure PCI devices while
running in protected mode, there must be a data structure somewhere
which keeps this information around. When WinPmem queries for this
information, it can not be retrieved directly from the BIOS - since the
machine is already running in protected mode.

The usual way to get the physical memory ranges is to
call **MmGetPhysicalMemoryRanges()**. This is the function API:

**PPHYSICAL_MEMORY_DESCRIPTOR NTAPI MmGetPhysicalMemoryRanges(VOID);**

We can get Rekall to disassemble this function for us. First we
initialize the notebook, opening the winpmem driver to analyze the live
system. Since Rekall uses exact profiles generated from accurate
debugging information for the running system, it can resolve all
debugging symbols directly. We therefore can simply disassemble the
function by name:

In [2]:

```text
from rekall import interactive
interactive.ImportEnvironment(filename=r"\\.\pmem")
```

```text
Initializing Rekall session.
Done!
```

In [3]:

```text
dis "nt!MmGetPhysicalMemoryRanges"
```

```text
   Address      Rel Op Codes             Instruction                    Comment
-------------- ---- -------------------- ------------------------------ -------
------ nt!MmGetPhysicalMemoryRanges ------
0xf80002cd9690    0 488bc4               MOV RAX, RSP
0xf80002cd9693    3 48895808             MOV [RAX+0x8], RBX
0xf80002cd9697    7 48896810             MOV [RAX+0x10], RBP
0xf80002cd969b    B 48897018             MOV [RAX+0x18], RSI
0xf80002cd969f    F 48897820             MOV [RAX+0x20], RDI
0xf80002cd96a3   13 4154                 PUSH R12
0xf80002cd96a5   15 4155                 PUSH R13
0xf80002cd96a7   17 4157                 PUSH R15
0xf80002cd96a9   19 4883ec20             SUB RSP, 0x20
0xf80002cd96ad   1D 65488b1c2588010000   MOV RBX, [GS:0x188]
0xf80002cd96b6   26 41bf11000000         MOV R15D, 0x11
0xf80002cd96bc   2C 4533e4               XOR R12D, R12D
0xf80002cd96bf   2F f6835904000020       TEST BYTE [RBX+0x459], 0x20
0xf80002cd96c6   36 458d6ff0             LEA R13D, [R15-0x10]
0xf80002cd96ca   3A 7405                 JZ 0xf80002cd96d1              nt!MmGetPhysicalMemoryRanges + 0x41
0xf80002cd96cc   3C 418bfc               MOV EDI, R12D
0xf80002cd96cf   3F eb2a                 JMP 0xf80002cd96fb             nt!MmGetPhysicalMemoryRanges + 0x6B
0xf80002cd96d1   41 66ff8bc6010000       DEC WORD [RBX+0x1c6]
0xf80002cd96d8   48 33c0                 XOR EAX, EAX
0xf80002cd96da   4A f04c0fb13de5e4dcff   LOCK CMPXCHG [RIP-0x231b1b], R15 0x0 nt!MmDynamicMemoryLock
0xf80002cd96e3   53 740c                 JZ 0xf80002cd96f1              nt!MmGetPhysicalMemoryRanges + 0x61
0xf80002cd96e5   55 488d0ddce4dcff       LEA RCX, [RIP-0x231b24]        0x0 nt!MmDynamicMemoryLock
0xf80002cd96ec   5C e83f00c3ff           CALL 0xf80002909730            nt!ExfAcquirePushLockShared
0xf80002cd96f1   61 808b5904000020       OR BYTE [RBX+0x459], 0x20
0xf80002cd96f8   68 418bfd               MOV EDI, R13D
0xf80002cd96fb   6B 488b053679e3ff       MOV RAX, [RIP-0x1c86ca]        0xFFFFFA8001793FD0 nt!MmPhysicalMemoryBlock
0xf80002cd9702   72 33c9                 XOR ECX, ECX
0xf80002cd9704   74 41b84d6d5068         MOV R8D, 0x68506d4d
0xf80002cd970a   7A 8b10                 MOV EDX, [RAX]
0xf80002cd970c   7C 4103d5               ADD EDX, R13D
0xf80002cd970f   7F c1e204               SHL EDX, 0x4
0xf80002cd9712   82 e8f944d3ff           CALL 0xf80002a0dc10            nt!ExAllocatePoolWithTag
0xf80002cd9717   87 488be8               MOV RBP, RAX
0xf80002cd971a   8A 493bc4               CMP RAX, R12
0xf80002cd971d   8D 7545                 JNZ 0xf80002cd9764             nt!MmGetPhysicalMemoryRanges + 0xD4
0xf80002cd971f   8F 413bfd               CMP EDI, R13D
0xf80002cd9722   92 7539                 JNZ 0xf80002cd975d             nt!MmGetPhysicalMemoryRanges + 0xCD
0xf80002cd9724   94 498bc7               MOV RAX, R15
0xf80002cd9727   97 f04c0fb12598e4dcff   LOCK CMPXCHG [RIP-0x231b68], R12 0x0 nt!MmDynamicMemoryLock
0xf80002cd9730   A0 740c                 JZ 0xf80002cd973e              nt!MmGetPhysicalMemoryRanges + 0xAE
0xf80002cd9732   A2 488d0d8fe4dcff       LEA RCX, [RIP-0x231b71]        0x0 nt!MmDynamicMemoryLock
0xf80002cd9739   A9 e80655bfff           CALL 0xf800028cec44            nt!ExfReleasePushLockShared
0xf80002cd973e   AE 80a359040000df       AND BYTE [RBX+0x459], 0xdf
0xf80002cd9745   B5 664401abc6010000     ADD [RBX+0x1c6], R13W
0xf80002cd974d   BD 750e                 JNZ 0xf80002cd975d             nt!MmGetPhysicalMemoryRanges + 0xCD
0xf80002cd974f   BF 488d4350             LEA RAX, [RBX+0x50]
```

Note that Rekall is able to resolve the addresses back to the symbol
names by using debugging information. This makes reading the disassembly
much easier. We can see that this function essentially copies the data
referred to from the symbol **nt!MmPhysicalMemoryBlock** into user
space.

Lets dump this memory:

In [8]:

```text
dump "nt!MmPhysicalMemoryBlock", rows=2
```

```text
    Offset                           Hex                              Data       Comment
-------------- ------------------------------------------------ ---------------- -------
0xf80002b11038 d0 3f 79 01 80 fa ff ff 01 00 01 00 fe 3d 09 a1  .?y..........=.. nt!MmPhysicalMemoryBlock + 0
0xf80002b11048 a0 a8 83 01 80 fa ff ff 70 6a 7b 01 80 fa ff ff  ........pj{..... nt!IoFileObjectType + 0
```

This appears to be an address, lets dump it:

In [10]:

```text
dump 0xfa8001793fd0, rows=4
```

```text
    Offset                           Hex                              Data       Comment
-------------- ------------------------------------------------ ---------------- -------
0xfa8001793fd0 02 00 00 00 00 00 00 00 8e cf 07 00 00 00 00 00  ................
0xfa8001793fe0 01 00 00 00 00 00 00 00 9e 00 00 00 00 00 00 00  ................
0xfa8001793ff0 00 01 00 00 00 00 00 00 f0 ce 07 00 00 00 00 00  ................
0xfa8001794000 fe ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff  ................
```

The data at this location contains a struct of
type **_PHYSICAL_MEMORY_DESCRIPTOR** which is also the return value
from the **MmGetPhysicalMemoryRanges()**call. We can use Rekall to
simply construct this struct at this location and print out all its
members.

In [12]:

```text
memory_range = session.profile._PHYSICAL_MEMORY_DESCRIPTOR(0xfa8001793fd0)
print memory_range
```

```text
[_PHYSICAL_MEMORY_DESCRIPTOR _PHYSICAL_MEMORY_DESCRIPTOR] @ 0xFA8001793FD0
  0x00 NumberOfRuns   [unsigned long:NumberOfRuns]: 0x00000002
  0x08 NumberOfPages  [unsigned long long:NumberOfPages]: 0x0007CF8E
  0x10 Run
```

In [13]:

```text
for r in memory_range.Run:
    print r
```

```text
[_PHYSICAL_MEMORY_RUN Run[0] ] @ 0xFA8001793FE0
  0x00 BasePage   [unsigned long long:BasePage]: 0x00000001
  0x08 PageCount  [unsigned long long:PageCount]: 0x0000009E

[_PHYSICAL_MEMORY_RUN Run[1] ] @ 0xFA8001793FF0
  0x00 BasePage   [unsigned long long:BasePage]: 0x00000100
  0x08 PageCount  [unsigned long long:PageCount]: 0x0007CEF0
```

So what have we found?

* There is a symbol called **nt!MmPhysicalMemoryBlock** which is a pointer
 to a **_PHYSICAL_MEMORY_DESCRIPTOR** struct.
* This struct contains the total number of runs, and a list of each run in
 pages (0x1000 bytes long).

Lets write a Rekall plugin for this:

In [15]:

```text
from rekall.plugins.windows import common

class WinPhysicalMap(common.WindowsCommandPlugin):
    """Prints the boot physical memory map."""

    __name = "phys_map"

    def render(self, renderer):
        renderer.table_header([
                ("Physical Start", "phys", "[addrpad]"),
                ("Physical End", "phys", "[addrpad]"),
                ("Number of Pages", "pages", "10"),
                ])

        descriptor = self.profile.get_constant_object(
            "MmPhysicalMemoryBlock",
            target="Pointer",
            target_args=dict(
                target="_PHYSICAL_MEMORY_DESCRIPTOR",
                ))

        for memory_range in descriptor.Run:
            renderer.table_row(
                memory_range.BasePage * 0x1000,
                (memory_range.BasePage + memory_range.PageCount) * 0x1000,
                memory_range.PageCount)
```

This plugin will be named **phys_map** and essentially creates a table
with three columns. The memory descriptor is created directly from the
profile, then we iterate over all the runs and output the start and end
range into the table.

In [16]:

```text
phys_map
```

```text
Physical Start  Physical End  Number of Pages
-------------- -------------- ---------------
0x000000001000 0x00000009f000 158
0x000000100000 0x00007cff0000 511728
```

So far, this is a pretty simple plugin. However, lets put on our black
hat for a sec.

In our DFRWS 2013 paper we pointed out that since most memory
acquisition tools end up calling **MmGetPhysicalMemoryRanges()** (all
the ones we tested at least), then by disabling this function we would
be able to sabotage all memory acquisition tools. This turned out to be
the case, however, by patching the running code in memory we would
trigger Microsoft's **Patch Guard**. In our tests, we disabled Patch
Guard to prove the point, but this is less practical in a real rootkit.

In reality, a rootkit would like to be able to modify the underlying
data structure behind the API call itself. This is much easier to do and
wont modify any kernel code, thereby bypassing Patch Guard protections.

To test this, we can do this directly from Rekall's interactive console.

In [18]:

```text
descriptor = session.profile.get_constant_object(
    "MmPhysicalMemoryBlock",
    target="Pointer",
    target_args=dict(
      target="_PHYSICAL_MEMORY_DESCRIPTOR",
    )).dereference()

print descriptor
```

```text
[_PHYSICAL_MEMORY_DESCRIPTOR Pointer] @ 0xFA8001793FD0
  0x00 NumberOfRuns   [unsigned long:NumberOfRuns]: 0x00000002
  0x08 NumberOfPages  [unsigned long long:NumberOfPages]: 0x0007CF8E
  0x10 Run
```

Since we loaded the memory driver with write support, we are able to
directly modify each field in the struct. For this proof of concept we
simply set the NumberOfRuns to 0, but a rootkit can get creative by
modifying the runs to contain holes located in strategic regions. By
specifically crafting a physical memory descriptor with a hole in it, we
can cause memory acquisition tools to just skip over some region of the
physical memory. The responders can then walk away thinking they have
their evidence, but critical information is missing.

In [19]:

```text
descriptor.NumberOfRuns = 0
```

Now we can repeat our **phys_map** plugin, but this time, no runs will
be found:

In [20]:

```text
phys_map
```

```text
Physical Start  Physical End  Number of Pages
-------------- -------------- ---------------
```

To unload the driver, we need to close any handles to it. We then try to
acquire a memory image in the regular way.

In [32]:

```text
session.physical_address_space.close()
```

In [2]:

```text
!c:/Users/mic/winpmem_write_1.5.5.exe test.raw
```

```text
Driver Unloaded.
Loaded Driver C:\Users\mic\AppData\Local\Temp\pme3879.tmp.
Will generate a RAW image
CR3: 0x0000187000
 0 memory ranges:
Acquitision mode PTE Remapping

Driver Unloaded.
```

This time, however, Winpmem reports no memory ranges available. The
result image is also 0 bytes big:

In [3]:

```text
!dir test.raw
```

```text
 Volume in drive C has no label.
 Volume Serial Number is 6438-7315

 Directory of C:\Users\mic

03/07/2014  12:02 AM                 0 test.raw
               1 File(s)              0 bytes
               0 Dir(s)   3,416,547,328 bytes free
```

At this point, running the dumpit program from
Moonsols will cause the system to immediately reboot. (It seems that
dumpit is unable to handle 0 memory ranges gracefully and crashes the
kernel).

## How stable is this

We have just disabled a kernel function, but this might de-stabilize the
system. What other functions in the kernel are
calling *MmGetPhysicalMemoryRanges*?

Lets find out by disassembling the entire kernel. First we need to find
the range of memory addresses the kernel code is in. We use
the *peinfo* plugin to show us the sections which are mapped into
memory.

In [2]:

```bash
peinfo "nt"
```

```text
Attribute            Value
---------------------- -----
```

```text
Machine              IMAGE_FILE_MACHINE_AMD64
TimeDateStamp        2009-07-13 23:40:48+0000
Characteristics      IMAGE_FILE_EXECUTABLE_IMAGE, IMAGE_FILE_LARGE_ADDRESS_AWARE
GUID/Age             F8E2A8B5C9B74BF4A6E4A48F180099942
PDB                  ntkrnlmp.pdb
MajorOperatingSystemVersion 6
MinorOperatingSystemVersion 1
MajorImageVersion    6
MinorImageVersion    1
MajorSubsystemVersion 6
MinorSubsystemVersion 1

Sections (Relative to 0xF8000261F000):
Perm Name          VMA            Size
---- -------- -------------- --------------
xr-  .text    0x000000001000 0x00000019b800
xr-  INITKDBG 0x00000019d000 0x000000003a00   These are Executable sections.
xr-  POOLMI   0x0000001a1000 0x000000001c00
xr-  POOLCODE 0x0000001a3000 0x000000003000
xrw  RWEXEC   0x0000001a6000 0x000000000000
-r-  .rdata   0x0000001a7000 0x00000003ca00
-rw  .data    0x0000001e4000 0x00000000fc00
-r-  .pdata   0x000000278000 0x00000002fa00
-rw  ALMOSTRO 0x0000002a8000 0x000000000800
-rw  SPINLOCK 0x0000002aa000 0x000000000a00
xr-  PAGELK   0x0000002ac000 0x000000014c00
xr-  PAGE     0x0000002c1000 0x000000232600
xr-  PAGEKD   0x0000004f4000 0x000000004e00
xr-  PAGEVRFY 0x0000004f9000 0x000000021600
xr-  PAGEHDLS 0x00000051b000 0x000000002800
xr-  PAGEBGFX 0x00000051e000 0x000000006800
-rw  PAGEVRFB 0x000000525000 0x000000000000
-r-  .edata   0x000000529000 0x000000010a00
-rw  PAGEDATA 0x00000053a000 0x000000004c00
-r-  PAGEVRFC 0x000000548000 0x000000002a00
-rw  PAGEVRFD 0x00000054b000 0x000000001400
xrw  INIT     0x00000054d000 0x000000056c00
-r-  .rsrc    0x0000005a4000 0x000000035e00
-r-  .reloc   0x0000005da000 0x000000002200

Data Directories:
-                                             VMA            Size
---------------------------------------- -------------- --------------
IMAGE_DIRECTORY_ENTRY_EXPORT             0xf80002b48000 0x000000010962
IMAGE_DIRECTORY_ENTRY_IMPORT             0xf80002bc1cec 0x000000000078
IMAGE_DIRECTORY_ENTRY_RESOURCE           0xf80002bc3000 0x000000035d34
IMAGE_DIRECTORY_ENTRY_EXCEPTION          0xf80002897000 0x00000002f880
IMAGE_DIRECTORY_ENTRY_SECURITY           0xf80002b5ec00 0x000000001c50
IMAGE_DIRECTORY_ENTRY_BASERELOC          0xf80002bf9000 0x000000002078
IMAGE_DIRECTORY_ENTRY_DEBUG              0xf800027bb5c0 0x000000000038
IMAGE_DIRECTORY_ENTRY_COPYRIGHT          0x000000000000 0x000000000000
IMAGE_DIRECTORY_ENTRY_GLOBALPTR          0x000000000000 0x000000000000
IMAGE_DIRECTORY_ENTRY_TLS                0x000000000000 0x000000000000
IMAGE_DIRECTORY_ENTRY_LOAD_CONFIG        0x000000000000 0x000000000000
IMAGE_DIRECTORY_ENTRY_BOUND_IMPORT       0x000000000000 0x000000000000
IMAGE_DIRECTORY_ENTRY_IAT                0xf800027c6000 0x000000000380
IMAGE_DIRECTORY_ENTRY_DELAY_IMPORT       0x000000000000 0x000000000000
IMAGE_DIRECTORY_ENTRY_COM_DESCRIPTOR     0x000000000000 0x000000000000
IMAGE_DIRECTORY_ENTRY_RESERVED           0x000000000000 0x000000000000

Import Directory (Original):
Name                                               Ord
-------------------------------------------------- -----

Export Directory:
    Entry      Stat Ord   Name
-------------- ---- ----- --------------------------------------------------
0xf80002677794 M    0     ntoskrnl.exe!AlpcGetHeaderSize (nt!AlpcGetHeaderSize)
0xf80002677760 M    1     ntoskrnl.exe!AlpcGetMessageAttribute (nt!AlpcGetMessageAttribute)
0xf80002665eb0 M    2     ntoskrnl.exe!AlpcInitializeMessageAttribute (nt!AlpcInitializeMessageAttribute)
0xf800026b5ac0 M    3     ntoskrnl.exe!CcCanIWrite (nt!CcCanIWrite)
0xf8000262a244 M    4     ntoskrnl.exe!CcCoherencyFlushAndPurgeCache (nt!CcCoherencyFlushAndPurgeCache)
... (Truncated)
0xf80002b4d2ab M    2111  ntoskrnl.exe! (None)
Version Information:
key                  value
-------------------- -----
```

Now instead of disassembling to the interactive notebook, we store it in
a file. This does take a while but will produce a large text file
containing the complete disassembly of the windows kernel (With
debugging symbols cross referenced).

In [3]:

```text
dis offset=0xF8000261F000+0x1000, end=0xF8000261F000+0x525000, output="ntkrnl_amd64.dis"
```

Now we can use our favourite editor (Emacs) to check all references
to **MmGetPhysicalMemoryRanges**. We can see references from:

* nt!PfpMemoryRangesQuery - Part of ExpQuerySystemInformation.
* nt!IoFillDumpHeader - Called from crashdump facility.
* nt!IopGetPhysicalMemoryBlock - Called from crashdump facility.

We can also check references to **MmPhysicalMemoryBlock**. Many of these functions appear related
to the [Hot-Add memory functionality](https://learn.microsoft.com/en-us/previous-versions/windows/hardware/design/dn613938(v=vs.85)):

* nt!IoSetDumpRange
* nt!MiFindContiguousPages
* nt!MmIdentifyPhysicalMemory
* nt!MmReadProcessPageTables
* nt!MiAllocateMostlyContiguous
* nt!IoFillDumpHeader
* nt!MiReleaseAllMemory
* nt!MmDuplicateMemory
* nt!MiRemovePhysicalMemory
* nt!MmAddPhysicalMemory
* nt!MmGetNumberOfPhysicalPages - This seems to be called from Hibernation
 code.
* nt!MiScanPagefileSpace
* nt!MmPerfSnapShotValidPhysicalMemory
* nt!MmGetPhysicalMemoryRanges

Some testing remains to see how stable this modification is in practice.
It appears that probably Hot Add memory will no longer work, and
possibly hibernation will fail (Hibernation is an alternate way to
capture memory images, as Rekall can also operate on hibernation files).
Although the above suggests that crash dumps are affected, I have tried
to produce a crashdump after this modification, but it still worked as
expected (This is actually kind of interesting in itself).
