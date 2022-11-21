---
tags:
  -  File Formats
  -  Archive
  -  Linux
  -  FreeBSD
  -  OpenBSD
  -  NetBSD
  -  Solaris
  -  AIX
---
The bzip2 (.bz2) file consists of a single bzip2 stream. The bzip2
stream consists of:

- The stream header.

The stream header is 4 bytes in size and contains:

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
<td><p>"BZ"</p></td>
<td><p>Signature (magic number)</p></td>
</tr>
<tr class="even">
<td style="text-align: left;"><p>2</p></td>
<td><p>1</p></td>
<td></td>
<td><p>Version<br />
'h' for Bzip2 ('H'uffman coding), '0' for Bzip1 (deprecated)</p></td>
</tr>
<tr class="odd">
<td style="text-align: left;"><p>3</p></td>
<td><p>1</p></td>
<td></td>
<td><p>Block size<br />
Value is defined in increments of 100 kB<br />
'1'..'9' block-size 100 kB-900 kB (uncompressed)<br />
<b>Note: currently assumed that kB should be kiB</b></p></td>
</tr>
</tbody>
</table>

- followed by zero or more compressed blocks

<!-- -->

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

- immediately followed by an end-of-stream marker containing a 32-bit
  CRC for the uncompressed data.

<!-- -->

    .eos_magic:48                   = 0x177245385090 (BCD sqrt(pi))
    .crc:32                         = checksum for whole stream
    .padding:0..7                   = align to whole byte

The compressed blocks are bit-aligned and no padding occurs.

## See also

- [cpio](cpio.md)
- [gzip](gzip.md)
- [tar](tar.md)
- [xz](xz.md)

## External Links

- [Wikipedia: bzip2](http://en.wikipedia.org/wiki/Bzip2)

