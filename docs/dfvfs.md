---
tags:
  -  Open Source Software
  -  Disk Analysis
  -  Linux
  -  MacOS
  -  Windows
---
dfVFS, or Digital Forensics Virtual File System, provides read-only
access to file-system objects from various storage media types and file
formats. The goal of dfVFS is to provide a generic interface for
accessing file-system objects, for which it uses several back-ends that
provide the actual implementation of the various storage media types,
volume systems and file systems.

dfVFS is currently implemented as a Python module.

## Supported Formats

The information below is based of version 20221207.

### Storage media types

- [Encase image file format](encase_image_file_format.md) or EWF (EWF-E01,
  EWF-Ex01, EWF-S01) using [libewf](libewf "wikilink")
- Mac OS disk image using [libmodi](libmodi "wikilink")
  - Sparse bundle disk image
  - Sparse disk image
  - Universal Disk Image Format (UDIF) image
- Parallels Hard Disk image format version 2 using [libphdi](libphdi "wikilink")
- [QCOW Image Format](qcow_image_format.md) or QCOW using
  [libqcow](libqcow.md "wikilink")
  - currently no differential image support
- [Raw Image Format](raw_image_format.md) RAW using [libsmraw](libsmraw.md)
- Storage media devices using [libsmdev](libsmdev.md)
- [Virtual Disk Image (vdi)](virtual_disk_image_(vdi).md) or VHD(X) using
  [libvhdi](libvhdi.md "wikilink")
- [VMWare Virtual Disk Format (vmdk)](vmware_virtual_disk_format_(vmdk).md)
  using [libvmdk](libvmdk.md "wikilink")
  - currently no differential image support

### Volume systems

- [Apple Partition Map](apm.md) or APM using
  [sleuthkit](sleuthkit.md "wikilink") and [pytsk](pytsk "wikilink")
- Apple File System or APFS container version 2 using
  [libfsapfs](libfsapfs.md "wikilink")
- [BitLocker Disk Encryption](bitlocker_disk_encryption.md) or BDE using
  [libbde](libbde.md)
- Core Storage (CS) including [FileVault Disk
  Encryption](filevault_disk_encryption.md) or FVDE, or FileVault 2 using
  [libfvde](libfvde.md "wikilink")
- [GPT](gpt.md) using [libvsgpt](libvsgpt "wikilink") with fallback to
  [sleuthkit](sleuthkit.md "wikilink") and [pytsk](pytsk "wikilink")
- [Linux Logical Volume Manager](linux_logical_volume_manager_(lvm).md) or
  Linux LVM using [libvslvm](libvslvm.md "wikilink")
  - At the moment only single physical volume LVM support
- [Linux Unified Key Setup](linux_unified_key_setup_(luks).md) or LUKS using
  [libluksde](libluksde.md "wikilink")
- [MBR](mbr.md) using [sleuthkit](sleuthkit.md "wikilink") and
  [pytsk](pytsk "wikilink")
- [Windows Shadow Volumes](windows_shadow_volumes.md) or VSS using
  [libvshadow](libvshadow.md "wikilink")

### File systems

- Apple File System or APFS version 2 using [libfsapfs](libfsapfs.md "wikilink")
- [Extended File System (ext)](extended_file_system_(ext).md) version 2, 3, 4
  using [libfsext](libfsext "wikilink") with fallback to
  [sleuthkit](sleuthkit.md "wikilink") and [pytsk](pytsk "wikilink")
- [FAT-12](fat.md), FAT-16, FAT-32 and exFAT using
  [sleuthkit](sleuthkit.md "wikilink") and [pytsk](pytsk "wikilink") with
  fallback to [libfsfat](libfsfat "wikilink")
- [HFS+, HFSX](hfs+.md) using [libfshfs](libfshfs "wikilink") with fallback to
  [sleuthkit](sleuthkit.md "wikilink") and [pytsk](pytsk "wikilink")
- ISO-9660 version 1 using [sleuthkit](sleuthkit.md "wikilink") and
  [pytsk](pytsk "wikilink")
- [New Technology File System](new_technology_file_system_(ntfs).md) or NTFS
  version 3 using [libfsntfs](libfsntfs "wikilink") with fallback to
  [sleuthkit](sleuthkit.md "wikilink") and [pytsk](pytsk "wikilink")
- [Unix File System](unix_file_system_(ufs).md) or UFS version 1, 2 using
  [sleuthkit](sleuthkit.md "wikilink") and [pytsk](pytsk "wikilink")
- XFS version 4, 5 using [libfsxfs](libfsxfs "wikilink")

## History

dfVFS originates from [Plaso](plaso.md). It was largely rewritten and made into
a stand-alone project to provide more flexibility and allow other projects to
make use of the VFS functionality. dfVFS originally was named PyVFS, but that
name conflicted with another project.

## See Also

- [dfWinReg](dfwinreg.md)
- [Plaso](plaso.md)

## External Links

- [Project site](https://github.com/log2timeline/dfvfs/)
- [Project documentation](https://github.com/log2timeline/dfvfs/wiki)
- [Developing Python code using
  dfvfs](https://github.com/log2timeline/dfvfs/wiki/Development)
