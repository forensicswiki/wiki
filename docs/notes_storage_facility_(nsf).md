---
tags:
  - Database
  - File Formats
  - Windows
---
Lotus Notes and Domino database to store e-mails, appointments, tasks,
contacts, notes, etc.

## MIME types

* application/x-lotus-notes
* application/vnd.lotus-notes

## File signature

The NSF has the following file signature: hexadecimal: 1a 00 (which is
often followed by: 00 04 00 00)

## File types

NSF defines an on-disk structure (ODS) version.

* 16 (Notes 1.x, 2x)
* 17 (Notes 3.x)
* 20 (Notes 4.x)
* 41 (Notes 5.x)
* 43 (Notes 6, 7 and 8)
* 48 (Notes 8)
* 51 (Notes 8.5)

One significant change in the Record Relocation Vector (RRV) seems to be
introduced in format revision 22.

## Contents

The NSF basically is a collection of **Notes**. A **Note** in concept is
similar to that of an object or item; mainly a container for data and
metadata. **Notes** are used to store a vast variety of items, e.g.
emails, documents, appointments, log-entries, data-views, forms, etc.

## Encryption

Notes can use various forms of encryption.

## See also

* [Wikipedia: HCL Domino](https://en.wikipedia.org/wiki/HCL_Domino)
* [Notes Storage Facility (NSF) database file format.pdf](https://github.com/libyal/libnsfdb/blob/main/documentation/Notes%20Storage%20Facility%20(NSF)%20database%20file%20format.asciidoc),
  by the [libnsfdb project](libnsfdb.md), February 2010
* [Lotus Notes Forensics](https://www.systoolsgroup.com/forensics/lotus-notes/)
