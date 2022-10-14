---
tags:
  -  Tools
  -  Articles that need to be expanded
  -  Disk Imaging
  -  Linux
  -  FreeBSD
  -  OpenBSD
  -  NetBSD 
  -  Opensource Software
---
Description taken from xmount project site on Pinguin's HQ:

xmount allows you to convert on-the-fly between multiple input and
output harddisk image types. xmount creates a virtual file system using
FUSE (Filesystem in Userspace) that contains a virtual representation of
the input image.

The virtual representation can be in:

- [raw DD](raw_image_format.md)
- DMG
- [VHD](virtual_hard_disk_(vhd).md)
- [VirtualBox's virtual disk file
  format](virtual_disk_image_(vdi).md)
- [VmWare's VMDK file
  format](vmware_virtual_disk_format_(vmdk).md)

Input images can be:

- [raw DD](raw_image_format.md)
- [EWF (Expert Witness Compression
  Format)](encase_image_file_format.md)
- [Advanced Forensics Format](aff.md)

In addition, xmount also supports virtual write access to the output
files that is redirected to a cache file. This makes it possible to boot
acquired harddisk images using QEMU, KVM, VirtualBox, VmWare or alike.

## See Also

- [Disk Images](disk_images.md)

## External Links

- [Pinguin's HQ](https://www.pinguin.lu/index.php)
- [HOWTO: Booting an acquired hard disk image containing a Windows
  installation using xmount and
  OpenGates](https://files.pinguin.lu/HOWTO-BootingAcquiredWindows.pdf).
- [Xmount: When "Changing" the Evidence isn't so
  Bad](http://linuxsleuthing.blogspot.ch/2013/03/xmount-when-changing-evidence-isnt-so.html),
  by [John Lehr](john_lehr.md), March 21, 2013