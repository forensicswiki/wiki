---
tags:
  - Data Files
  - File Formats
  - Windows
---
[Microsoft Internet Explorer](internet_explorer.md) stores its web browsing
history in files named **index.dat** as of version 4 up to version 9.

## Overview

By design these index.dat files are cache files but are used to:

- keep a record of URLs that the browser has visited
- cookies that were created by a site
- temporary internet files that were downloaded in the cache during a
  visit to a size

Regardless of the information stored in the file, the file is named
index.dat.

**Note that not every file named index.dat is a MSIE History (Cache)
file.**

The file format of MSIE 4 is slightly different then that of MSIE 5 up
to 9. Most of the information on this page applies to the format used by
MSIE 5 - 9.

MSIE 3 probably uses similar records in its History (Cache) files.

## File Locations

The index.dat files are stored in multiple locations.

### MSIE 5 - 9

The actual location can vary per version of MSIE and version of
[Windows](windows.md).

On Windows 95/98 these files were located in the following locations:

    %systemdir%\Temporary Internet Files\Content.ie5
    %systemdir%\Cookies
    %systemdir%\History\History.ie5

On Windows 2000/XP the file locations have changed:

    %systemdir%\Documents and Settings\%username%\Local Settings\Temporary Internet Files\Content.ie5
    %systemdir%\Documents and Settings\%username%\Cookies
    %systemdir%\Documents and Settings\%username%\Local Settings\History\history.ie5

On Windows Vista/7

    %systemdir%\Users\%username%\AppData\Local\Microsoft\Windows\Temporary Internet Files\
    %systemdir%\Users\%username%\AppData\Local\Microsoft\Windows\Temporary Internet Files\Low\

Internet Explorer also keeps daily, weekly, and monthly history logs
that will be located in a sub directory of the global history e.g. on
Windows XP:

    %systemdir%\Documents and Settings\%username%\Local Settings\History\history.ie5

The folders will be named
`MSHist`<two-digit number><starting four-digit year><starting two-digit month><starting two-digit day><ending four-digit year><ending two-digit month><ending two-digit day>.
For example, the folder containing data from March 26, 2008 to March 27,
2008 might be named `MSHist012008032620080327`.

## File Header

The MSIE 4 History (Cache) file starts with the following ACSII string:
"Client UrlCache MMF Ver 4.7"

The MSIE 5 - 9 History (Cache) file starts with the following ACSII
string: "Client UrlCache MMF Ver 5.2"

This string (or signature) is followed (at byte offset 28) by a four
byte value containing the file size. The value is stored in
[little-endian](endianness.md) so the individual bytes must read
in reverse.

The file header also can contain the name of the cache directories. In
the URL records the cache directories are given as a number, with one
representing the first cache directory, two representing the second and
so on. The names of the cache directories are kept at byte offset 64 in
the file. Each directory entry is 12 bytes long of which the first eight
bytes contain the directory name.

## Allocation bitmap

The IE History File contains an allocation bitmap starting from offset
0x250 to 0x4000.

## Record Formats

Every record has a similar header that consists of 8 bytes.

    typedef struct _RECORD_HEADER {
      /* 000 */ char        Signature[4];
      /* 004 */ uint32_t    NumberOfBlocksInRecord;
    } RECORD_HEADER;

The size of the record can be determined from the number of blocks in
the record; per default the block size is 128 bytes. Therefore, a length
of

    05 00 00 00

would indicate five blocks (because the number is stored in
little-endian format) of 128 bytes for a total record length of 640
bytes. Note that even for allocated records the number of blocks value
cannot be fully relied upon.

The blocks that make up a record can have slack space.

Currently 4 types of records are known:

* URL
* REDR
* HASH
* LEAK

Note that the location and filename strings are stored in the local
codepage, normally these strings will only use the ASCII character set.
Chinese versions of Windows are known to also use extended characters as
well.

### URL Records

These records indicate URIs that were actually requested. They contain
the location and additional data like the web server's HTTP response.
They begin with the header, in hexadecimal:

    55 52 4C 20

This corresponds to the string `URL` followed by a space.

The definition for the structure in C99 format:

    typedef struct _URL_RECORD_HEADER {
      /* 000 */ char        Signature[4];
      /* 004 */ uint32_t    AmountOfBlocksInRecord;
      /* 008 */ FILETIME    LastModified;
      /* 010 */ FILETIME    LastAccessed;
      /* 018 */ FATTIME     Expires;
      /* 01c */
      // Not finished yet
    } URL_RECORD_HEADER;

    typedef struct _FILETIME {
      /* 000 */ uint32_t    lower;
      /* 004 */ uint32_t    upper;
    } FILETIME;

    typedef struct _FATTIME {
      /* 000 */ uint16_t    date;
      /* 002 */ uint16_t    time;
    } FATTIME;

The actual interpretation of the "LastModified" and "LastAccessed"
fields depends on the type of history file in which the record is
contained. As a matter of fact, Internet Explorer uses three different
types of history files, namely Daily History, Weekly History, and Main
History. Other "index.dat" files are used to store cached copies of
visited pages and cookies. The information concerning how to intepret
the dates of these different files can be found on Capt. Steve Bunting's
web page at the University of Delaware Computer Forensics Lab
(http://www.stevebunting.org/udpd4n6/forensics/index_dat2.htm). Please
be aware that most free and/or open source index.dat parsing programs,
as well as quite a few commercial forensic tools, are not able to
correctly interpret the above dates. More specifically, they interpret
all the time and dates as if the records were contained into a Daily
History file regardless of the actual type of the file they are stored
in.

### REDR Records

REDR records are very simple records. They simply indicate that the
browser was redirected to another site. REDR records always start with
the string REDR (0x52 45 44 52). The next four bytes are the size of the
record in little endian format. The size will indicate the number 128
byte blocks.

At offset 8 from the start of the REDR record is an unknown data field.
It has been confirmed that this is not a date field.

16 bytes into the REDR record is the URL that was visited in a
null-terminated string. After the URL, the REDR record appears to be
padded with zeros until the end of the 128 byte block.

### HASH Records

### LEAK Records

The exact purpose of LEAK records remains unknown, however research
performed by Mike Murr suggests that LEAK records are created when the
machine attempts to delete records from the history file while a
corresponding Temporary Internet File (TIF) is held open and cannot be
deleted.

## See Also

* [Internet Explorer](internet_explorer.md)

## External Links

* [What is in Index.dat files](http://www.milincorporated.com/a3_index.dat.html)
* [MSIE Cache File (index.dat) format specification](https://github.com/libyal/libmsiecf/blob/main/documentation/MSIE%20Cache%20File%20(index.dat)%20format.asciidoc),
  by the [libmsiecf project](libmsiecf.md)
* [Digital Detective Knowledge Base: Internet Explorer](https://kb.digital-detective.net/display/BF/Internet+Explorer)
* [Understanding index.dat Files - Part 1](http://web.archive.org/web/20090605202325/http://128.175.24.251/forensics/index_dat1.htm),
  by Stephen M. Bunting
* [Understanding index.dat Files - Part 2](http://web.archive.org/web/20090605200839/http://128.175.24.251/forensics/index_dat2.htm),
  by Stephen M. Bunting
* [Detailed analysis of index.dat file format](http://web.archive.org/web/20090824054415/http://www.foundstone.com/us/pdf/wp_index_dat.pdf),
  by Keith J. Jones, March 19, 2003
* [The Meaning of LEAK records](https://forensicblog.org/the-meaning-of-leak-records/),
  [Mike Murr](mike_murr.md), September 10, 2009
* [Microsoft Internet Explorer PrivacIE Entries](https://www.digital-detective.net/microsoft-internet-explorer-privacie-entries/),
  by Digital Detective, April 29, 2010
* [The INDEX.DAT File Format](https://www.geoffchappell.com/studies/windows/ie/wininet/api/urlcache/indexdat.htm?tx=20,78,83,84,88,89),
  by [Geoff Chappell](geoff_chappell.md), September 13, 2010
* [The Hash Algorithm for URL Caching](https://www.geoffchappell.com/studies/windows/ie/wininet/api/urlcache/hashkey.htm?tx=20,78,83,84,88),
  by [Geoff Chappell](geoff_chappell.md), September 20, 2010
* [A Primer on Temporary Internet Files](http://blogs.msdn.com/b/ieinternals/archive/2011/03/19/wininet-temporary-internet-files-cache-and-explorer-folder-view.aspx),
  by Eric Law, March 19, 2011

## Tools

* [IEHist](http://www.cqure.net/wp/iehist/)
* [libmsiecf](libmsiecf.md)
* [pasco](https://sourceforge.net/projects/odessa/), note this tool has
  not been updated since 2004 and is considered deprecated
* [pasco2](https://sourceforge.net/projects/pasco2/)
* [Windows 'index.dat' Parser (id)](http://www.tzworks.net/prototype_page.php?proto_id=6),
  by [TZWorks LLC](tzworks_llc.md)
