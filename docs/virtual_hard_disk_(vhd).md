---
tags:
  -  File Formats
  -  Articles that need to be expanded
---
The Virtual Hard Disk (VHD) commonly uses the .vhd extension.

This format is used to store virtual disk images by:

- Microsoft Virtual PC
- Microsoft Virtual Server
- Microsoft Hyper-V Server

VHD support is also integrated into [Windows](windows.md) (at
least in Windows 7) where "Disk Management" (part of "Computer
Management") supports attaching and creating Fixed and Dynamic VHD image
files.

## Image types

There are multiple types of Virtual Hard Disk (VHD) images:

- Fixed-size hard disk image; the image contains all data
- Dynamic-size (or sparse) hard disk image; the image contains used data
  only
- Differential (or differencing, or delta) hard disk image; the image
  contains changes relative to its parent image

## Snapshots

Hyper-V has functionality to create snapshots.

These snapshots are stored in Snapshot Differencing Disk (AVHD) files
which commonly uses the .avhd extension.

The snapshot can be interdependent on one-another, because they are
differential images of the previous snapshot.

## See Also

- [Disk Images](disk_images.md)
- [Windows](windows.md)

## External Links

- [VHD (file format)](http://en.wikipedia.org/wiki/VHD_(file_format)),
  by Wikipedia
- [Virtual Hard Disk Image Format
  Specification](http://technet.microsoft.com/en-us/library/bb676673.aspx),
  by Microsoft, October 2006
- [Overview of VHD & VHDX Virtual Hard
  Drive](http://www.bitrecover.com/blog/what-is-virtual-hard-disk/) An
  overview of virtual hard drive image files
- [Virtual Hard Disk (VHD) image
  format](https://googledrive.com/host/0B3fBvzttpiiSY250RjRzRXQ0bDg/Virtual%20Hard%20Disk%20(VHD)%20image%20format.pdf),
  by the [libvhdi project](libvhdi.md), September 2012

### Snapshots

- [Hyper-V Concepts -
  Snapshots](http://social.technet.microsoft.com/wiki/contents/articles/670.hyper-v-concepts-snapshots.aspx)
- [Virtual Machine Snapshotting under
  Hyper-V](http://blogs.msdn.com/b/virtual_pc_guy/archive/2008/03/11/virtual-machine-snapshotting-under-hyper-v.aspx)
- [Hyper-V SnapShot Files – AVHD and VHD? What The
  ?](http://www.msserveradmin.com/hyper-v-snapshot-files-avhd-and-vhd-what-the/)
- [Manually Merge .avhd to .vhd in
  Hyper-V](http://social.technet.microsoft.com/wiki/contents/articles/6257.manually-merge-avhd-to-vhd-in-hyper-v.aspx)

## Tools

- [libvhdi](libvhdi.md)
- [VHD Data Recovery](http://www.bitrecover.com/vhd-recovery-software/)
  Help you recover & extract your files from a corrupt or damaged .vhd /
  .vhdx files. Supports Microsoft Hyper-V, Microsoft Virtual PC,
  Microsoft Virtual Server virtual machine drive images.

