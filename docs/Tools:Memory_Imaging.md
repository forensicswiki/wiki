## Memory Imaging Tools

### x86 Hardware

[WindowsSCOPE](http://www.windowsscope.com) CaptureGUARD PCIe card (commercial) - desktops, servers
Publicly available, supports all Windows OS; windd and other formats.

CaptureGUARD Gateway performs DRAM acquisition even on locked computers

Inquire at <http://www.windowsscope.com>.

<!-- -->

[WindowsSCOPE](http://www.windowsscope.com) CaptureGUARD ExpressCard (commercial) - laptop applications
Publicly available, supports all Windows OS; windd and other formats.

CaptureGUARD Gateway performs DRAM acquisition even on locked computers

Inquire at <http://www.windowsscope.com>.

<!-- -->

Tribble PCI Card (research project)
<http://www.digital-evidence.org/papers/tribble-preprint.pdf>

<!-- -->

CoPilot by Komoku
Komoku was acquired by Microsoft and the card was not made publicly
available.

<!-- -->

Forensic RAM Extraction Device (FRED) by BBN
Not publicly available. <http://www.ir.bbn.com/~vkawadia/>

### [Windows](Windows "wikilink") Software

There are many Windows memory acquisition tools. Most of them will not
work on Windows Vista or 7, as user programs have been denied access to
the *\Device\Physicalmemory* object starting in Windows 2003 Service
Pack 1 and Windows Vista. Modern tools acquire physical memory by first
installing a device driver, so administrative privileges are needed.

We have edited this list so that it only includes current tools:

Belkasoft Live RAM Caputer
This free forensic tool, unlike many others, works in kernel-mode, which
allows bypassing proactive anti-debugging protection used by many modern
applications such as online games and intrusion detection systems.
Kernel-mode operation yields more reliable results compared to user-mode
tools.

<!-- -->


Designed specifically for computer forensics. Fully portable, runs off a
flash drive, produces uncompressed raw binary output of the computer’s
volatile memory. Includes kernel-mode drivers for all Windows OS’es
including XP, Vista, 7, 8, 2003 and 2008 Server. 32 and 64-bit drivers
are included.

<!-- -->


<http://forensic.belkasoft.com/en/ram-capturer>

<!-- -->

WindowsSCOPE Pro and Ultimate, available at <http://www.windowsscope.com>
Can capture, analyze, graph in depth physical and virtual memory codes
and structures

Proprietary and standard formats (windd), snapshot repository, snapshot
comparison

All Windows OSs (Xp, Vista, 7), 32 and 64 bit supported

Phantom Probe USB based fetch

CaptureGUARD PCIe card and ExpressCard for hardware-assisted DRAM
acquisition

CaptureGUARD Gateway for hardware-assisted DRAM acquisition of locked
computers

launched in 2011

<!-- -->

WindowsSCOPE Live
available at <http://www.windowsscope.com> and Android market

allows live memory analysis of Windows computers from Android phones and
tablets

launched in 2011

<!-- -->

winen.exe (Guidance Software - included with Encase 6.11 and higher)
included on [Helix 2.0](http://www.e-fense.com/helix/)

<http://forensiczone.blogspot.com/2008/06/winenexe-ram-imaging-tool-included-in.html>

<!-- -->

[Mdd](Mdd "wikilink") (Memory DD) ([ManTech](ManTech "wikilink"))
<http://sourceforge.net/projects/mdd>

<!-- -->

MANDIANT Memoryze
Can capture and analyze memory. Supports reading dumps (raw/dd format)
from other tools.

<http://www.mandiant.com/software/memoryze.htm>

<!-- -->

[Kntdd](Kntdd "wikilink")
<http://www.gmgsystemsinc.com/knttools/>

<!-- -->

[Moonsols](Moonsols "wikilink"): [DumpIt](DumpIt "wikilink")
This utility is used to generate a physical memory dump of Windows
machines. It works with both x86 (32-bits) and x64 (64-bits) machines.

The raw memory dump is generated in the current directory, only a
confirmation question is prompted before starting.

Perfect to deploy the executable on USB keys, for quick incident
responses needs.

<http://www.moonsols.com/wp-content/plugins/download-monitor/download.php?id=7>

<!-- -->

[HBGary](HBGary "wikilink"): Fastdump and Fastdump Pro
[Fastdump](Fastdump "wikilink") (free with registration) Can acquire
physical memory on Windows 2000 through Windows XP 32 bit but not
Windows 2003 or Vista.

[Fastdump Pro](Fastdump_Pro "wikilink") Can acquire physical memory on
Windows 2000 through Windows 2008, all service packs. Additionally,
Fastdump Pro supports:

-32 bit and 64 bit architectures

-Acquisitions of greater than 4GB

-Fast acquisitions through the use of larger page sizes (1024KB) but
also supports a strict mode that enforces 4KB page sizes.

-Process probing which allows for a more complete memory image of a
process of interest.

-Acquisition of the system page file during physical memory acquisition.
This allows for a more complete memory analysis.

<!-- -->

[FTK Imager](FTK_Imager "wikilink"): FTK Imager
<http://accessdata.com/support/adownloads#FTKImager>

FTK Imager can acquire live memory and paging file on 32bit and 64bit
systems.

<!-- -->

[OSForensics](OSForensics "wikilink"): OSForensics
<http://www.osforensics.com/>

OSForensics can acquire live memory on 32bit and 64bit systems. A dump
of an individual process's memory space or physical memory dump can be
done. Output can be a straight dump or a Microsoft crash dump file, for
use with Micrsoft's WinDbg debugger.

<!-- -->

[WinPmem](Rekall "wikilink")
WinPmem is a free, actively developed, opensource forensic memory
acquisition tool for Windows. It supports Windows XP to Windows 8, both
32 and 64 bit architectures. It can produce raw dumps as well as dumps
in crashdump format (for analysis with Volatility or windbg). It
supports output to STDOUT for piping the dump through tools like netcat
or ssh. WinPmem can be used together with the Volatility Technology
Preview to analyse a live windows system for live response and triaging.

<!-- -->

[Windows Memory Reader](http://cybermarshal.atc-nycorp.com/index.php/cyber-marshal-utilities/windows-memory-reader)
Windows Memory Reader is a simple command-line utility to capture the
contents of physical RAM. Results are stored in a Windows crash dump or
raw binary file. Researchers can also use Windows Memory Reader to
capture memory-mapped device data, such as shared video memory. Windows
Memory Reader supports Windows XP through Windows 8, both 32-bit and
64-bit versions, and is available free of charge.

### Linux

[LiME](http://code.google.com/p/lime-forensics/)
Linux Memory Extractor (LiME) is a Loadable Kernel Module (LKM), which
allows the acquisition of volatile memory from Linux and Linux-based
devices, such as those powered by Android. The tool supports dumping
memory either to the file system of the device or over the network.

[Linux Memory Grabber](https://github.com/halpomeranz/lmg/) by Hal Pomeranz
a tool to create Linux Volatility profiles and dump memory (using LiME)
from an USB Key, without installation on local HDD. Very useful

[Tools:Memory_Imaging//dev/crash](Tools:Memory_Imaging/dev/crash "wikilink")
On Red Hat systems (and those running related distros such as Fedora or
CentOS), the crash driver can be loaded to create pseudo-device
/dev/crash for raw physical memory access (via command "modprobe
crash"). This module can also be compiled for other Linux distributions
with minor effort (see, for example,
<http://gleeda.blogspot.com/2009/08/devcrash-driver.html>). When the
crash driver is modified, compiled, and loaded on other systems, the
resulting memory access device is not safe to image in its entirety.
Care must be taken to avoid addresses that are not RAM-backed. On Linux,
/proc/iomem exposes the correct address ranges to image, marked with
"System RAM".

[Tools:Memory_Imaging//dev/mem](Tools:Memory_Imaging/dev/mem "wikilink")
On older Linux systems, the program [dd](dd "wikilink") can be used to
read the contents of [physical memory](physical_memory "wikilink") from
the device file `/dev/mem`. On recent Linux systems, however, /dev/mem
provides access only to a restricted range of addresses, rather than the
full physical memory of a system. On other systems it may not be
available at all. Throughout the 2.6 series of the Linux kernel, the
trend was to reduce direct access to memory via pseudo-device files.
See, for example, the message accompanying this patch:
<http://lwn.net/Articles/267427/>.

[Second Look: Linux Memory Forensics](http://secondlookforensics.com)
This commercial memory forensics product ships with a modified version
of the crash driver and a script for safely dumping memory using the
original or modified driver on any given Linux system.

[fmem](http://hysteria.sk/~niekt0/foriana/fmem_current.tgz)
fmem is kernel module that creates device /dev/fmem, similar to /dev/mem
but without limitations. This device (physical RAM) can be copied using
dd or other tool. Works on 2.6 Linux kernels. Under GNU GPL.

[lmap](Rekall "wikilink") and [pmem](Rekall "wikilink")
pmem is a loadable kernel module that exposes /dev/pmem. lmap allows to
inject the pmem functionality into existing kernel modules to bypass
having to build a pmem kernel module for every different kernel version.

### Mac OS X

[Goldfish](http://digitalfire.ucd.ie/?page_id=430)
Goldfish is a [Mac OS X](Mac_OS_X "wikilink") live forensic tool. Its
main purpose is to provide an easy to use interface to dump the system
RAM of a target machine via a [Firewire](Firewire "wikilink")
connection. It then automatically extracts the current user login
password and any open AOL Instant Messenger conversation fragments that
may be available. Please see [1](http://digitalfire.ucd.ie/?page_id=430)
for more information.

<!-- -->

[Mac Memory Reader](http://cybermarshal.atc-nycorp.com/index.php/cyber-marshal-utilities/mac-memory-reader)
Mac Memory Reader is a simple command-line utility to capture the
contents of physical RAM. Results are stored in a Mach-O binary or raw
data file. Mac Memory Reader is available free of charge. It executes
directly on 32- and 64-bit target machines running Mac OS X 10.4 through
10.7 and requires a PowerPC G4 or newer, or any Intel processor.

<!-- -->

[OSXPMem](Rekall "wikilink")
The OSX Memory Imager is an open source tool to acquire physical memory
on an Intel based Mac. The imager supports multiple output formats, at
the moment these are Mach-O, ELF and zero-padded RAW.

### Virtual

Qemu
Qemu allows you to dump the memory of a running image using pmemsave.

e.g. pmemsave 0 0x20000000 /tmp/dumpfile

Xen
Xen allows you to live dump the memory of a guest domain using the
dump-core command.

You can list the available machines to find the host machine you care
about using xm list and see the configuration.

Dumping is a matter of sudo xm dump-core -L /tmp/dump-core-6 6

VMWare ESXi
One way to make a memory dump on ESXi is to make a snapshot of the
running instance. This can be done using one of the

client side tools for ESXi, but also on the ESXi ssh shell.

To make a snapshot on the ESXi ssh shell the following commands can be
used:

- vim-cmd vmsvc/getallvms
- vim-cmd vmsvc/get.summary vmid \| grep \[some identity e.g. ip address
  if name is not known\]
- vim-cmd vmsvc/snapshot.create vmid \[snapshotName\]
  \[snapshotDescription\] \[includeMemory (thus 1)\] \[quiesced\]


the .vmsn file can be copied from the ESXi using e.g. scp

volatility can be used to convert the memdump into a raw dump. In my
experience it is not possible to use volatility directly on the
non-converted dump.

## See Also

- [Linux Memory Analysis](Linux_Memory_Analysis "wikilink")
- [Memory Imaging](Memory_Imaging "wikilink")
- [Windows Memory Analysis](Windows_Memory_Analysis "wikilink")

[Category:Tools](Category:Tools "wikilink")