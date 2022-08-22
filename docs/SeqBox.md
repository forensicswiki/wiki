SeqBox (SBX) is a single file container/archive that can be
reconstructed even after total loss of file system structures.

An SBX container is composed of a collections of blocks with size
sub/equal to that of a sector, so they can survive any level of
fragmentation. Each block have a minimal header that include a unique
file identifier, block sequence number, checksum, version. Additional,
non critical info/metadata are contained in block 0 (like name, file
size, crypto-hash, other attributes, etc.).

If disaster strikes, recovery can be performed simply scanning a
volume/image, reading sector sized slices and checking blocks signatures
and then CRCs to detect valid SBX blocks. Then the blocks can be grouped
by UIDs, sorted by sequence number and reassembled to form the original
SeqBox containers.

## Tech spec

Byte order: Big Endian

### Common blocks header

| pos | to pos | size | desc                                                                      |
|-----|--------|------|---------------------------------------------------------------------------|
| 0   | 2      | 3    | Recoverable Block signature = ‘SBx’                                       |
| 3   | 3      | 1    | Version byte (1)                                                          |
| 4   | 5      | 2    | CRC-16-CCITT of the rest of the block (Version is used as starting value) |
| 6   | 11     | 6    | file UID                                                                  |
| 12  | 15     | 4    | Block sequence number                                                     |

### Block 0

| pos | to pos   | size | desc             |
|-----|----------|------|------------------|
| 16  | n        | var  | encoded metadata |
| n+1 | blockend | var  | padding (0x1a)   |

### Blocks \> 0 & \< last:

| pos | to pos   | size | desc |
|-----|----------|------|------|
| 16  | blockend | var  | data |

=== Blocks == last: ===

| pos | to pos   | size | desc           |
|-----|----------|------|----------------|
| 16  | n        | var  | data           |
| n+1 | blockend | var  | padding (0x1a) |

### Metadata encoding:

| Bytes | Field |
|-------|-------|
| 3     | ID    |
| 1     | Len   |
| n     | Data  |

#### IDs

| ID  | Desc                                                                     |
|-----|--------------------------------------------------------------------------|
| FNM | filename (utf-8)                                                         |
| SNM | sbx filename (utf-8)                                                     |
| FSZ | filesize (8 bytes)                                                       |
| HSH | crypto hash (SHA256, using [Multihash](http://multiformats.io) protocol) |

## External Links

- [SeqBox GitHub](https://github.com/MarcoPon/SeqBox) repository with
  encoder, decoder and recovery tools
- [SeqBox page](http://mark0.net/soft-seqbox-e.html) at Marco Pontello's
  Home

[Category:File Formats](Category:File_Formats "wikilink")