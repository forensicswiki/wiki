---
tags:
  - File Formats
---
The [Kaspersky Anti-Virus](kaspersky_anti-virus.md) report files
are stored in a [propriety file format](file_formats.md).

The following information is based on the current understanding of the
Kaspersky Report File format.

## Overview

A Kaspersky Report File consists of:

* file header
* log record index
* array of log records

## File header

The file header is 80 bytes of size and consists of:

| Offset | Size | Value | Description |
| --- | --- | --- | --- |
| 0 | 4 | "RPD2" | Signature |
| 4 | 4 | 2 | Unknown, version? |
| 8 | 8 | | Unknown (empty values?) |
| 16 | 4 | | Unknown A. Next available record number or 0? |
| 20 | 4 | 0x1000 | Unknown (record index size?) |
| 24 | 4 | | Unknown (Record offset?) |
| 28 | 4 | | Unknown (empty value) |
| 32 | 4 | | File size |
| 36 | 4 | | Unknown (empty value) |
| 40 | 8 | | Unknown timestamp. Creation time? |
| 48 | 8 | | Unknown timestamp. Last write time? |
| 56 | 8 | | Unknown timestamp. Access time? |
| 64 | 8 | | Unknown (empty values?) |
| 72 | 4 | | Next available record number? |
| 76 | 4 | | Unknown (empty value) |

## Log records index

### Log records index entry

The file header is 80 bytes of size and consists of:

| Offset | Size | Value | Description |
| --- | --- | --- | --- |
| 0 | 4 | | Record offset. The offset is relative to the start of the file |
| 4 | 4 | | Unknown (empty value) |
| 8 | 4 | | Record number |
| 12 | 4 | | Unknown (empty value) |

## Log records

### Log record header

| Offset | Size | Value | Description |
| --- | --- | --- | --- |
| 0 | 4 | | Log record data size. Log record size = Log record data size + 12 |
| 4 | 8 | | Unknown timestamp. Creation time? |
| 12 | ... | | Log record data |

### Log record data

The record data contains some types, followed by the data. Currently it
is assumed that the record data format is (partially) dependent on the
subsystem, e.g. on-access scan (oas), that generated the log record
data.

## Date and time values

The date and time values are stored in intervals of 10 ns since January
1, 1 00:00:00 local time.

E.g. the timestamp: 0x582db22720fb9bc9

```python
import datetime

print(datetime.datetime(1, 1, 1) + datetime.timedelta(microseconds=0x582db22720fb9bc9 / 100))
2014-06-25 15:01:44.164668
```

## See Also

* [Kaspersky Anti-Virus](kaspersky_anti-virus.md)
* [Kaspersky Quarantine File](kaspersky_quarantine_file.md)
