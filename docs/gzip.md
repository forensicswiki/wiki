---
tags:
  -  File Formats
---
## File format

The gzip file (.gz) format consists of:

- a file header
- optional headers
  - extra fields
  - original file name
  - comment
  - header checksum
- compressed data (commonly used compression method DEFLATE, without
  zlib header)
- a file footer

<table>
<thead>
<tr class="header">
<th style="text-align: left;"><p>Characteristics</p></th>
<th><p>Description</p></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td style="text-align: left;"><p>Byte order</p></td>
<td><p>little-endian</p></td>
</tr>
<tr class="even">
<td style="text-align: left;"><p>Date and time values</p></td>
<td><p>POSIX timestamp<br />
Number of seconds since January 1, 1970 00:00:00 UTC</p></td>
</tr>
<tr class="odd">
<td style="text-align: left;"><p>Character strings</p></td>
<td><p>ISO 8859-1 (LATIN-1)</p></td>
</tr>
</tbody>
</table>

### File header

The file header is 10 bytes in size and contains:

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
<td><p>2</p></td>
<td><p>0x1f 0x8b</p></td>
<td><p>Signature (or identification byte 1 and 2)</p></td>
</tr>
<tr class="even">
<td style="text-align: left;"><p>2</p></td>
<td><p>1</p></td>
<td></td>
<td><p>Compression Method</p></td>
</tr>
<tr class="odd">
<td style="text-align: left;"><p>3</p></td>
<td><p>1</p></td>
<td></td>
<td><p>Flags</p></td>
</tr>
<tr class="even">
<td style="text-align: left;"><p>4</p></td>
<td><p>4</p></td>
<td></td>
<td><p>Last modification time<br />
Contains a POSIX timestamp.</p></td>
</tr>
<tr class="odd">
<td style="text-align: left;"><p>8</p></td>
<td><p>1</p></td>
<td></td>
<td><p>Compression flags (or extra flags)</p></td>
</tr>
<tr class="even">
<td style="text-align: left;"><p>9</p></td>
<td><p>1</p></td>
<td></td>
<td><p>Operating system<br />
Value that indicates on which operating system the gzip file was
created.</p></td>
</tr>
</tbody>
</table>

#### Compression method

| Value | Identifier | Description             |
|:------|------------|-------------------------|
| 0 - 7 |            | Reserved                |
| 8     | deflate    | deflate compressed data |

#### Flags

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
<td><p>FTEXT</p></td>
<td><p>If set the uncompressed data needs to be treated as text instead
of binary data.<br />
This flag hints end-of-line conversion for cross-platform text files but
does not enforce it.</p></td>
</tr>
<tr class="even">
<td style="text-align: left;"><p>0x02</p></td>
<td><p>FHCRC</p></td>
<td><p>The file contains a header checksum (CRC-16)</p></td>
</tr>
<tr class="odd">
<td style="text-align: left;"><p>0x04</p></td>
<td><p>FEXTRA</p></td>
<td><p>The file contains extra fields</p></td>
</tr>
<tr class="even">
<td style="text-align: left;"><p>0x08</p></td>
<td><p>FNAME</p></td>
<td><p>The file contains an original file name string</p></td>
</tr>
<tr class="odd">
<td style="text-align: left;"><p>0x10</p></td>
<td><p>FCOMMENT</p></td>
<td><p>The file contains comment</p></td>
</tr>
<tr class="even">
<td style="text-align: left;"><p>0x20</p></td>
<td></td>
<td><p>Reserved</p></td>
</tr>
<tr class="odd">
<td style="text-align: left;"><p>0x40</p></td>
<td></td>
<td><p>Reserved</p></td>
</tr>
<tr class="even">
<td style="text-align: left;"><p>0x80</p></td>
<td></td>
<td><p>Reserved</p></td>
</tr>
</tbody>
</table>

<b>Notes:</b>

- Reserved flags bits must be zero.
- The FHCRC bit was never set by versions of gzip up to 1.2.4, even
  though it was documented with a different meaning in gzip 1.2.4.

#### Compression flags

This value contains flags specific to the compression method.

##### Compression flags - deflate

If compression method value is 8 (deflate) the following compression
flags can be used:

| Value | Identifier | Description                                            |
|:------|------------|--------------------------------------------------------|
| 0x02  |            | compressor used maximum compression, slowest algorithm |
| 0x04  |            | compressor used fastest algorithm                      |

#### Operating System

| Value | Identifier | Description                             |
|:------|------------|-----------------------------------------|
| 0     |            | FAT filesystem (MS-DOS, OS/2, NT/Win32) |
| 1     |            | Amiga                                   |
| 2     |            | VMS (or OpenVMS)                        |
| 3     |            | Unix                                    |
| 4     |            | VM/CMS                                  |
| 5     |            | Atari TOS                               |
| 6     |            | HPFS filesystem (OS/2, NT)              |
| 7     |            | Macintosh                               |
| 8     |            | Z-System                                |
| 9     |            | CP/M                                    |
| 10    |            | TOPS-20                                 |
| 11    |            | NTFS filesystem (NT)                    |
| 12    |            | QDOS                                    |
| 13    |            | Acorn RISCOS                            |
| 255   |            | unknown                                 |

### Optional headers

#### Extra fields

This value is present in the file if the FEXTRA flag is set in the file
header flags.

The extra field are variable of size and contains:

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
<td><p>2</p></td>
<td></td>
<td><p>Extra field data size<br />
Value in bytes.</p></td>
</tr>
<tr class="even">
<td style="text-align: left;"><p>2</p></td>
<td><p>...</p></td>
<td></td>
<td><p>Extra field data</p></td>
</tr>
</tbody>
</table>

#### Original file name

This value is present in the file if the FNAME flag is set in the file
header flags.

This is the original name of the file being compressed, with any
directory components removed, and, if the file being compressed is on a
file system with case insensitive names, forced to lower case.

Contains an ISO 8859-1 (LATIN-1) string with end-of-string character.

#### Comment

This value is present in the file if the FCOMMENT flag is set in the
file header flags.

Contains an ISO 8859-1 (LATIN-1) string with end-of-string character.
Line breaks should be denoted by a single line feed character.

#### Header checksum

The header checksum contain a CRC-16 that consists of the two least
significant bytes of the CRC-32 for all bytes of the gzip header up to
and not including the CRC-16.

### File footer

The file footer is 8 bytes in size and contains:

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
<td><p>4</p></td>
<td></td>
<td><p>Checksum (CRC-32)</p></td>
</tr>
<tr class="even">
<td style="text-align: left;"><p>4</p></td>
<td><p>4</p></td>
<td></td>
<td><p>Uncompressed data size<br />
Value in bytes.</p></td>
</tr>
</tbody>
</table>

## See Also

* [bzip2](bzip2.md)
* [cpio](cpio.md)
* [tar](tar.md)
* [xz](xz.md)

## External Links

* [GNU Gzip: documentation](https://www.gnu.org/software/gzip/manual/gzip.html),
  by the [gzip project](https://www.gzip.org/)
* [RFC1952: GZIP file format specification](https://www.ietf.org/rfc/rfc1952.txt),
  by IETF
* [Wikipedia: gzip](https://en.wikipedia.org/wiki/Gzip)
