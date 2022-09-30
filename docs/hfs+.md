---
tags:
  -  File Systems
---
HFS+, or Hierarchical File System Plus, is the file system designed by
[Apple Computer](http://www.apple.com) to supersede HFS.

HFS+ was first introduced with Mac OS 8.1, one of the biggest
differences was the lower allocation block size of 4 KiB (4096 bytes),
which increased performance and lowered fragmentation (See: Technical
Note TN1121). It also implemented Unicode (rather than Mac proprietary
encoding formats) for naming files. HFSX is a variant of HSF+ that is
case sensitive.

Mac OS X 10.6, dropped support for formatting or writing (classic) HFS
and macOS 10.15 can no longer read (classic) HFS
[1](https://en.wikipedia.org/wiki/Hierarchical_File_System).

Apple technical notes are available for the HFS+ file system from their
[website](http://developer.apple.com/cgi-bin/search.pl?q=HFS+&num=10&site=default_collection).

## Features

There are structurally many differences between HFS and HFS+, which are
listed below (Also see: Technical Note TN1150).


<CENTER>
<TABLE Border=1 cellpadding=2 cellspacing=0 width=75%>
<TR>
<TD>

<B>Feature</B>

</TD>
<TD>

<B>HFS</B>

</TD>
<TD>

<B>HFS Plus</B>

</TD>
<TD>

<B>Benefit/Comment</B>

</TD>
</TR>
<TR>
<TD>

User visible name

</TD>
<TD>

Mac OS Standard

</TD>
<TD>

Mac OS Extended

</TD>
<TD>
</TD>
</TR>
<TR>
<TD>

Number of allocation blocks

</TD>
<TD>

16 bits worth

</TD>
<TD>

32 bits worth

</TD>
<TD>

Radical decrease in disk space used on large

`                 volumes, and a larger number of files per volume.`

</TD>
</TR>
<TR>
<TD>

Long file names

</TD>
<TD>

31 characters

</TD>
<TD>

255 characters

</TD>
<TD>

Obvious user benefit; also improves

`                 cross-platform compatibility`

</TD>
</TR>
<TR>
<TD>

File name encoding

</TD>
<TD>

Mac OS encoding (such as MacRoman)

</TD>
<TD>

Unicode

</TD>
<TD>

Allows for international-friendly file names,

`                 including mixed script names`

</TD>
</TR>
<TR>
<TD>

File/folder attributes

</TD>
<TD>

Support for fixed size attributes (FileInfo and

`                 ExtendedFileInfo)`

</TD>
<TD>

Allows for future meta-data extensions

</TD>
<TD>

Future systems may use metadata for a richer

`                 Finder experience`

</TD>
</TR>
<TR>
<TD>

OS startup support

</TD>
<TD>

System Folder ID

</TD>
<TD>

Also supports a dedicated startup file

</TD>
<TD>

May help non-Mac OS systems to boot from HFS

`                 Plus volumes`

</TD>
</TR>
<TR>
<TD>

catalog node size

</TD>
<TD>

512 bytes

</TD>
<TD>

4 KiB (4096 bytes)

</TD>
<TD>

Maintains efficiency in the face of the other

`                 changes. (This larger catalog node size is due to`
`                 the much longer file names [512 bytes as opposed to`
`                 32 bytes], and larger catalog records (because of`
`                 more/larger fields)).`

</TD>
</TR>
<TR>
<TD>

Maximum file size

</TD>
<TD>

2<sup>31</sup> bytes

</TD>
<TD>

2<sup>63</sup> bytes

</TD>
<TD>

Obvious user benefit, especially for multimedia

`                 content creators.`

</td>
</tr>
<TR>
<TD>

Hard links

</TD>
<TD>

Not supported

</TD>
<TD>

File only

</TD>
<TD>
</tr>
<TR>
<TD>

Symbolic links

</TD>
<TD>

Not supported

</TD>
<TD>

Directories and files

</TD>
<TD>
</tr>
</table>
</CENTER>

## File system metadata file entries

An HFS volume contains multiple special file entries:

1.  Catalog file - Describes the folder and file hierarchy of the
    volume. It is organized as a "balanced tree" for fast and efficient
    searches
2.  Extents overflow file - Additional extents (contiguous allocation
    blocks allocated to forks) are stored in a b-tree in this file
3.  Allocation file - Specifies whether an allocation block is free
    (similar to \$Bitmap in NTFS). This is stored in a bitmap,
    specifying a free allocation block with a "clear bit" (introduced in
    HFS+)
4.  Attributes file - Contains attribute information regarding files or
    folders (introduced in HFS+)
5.  Startup file - Allows computers to boot that do have built in
    support for HFS+ file systems (introduced in HFS+)

The first 16 catalog node identifiers (CNIDs) are reserved for special
file system metadata file entries. Note that these file entries are not
full fledged files, like for example on other file systems like NTFS.
These file entries do not appear to have a corresponding entry in the
catalog file.

## Journaling

HFS+ also implements journaling, which allows fast recovery in the case
of a crash or power outage. According to Apple, "The purpose of the
journal is to ensure that when a group of related changes are being
made, that either all of those changes are actually made, or none of
them are made."
[2](http://developer.apple.com/technotes/tn/tn1150.html#Journal)

## Date and time values

In HFS+ date and time values are stored in an unsigned 32-bit integer
containing the number of seconds since January 1, 1904 at 00:00:00
(midnight) UTC (GMT). This is slightly different from HFS where the date
and time value are stored using the local time. The maximum
representable date is February 6, 2040 at 06:28:15 UTC (GMT). The date
values do not account for leap seconds. They do include a leap day in
every year that is evenly divisible by four. This is sufficient given
that the range of representable dates does not contain 1900 or 2100,
neither of which have leap days. Also see: [Technical Note TN1150 - HFS
Plus Volume
Format](http://web.archive.org/web/20090214212148/http://developer.apple.com/technotes/tn/tn1150.html)

Converting HFS/HFS+ date and time values with Python:

    import datetime

    print datetime.datetime( 1904, 1, 1 ) + datetime.timedelta( seconds=0xCBDAF25B )

## Observations

Observed on Mac OS 10.15.7

HFS+ allows for the '/' character in file names. On Mac OS, Finder this
will be represented as a '/' but in Terminal it is replaced by ':'
seeing the same character is used as path segment separator. A file name
with a ':' created in Terminal will be shown as '/' in Finder. Finder
does not allow the creation of a file containing ':' in the name. A
symbolic link created in Terminal to a file with a ':' in name will not
convert the ':' character in the link target data. The Linux HFS+
implementation appears to apply a similar conversion logic as Terminal.

HFS+ stores U+2400 as U+0

## Also see

- [Apple File System (apfs)](apple_file_system_(apfs).md)

## External Links

- [Insided Macintosh: Files - Data Organization on
  Volumes](https://developer.apple.com/library/archive/documentation/mac/Files/Files-99.html),
  by Apple 1996
- Internet Archive Copy of: [Technical Note
  TN1121](http://web.archive.org/web/20090530120010/http://developer.apple.com/technotes/tn/tn1121.html),
  original location:
  <http://developer.apple.com/technotes/tn/tn1121.html#HFSPlus>
- Internet Archive Copy of: [Technical Note TN1150: HFS plus volume
  format](http://web.archive.org/web/20090214212148/http://developer.apple.com/technotes/tn/tn1150.html),
  original location:
  <http://developer.apple.com/technotes/tn/tn1150.html>
- Copy of: [Mac Forensics: Mac OS X and the HFS+ File
  System](http://cet4861.pbworks.com/w/file/fetch/71245694/mac.forensics.craiger-burke.IFIP.06.pdf)
  by P. Craiger, November 2005, original location:
  <http://www2.tech.purdue.edu/cit/Courses/cit556/readings/MacForensicsCraiger.pdf>
- [Using the HFSD journal for deleted ﬁle
  recovery](http://www.dfrws.org/2008/proceedings/p76-burghardt.pdf), by
  [Aaron Burghardt](aaron_burghardt.md), [Adam
  Feldman](adam_feldman.md), DRFWS 2008

## Tools

- [sleuthkit](sleuthkit.md) - partially supports HFS+/HSX, does
  not support (classic) HFS
  [3](https://wiki.sleuthkit.org/index.php?title=HFS)
- [HFSExplorer](http://www.catacombae.org/hfsexplorer/)

