---
tags:
  -  Tools
  -  Linux
  -  Data Recovery
  -  Opensource Software
---
BlockHashLoc (BHL) enable the recovery of files via previously made
small files with a list of blocks hashes.

With adequately sized blocks (512 bytes, 4KB, etc. depending on the
media and File System), this let one recover a file regardless of the FS
used, or the FS integrity, or the fragmentation level.

## Tech spec

Byte order: Big Endian Hash: SHA-256

### BHL file structure

| section    | desc                                 | note      |
|------------|--------------------------------------|-----------|
| Header     | Signature & version                  |           |
| Metadata   | Misc info                            |           |
| Hash       | Blocks hash list & final hash        |           |
| Last block | zlib compressed last block remainder | if needed |

### Header

| pos | to pos | size | desc                              |
|-----|--------|------|-----------------------------------|
| 0   | 12     | 13   | Signature = ‘BlockHashLoc’ + 0x1a |
| 13  | 13     | 1    | Version byte                      |
| 14  | 16     | 4    | Block size                        |
| 18  | 24     | 8    | File size                         |

### Metadata

| pos | to pos | size | desc                  |
|-----|--------|------|-----------------------|
| 26  | 28     | 4    | Metadata section size |
| 30  | var    | var  | Encoded metadata list |

### Hash

| pos | to pos | size | desc                              |
|-----|--------|------|-----------------------------------|
| var | var    | 32   | 1st block hash                    |
| …   | …      | 32   | …                                 |
| var | var    | 32   | Last block hash                   |
| var | var    | 32   | Hash of all previous block hashes |

### Versions

Currently the only version is 1.

### Metadata encoding

| Bytes | Field |
|-------|-------|
| 3     | ID    |
| 1     | Len   |
| n     | Data  |

### IDs

| ID  | Desc                                       |
|-----|--------------------------------------------|
| FNM | filename (utf-8)                           |
| FDT | date & time (8 bytes, seconds since epoch) |

## External Links

- [BlockHashLoc GitHub](https://github.com/MarcoPon/BlockHashLoc)