---
tags:
  - Articles that need to be expanded
  - Disk Analysis
  - Linux
  - Mac OS
  - Open Source Software
  - Tools
  - Windows
---
Autopsy® is an easy to use, GUI-based program that allows you to
efficiently analyze hard drives and smart phones. It has a plug-in
architecture that allows you to find add-on modules or develop custom
modules in Java or Python.

**Autopsy** uses [The Sleuth Kit](the_sleuth_kit.md) for file
system analysis. It can analyze [Windows](windows.md),
[Mac OS X](mac_os_x.md), and [UNIX](unix.md) disks, as well as
cell phone dumps and collections of individual files. There are many
third-party plug-in modules.

## Version 2

Autopsy 2 was a graphical interface to the command line digital
investigation analysis tools in [The Sleuth Kit](the_sleuth_kit.md).
Together, they can analyze [Windows](windows.md) and [UNIX](unix.md)
disks and [file systems](file_systems.md) such as:

* [NTFS](new_technology_file_system_(ntfs).md)
* [FAT](fat.md)
* UFS1/UFS2
* [Ext2/Ext3](extended_file_system_(ext).md)

[The Sleuth Kit](the_sleuth_kit.md) and Autopsy are both Open Source
and run on UNIX platforms. As Autopsy is [HTML](html.md)-based,
you can connect to the Autopsy server from any platform using a web
browser. It provides a "File Manager"-like interface and shows
details about deleted data and file system structures.

### Current state

As of 2014, Autopsy 2.24 is the last version of Autopsy that supports
non-Windows platforms. Since Autopsy 2.24 was released in 2010, it
cannot support all features introduced in latest
[The Sleuth Kit](the_sleuth_kit.md) versions. Various modifications
introduced in Sleuthkit since 2010 break Autopsy 2.24.

There are several known conflicts between Autopsy 2.24 and Sleuthkit
4.1.3:

* Autopsy cannot normally jump through directories on HFS.
* Autopsy cannot handle Sun VTOC.
* Autopsy cannot view timelines in most cases.

Also, Ext4 file creation timestamps cannot be viewed in the Autopsy
"File Manager"-like interface. Unofficial
[patch](https://github.com/msuhanov/autopsy-2.24-patch/blob/master/autopsy-2.24-1.patch)
exists to fix or "hack around" these issues.

## History

### Owning organizations

Autopsy was originally developed in March 2001 as a graphical
interface to The Coroner's Toolkit (TCT) and TCTUTIL.
[Brian Carrier](brian_carrier.md) developed most of the code in
Autopsy 1, Autopsy 2, and
[The Sleuth Kit](the_sleuth_kit.md).

Basis Technology, a company that develops digital forensic tools, was
the company behind The Sleuth Kit and Autopsy for many years.
Autopsy version 3 was a complete rewrite and was largely funded by
Basis Technology, which continued building Autopsy from version 3
onward.

The digital forensics division of Basis Technology split off to
become its own independent company, Sleuth Kit Labs. The Sleuth Kit
Labs team started when Carrier joined Basis Technology to build its
digital forensics department, and Sleuth Kit Labs provides the
primary development of Autopsy.

## External Links

* [Search Autopsy Addon Modules](https://sleuthkit.github.io/autopsy_addon_modules/)
* [Carlos Lannister's catalog of Autopsy Modules](https://github.com/CarlosLannister/awesome-autopsy-plugins)
