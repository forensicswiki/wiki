---
tags:
  - File Formats
---
The **Object Linking and Embedding (OLE) Compound File (CF)** is used in
other file formats as its underlying container file. It allows data to
be stored in multiple streams.

The OLECF is also known as:

* Compound Binary File (current name used by [Microsoft](microsoft.md)
* Compound Document File (name used by OpenOffice)
* OLE2 file

## MIME types

Because the OLECF by itself is just a container it does not use a mime
type. A mime type assigned to an OLECF refers to its contents.

## File signature

The OLECF has the following file signature (as a hexadecimal byte
sequence):

    d0 cf 11 e0 a1 b1 1a e1

For earlier beta version of the format the following signature was used:

    0e 11 fc 0d d0 cf 11 0e

The OLECF has no distinct footer.

## Contents

The OLECF uses a FAT-like file system to define blocks that are assigned
to the stream using multiple allocation tables. It uses a directory
structure to define the name of the streams.

The OLECF is used to store:

* [Microsoft Office](microsoft_office.md) 97-2003 documents:
  * [Word Document (doc)](word_document_(doc).md)
  * [Excel Spreadsheet (xls)](excel_spreadsheet_(xls).md)
  * Powerpoint Presentation (ppt)
* MSN (Toolbar) (C:\Documents and Settings\\%USERNAME%\Local
  Settings\Application Data\Microsoft\MSNe\msninfo.dat)
* [Jump Lists](jump_lists.md)
* StickyNotes.snt
* [Thumbs.db](thumbs.db.md)
* Windows Installer (.msi) and patch file (.msp)
* Windows Search (srchadm.msc)

## External Links

* [Compound Binary File Specification](https://download.microsoft.com/download/0/B/E/0BE8BDD7-E5E8-422A-ABFD-4342ED7AD886/WindowsCompoundBinaryFileFormatSpecification.pdf),
  by [Microsoft](microsoft.md). Be warned this file contains at least one
  error: the directory entry name length is a size in bytes not in characters.
* [MS-CFB: Compound File Binary File Format](https://learn.microsoft.com/en-us/openspecs/windows_protocols/ms-cfb/53989ce4-7b05-4f8d-829b-d08d6148375b),
  by [Microsoft](microsoft.md)
* [Microsoft Compound Document File Format](http://www.openoffice.org/sc/compdocfileformat.pdf),
  by OpenOffice.org
* [OLE Compound File format specification](https://github.com/libyal/libolecf/blob/main/documentation/OLE%20Compound%20File%20format.asciidoc),
  by the [libolecf project](libolecf.md)

### Office VBA

* [MS-OVBA: Office VBA File Format Structure](https://learn.microsoft.com/en-us/openspecs/office_file_formats/ms-ovba/575462ba-bf67-4190-9fac-c275523c75fc),
  by [Microsoft](microsoft.md)

## Tools

* [libolecf](libolecf.md)
* [MiTec Structured Storage Viewer](http://www.mitec.cz/ssv.html)
* [oletools](https://github.com/decalage2/oletools)
