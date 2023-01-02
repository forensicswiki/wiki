---
tags:
  - Articles that need to be expanded
---
There are various types of disk image formats. For clarity the formats
are divided by means of their original purpose, e.g. were they intended
to be used in (disk) forensics or virtualization.

Disk images are usually block by block copies of the original data
source. Depending on the data source, the blocks can be bytes, sectors,
clusters, pages or similar. The disk image format may be further
enhanced with additional information, such as error detection, error
correction, data digest ([hash](hash.md), and compression.

## Forensics Disk Image formats

Forensics File Formats

* [Advanced Forensics Format (aff)](aff.md)
* [Advanced Forensic Framework 4 (aff4)](aff4.md)
* [Expert Witness Compression Format (ewf)](encase_image_file_format.md)
* [gfzip](gfzip.md)
* [ProDiscover image file format](prodiscover_image_file_format.md)
* [Raw Image Format](raw_image_format.md)
* [sgzip](sgzip.md)

## Virtualization Disk Image formats

* [Open Virtualization Format (ovf)](open_virtualization_format_(ovf).md)
* [Parallels Virtual Hard Disk Format](parallels_virtual_hard_disk_format.md)
* [QCOW Image Format](qcow_image_format.md)
* [Virtual Disk Image (vdi)](virtual_disk_image_(vdi).md)
* [Virtual Hard Disk (vhd)](virtual_hard_disk_(vhd).md)
* [VMWare Virtual Disk Format (vmdk)](vmware_virtual_disk_format_(vmdk).md)

## Other Disk Image formats

[Mac OS X](mac_os_x.md) has support for various disk image types
build-in, some of which are:

* read-write disk image (.dmg): [raw](raw_image_format.md),
  [UDIF](http://newosxbook.com/DMG.html), NDIF
* [Sparse disk image (.spareimage)](sparse_image_format.md)
* [Sparse bundle disk image (.sparsebundle)](sparse_bundle_image_format.md)

[Windows](windows.md)

* [Windows Imaging File Format (wim)](windows_imaging_file_format_(wim).md)
