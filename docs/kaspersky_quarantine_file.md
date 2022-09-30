---
tags:
  -  File Formats
---
The [Kaspersky Anti-Virus](kaspersky_anti-virus.md) quarantined
files are stored in a [propriety file format](file_formats.md).

The following information is based on the current understanding of the
Kaspersky Quarantine File format.

## Overview

A Kaspersky Quarantine File consists of:

- file header
- obfuscated quarantined file
- obfuscated metadata

## File header

The file header is 64 bytes of size and consists of:

| Offset | Size | Value  | Description                                              |
|--------|------|--------|----------------------------------------------------------|
| 0      | 4    | "KLQB" | Signature                                                |
| 4      | 4    | 1      | Unknown, version?                                        |
| 8      | 4    |        | Unknown, header size or offset to quarantined file data? |
| 12     | 4    |        | Unknown, empty values?                                   |
| 16     | 4    |        | Unknown, offset to metadata?                             |
| 20     | 12   |        | Unknown                                                  |
| 32     | 4    |        | Unknown, size of metadata?                               |
| 36     | 4    |        | Unknown, empty values?                                   |
| 40     | 4    |        | Unknown, header size?                                    |
| 44     | 4    |        | Unknown, empty values?                                   |
| 48     | 4    |        | Unknown, quarantined file size?                          |
| 52     | 4    |        | Unknown, empty values?                                   |
| 56     | 4    | 1      | Unknown                                                  |
| 60     | 4    |        | Unknown, empty values?                                   |
|        |      |        |                                                          |

## Quarantined file

The quarantined file is stored obfuscated using an 8 byte XOR key: "e2
45 48 ec 69 0e 5c ac".

## Metadata

How the metadata is stored is not fully known at the moment but part of
the metadata is stored obfuscated using an 8 byte XOR key: "48 ec 69 0e
5c ac e2 45".

### Date and time values

The date and time values in the metadata are stored in intervals of 10
ns since January 1, 1 00:00:00 local time.

E.g. the timestamp: 0x582db22720fb9bc9

    import datetime

    print datetime.datetime(1, 1, 1) + datetime.timedelta(microseconds=0x582db22720fb9bc9 / 100)
    2014-06-25 15:01:44.164668

## See Also

- [Kaspersky Anti-Virus](kaspersky_anti-virus.md)
- [Kaspersky Report File](kaspersky_report_file.md)

