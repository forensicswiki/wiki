---
tags:
  - Desktop Search
---
Windows Desktop Search (or Windows Search) is a 'desktop' indexer for
Microsoft Windows. In Windows XP, Search 4.0 (or Search XP) was an
add-on. However Microsoft integrated Search into Windows Vista as 'part
of the package'.

## Data location

Windows Search stores its data in:

    %CommonApplicationData%\Microsoft\Search\Data\Applications\Windows\

Note that '%CommonApplicationData%' is dependent on the
[Windows](windows.md) version.

E.g. on Windows XP

    C:\Documents and Settings\All Users\Application Data\Microsoft\Search\Data\Applications\Windows\

E.g. on Windows 7

    C:\ProgramData\Microsoft\Search\Data\Applications\Windows\

The search index is stored in a file named **Windows.edb**. This file is
an [Extensible Storage Engine Database
(edb)](extensible_storage_engine_(ese)_database_file_(edb)_format.md).

To access the Windows.edb file (on a live system) the the Windows Search
service needs to be deactivated and the necessary access rights are
required.

## Analysis

Currently there are not many [tools](#tools) which allow you to 'forensically'
analyze the Windows Search database.

### Artifacts

The artifacts in the Windows Search database can be useful in forensic
analysis of a desktop Windows system, especially Windows Vista and
later. A few applications are:

* to (partial) recover the content of indexed documents and even email
  messages stored on a Microsoft Exchange server
* to indicate the former existence of files
* time-line analysis

### Dirty database

When analyzing Windows Search databases you can come across a 'dirty
database'. This is one left in a dirty state. Some of the tools fail to
open these databases. You might have to resort to repairing the database
or use a tools that does not have such limitations.

### Obfuscation and compression

Windows Search uses both obfuscation and compression to store some of
its data, but according to 'Forensic analysis of the Windows Search
database' this is easily circumvented.

## See Also

* [Google Desktop Search](google_desktop_search.md)
* [Windows.edb file
  format](extensible_storage_engine_(ese)_database_file_(edb)_format.md)

## External Links

* [Official website](http://www.microsoft.com/windows/desktopsearch/)
* [Wikipedia entry on Windows Desktop
  Search](https://en.wikipedia.org/wiki/Windows_Desktop_Search)
* [Wikipedia list of Desktop search
  engines](http://en.wikipedia.org/wiki/List_of_search_engines#Desktop_search_engines)
* [Forensic analysis of the Windows Search
  database](https://code.google.com/archive/p/libesedb/downloads)

## Tools

* [EseDBViewer](http://www.woany.co.uk/esedbviewer/)
* [libesedb](libesedb.md)
* [Windows Search Index Examiner](https://www.passware.com/products/)
