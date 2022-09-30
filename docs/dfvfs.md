---
tags:
  - No Category
---
dfVFS, or Digital Forensics Virtual File System, provides read-only
access to file-system objects from various storage media types and file
formats. The goal of dfVFS is to provide a generic interface for
accessing file-system objects, for which it uses several back-ends that
provide the actual implementation of the various storage media types,
volume systems and file systems.

dfVFS is currently implemented as a Python module.

## Supported Formats

The information below is based of version 20160918.

### Storage media types

- [Encase image file format](encase_image_file_format.md) or EWF
  (ewf-e01,.md) using [libewf](libewf "wikilink")
- [QCOW Image Format](qcow_image_format.md) or QCOW using
  [libqcow](libqcow.md)
- [Raw Image Format](raw_image_format.md) RAW using
  [libsmraw](libsmraw.md)
- Storage media devices using [libsmdev](libsmdev.md)
- [Virtual Disk Image (vdi)](virtual_disk_image_(vdi).md) or VHD
  using [libvhdi](libvhdi.md)
- [VMWare Virtual Disk Format
  (vmdk)](vmware_virtual_disk_format_(vmdk).md) using
  [libvmdk](libvmdk.md)

### Volume systems

- using [sleuthkit](sleuthkit.md) and [pytsk](pytsk "wikilink")
  - [APM](apm.md)
  - [GPT](gpt.md)
  - [MBR](mbr.md)
- [BitLocker Disk Encryption](bitlocker_disk_encryption.md) or
  BDE using [libbde](libbde.md)
- [FileVault Disk Encryption](filevault_disk_encryption.md) or
  FVDE, or FileVault 2 using [libfvde](libfvde.md)
- [Linux Logical Volume
  Manager](linux_logical_volume_manager_(lvm).md) or Linux LVM
  using [libvslvm](libvslvm.md)
- [Windows Shadow Volumes](windows_shadow_volumes.md) or VSS
  using [libvshadow](libvshadow.md)

Upcoming:

- [Linux Unified Key Setup](linux_unified_key_setup_(luks).md)
  or LUKS using [libluksde](libluksde.md)

### File systems

- using [sleuthkit](sleuthkit.md) and [pytsk](pytsk "wikilink")
  - [Extended File System (ext)](extended_file_system_(ext).md)
    version 2, 3, 4
  - [FAT](fat.md)
  - [HFS, HFS+, HFSX](hfs+.md)
  - [New Technology File System
    (ntfs)](new_technology_file_system_(ntfs).md) version 3
  - [Unix File System (ufs)](unix_file_system_(ufs).md) version
    1, 2

## History

dfVFS originates from the [Plaso project](plaso.md). It was
largely rewritten and made into a stand-alone project to provide more
flexibility and allow other projects to make use of the VFS
functionality. dfVFS originally was named PyVFS, but that name
conflicted with another project.

## See Also

- [dfwinreg](dfwinreg.md)
- [plaso](plaso.md)

## External Links

- [Project site](https://github.com/log2timeline/dfvfs/)
- [Project documentation](https://github.com/log2timeline/dfvfs/wiki)
- [Developing Python code using
  dfvfs](https://github.com/log2timeline/dfvfs/wiki/Development)