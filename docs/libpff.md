---
tags:
  - Libyal
  - Analysis
  - LGPL
  - Tools
---
The **libpff** package contains a library and tools to read the
[Personal Folder File (PAB, PST, OST)](personal_folder_file_(pab,_pst,_ost).md)
format.

## Features

Libpff is a cross-platform shared library that support PST, OST and PAB
files. Currently the data in PAB files is only partially supported.
Support was added to deal with corrupted files and to recover data.

## Tools

The **libpff** package contains the following tools:

- **pffexport**, which exports the items stored in PAB, PST and OST
  (PFF) files
- **pffinfo**, which shows information about PFF files.

**pffrecover**, has been replaced by **pffexport -m recovered**

## History

Libpff was created by [Joachim Metz](joachim_metz.md) in 2008,
while working for Hoffmann Investigations.

Libpff is a rewrite of earlier work on the PST file format by the
[libpst project](libpst.md).

## See Also

- [Personal Folder File (PAB, PST,
  OST)](personal_folder_file_(pab,_pst,_ost).md)
- [libpst](libpst.md)

## External Links

- [Project site](https://github.com/libyal/libpff/)
- [Building libpff and tools from source](https://github.com/libyal/libpff/wiki/Building)
