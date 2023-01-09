---
tags:
  - File Formats
  - Windows
---
The **Common Log File System** (**CLFS**) is a special purpose file
(sub)system designed for transaction logging and/or recovery. The CLFS
is not a file system in the traditional meaning of a disk file system,
but more of a logical (special purpose) file system that operates in
combination with a disk file system like [NTFS](ntfs.md).

## Overview

A CLFS log consists of a base log file (.blf) and one or more container
files.

There are two types of logs:

- dedicated logs; contains a single stream of log records.
- multiplexed (or common) logs; contains several streams of log records.

## Implementation

According to Wikipedia CLFS was introduced in Windows server 2003 R2.

In Windows Vista the CLFS is implemented as a driver named: clfs.sys.
User space equivalent functionality is provided by clfsw32.dll, which
communicates to the driver by DeviceIoControl calls.

## Also see

Windows Internals 5 by Mark E. Russinovich and David A. Solomon

## External links

- [MSDN on Common Log File System](https://learn.microsoft.com/en-us/previous-versions/windows/desktop/clfs/common-log-file-system-portal)
- [Wikipedia on Common Log File System](https://en.wikipedia.org/wiki/Common_Log_File_System)
- [Common Log File System (CLFS)](https://github.com/libyal/libfsclfs/blob/main/documenation/Common%20Log%20File%20System%20(CLFS).asciidoc),
  by the libfslibs project, November 2010
