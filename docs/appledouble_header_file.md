---
tags:
  - File Formats
  - MacOS
---
A separate file in a filesystem containing the
[Apple resource fork](https://en.wikipedia.org/wiki/Resource_fork) for a
related data file, developed by Apple for A/UX and therefore compatible with
other filesystems including those mounted remotely. They are heavily used under
[Mac OS X](mac_os_x.md).

This file is named the same as the data file, with ".\_" prepended to the
original name. These header files are automatically included in ZIP files under
a hierarchy starting with "\_\_MACOSX" when utilizing the Finder's "Archive
as..." function.

Per "A/UX Toolbox: Macintosh ROM Interface manual", Chapter 6 File Systems and
File Formats, AppleDouble files can be idenfied by the magic number 0x00051607
stored in the first 4 bytes of the file.

## External Links

* [A/UX® Toolbox: Macintosh® ROM Interface](https://bitsavers.org/pdf/apple/mac/a_ux/aux_2.0/030-0787-A_AUX_Toolbox_Macintosh_ROM_Interface_1990.pdf),
* [Wikipedia: AppleSingle and AppleDouble formats](https://en.wikipedia.org/wiki/AppleSingle_and_AppleDouble_formats)
* [RFC 1740 - MIME Encapsulation of Macintosh files - MacMIME](https://www.ietf.org/rfc/rfc1740.txt)
