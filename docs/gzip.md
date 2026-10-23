---
tags:
  - File Formats
---
## File format

The gzip file (.gz) format consists of:

* a file header
* optional headers
  * extra fields
  * original file name
  * comment
  * header checksum
* compressed data (commonly used compression method DEFLATE, without
  zlib header)
* a file footer

| Characteristics | Description |
| --- | --- |
| Byte order | little-endian |
| Date and time values | POSIX timestamp. Number of seconds since January 1, 1970 00:00:00 UTC |
| Character strings | ISO 8859-1 (LATIN-1) |

### File header

The file header is 10 bytes in size and contains:

| Offset | Size | Value | Description |
| --- | --- | --- | --- |
| 0 | 2 | 0x1f 0x8b | Signature (or identification byte 1 and 2) |
| 2 | 1 | | Compression Method |
| 3 | 1 | | Flags |
| 4 | 4 | | Last modification time. Contains a POSIX timestamp. |
| 8 | 1 | | Compression flags (or extra flags) |
| 9 | 1 | | Operating system. Value that indicates on which operating system the gzip file was created. |

#### Compression method

| Value | Identifier | Description |
| --- | --- | --- |
| 0 - 7 | | Reserved |
| 8 | deflate | deflate compressed data |

#### Flags

| Value | Identifier | Description |
| --- | --- | --- |
| 0x01 | FTEXT | If set the uncompressed data needs to be treated as text instead of binary data. This flag hints end-of-line conversion for cross-platform text files but does not enforce it. |
| 0x02 | FHCRC | The file contains a header checksum (CRC-16) |
| 0x04 | FEXTRA | The file contains extra fields |
| 0x08 | FNAME | The file contains an original file name string |
| 0x10 | FCOMMENT | The file contains comment |
| 0x20 | | Reserved |
| 0x40 | | Reserved |
| 0x80 | | Reserved |

**Notes:**

* Reserved flags bits must be zero.
* The FHCRC bit was never set by versions of gzip up to 1.2.4, even
  though it was documented with a different meaning in gzip 1.2.4.

#### Compression flags

This value contains flags specific to the compression method.

##### Compression flags - deflate

If compression method value is 8 (deflate) the following compression
flags can be used:

| Value | Identifier | Description |
| --- | --- | --- |
| 0x02 | | compressor used maximum compression, slowest algorithm |
| 0x04 | | compressor used fastest algorithm |

#### Operating System

| Value | Identifier | Description |
| --- | --- | --- |
| 0 | | FAT filesystem (MS-DOS, OS/2, NT/Win32) |
| 1 | | Amiga |
| 2 | | VMS (or OpenVMS) |
| 3 | | Unix |
| 4 | | VM/CMS |
| 5 | | Atari TOS |
| 6 | | HPFS filesystem (OS/2, NT) |
| 7 | | Macintosh |
| 8 | | Z-System |
| 9 | | CP/M |
| 10 | | TOPS-20 |
| 11 | | NTFS filesystem (NT) |
| 12 | | QDOS |
| 13 | | Acorn RISCOS |
| 255 | | unknown |

### Optional headers

#### Extra fields

This value is present in the file if the FEXTRA flag is set in the file
header flags.

The extra field are variable of size and contains:

| Offset | Size | Value | Description |
| --- | --- | --- | --- |
| 0 | 2 | | Extra field data size. Value in bytes. |
| 2 | ... | | Extra field data |

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

| Offset | Size | Value | Description |
| --- | --- | --- | --- |
| 0 | 4 | | Checksum (CRC-32) |
| 4 | 4 | | Uncompressed data size. Value in bytes. |

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
