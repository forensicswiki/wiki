**Snorkel** is a Java software library that is used by developers of
forensic software. Snorkel is not a standalone forensic application, but
it is an important piece of infrastructure that can be used by many
forensic applications: Snorkel gives access to digital evidence files,
file systems, files, slack space, unallocated clusters, etc. This type
of access is a key enabler in the development of forensic software
systems, ranging from single-purpose stand-alone tools to integrated
forensic processing systems.

Snorkel is developed by the Netherlands Forensic Institute

# Features

Snorkel recognizes and gives access to numerous storage formats for
digital evidence, disk partitioning schemes, volume managers, file
systems, and structured files. The formats supported are summarized
below.

## Image File Formats Understood

|                    |                                                               |
|--------------------|---------------------------------------------------------------|
| Image file formats | [EnCase](Encase_image_file_format "wikilink")                 |
|                    | [RAW (dd)](Raw_Image_Format "wikilink")                       |
|                    | [VMWare (VMDK)](VMWare_Virtual_Disk_Format_(VMDK) "wikilink") |

## File Systems Understood

|                      |                                                                               |
|----------------------|-------------------------------------------------------------------------------|
| Volume managers      | [Windows (LDM)](Logical_Disk_Manager_(LDM) "wikilink")                        |
| Partitioning schemes | PC/MBR                                                                        |
|                      | Apple                                                                         |
|                      | GPT                                                                           |
|                      | BSD                                                                           |
| File systems         | Windows ([FAT](FAT "wikilink"), [NTFS](NTFS "wikilink"))                      |
|                      | Apple ([MFS](MFS "wikilink"), [HFS](HFS "wikilink"), [HFS+](HFS+ "wikilink")) |
|                      | Linux ([EXT](Ext3 "wikilink"), [Reiser](Reiserfs "wikilink"))                 |
|                      | Solaris, BSD ([UFS](UFS "wikilink"))                                          |
|                      | CD ([ISO9660](ISO9660 "wikilink"), Joliet)                                    |
| File Formats         | Windows registry (Win 9x, NT)                                                 |
|                      | Microsoft Office (OLE2)                                                       |

## License Notes

Snorkel is has a proprietary license. An evaluation version is available
from the website.

# External Links

- [the Netherlands Forensic
  Institute](http://www.forensischinstituut.nl/)
- [Snorkel website](http://www.holmes.nl/NFIlabs/Snorkel)