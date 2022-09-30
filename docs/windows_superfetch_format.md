---
tags:
  -  File Formats
---
SuperFetch, is a memory management scheme that enhances the
least-recently accessed approach with historical information and
proactive memory management.
[1](http://technet.microsoft.com/en-us/magazine/2007.03.vistakernel.aspx)

<b>Note that the following format specification are incomplete.</b>

## SuperFetch DB files

The `Ag*.db` files are of the SuperFetch file format. E.g.

    AgAppLaunch.db
    AgCx_SC*.db
    AgGlFaultHistory.db
    AgGlFgAppHistory.db
    AgGlGlobalHistory.db
    AgGlUAD_%SID%.db
    AgGlUAD_P_%SID%.db
    AgRobust.db

The SuperFetch DB files can be stored in uncompressed or compressed
form, where different version of Windows use different compressed forms:

- Compressed SuperFetch DB - MEMO file format; Windows Vista
- Compressed SuperFetch DB - MEM0 file format; Windows 7
- Compressed SuperFetch DB - MAM file format; Windows 8

### Compressed SuperFetch DB - MEMO file format

The MEM file consists of:

- file header
- compressed blocks

This format uses the LZNT1 compression method

#### File header

The file header is 84 bytes of size and consists of:

| Offset | Size | Value                           | Description                    |
|--------|------|---------------------------------|--------------------------------|
| 0      | 4    | "MEMO" (0x4d, 0x45, 0x4d, 0x4f) | Signature                      |
| 4      | 4    |                                 | Uncompressed (total) data size |
|        |      |                                 |                                |

#### Compressed blocks

The compressed block size is the chunk data size, which is part of the
LZNT1 compressed data, + 2 bytes for the size of the chunk header
itself.

The uncompressed block size is 4096 (0x1000) or the remaining
uncompressed data size for the last block.

### Compressed SuperFetch DB - MEM0 file format

The MEM file consists of:

- file header
- compressed blocks

This format uses the LZXPRESS Huffman compression method

#### File header

The file header is 8 bytes of size and consists of:

| Offset | Size | Value                           | Description                    |
|--------|------|---------------------------------|--------------------------------|
| 0      | 4    | "MEM0" (0x4d, 0x45, 0x4d, 0x30) | Signature                      |
| 4      | 4    |                                 | Uncompressed (total) data size |
|        |      |                                 |                                |

#### Compressed blocks

The file header is followed by compressed blocks:

| Offset | Size | Value | Description          |
|--------|------|-------|----------------------|
| 0      | 4    |       | Compressed data size |
| 4      | ...  |       | Compressed data      |
|        |      |       |                      |

The uncompressed block size is 65536 (0x10000) or the remaining
uncompressed data size for the last block.

### Compressed SuperFetch DB - MAM file format

The MAM file consists of:

- file header
- compressed blocks

This format uses the LZXPRESS Huffman compression method.

#### File header

The file header is 12 bytes of size and consists of:

| Offset | Size | Value                              | Description                    |
|--------|------|------------------------------------|--------------------------------|
| 0      | 4    | "MAM\x84" (0x4d, 0x41, 0x4d, 0x84) | Signature                      |
| 4      | 4    |                                    | Uncompressed (total) data size |
| 8      | 4    |                                    | Unknown (checksum?)            |
|        |      |                                    |                                |

#### Compressed blocks

The uncompressed block size is 65536 (0x10000) or the remaining
uncompressed data size for the last block.

Note the LZXPRESS Huffman variant used differs from the one used in the
MEM0 format. This variant can refer to uncompressed data stored in the
previous compressed block. The compressed blocks are essentially a
single compressed stream.

### Uncompressed SuperFetch DB format

<b>TODO</b>

#### File header

<b>TODO</b>

| Offset | Size | Value      | Description                           |
|--------|------|------------|---------------------------------------|
| 0      | 4    | 0x0000000e | Unknown (Database type or signature?) |
| 4      | 4    |            | Uncompressed (total) data size        |
|        |      |            |                                       |

## TRX files

The `Ag*.db.trx` files are of the TRX file format. E.g.

    AgCx_SC*.db.trx

<b>Note that the following format specification is incomplete.</b>

### File header

The file header is variable of size and consists of:

| Offset | Size | Value | Description                                                                                           |
|--------|------|-------|-------------------------------------------------------------------------------------------------------|
| 0      | 4    | 1     | Unknown (Version?)                                                                                    |
| 4      | 4    |       | Unknown                                                                                               |
| 8      | 4    |       | File size                                                                                             |
| 12     | 4    |       | Maximum number of records (of the record offsets array)                                               |
| 16     | 4    |       | Number of records                                                                                     |
| 20     | ...  |       | Record offsets array, where the record offset is a 32-bit integer. Unused record offset are set to 0. |
|        |      |       |                                                                                                       |

### Record

<b>TODO describe</b>

## See Also

- [SuperFetch](superfetch.md)

## External Links

- [Windows SuperFetch file format – partial
  specification](http://blog.rewolf.pl/blog/?p=214), by ReWolf, October
  5, 2011
- [Windows SuperFetch database
  format](https://googledrive.com/host/0B3fBvzttpiiSWFFkSTBOUHdjOVU/Windows%20SuperFetch%20(DB)%20format.pdf),
  by the [libagdb project](libagdb.md), April 2014

