---
tags:
  - Data Carving
  - Linux
  - Open Source Software
  - Tools
---
Foremost is a [Linux](linux.md) based program for
[recovering deleted files](recovering_deleted_data.md) and served as the basis for the more modern
[Scalpel](scalpel.md). The program uses a configuration file to specify
[headers and footers](file_formats.md) to search for. Intended to be run on
[disk images](disk_image.md), foremost can search through most any kind of data without worrying
about the format.

## Caution

Due to programming difficulties, foremost is limited to processing files smaller than 2GB.

Foremost's authors have recommended that practitioners use [Scalpel](scalpel.md) instead.

## History

First published in 2000, a major update was released in 2005 when Nick Mikus joined the project.

### Spinoffs

Foremost served as the basis for [Golden G. Richard III's](golden_g_richard_iii.md)
[Scalpel](scalpel.md), a significantly faster program to also recover deleted files. It has also
inspired [tcpxtract](tcpxtract.md), a program for extracting file from network traffic.

## See Also

* [File carving](file_carving.md)
* [File Carving Tools](tools_data_recovery.md#carving)
* [Recovering deleted data](recovering_deleted_data.md)
* [Scalpel](scalpel.md)
* [TCExtract](tcpxtract.md)

## External Links

* [Foremost on SourceForge](https://foremost.sourceforge.net/)
