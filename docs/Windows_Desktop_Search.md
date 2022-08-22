Windows Desktop Search (or Windows Search) is a 'desktop' indexer for
Microsoft Windows. In Windows XP, Search 4.0 (or Search XP) was an
add-on. However Microsoft integrated Search into Windows Vista as 'part
of the package'.

## Data location

Windows Search stores its data in:

    %CommonApplicationData%\Microsoft\Search\Data\Applications\Windows\

Note that '%CommonApplicationData%' is dependent on the
[Windows](Windows "wikilink") version.

E.g. on Windows XP

    C:\Documents and Settings\All Users\Application Data\Microsoft\Search\Data\Applications\Windows\

E.g. on Windows 7

    C:\ProgramData\Microsoft\Search\Data\Applications\Windows\

The search index is stored in a file named **Windows.edb**. This file is
an [Extensible Storage Engine Database
(EDB)](Extensible_Storage_Engine_(ESE)_Database_File_(EDB)_format "wikilink").

To access the Windows.edb file (on a live system) the the Windows Search
service needs to be deactivated and the necessary access rights are
required.

## Analysis

Currently there are not many
[tools](Windows_Desktop_Search#Tools "wikilink") which allow you to
'forensically' analyze the Windows Search database.

### Artifacts

The artifacts in the Windows Search database can be useful in forensic
analysis of a desktop Windows system, especially Windows Vista and
later. A few applications are:

- to (partial) recover the content of indexed documents and even email
  messages stored on a Microsoft Exchange server
- to indicate the former existence of files
- time-line analysis

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

- [Google Desktop Search](Google_Desktop_Search "wikilink")
- [Windows.edb file
  format](Extensible_Storage_Engine_(ESE)_Database_File_(EDB)_format "wikilink")

## External Links

- [Official website](http://www.microsoft.com/windows/desktopsearch/)
- [Wikipedia entry on Windows Desktop
  Search](http://en.wikipedia.org/wiki/Windows_Desktop_Search)
- [Wikipedia list of Desktop search
  engines](http://en.wikipedia.org/wiki/List_of_search_engines#Desktop_search_engines)
- [Forensic analysis of the Windows Search
  database](http://code.google.com/p/libesedb/downloads/detail?name=Forensic%20analysis%20of%20the%20Windows%20Search%20database.pdf)

## Tools

- [EseDBViewer](http://www.woany.co.uk/esedbviewer/)
- [libesedb](libesedb "wikilink")
- [Windows Search Index
  Examiner](http://www.lostpassword.com/search-index-examiner.htm)

[Category:Desktop Search](Category:Desktop_Search "wikilink")
[Category:Windows](Category:Windows "wikilink")