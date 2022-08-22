Linux refers to the family of Unix-like computer operating systems using
the Linux kernel. Due to the nature of Linux it is possible for a wide
range of high penetration forensic tools.

The wide variety of useful Linux utilities exist for desktop computers
can also be used on Linux-based PDAs. These utilities can often be used
as a part of the [forensics
investigation](forensics_investigation "wikilink") process.

Software for Linux systems are not only targets at personal computers,
desktops, laptops etc, but also server based tools exist for both
accessing, monitoring and analysing servers.

## Specialist Software

### Helix

[Helix](http://www.e-fense.com/h3-enterprise.php) is a live Linux CD
designed for live incident response. Helix is targeted towards the more
experienced users and forensic investigators.

The latest version of Helix, Helix 3, is based on the Ubuntu version of
Linux, this allows for greater stability and ease of use.

Due to Helix being a live disc it is possible to run it on a "suspect"
machine whilst the installed operating system remains inactive, also
live network forensics are possible when running the Helix Live Disc
allowing for users to perform checks on networks that their machines are
attached to.

## Tools

### dd

**[dd](dd "wikilink")**, or duplicate disk, is a Unix and Linux utility
that allows the user to create a bitstream image of a disk or device.
Once the Linux-based PDA is connected to another device and the dd
utility is run, the mirror image can be uploaded onto [memory
cards](memory_card "wikilink") or even an external desktop workstation
connected via a network. Images created by dd are readable by [forensics
software](forensics_software "wikilink") tools such as
[EnCase](EnCase "wikilink") and [Forensic
Toolkit](Forensic_Toolkit "wikilink"). Since the device uses a Linux
[filesystem](filesystem "wikilink"), the image may also be mounted and
examined on a Linux workstation.

### foremost

**[foremost](foremost "wikilink")** is a Linux based program data for
[recovering deleted files](Recovering_deleted_data "wikilink") and
served as the basis for the more modern [Scalpel](Scalpel "wikilink").
The program uses a configuration file to specify [headers and
footers](File_Formats "wikilink") to search for. Intended to be run on
disk images, foremost can search through most any kind of data without
worrying about the format.

### EtherApe

[EtherApe](http://etherape.sourceforge.net/)is a free program built on
the structure of Etherman. It is designed as a high level wide range
network monitoring tool which provides a graphical display to the user
illustrating packet information. Although EtherApe might be seen as a
security orientated tool it does have forensic application.

EtherApe has two main modes, live monitoring which can be run on a
server machine which will map any packets passing to and from that
machine, illustrating with colours the type of packet, as well as by
diameter the amount of traffic that type of packet brings. It is also
possible to see the different nodes attached , by IP and IPv6 addresses.

EtherApe's secondary function is a review ability, taking a selection of
packets captured either by TCPDUMP command or another piece of capture
software. When running the file through EtherApe the program displays
the same information as it does with a live capture but reading from the
data file imported instead of the live network. A review of files can be
done on any machine, regardless of network connectivity.

### Memory Forensics

Memory forensics tools help preserve the volatile state of the system,
and find stealthy malware. For a list of memory acquisition tools for
Linux, see [Tools:Memory Imaging](Tools:Memory_Imaging "wikilink"). For
a list of memory analysis tools for Linux, see [Linux Memory
Analysis](Linux_Memory_Analysis "wikilink").

# External Links

- <http://en.wikipedia.org/wiki/Linux>
- <http://en.wikipedia.org/wiki/Android_(mobile_device_platform)>

## Activity tracking

- [Tracking user actions with the Linux audit
  subsystem](http://civilfritz.net/tracking-user-actions-with-the-linux-audit-subsystem/)

## Control groups (cgroups)

- [Wikipedia: Cgroups](http://en.wikipedia.org/wiki/Cgroups)
- [⁠Chapter 1. Introduction to Control Groups
  (Cgroups)](https://access.redhat.com/documentation/en-US/Red_Hat_Enterprise_Linux/6/html/Resource_Management_Guide/ch01.html)

## Initrd, Initramfs

- <https://www.kernel.org/doc/Documentation/early-userspace/buffer-format.txt>

[Category:Operating systems](Category:Operating_systems "wikilink")