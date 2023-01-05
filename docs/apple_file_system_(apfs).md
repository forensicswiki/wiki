---
tags:
  - File Systems
  - MacOS
---
APFS, or Apple File System, is the file system designed by [Apple](apple_inc.md)
to supersede [HFS+](hfs+.md) and take advantage of flash/SSD storage and native
encryption support. APFS also introduced file system snapshots, support for
sparse files, and greater time stamp granularity.

It was announced at the Apple Worldwide Developer Conference (WWDC) in
2016 and is meant to be used with watchOS, iOS, tvOS, and macOS. A
Developer Preview version was first released with macOS Sierra 10.12.
APFS became the default file system with the release of macOS High
Sierra 10.13 released to the public on September 25, 2017.

## Features

Max file size of 2<sup>63</sup> bytes was mantinted from
[HFS+](hfs+.md) and new features include:

- Snapshots (can be mounted read-only)
- Atomic Safe-save (single transaction save)
- File and directory clones (without using additional storage space)
- Space-Sharing (volumes grow and shrink, sharing underlying free space)
- Sparse file support (more efficient empty space representation)
- Fast directory sizing (more efficient total space computation of a
  directory)

<CENTER>
<TABLE Border=1 cellpadding=2 cellspacing=0 width=75%>
<TR>
<TD>

<B>Feature</B>

</TD>
<TD>

<B>Mac OS Extended (HFS+)</B>

</TD>
<TD>

<B>Apple File System (APFS)</B>

</TD>
</TR>
<TR>
<TD>

Number of allocation blocks (Maximum Number of Files)

</TD>
<TD>

2<sup>32</sup> (4 billion)

</TD>
<TD>

2<sup>63</sup> (9 quintillion)

</TD>
</TR>
<TR>
<TD>

File IDs (iNode numbering)

</TD>
<TD>

32-bit

</TD>
<TD>

64-bit

</TD>
</TR>
<TR>
<TD>

Time stamp granularity

</TD>
<TD>

1 second

</TD>
<TD>

1 nanosecond

</TD>
</TR>
<TR>
<TD>

Crash protection

</TD>
<TD>

Journaled

</TD>
<TD>

Copy-on-write

</TD>
</TR>
<TR>
<TD>

Full disk encryption

</TD>
<TD>

Yes (FileVault)

</TD>
<TD>

Yes (native)

</TD>
</TR>
<TR>
<TD>

Extended Attribute Support

</TD>
<TD>

Yes (retrofitted)

</TD>
<TD>

Yes (native)

</TD>
</TR>
</table>
</CENTER>

## External Links

* [Apple File System Guide - Introduction](https://developer.apple.com/library/archive/documentation/FileManagement/Conceptual/APFS_Guide/Introduction/Introduction.html)
* [Introducing Apple File System](http://devstreaming.apple.com/videos/wwdc/2016/701q0pnn0ietcautcrv/701/701_introducing_apple_file_system.pdf)
* [Slides from filesystem talk at MacSysAdmin 2016 by Rich Trouton](https://derflounder.wordpress.com/2016/10/05/slides-from-the-whats-new-in-file-system-session-at-macsysadmin-2016/)
* [Creating APFS volumes by Howard Oakley](https://eclecticlight.co/2017/04/08/how-to-make-your-own-apfs-volume/)
