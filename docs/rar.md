---
tags:
  -  File Formats
  -  Archive
  -  Windows
  -  Linux
  -  MacOS
  -  NetBSD
  -  FreeBSD
  -  OpenBSD
---
RAR Archives (**R**oshal **AR**chive file format) are a proprietary
format for storing information created by Eugene Roshal. The format is
currently handled by Alexander Roshal, Eugene's brother.

## Format

The file has the magic number of:

    0x 52 61 72 21 1A 07 00

Which is a break down of the following to describe an Archive Header:

:\* 0x6152 - HEAD_CRC

:\* 0x72 - HEAD_TYPE

:\* 0x1A21 - HEAD_FLAGS

:\* 0x0007 - HEAD_SIZE

Older versions of the RAR file format have a magic number of :

    0x 52 45 7E 5E

This format will not be discussed as documentation cannot be found.

------------------------------------------------------------------------

### RAR File Format

Each Block has the following fields:

| Name       | Size (bytes) | Description                       |
|------------|--------------|-----------------------------------|
| HEAD_CRC   | 2            | CRC of total block or block part  |
| HEAD_TYPE  | 1            | Block type                        |
| HEAD_FLAGS | 2            | Block flags                       |
| HEAD_SIZE  | 2            | Block size                        |
| ADD_SIZE   | 4            | Optional field - added block size |

Block Fields

The field ADD_SIZE present only if (HEAD_FLAGS & 0x8000) != 0.

Total block size is HEAD_SIZE if (HEAD_FLAGS & 0x8000) == 0 and
HEAD_SIZE+ADD_SIZE if the field ADD_SIZE is present - when (HEAD_FLAGS &
0x8000) != 0.

In each block the followings bits in HEAD_FLAGS have the same meaning:

- 0x4000 - if set, older RAR versions will ignore the block and remove
  it when the archive is updated. If clear, the block is copied to the
  new archive file when the archive is updated;
- 0x8000 - if set, ADD_SIZE field is present and the full block size is
  HEAD_SIZE+ADD_SIZE.

------------------------------------------------------------------------

There are certain block types:

| Head Type Signifier | Description                        |
|---------------------|------------------------------------|
| HEAD_TYPE=0x72      | marker block                       |
| HEAD_TYPE=0x73      | archive header                     |
| HEAD_TYPE=0x74      | file header                        |
| HEAD_TYPE=0x75      | old style comment header           |
| HEAD_TYPE=0x76      | old style authenticity information |
| HEAD_TYPE=0x77      | old style subblock                 |
| HEAD_TYPE=0x78      | old style recovery record          |
| HEAD_TYPE=0x79      | old style authenticity information |
| HEAD_TYPE=0x7a      | subblock                           |
| HEAD_TYPE=0x7b      | terminator                         |

Block Types

------------------------------------------------------------------------

### Block Formats

There are several block formats that are contained within a RAR file.
They are Marker Block, Archive Header, and File Header.

------------------------------------------------------------------------

#### Marker Block (MARK_HEAD)

| Field Name | Size (bytes) | Possibilities       |
|------------|--------------|---------------------|
| HEAD_CRC   | 2            | Always 0x6152       |
| HEAD_TYPE  | 1            | Header type: 0x72   |
| HEAD_FLAGS | 2            | Always 0x1A21       |
| HEAD_SIZE  | 2            | Block size = 0x0007 |

MARK_HEAD

- Note: the marker block is considered a fixed byte sequence (AKA, magic
  number) of: 0x52 0x61 0x72 0x21 0x1A 0x07 0x00 (which is seen as 'Rar!
  ').

------------------------------------------------------------------------

#### Archive Header (MAIN_HEAD)

| Field Name | Size (bytes) | Description                                                                   |
|------------|--------------|-------------------------------------------------------------------------------|
| HEAD_CRC   | 2            | CRC of fields HEAD_TYPE to RESERVED2                                          |
| HEAD_TYPE  | 1            | Header Type: 0x73                                                             |
| HEAD_FLAGS | 2            | Bit Flags (Please see 'Bit Flags for MAIN_HEAD' table for all possibilities). |
| HEAD_SIZE  | 2            | Archive header total size including archive comments                          |
| RESERVED1  | 2            | RESERVED                                                                      |
| RESERVED2  | 4            | RESERVED                                                                      |

MAIN_HEAD

| Flag (0x) | Description                                                                                 |
|-----------|---------------------------------------------------------------------------------------------|
| 0001      | Volume attribute (archive volume)                                                           |
| 0002      | Archive comment present RAR 3.x uses the separate comment block and does not set this flag. |
| 0004      | Archive lock attribute                                                                      |
| 0008      | Solid attribute (solid archive)                                                             |
| 0010      | New volume naming scheme ('volname.partN.rar')                                              |
| 0020      | Authenticity information present RAR 3.x does not set this flag.                            |
| 0040      | Recovery record present                                                                     |
| 0080      | Block headers are encrypted                                                                 |
| 0100      | First volume (set only by RAR 3.0 and later)                                                |

Bit Flags for MAIN_HEAD

- Other bits in HEAD_FLAGS are reserved for internal use.

------------------------------------------------------------------------

#### File Header (File in Archive)

| Field Name     | Size (bytes)    | Description                                                                                                              |
|----------------|-----------------|--------------------------------------------------------------------------------------------------------------------------|
| HEAD_CRC       | 2               | CRC of fields from HEAD_TYPE to FILEATTR and file name                                                                   |
| HEAD_TYPE      | 1               | Header Type: 0x74                                                                                                        |
| HEAD_FLAGS     | 2               | Bit Flags (Please see 'Bit Flags for File in Archive' table for all possibilities)                                       |
| HEAD_SIZE      | 2               | File header full size including file name and comments                                                                   |
| PACK_SIZE      | 4               | Compressed file size                                                                                                     |
| UNP_SIZE       | 4               | Uncompressed file size                                                                                                   |
| HOST_OS        | 1               | Operating system used for archiving (See the 'Operating System Indicators' table for the flags used)                     |
| FILE_CRC       | 4               | File CRC                                                                                                                 |
| FTIME          | 4               | Date and time in standard MS DOS format                                                                                  |
| UNP_VER        | 1               | RAR version needed to extract file (Version number is encoded as 10 \* Major version + minor version.)                   |
| METHOD         | 1               | Packing method (Please see 'Packing Method' table for all possibilities                                                  |
| NAME_SIZE      | 2               | File name size                                                                                                           |
| ATTR           | 4               | File attributes                                                                                                          |
| HIGH_PACK_SIZE | 4               | High 4 bytes of 64-bit value of compressed file size. Optional value, presents only if bit 0x100 in HEAD_FLAGS is set.   |
| HIGH_UNP_SIZE  | 4               | High 4 bytes of 64-bit value of uncompressed file size. Optional value, presents only if bit 0x100 in HEAD_FLAGS is set. |
| FILE_NAME      | NAME_SIZE bytes | File name - string of NAME_SIZE bytes size                                                                               |
| SALT           | 8               | present if (HEAD_FLAGS & 0x400) != 0                                                                                     |
| EXT_TIME       | variable size   | present if (HEAD_FLAGS & 0x1000) != 0                                                                                    |

File Header

- other new fields may appear here.

| Flag (0x)                                     | Description                                                                                                                                                                                                                                                                                       |
|-----------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 01                                            | File continued from previous volume                                                                                                                                                                                                                                                               |
| 02                                            | File continued in next volume                                                                                                                                                                                                                                                                     |
| 04                                            | File encrypted with password                                                                                                                                                                                                                                                                      |
| 08                                            | File comment present. RAR 3.x uses the separate comment block and does not set this flag.                                                                                                                                                                                                         |
| 10                                            | Information from previous files is used (solid flag) (for RAR 2.0 and later)                                                                                                                                                                                                                      |
| Dictionary bits 7 6 5 (for RAR 2.0 and later) | Please see the 'Dictionary Bits' table for this descriptions                                                                                                                                                                                                                                      |
| 100                                           | HIGH_PACK_SIZE and HIGH_UNP_SIZE fields are present. These fields are used to archive only very large files (larger than 2Gb), for smaller files these fields are absent.                                                                                                                         |
| 200                                           | FILE_NAME contains both usual and encoded Unicode name separated by zero. In this case NAME_SIZE field is equal to the length of usual name plus encoded Unicode name plus 1. If this flag is present, but FILE_NAME does not contain zero bytes, it means that file name is encoded using UTF-8. |
| 400                                           | The header contains additional 8 bytes after the file name, which are required to increase encryption security (so called 'salt').                                                                                                                                                                |
| 800                                           | Version flag. It is an old file version, a version number is appended to file name as ';n'.                                                                                                                                                                                                       |
| 1000                                          | Extended time field present.                                                                                                                                                                                                                                                                      |
| 8000                                          | This bit always is set, so the complete block size is HEAD_SIZE + PACK_SIZE (and plus HIGH_PACK_SIZE, if bit 0x100 is set)                                                                                                                                                                        |

Bit Flags for Files in Archive

| Bits (7 6 5) | Description         | Size (KB) |
|--------------|---------------------|-----------|
| 0 0 0        | Dictionary Size     | 64        |
| 0 0 1        | Dictionary Size     | 128       |
| 0 1 0        | Dictionary Size     | 256       |
| 0 1 1        | Dictionary Size     | 512       |
| 1 0 0        | Dictionary Size     | 1024      |
| 1 0 1        | Dictionary Size     | 2048      |
| 1 1 0        | Dictionary Size     | 4096      |
| 1 1 1        | file is a directory | N/A       |

Dictionary Bits

| Byte Indicator | Operating System |
|----------------|------------------|
| 0              | MS DOS           |
| 1              | OS/2             |
| 2              | Windows          |
| 3              | Unix             |
| 4              | Mac OS           |
| 5              | BeOS             |

Operating System Indicators

| Byte Indicator | Method              |
|----------------|---------------------|
| 0x30           | Storing             |
| 0x31           | Fastest Compression |
| 0x32           | Fast Compression    |
| 0x33           | Normal Compression  |
| 0x34           | Good Compression    |
| 0x35           | Best Compression    |

Packing Method

------------------------------------------------------------------------

#### Terminator (terminator)

There is often a terminating block present.

| Field Name | Size (bytes) | Possibilities       |
|------------|--------------|---------------------|
| HEAD_CRC   | 2            | Always 0x3DC4       |
| HEAD_TYPE  | 1            | Header type: 0x7b   |
| HEAD_FLAGS | 2            | Always 0x4000       |
| HEAD_SIZE  | 2            | Block size = 0x0007 |

terminator

As such, it is possible to use the terminator as a footer when carving,
although, as always, file fragmentation should be considered.

    0x C4 3D 7B 00 40 07 00

------------------------------------------------------------------------

## Metadata

## Sub-formats

The RAR format is comprised of many sub-formats that have changed over
the years. The different formats and their descriptions are as follows:

:\* 1.3 (Does not have the RAR! signature)

:\*\* There is difficulty finding information regarding this sub-format.
Please update if you know something.

:\* 1.5

:\*\* Utilizes a proprietary compression method that is not available to
the public.

:\*\* Considered the root model of subsequent formats.

:\*\* A detailed list of information can be found
[here](http://www.win-rar.com/index.php?id=24&kb_article_id=162).

:\* 2.0

:\*\* Utilizes a proprietary compression method that is not available to
the public.

:\*\* Based off of version 1.5 of the RAR file format.

:\* 3.0

:\*\* Utilizes the
[PPMII](http://en.wikipedia.org/wiki/Prediction_by_Partial_Matching) and
[Lempel-Ziv (LZSS)](http://en.wikipedia.org/wiki/LZ77_and_LZ78)\]
algorithms.

:\*\* Encryption now uses cipher block chaining (CBC) instead of
Advanced Encryption Standard (AES).

:\*\* Based off of version 1.5 of the RAR file format.

## Software

This only way to create a RAR file is using the [Winrar
software](http://www.rarlab.com/). There are several implementations of
the process to open a RAR file (commonly known as the "unrar" process).
Some of them are:

unrarLib

:\* RAR file unarchiver written in C

:\* Easy implementation with a header file and the source code file

:\* Only works with RAR files up to version 2.0

:\* [Information Link](http://www.unrarlib.org/)

WinRAR

:\* Only software that can create and open a RAR file

:\* Distributed by a proprietary license

:\* Works with all versions of RAR files

:\* [WinRAR executable for Windows](http://www.rarlab.com/download.htm)

UnRAR

:\* Created by Eugene Roshal for opening up RAR files only

:\* May not be used to reverse engineer the RAR file format and create
RAR files

:\* Source code provided for people to implement/integrate methods of
opening RAR files

:\* Additionally, implementations of UnRAR are available for a plethora
of operating systems

:\* [Download Link](http://www.rarlab.com/rar_add.htm)

The Unarchiver

:\* Utility made for Mac OSX to open a multitude of files, including RAR
files

:\* Very handy for dealing with multiple file types

:\* [Source Code
Download](http://code.google.com/p/theunarchiver/downloads/list)

:\* [Information Website](http://unarchiver.c3.cx/)

7-Zip

:\* Utility made for Windows applications to open a multitude of files,
including RAR files

:\* [Download Link](http://www.7-zip.org/download.html)

There is a lot more software to open RAR files, but have been omitted
due to redundancy.

## See Also

- [Wikipedia: RAR](http://en.wikipedia.org/wiki/RAR)
- [RAR File Format Information](http://acritum.com/winrar/rar-format)
- RAR File Format Technical Information for Version 4.11
  ![<File:RARFileStructure.txt>](RARFileStructure.txt "File:RARFileStructure.txt")