SQLite databases are used by many programs including several forensics
tools, e.g. [Autopsy](Autopsy "wikilink") 3. SQLite 3 is current and
older SQLite packages cannot use sqlite3 databases so use sqlite3 tools.

## SQLite3

SQLite version 3 uses a page-based storage where the pages are used for
various types of data e.g. there are:

- lock-byte pages
- freelist pages
  - freelist trunk pages
  - freelist leaf pages
- B-tree pages
  - table B-tree interior pages
  - table B-tree leaf pages
  - index B-tree interior pages
  - index B-tree leaf pages
- payload overflow pages
- pointer map pages

### Write-Ahead Log (WAL)

The default method by which SQLite implements atomic commit and rollback
is a rollback journal. In version 3.7.0 a "Write-Ahead Log" option was
added.

## Temporary sqlite files

Seen in e.g.

    /Users/%USERNAME%/AppData/Local/Temp/etilqs_%RANDOM%

Where "etilqs" is "sqlite" in reverse

## Use Cases

### Web Browser Data

[Mozilla Firefox](Mozilla_Firefox "wikilink") and [Google
Chrome](Google_Chrome "wikilink") both use SQLite version 3 databases
for user data such as history, downloaded files.

### Mobile OS

[Google Android](Google_Android "wikilink") and [Apple
iOS](Apple_iOS "wikilink") use SQLite3 databases for many system
applications. Phone data including calls, messages, and credentials are
all stored in SQLite3.

## External Links

- [Recovering Deleted Records from an SQLite
  database](http://sandersonforensics.com/forum/content.php?222-Recovering-deleted-records-from-an-SQLite-database)
- [Forensic examination of WAL
  files](http://sandersonforensics.com/forum/content.php?197-Forensic-examination-of-SQLite-Write-Ahead-Log-%28WAL%29-files)
- [Forensic Examination of Rollback
  journals](http://sandersonforensics.com/forum/content.php?208-Dealing-with-records-found-in-SQLite-Rollback-Journals)
- [Forensic Analysis of SQLite Databases: Free Lists, Write Ahead Log,
  Unallocated Space and Carving](http://belkasoft.com/sqlite-analysis),
  article by [Belkasoft](Belkasoft "wikilink")
- [The SQLite Database File Format](http://sqlite.org/fileformat2.html),
  by the [SQLite project](SQLite "wikilink")
- [Write-Ahead Logging](http://sqlite.org/wal.html), by the [SQLite
  project](SQLite "wikilink")
- [Carving SQLite databases from unallocated
  clusters](http://forensicsfromthesausagefactory.blogspot.com/2011/04/carving-sqlite-databases-from.html),
  by Richard Drinkwater, April 27, 2011
- [Recovering Data from Deleted SQLite Records:
  Redux](http://linuxsleuthing.blogspot.ch/2013/09/recovering-data-from-deleted-sqlite.html),
  by [John Lehr](John_Lehr "wikilink"), September 13, 2013

## Tools

- [Forensic Toolkit for SQLite](Forensic_Toolkit_for_SQLite "wikilink")
- [SQLite Forensics
  Explorer](http://www.acquireforensics.com/products/sqlite-forensic-explorer/)
- [Belkasoft Evidence Center](Belkasoft "wikilink")
- [SQLite](SQLite "wikilink")
- [SQLite Recovery](SQLite_Recovery "wikilink")
- [SQLite Forensic Reporter](SQLite_Forensic_Reporter "wikilink")
- [SQLite Forensics](http://www.freeviewer.org/sqlite/forensics/)

[Category:File Formats](Category:File_Formats "wikilink")
[Category:Database File
Formats](Category:Database_File_Formats "wikilink")