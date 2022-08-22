Microsoft [Windows](Windows "wikilink") uses a **paging file**, called
`pagefile.sys`, to store frames of memory that do not current fit into
[physical memory](physical_memory "wikilink"). Although Windows supports
up to 16 paging files, in practice normally, only one is used. This
file, stored in `%SystemDrive%\pagefile.sys` is a hidden system file.
Because the operating system keeps this file open during normal
operation, it can never be read or accessed by a user. It is possible to
read this file by parsing the raw file system (e.g. using [The Sleuth
Kit](The_Sleuth_Kit "wikilink")).

## Analysis Options

Data is stored in the paging file when [Windows](Windows "wikilink")
determines that it needs more space in physical memory. Because storage
locations in the paging file are not necessarily sequential, it is
unlikely to find consecutive pages there. Although it is possible to
find data in chunks smaller than or equal to 4KB, it's the largest an
examiner can hope for.

Sadly, the most productive method to date for analyzing paging files is
searching for [strings](strings "wikilink"). It is possible to [carve
out files](Carving "wikilink"), but as noted, the examiner is unlikely
to find anything larger than 4KB. Also, bulk-extractor can be used to
extract streams from the page file.

## Artifacts details

- Executable file fragments: Any executable file fragments found in the
  page file may have been downloaded, extracted from a zip file, or run
  from a network share

## See Also

- [Windows Memory Analysis](Windows_Memory_Analysis "wikilink")

## External Links

- [Acquisition and Analysis of Windows
  Memory](http://www.4tphi.net/fatkit/papers/NickMaclean2006.pdf), by
  [Nicholas Maclean](Nicholas_Maclean "wikilink") in 2006. Thesis on
  [Windows memory analysis](Windows_Memory_Analysis "wikilink") and
  discusses the paging file.
- [Using Every Part of the Buffalo in Windows Memory
  Analysis](http://jessekornblum.com/publications/di07.pdf), by [Jesse
  Kornblum](Jesse_Kornblum "wikilink") in 2006. A paper discussing the
  different states of memory including where to find data in the paging
  file.
- [Microsoft Windows
  Internals](http://www.microsoft.com/MSPress/books/6710.aspx) - An
  excellent guide to the inner workings of Microsoft Windows.

## Tools

- [bulk-extractor](https://github.com/simsong/bulk_extractor)
- [page_brute](https://github.com/matonis/page_brute)

[Category:Memory Analysis](Category:Memory_Analysis "wikilink")