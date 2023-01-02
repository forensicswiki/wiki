---
tags:
  - Tools
  - Memory Imaging
---
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

Forensic RAM Extraction Device (FRED) by BBN
Not publicly available. <http://www.ir.bbn.com/~vkawadia/>

### [Windows](windows.md) Software

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

launched in 2011International Organisations

<!-- -->

winen.exe (Guidance Software - included with Encase 6.11 and higher)
included on [Helix 2.0](http://www.e-fense.com/helix/)

<http://forensiczone.blogspot.com/2008/06/winenexe-ram-imaging-tool-included-in.html>

<!-- -->

[Mdd](mdd.md) ([ManTech](mantech.md))
<http://sourceforge.net/projects/mdd>

<!-- -->

MANDIANT Memoryze
Can capture and analyze memory. Supports reading dumps (raw/dd format)
from other tools.

<http://www.mandiant.com/software/memoryze.htm>

<!-- -->

[Moonsols](moonsols.md): [DumpIt](dumpit.md)
This utility is used to generate a physical memory dump of Windows
machines. It works with both x86 (32-bits) and x64 (64-bits) machines.

The raw memory dump is generated in the current directory, only a
confirmation question is prompted before starting.

Perfect to deploy the executable on USB keys, for quick incident
responses needs.

<http://www.moonsols.com/wp-content/plugins/download-monitor/download.php?id=7>

<!-- -->

[FTK Imager](ftk_imager.md): FTK Imager
<http://accessdata.com/support/adownloads#FTKImager>

FTK Imager can acquire live memory and paging file on 32bit and 64bit
systems.

<!-- -->

[OSForensics](osforensics.md): OSForensics
<http://www.osforensics.com/>

OSForensics can acquire live memory on 32bit and 64bit systems. A dump
of an individual process's memory space or physical memory dump can be
done. Output can be a straight dump or a Microsoft crash dump file, for
use with Micrsoft's WinDbg debugger.

<!-- -->

[WinPmem](rekall.md)
WinPmem is a free, actively developed, opensource forensic memory
acquisition tool for Windows. It supports Windows XP to Windows 8, both
32 and 64 bit architectures. It can produce raw dumps as well as dumps
in crashdump format (for analysis with Volatility or windbg). It
supports output to STDOUT for piping the dump through tools like netcat
or ssh. WinPmem can be used together with the Volatility Technology
Preview to analyse a live windows system for live response and triaging.

### Linux

[LiME](http://code.google.com/p/lime-forensics/)
Linux Memory Extractor (LiME) is a Loadable Kernel Module (LKM), which
allows the acquisition of volatile memory from Linux and Linux-based
devices, such as those powered by Android. The tool supports dumping
memory either to the file system of the device or over the network.

[Linux Memory Grabber](https://github.com/halpomeranz/lmg/) by Hal Pomeranz
a tool to create Linux Volatility profiles and dump memory (using LiME)
from an USB Key, without installation on local HDD. Very useful

[Tools:Memory_Imaging//dev/crash](tools:memory_imaging/dev/crash.md)
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

[Tools:Memory_Imaging//dev/mem](tools:memory_imaging/dev/mem.md)
On older Linux systems, the program [dd](dd.md) can be used to
read the contents of [physical memory](physical_memory.md) from
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

[lmap](rekall.md) and [pmem](rekall.md)
pmem is a loadable kernel module that exposes /dev/pmem. lmap allows to
inject the pmem functionality into existing kernel modules to bypass
having to build a pmem kernel module for every different kernel version.

### Mac OS X

[Goldfish](http://digitalfire.ucd.ie/?page_id=430)
Goldfish is a [Mac OS X](mac_os_x.md) live forensic tool. Its
main purpose is to provide an easy to use interface to dump the system
RAM of a target machine via a [Firewire](firewire.md)
connection. It then automatically extracts the current user login
password and any open AOL Instant Messenger conversation fragments that
may be available. Please see [1](http://digitalfire.ucd.ie/?page_id=430)
for more information.

<!-- -->

[OSXPMem](rekall.md)
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

- [Linux Memory Analysis](linux_memory_analysis.md)
- [Memory Imaging](memory_imaging.md)
- [Windows Memory Analysis](windows_memory_analysis.md)
