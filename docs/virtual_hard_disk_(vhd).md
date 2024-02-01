---
tags:
  - Articles that need to be expanded
  - Disk Analysis
  - File Formats
  - Linux
  - MacOS
  - Virtual Disk
  - Windows
---
The Virtual Hard Disk (VHD) commonly uses the .vhd extension.

This format is used to store virtual disk images by:

* Microsoft Virtual PC
* Microsoft Virtual Server
* Microsoft Hyper-V Server

VHD support is also integrated into [Windows](windows.md) (at
least in Windows 7) where "Disk Management" (part of "Computer
Management") supports attaching and creating Fixed and Dynamic VHD image
files.

## Image types

There are multiple types of Virtual Hard Disk (VHD) images:

* Fixed-size hard disk image; the image contains all data
* Dynamic-size (or sparse) hard disk image; the image contains used data
  only
* Differential (or differencing, or delta) hard disk image; the image
  contains changes relative to its parent image

## Snapshots

Hyper-V has functionality to create snapshots.

These snapshots are stored in Snapshot Differencing Disk (AVHD) files
which commonly uses the .avhd extension.

The snapshot can be interdependent on one-another, because they are
differential images of the previous snapshot.

## See Also

* [Disk Images](disk_images.md)
* [Windows](windows.md)

## External Links

* [VHD (file format)](https://en.wikipedia.org/wiki/VHD_(file_format)),
  by Wikipedia
* [Virtual Hard Disk Image Format Specification](https://learn.microsoft.com/en-us/previous-versions/windows/it-pro/windows-server-2012-R2-and-2012/mt169373(v=ws.11)),
  by Microsoft, October 2006
* [Overview of VHD & VHDX Virtual Hard Drive](https://www.bitrecover.com/blog/what-is-virtual-hard-disk/) An
  overview of virtual hard drive image files
* [Virtual Hard Disk (VHD) image format](https://github.com/libyal/libvhdi/blob/main/documentation/Virtual%20Hard%20Disk%20(VHD)%20image%20format.asciidoc),
  by the [libvhdi project](libvhdi.md), September 2012

### Snapshots

* [Hyper-V Concepts - Snapshots](https://social.technet.microsoft.com/wiki/contents/articles/670.hyper-v-concepts-snapshots.aspx)
* [Manually Merge .avhd to .vhd in Hyper-V](https://social.technet.microsoft.com/wiki/contents/articles/6257.manually-merge-avhd-to-vhd-in-hyper-v.aspx)

## Tools

* [libvhdi](libvhdi.md)
* [VHD Data Recovery](https://www.bitrecover.com/vhd-recovery-software/)
  Help you recover & extract your files from a corrupt or damaged .vhd /
  .vhdx files. Supports Microsoft Hyper-V, Microsoft Virtual PC,
  Microsoft Virtual Server virtual machine drive images.
