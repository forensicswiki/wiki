---
tags:
  - AIX
  - Archive Format
  - File Formats
  - FreeBSD
  - Linux
  - NetBSD
  - OpenBSD
  - Solaris
---
The bzip2 (.bz2) file consists of a single bzip2 stream. The bzip2
stream consists of:

* The stream header.

The stream header is 4 bytes in size and contains:

| Offset | Size | Value | Description |
| --- | --- | --- | --- |
| 0 | 2 | "BZ" | Signature (magic number) |
| 2 | 1 | | Version. 'h' for Bzip2 ('H'uffman coding), '0' for Bzip1 (deprecated) |
| 3 | 1 | | Block size. Value is defined in increments of 100 kB. '1'..'9' block-size 100 kB-900 kB (uncompressed). **Note: currently assumed that kB should be kiB** |

* followed by zero or more compressed blocks

```text
.compressed_magic:48            = 0x314159265359 (BCD (pi))
.crc:32                         = checksum for this block
.randomised:1                   = 0=>normal, 1=>randomised (deprecated)
.origPtr:24                     = starting pointer into BWT for after untransform
.huffman_used_map:16            = bitmap, of ranges of 16 bytes, present/not present
.huffman_used_bitmaps:0..256    = bitmap, of symbols used, present/not present (multiples of 16)
.huffman_groups:3               = 2..6 number of different Huffman tables in use
.selectors_used:15              = number of times that the Huffman tables are swapped (each 50 bytes)
*.selector_list:1..6            = zero-terminated bit runs (0..62) of MTF'ed Huffman table (*selectors_used)
.start_huffman_length:5         = 0..20 starting bit length for Huffman deltas
*.delta_bit_length:1..40        = 0=>next symbol; 1=>alter length
                                                { 1=>decrement length;  0=>increment length } (*(symbols+2)*groups)
.contents:2..∞                  = Huffman encoded data stream until end of block
```

* immediately followed by an end-of-stream marker containing a 32-bit
  CRC for the uncompressed data.

```text
.eos_magic:48                   = 0x177245385090 (BCD sqrt(pi))
.crc:32                         = checksum for whole stream
.padding:0..7                   = align to whole byte
```

The compressed blocks are bit-aligned and no padding occurs.

## See also

* [cpio](cpio.md)
* [gzip](gzip.md)
* [tar](tar.md)
* [xz](xz.md)

## External Links

* [Wikipedia: bzip2](https://en.wikipedia.org/wiki/Bzip2)
