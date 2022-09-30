---
tags:
  -  File Formats
---
[Outlook Express](outlook_express.md) uses the **Outlook
Express Database (DBX)** database to store emails, folders, etc. The DBX
was introduced in version 5. Earlier versions of OE use different file
formats.

## MIME types

## File signature

OE5 DBX files start with hexadecimal: 0xcf 0xad 0x12 0xfe. For now it is
assumed that this is the file signature. It is followed by a content
class identifier (CLSID), which is unique for the type of DBX file.

## File types

Although DBX probably contains a minor/major version (offset: 20 and 24)
until now it is unknown how it affects the file type.

## Contents

The contents of a DBX file is dependent on the content CLSID.

- Message Database (CLSID: 6F74FDC5-E366-11d1-9A4E-00C04FA309D4)
- Folder Database (CLSID: 6F74FDC6-E366-11d1-9A4E-00C04FA309D4)

## Encryption

## External Links

- [Outlook Express
  Wikipedia](http://en.wikipedia.org/wiki/Outlook_Express)
- [Outlook Express dbx file format by Arne
  Schloh](http://oedbx.aroh.de/)
- [Outlook Express Version 5.0 file
  format](http://www.fpns.net/willy/DBX-FMT.HTM)
- [libdbx](http://sourceforge.net/projects/ol2mbox/), see FILE-FORMAT in
  the package.

[Category:File Formats](category:file_formats.md)
