---
tags:
  -  File Formats
  -  Archive
  -  Windows
  -  FreeBSD
  -  Linux
  -  OpenBSD
  -  NetBSD
  -  AIX
  -  Solaris
  -  MacOS
  -  Articles that need to be expanded
---
.ZIP is an archive file format that supports lossless data compression.

<b>TODO</b> describe ZIP64

## File format

|                                        | ZIP           | ZIP64                                           |
|----------------------------------------|---------------|-------------------------------------------------|
| Maximum archive size (bytes)           | 4,294,967,295 | 18,446,755,073,709,551,615 ( 2<sup>64</sup>-1 ) |
| Maximum object size in archive (bytes) | 4,294,967,295 | 18,446,755,073,709,551,615 ( 2<sup>64</sup>-1 ) |
| Maximum objects in archive             | 65,535        | 18,446,755,073,709,551,615 ( 2<sup>64</sup>-1 ) |
| Maximum central directory size (bytes) | 4,294,967,295 | 18,446,755,073,709,551,615 ( 2<sup>64</sup>-1 ) |
| Maximum spanned archive segments       | 999           | 4,294,967,294                                   |
| Maximum split archive segments         | 65,535        | 4,294,967,294                                   |

| Overall ZIP File Structure             |
|----------------------------------------|
| Files                                  |
| local file header 1                    |
| encryption header 1                    |
| file data 1                            |
| data descriptor 1                      |
| ...                                    |
| local file header *n*                  |
| encryption header *n*                  |
| file data *n*                          |
| data descriptor *n*                    |
| Central directory                      |
| archive decryption header              |
| archive extra data record              |
| central directory header 1             |
| ...                                    |
| central directory header *n*           |
| zip64 end of central directory record  |
| zip64 end of central directory locator |
| end of central directory record        |

| Characteristics      | Description   |
|:---------------------|---------------|
| Byte order           | little-endian |
| Date and time values |               |
| Character strings    |               |

### Central directory (archived) file header

The central directory (archived) file header is variable of size and
consists of:

| Offset | Size | Value | Description |
| --- | --- | --- | --- |
| 0 | 4 | "PK\x01\x02" | Signature |
| 4 | 2 | | Creator version |
| 6 | 2 | | Extractor version |
| 8 | 2 | | Flags |
| 10 | 2 | | Compression method |
| 12 | 2 | | Last modification time |
| 14 | 2 | | Last modification date |
| 16 | 4 | | Checksum (CRC-32) |
| 20 | 4 | | Compressed data size |
| 24 | 4 | | Uncompressed data size |
| 28 | 2 | | File name size |
| 30 | 2 | | Extra field size |
| 32 | 2 | | File comment size |
| 34 | 2 | | Segment file (disk) number |
| 36 | 2 | | Internal file attributes |
| 38 | 4 | | External file attributes |
| 42 | 4 | | Local header offset, which is relative to the start of the segment file it is stored in |
| 46 | ... | | File name |
| ... | ... | | Extra field |
| ... | ... | | File comment |

#### Creator version

The creator (or version made by) is 2 bytes of size and consists of:

<table>
<thead>
<tr class="header">
<th style="text-align: left;"><p>Offset</p></th>
<th><p>Size</p></th>
<th><p>Value</p></th>
<th><p>Description</p></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td style="text-align: left;"><p>0</p></td>
<td><p>1</p></td>
<td></td>
<td><p>ZIP format version<br />
The value is stored as: ( major number x 10 ) + minor number</p></td>
</tr>
<tr class="even">
<td style="text-align: left;"><p>1</p></td>
<td><p>1</p></td>
<td></td>
<td><p>Creator system indicator</p></td>
</tr>
</tbody>
</table>

##### Creator system indicator

| Value    | Identifier | Description                                                             |
|:---------|------------|-------------------------------------------------------------------------|
| 0        |            | MS-DOS and OS/2 (FAT / VFAT / FAT32 file systems) or compatible systems |
| 1        |            | Amiga                                                                   |
| 2        |            | OpenVMS                                                                 |
| 3        |            | UNIX                                                                    |
| 4        |            | VM/CMS                                                                  |
| 5        |            | Atari ST                                                                |
| 6        |            | OS/2 H.P.F.S.                                                           |
| 7        |            | Macintosh                                                               |
| 8        |            | Z-System                                                                |
| 9        |            | CP/M                                                                    |
| 10       |            | Windows NTFS                                                            |
| 11       |            | MVS (OS/390 - Z/OS)                                                     |
| 12       |            | VSE                                                                     |
| 13       |            | Acorn Risc                                                              |
| 14       |            | VFAT                                                                    |
| 15       |            | alternate MVS                                                           |
| 16       |            | BeOS                                                                    |
| 17       |            | Tandem                                                                  |
| 18       |            | OS/400                                                                  |
| 19       |            | OS X (Darwin)                                                           |
| 20 - 255 |            | unused                                                                  |

#### Internal file attributes

<table>
<thead>
<tr class="header">
<th style="text-align: left;"><p>Value</p></th>
<th><p>Identifier</p></th>
<th><p>Description</p></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td style="text-align: left;"><p>0x01</p></td>
<td></td>
<td><p>If set the uncompressed data needs to be treated as text instead
of binary data.<br />
This flag hints end-of-line conversion for cross-platform text files but
does not enforce it.</p></td>
</tr>
<tr class="even">
<td style="text-align: left;"><p>0x02</p></td>
<td></td>
<td><p>If set the file contains control fields for mainframe data
transfer support.</p></td>
</tr>
</tbody>
</table>

#### External file attributes

The external attributes are creator system dependent.

The external attributes MS-DOS (0) is 4 bytes of size and consists of:

| Offset | Size | Value | Description                   |
|:-------|------|-------|-------------------------------|
| 0      | 1    |       | FAT (MS-DOS) file attributes. |
| 1      | 3    |       | Unknown                       |

The external attributes UNIX (3) is 4 bytes of size and consists of:

<table>
<thead>
<tr class="header">
<th style="text-align: left;"><p>Offset</p></th>
<th><p>Size</p></th>
<th><p>Value</p></th>
<th><p>Description</p></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td style="text-align: left;"><p>0</p></td>
<td><p>1</p></td>
<td></td>
<td><p>FAT (MS-DOS) file attributes.</p></td>
</tr>
<tr class="even">
<td style="text-align: left;"><p>1</p></td>
<td><p>1</p></td>
<td></td>
<td><p>Unknown</p></td>
</tr>
<tr class="odd">
<td style="text-align: left;"><p>2</p></td>
<td><p>16 bits</p></td>
<td></td>
<td><p>The UNIX mode (or permission).<br />
The value seems to be similar to stat.st_mode value.</p></td>
</tr>
</tbody>
</table>

## External Links

- [.ZIP File Format
  Specification](https://pkware.cachefly.net/webdocs/APPNOTE/APPNOTE-6.3.9.TXT),
  PKWARE Inc., September 1, 2012
- [Wikipedia: Zip (file
  format)](https://en.wikipedia.org/wiki/Zip_(file_format))
