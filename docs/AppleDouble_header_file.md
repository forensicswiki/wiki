A separate file in a filesystem containing the [Apple resource
fork](http://en.wikipedia.org/wiki/Resource_fork) for a related data
file, developed by Apple for A/UX and therefore compatible with other
filesystems including those mounted remotely. They are heavily used
under [Mac OS X](Mac_OS_X "wikilink").

This file is named the same as the data file, with "`._`" prepended to
the original name. These header files are automatically included in ZIP
files under a hierarchy starting with "`__MACOSX`" when utilizing the
Finder's "Archive as..." function.

## References

<http://users.phg-online.de/tk/netatalk/doc/Apple/v1/>
from "A/UX Toolbox: Macintosh ROM Interface manual", Chapter 6 File
Systems and File Formats

identifies the magic number `0x00051607` for AppleDouble files as the
first 4 bytes in the file

<!-- -->

<http://en.wikipedia.org/wiki/AppleDouble>
background and additional information

<!-- -->

<http://www.ietf.org/rfc/rfc1740.txt>
MIME Encapsulation of Macintosh files - MacMIME

[Category:File Formats](Category:File_Formats "wikilink")