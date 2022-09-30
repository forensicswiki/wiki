---
tags:
  - No Category
---
**Masterkey Linux** (or simply Masterkey) is a [Live
CD](live_cd.md) based on [Slackware](Slackware "wikilink")
developed by Dr. Qin Zhou of Coventry University. It focuses on
[incident response](incident_response.md) and [computer
forensics](computer_forensics.md).

Whilst designed for use by students entering the field of Computer
Forensics, Masterkey contains a diverse range of free and open source
tools that both students, computer forensics professionals and system
administrators alike can use.

## Tools Included

In addition to standard unix/linux tools, a suite of editors, office
applications and multimedia tools have been included, as well as the
following specialised tools in the Masterkey Linux distribution:

- **[AIR](air.md)** 1.2.8

AIR is a GUI front-end to dd/dcfldd designed for easily creating
forensic bit images.

- **[Autopsy](autopsy.md)** 2.21

The Autopsy Forensic Browser is a graphical interface to the command
line digital investigation tools in The Sleuth Kit.

- **[ClamAV](clamav.md)** for Unix 0.91.2

Clam AntiVirus is an anti-virus toolkit for UNIX

- **[chkrootkit](chkrootkit.md)** 0.47

chkrootkit is a tool to locally check for signs of a rootkit.

- **[chntpw](chntpw.md)** 070923

chntpw is an Offline password and Registry Editor

- **[dcfldd](dcfldd.md)** 1.3.4-1

dcfldd is an enhanced version of GNU dd (also included in this
distribution) with features useful for forensics and security

- **[dd_rescue](dd_rescue.md)** 1.14

dd_rescue copies data from one file or block device to another. It is
intended for error recovery.

- **[GParted](gparted.md)** 0.3.3

GParted is the Gnome Partition Editor application

- **[Foremost](foremost.md)** 1.5

Foremost is a console program to recover files based on their headers,
footers, and internal data structures. It is a data carving tool.

- **[mac-robber](mac-robber.md)** 1.00

mac-robber is a digital investigation tool that collects data from
allocated files in a mounted file system.

- **[md5deep](md5deep.md)** 1.12

md5deep is a cross-platform set of programs to compute MD5, SHA-1,
SHA-256, Tiger, or Whirlpool message digests on an arbitrary number of
files.

- **[memdump](memdump.md)** 1.01

memory dumper for UNIX-like systems

- **[Rootkit Hunter](rootkit_hunter.md)** 1.3.0

Rootkit Hunter is a rootkit scanner.

- **[Scalpel](scalpel.md)** 1.60

Scalpel is a fast file carver that reads a database of header and footer
definitions and extracts matching files from a set of image files or raw
device files.

- **[The Sleuth Kit](the_sleuth_kit.md)** 3.01

The Sleuth Kit (previously known as TASK) is a collection of UNIX-based
command line file and volume system forensic analysis tools.

- **[Stegdetect](stegdetect.md)** 0.6-4

Stegdetect is an automated tool for detecting steganographic content in
images.

- **[Wipe](wipe.md)** 2005-05-09

Wipe is a file and block device wiping utility.

- **[Wireshark](wireshark.md)** 0.99.6

Wireshark is a network protocol analyzer.

## Forensic Features

- Disk partitions and USB storage devices found by Masterkey are mounted
  read-only automatically. Icons for these mounted devices are displayed
  on the user's Desktop. This facilitates access and prevents a user
  from accidentally writing to the devices and contaminating evidence.

<!-- -->

- Mounting and use of swap partitions is not allowed. This prevents a
  user from destroying any evidence present on swap partitions.

<!-- -->

- Root privilege. The user works with the system as a super user
  (administrator) so that tools requiring root privilege can be used
  straightaway.

<!-- -->

- Console login. The Desktop environment (graphic user interface) does
  not start automatically during bootup. This makes it possible to work
  with Masterkey on older computers. The user can choose to start either
  the KDE or Fluxbox desktops if they wish.

## Forensic Issues

- Masterkey Linux relies on "-o ro" mount option to provide forensically
  sound mounts. Unfortunately, this option is not enough to provide real
  read-only access to media.

## External Links

- [Masterkey Web Site](http://masterkeylinux.com)
- [Masterkey Community Forum](http://masterkeylinux.com/community)
- [Live Forensic Toolkit](http://masterkeylinux.com/index.php/lft)