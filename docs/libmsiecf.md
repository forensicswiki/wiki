---
tags:
  -  Libyal
  -  Analysis
  -  LGPL
  -  Tools
---
The **libmsiecf** package contains a library and applications to read
the [MSIE Cache File](internet_explorer_history_file_format.md)
format.

## Tools

The libmsiecf package contains the following tools:

- **msiecfexport**, which exports the items stored in MSIECF files.
- **msiecfinfo**, which shows the information about MSIECF files.

## Examples

Exporting items from an index.dat:

    msiecfexport -m items index.dat

Exporting recovered items from an index.dat:

    msiecfexport -m recovered index.dat

Exporting an index.dat from a Chinese Windows installation:

    msiecfexport -c windows-936 index.dat

## History

Libmsiecf was created by [Joachim Metz](joachim_metz.md) in
2009, while working for [Hoffmann
Investigations](http://en.hoffmannbv.nl/).

Libmsiecf is a rewrite of
[pasco](http://sourceforge.net/projects/odessa/) with support for more
recent versions of [MSIE Cache
Files](internet_explorer_history_file_format.md)

## See Also

- [MSIE Cache Files](internet_explorer_history_file_format.md)

## External Links

- [Project site](https://github.com/libyal/libmsiecf/)

