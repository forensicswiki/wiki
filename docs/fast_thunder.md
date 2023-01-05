---
tags:
  -  Tools
  -  Download Managers
  -  Windows
  -  MacOS
  -  Android
  -  iOS
  -  Open Source Software
---
**Fast Thunder** (aka Xunlei) is a [download
manager](download_manager.md) developed by Thunder Networking
Technologies.

## SuperDownload database

The **SuperDownload database** can be found at:

On Windows

    C:\Program Files\Thunder Network\Thunder\data\SdInfoDb.dat

This file uses the [SQLite database
format](sqlite_database_format.md).

The timestamp:

- SuperDownloadInfo.ContentDownloadTime is stored as BIGINT and contains
  a POSIX timestamp
- SuperDownloadResource.DownloadTime is stored as BIGINT and contains
  **presumably** a POSIX timestamp

## Task database

The **Task database** can be found at:

On Windows

    C:\Program Files\Thunder Network\Thunder\Profiles\TaskDb.dat

The timestamp:

- TaskBase.CreationTime and TaskBase.CompletionTime are stored as BIGINT
  and contains a POSIX timestamp shifted 24-bits to the left, e.g.

<!-- -->

    printf "0x%x\n" 22090158425767936
    0x4e7ae1ce000000

    date -d @$(( 22029112998625280 >> 24 ))
    Thu Aug 11 06:37:35 CEST 2011

### Example queries

Some example queries:

To get an overview of the tasks:

    SELECT datetime((TaskBase.CreationTime >> 24), "unixepoch"), datetime((TaskBase.CompletionTime >> 24) , "unixepoch"), TotalReceiveSize, TotalSendSize, Url, ReferenceUrl, Name, Description, SavePath FROM TaskBase;

## See Also

- [SQLite database format](sqlite_database_format.md)

## External Links

- [Wikipedia article on Fast Thunder
  (Xunlei)](https://en.wikipedia.org/wiki/Xunlei)
