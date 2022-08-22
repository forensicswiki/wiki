## Image types

There are multiple types of VMWare Virtual Disk Format (VMDK) files:

- **2GbMaxExtentFlat** (or **twoGbMaxExtentFlat**); descriptor file
  (name.vmdk) with RAW extent data files (name-f###.vmdk). This image
  type is basically a [split RAW image](Raw_Image_Format "wikilink").
- **2GbMaxExtentSparse** (or **twoGbMaxExtentSparse**); descriptor file
  (name.vmdk) with VMDK sparse extent data files (name-s###.vmdk)
- **monolithicFlat**; descriptor file (name.vmdk) with RAW extent data
  file (name-f001.vmdk). This image type is basically a [RAW
  image](Raw_Image_Format "wikilink").
- **monolithicSparse**; VMDK sparse extent data file (name.vmdk) which
  contains the descriptor file data.

## Descriptor file

The descriptor file defines how and where the data of the VMDK image is
stored. The data is stored in extent data files.

## Extent data file types

There are multiple types extent data files:

- RAW extent data file or device
- VMDK sparse extent data file
- COWD sparse extent data file

Note that the **VMDK sparse extent data file** can be in a **dirty
state** (or uncleanShutdown).

## See Also

- [Disk Images](Disk_Images "wikilink")

## External Links

- [Virtual Disk Format
  5.0](http://www.vmware.com/support/developer/vddk/vmdk_50_technote.pdf?src=vmdk),
  by [VMWare](VMWare "wikilink")
- [VMware Virtual Disk (VMDK) format
  specification](https://googledrive.com/host/0B3fBvzttpiiSQ1dOUmhqMkR2cm8/VMWare%20Virtual%20Disk%20Format%20(VMDK).pdf),
  by the [libvmdk project](libvmdk "wikilink")

## Tools

- [libvmdk](libvmdk "wikilink")
- [VMWare VMDK Data
  Recovery](http://www.bitrecover.com/vmdk-recovery-software/) - Allows
  you to recover data from corrupt and crashed VMDK VMware virtual
  machine disk image files.

[Category:File Formats](Category:File_Formats "wikilink")