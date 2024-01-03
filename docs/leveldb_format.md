---
tags:
  - Database
  - File Formats
---

LevelDB is an Open Source key-value store database format.

The LevelDB database format is used to store various kinds of application-level
information such as the [Google Chrome](google_chrome.md) local storage.

A LevelDB database consists of a directory that contains the following files:

* `[0-9]{6}.ldb` (sorted tables file)
* `[0-9]{6}.log` (write ahead log file)
* CURRENT (contains the name of the current MANIFEST file)
* LOCK
* LOG, LOG.old (log with informational messages)
* MANIFEST-000001 (information about the sorted tables that make up the database)

## MIME types

Currently there are no know mime type for the LevelDB formats .

## File signature

Only sorted tables files are known to have an unique signature
"\x57\xfb\x80\x8b\x24\x75\x47\xdb" in the last 8 bytes of the file.

## File types

LevelDB is known to use several different file formats

* log descriptor format, used by MANIFEST-000001
* log format, used by `[0-9]{6}.log`
* table format, used by `[0-9]{6}.ldb`
* text, used by CURRENT, LOG, LOG.old

## External Links

* [LevelDB: Files](https://github.com/google/leveldb/blob/main/doc/impl.md)
* [LevelDB: leveldb File format](https://github.com/google/leveldb/blob/main/doc/table_format.md)
* [LevelDB: leveldb Log format](https://github.com/google/leveldb/blob/main/doc/log_format.md)
* [Wikipedia: LevelDB](https://en.wikipedia.org/wiki/LevelDB)
* [Recovering Deleted Data from LevelDB](https://antimatter15.com/2015/12/recovering-deleted-data-from-leveldb/),
  by Kevin Kwok, December 2, 2015

### IndexedDB

* [Chromium - LevelDB Coding Scheme](https://github.com/chromium/chromium/blob/master/content/browser/indexed_db/docs/leveldb_coding_scheme.md)
* [How the browsers store IndexedDB data](https://www.aaron-powell.com/posts/2012-10-05-indexeddb-storage/),
  by Aaron Powell, October 5, 2012
