The **libmsiecf** package contains a library and applications to read
the [MSIE Cache File](Internet_Explorer_History_File_Format "wikilink")
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

Libmsiecf was created by [Joachim Metz](Joachim_Metz "wikilink") in
2009, while working for [Hoffmann
Investigations](http://en.hoffmannbv.nl/).

Libmsiecf is a rewrite of
[pasco](http://sourceforge.net/projects/odessa/) with support for more
recent versions of [MSIE Cache
Files](Internet_Explorer_History_File_Format "wikilink")

## See Also

- [MSIE Cache Files](Internet_Explorer_History_File_Format "wikilink")

## External Links

- [Project site](https://github.com/libyal/libmsiecf/)

[Category:Libyal](Category:Libyal "wikilink")