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

- [Encase image file format](Encase_image_file_format "wikilink") or EWF
  (EWF-E01, EWF-Ex01, EWF-S01) using [libewf](libewf "wikilink")
- [QCOW Image Format](QCOW_Image_Format "wikilink") or QCOW using
  [libqcow](libqcow "wikilink")
- [Raw Image Format](Raw_Image_Format "wikilink") or (split) RAW using
  [libsmraw](libsmraw "wikilink")
- Storage media devices using [libsmdev](libsmdev "wikilink")
- [Virtual Disk Image (VDI)](Virtual_Disk_Image_(VDI) "wikilink") or VHD
  using [libvhdi](libvhdi "wikilink")
- [VMWare Virtual Disk Format
  (VMDK)](VMWare_Virtual_Disk_Format_(VMDK) "wikilink") using
  [libvmdk](libvmdk "wikilink")

### Volume systems

- using [sleuthkit](sleuthkit "wikilink") and [pytsk](pytsk "wikilink")
  - [APM](APM "wikilink")
  - [GPT](GPT "wikilink")
  - [MBR](MBR "wikilink")
- [BitLocker Disk Encryption](BitLocker_Disk_Encryption "wikilink") or
  BDE using [libbde](libbde "wikilink")
- [FileVault Disk Encryption](FileVault_Disk_Encryption "wikilink") or
  FVDE, or FileVault 2 using [libfvde](libfvde "wikilink")
- [Linux Logical Volume
  Manager](Linux_Logical_Volume_Manager_(LVM) "wikilink") or Linux LVM
  using [libvslvm](libvslvm "wikilink")
- [Windows Shadow Volumes](Windows_Shadow_Volumes "wikilink") or VSS
  using [libvshadow](libvshadow "wikilink")

Upcoming:

- [Linux Unified Key Setup](Linux_Unified_Key_Setup_(LUKS) "wikilink")
  or LUKS using [libluksde](libluksde "wikilink")

### File systems

- using [sleuthkit](sleuthkit "wikilink") and [pytsk](pytsk "wikilink")
  - [Extended File System (Ext)](Extended_File_System_(Ext) "wikilink")
    version 2, 3, 4
  - [FAT](FAT "wikilink")
  - [HFS, HFS+, HFSX](HFS+ "wikilink")
  - [New Technology File System
    (NTFS)](New_Technology_File_System_(NTFS) "wikilink") version 3
  - [Unix File System (UFS)](Unix_File_System_(UFS) "wikilink") version
    1, 2

## History

dfVFS originates from the [Plaso project](plaso "wikilink"). It was
largely rewritten and made into a stand-alone project to provide more
flexibility and allow other projects to make use of the VFS
functionality. dfVFS originally was named PyVFS, but that name
conflicted with another project.

## See Also

- [dfwinreg](dfwinreg "wikilink")
- [plaso](plaso "wikilink")

## External Links

- [Project site](https://github.com/log2timeline/dfvfs/)
- [Project documentation](https://github.com/log2timeline/dfvfs/wiki)
- [Developing Python code using
  dfvfs](https://github.com/log2timeline/dfvfs/wiki/Development)