---
tags:
  - Memory Analysis
---
Microsoft [Windows](windows.md) uses a **paging file**, called `pagefile.sys`,
to store frames of memory that do not current fit into [physical memory](physical_memory.md).
Although Windows supports up to 16 paging files, in practice normally, only one
is used. This file, stored in `%SystemDrive%\pagefile.sys` is a hidden system
file.  Because the operating system keeps this file open during normal
operation, it can never be read or accessed by a user. It is possible to read
this file by parsing the raw file system (e.g. using [The Sleuth Kit](the_sleuth_kit.md).

## Analysis Options

Data is stored in the paging file when [Windows](windows.md)
determines that it needs more space in physical memory. Because storage
locations in the paging file are not necessarily sequential, it is
unlikely to find consecutive pages there. Although it is possible to
find data in chunks smaller than or equal to 4KB, it's the largest an
examiner can hope for.

Sadly, the most productive method to date for analyzing paging files is
searching for [strings](strings.md). It is possible to [carve
out files](file_carving.md), but as noted, the examiner is unlikely
to find anything larger than 4KB. Also, bulk-extractor can be used to
extract streams from the page file.

## Artifacts details

* Executable file fragments: Any executable file fragments found in the
  page file may have been downloaded, extracted from a zip file, or run
  from a network share

## See Also

* [Windows Memory Analysis](windows_memory_analysis.md)

## External Links

* [Acquisition and Analysis of Windows Memory](https://citeseerx.ist.psu.edu/document?repid=rep1&type=pdf&doi=72fcd62f512c0a484a2514d06c86c8693c5a379c),
  by Nicholas Maclean, 2006. Thesis on [Windows memory analysis](windows_memory_analysis.md)
  and discusses the paging file.
* [Using Every Part of the Buffalo in Windows Memory Analysis](https://www.sciencedirect.com/science/article/abs/pii/S1742287607000047),
  by [Jesse Kornblum](jesse_kornblum.md) in 2006. A paper discussing the
  different states of memory including where to find data in the paging file.

## Tools

* [bulk-extractor](https://github.com/simsong/bulk_extractor)
* [page_brute](https://github.com/matonis/page_brute)
