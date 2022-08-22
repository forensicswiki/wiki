Description taken from xmount project site on Pinguin's HQ:

xmount allows you to convert on-the-fly between multiple input and
output harddisk image types. xmount creates a virtual file system using
FUSE (Filesystem in Userspace) that contains a virtual representation of
the input image.

The virtual representation can be in:

- [raw DD](Raw_Image_Format "wikilink")
- DMG
- [VHD](Virtual_Hard_Disk_(VHD) "wikilink")
- [VirtualBox's virtual disk file
  format](Virtual_Disk_Image_(VDI) "wikilink")
- [VmWare's VMDK file
  format](VMWare_Virtual_Disk_Format_(VMDK) "wikilink")

Input images can be:

- [raw DD](Raw_Image_Format "wikilink")
- [EWF (Expert Witness Compression
  Format)](Encase_image_file_format "wikilink")
- [AFF (Advanced Forensic Format)](AFF "wikilink")

In addition, xmount also supports virtual write access to the output
files that is redirected to a cache file. This makes it possible to boot
acquired harddisk images using QEMU, KVM, VirtualBox, VmWare or alike.

## See Also

- [Disk Images](Disk_Images "wikilink")

## External Links

- [Pinguin's HQ](https://www.pinguin.lu/index.php)
- [HOWTO: Booting an acquired hard disk image containing a Windows
  installation using xmount and
  OpenGates](https://files.pinguin.lu/HOWTO-BootingAcquiredWindows.pdf).
- [Xmount: When "Changing" the Evidence isn't so
  Bad](http://linuxsleuthing.blogspot.ch/2013/03/xmount-when-changing-evidence-isnt-so.html),
  by [John Lehr](John_Lehr "wikilink"), March 21, 2013