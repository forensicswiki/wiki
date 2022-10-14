---
tags:
  -  File Formats
  -  Datbase
  -  Windows
---
[Lotus](lotus.md) [Notes](notes.md) and
[Domino](domino.md)**
database to store e-mails, appointments, tasks, contacts, notes, etc.

## MIME types

- application/x-lotus-notes
- application/vnd.lotus-notes

## File signature

The NSF has the following file signature: hexadecimal: 1a 00 (which is
often followed by: 00 04 00 00)

## File types

NSF defines an on-disk structure (ODS) version.

- 16 (Notes 1.x, 2x)
- 17 (Notes 3.x)
- 20 (Notes 4.x)
- 41 (Notes 5.x)
- 43 (Notes 6, 7 and 8)
- 48 (Notes 8)
- 51 (Notes 8.5)

One significant change in the Record Relocation Vector (RRV) seems to be
introduced in format revision 22.

## Contents

The NSF basically is a collection of **Notes**. A **Note** in concept is
similar to that of an object or item; mainly a container for data and
metadata. **Notes** are used to store a vast variety of items, e.g.
emails, documents, appointments, log-entries, data-views, forms, etc.

## Encryption

Notes can use various forms of encryption see: [Notes from Support:
Notes Encryption - Locks for a Digital
World](http://www.ibm.com/developerworks/lotus/library/ls-Notes_Encryption/index.html).

## See also

- [Lotus C API Notes/Domino 7.0
  Reference](http://www-12.lotus.com/ldd/doc/tools/c/7.0/api70ref.nsf)
- [Wikipedia IBM Lotus
  Notes](http://en.wikipedia.org/wiki/Notes_Storage_Format)
- [Notes Storage Facility (NSF) database file
  format.pdf](https://googledrive.com/host/0B3fBvzttpiiSbkI4d1pRQmdMNWc/Notes%20Storage%20Facility%20(NSF)%20database%20file%20format.pdf),
  by the [libnsfdb project](libnsfdb.md), February 2010
- [Lotus Notes
  Forensics](http://www.systoolsgroup.com/forensics/lotus-notes/)