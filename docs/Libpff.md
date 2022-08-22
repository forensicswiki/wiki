The **libpff** package contains a library and tools to read the
[Personal Folder File (PAB, PST,
OST)](Personal_Folder_File_(PAB,_PST,_OST) "wikilink") format.

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

Libpff was created by [Joachim Metz](Joachim_Metz "wikilink") in 2008,
while working for [Hoffmann Investigations](http://en.hoffmannbv.nl/).

Libpff is a rewrite of earlier work on the PST file format by the
[libpst project](libpst "wikilink").

## See Also

- [Personal Folder File (PAB, PST,
  OST)](Personal_Folder_File_(PAB,_PST,_OST) "wikilink")
- [libpst](libpst "wikilink")

## External Links

- [Project site](https://github.com/libyal/libpff/)
- [Building libpff and tools from
  source](https://github.com/libyal/libpff/wiki/Building)

[Category:Libyal](Category:Libyal "wikilink")