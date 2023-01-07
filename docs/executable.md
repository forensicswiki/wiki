---
tags:
  - Binary
  - ChromeOS
  - File Formats
  - FreeBSD
  - Linux
  - MacOS
  - NetBSD
  - OpenBSD
  - Solaris
  - Windows
---
An executable file is used to perform tasks according to encoded
instructions. Executable files are sometimes also referred to as
binaries which technically can be considered a sub class of executable
files.

There are multiple families of executable files:

* Scripts; e.g. shell scripts, batch scripts (.bat)
* DOS, Windows executable files (.exe) which can be of various formats
  like: MZ, PE/COFF, NE
  - EFI fat binary; roughly a 48-byte header and 2x MZ-PE/COFF
* ELF
* Mach-O

## External Links

* [Wikipedia: Executable](https://en.wikipedia.org/wiki/Executable)
* [Anatomy of a Program in Memory](https://manybutfinite.com/post/anatomy-of-a-program-in-memory/),
  by Gustavo Duarte, January 27, 2009
* [Extracting Compiler Provenance from Program Binaries](ftp://ftp.cs.wisc.edu/paradyn/papers/Rosenblum10prov.pdf),
  by Nathan E. Rosenblum, Barton P. Miller, Xiaojin Zhu, June 2010
* [Journey to the Stack, Part I](https://manybutfinite.com/post/journey-to-the-stack/),
  by Gustavo Duarte, March 10, 2014

### MZ, PE/COFF

* [Wikipedia: Portable Executable](https://en.wikipedia.org/wiki/Portable_Executable)
* [Microsoft PE and COFF Specification](https://learn.microsoft.com/en-us/windows/win32/debug/pe-format)
* [Peering Inside the PE: A Tour of the Win32 Portable Executable File Format](https://learn.microsoft.com/en-us/previous-versions/ms809762(v=msdn.10)),
  by Matt Pietrek, March 1994
* [An In-Depth Look into the Win32 Portable Executable File Format](https://learn.microsoft.com/en-us/archive/msdn-magazine/2002/february/inside-windows-win32-portable-executable-file-format-in-detail),
  by Matt Pietrek, February 2002
* [MZ, PE-COFF executable file format (EXE)](https://github.com/libyal/libexe/blob/main/documentation/Executable%20(EXE)%20file%20format.asciidoc),
  by the libexe project, October 2011
* [The Internal of Reloc .text](https://seclists.org/fulldisclosure/2013/Oct/157),
  Full Disclosure Mailing list, October 21, 2013

### DBG, PDB

* [Wikipedia: Program database](https://en.wikipedia.org/wiki/Program_database)
* [Matching Debug Information](https://www.debuginfo.com/articles/debuginfomatch.html),
  by debuginfo.com
* [Public and Private Symbols](https://learn.microsoft.com/en-us/windows-hardware/drivers/debugger/public-and-private-symbols),
  by [Microsoft](microsoft.md)
* [DbgHelp Structures](https://learn.microsoft.com/en-us/windows/win32/debug/dbghelp-structures),
  by [Microsoft](microsoft.md)
* [Internet Archive: Microsoft Symbol and Type Information](http://web.archive.org/web/20070915060650/http://www.x86.org/ftp/manuals/tools/sym.pdf),
  by [Microsoft](microsoft.md)
* [Microsoft Symbol and Type Information](https://pierrelib.pagesperso-orange.fr/exec_formats/MS_Symbol_Type_v1.0.pdf)
* [Stream Descriptions](https://code.google.com/archive/p/pdbparse/wikis/StreamDescriptions.wiki),
  [pdbparse project](https://github.com/moyix/pdbparse/)
* [libmsdebug](https://sourceforge.net/p/mingw-w64/code/HEAD/tree/experimental/tools/libmsdebug/),
  by the MinGW project
* [The Types Stream](https://moyix.blogspot.com/2007/10/types-stream.html),
  by Brendan Dolan-Gavitt, October 4, 2007

### Minidump

* [MSDN: MINIDUMP_HEADER structure](https://learn.microsoft.com/en-us/windows/win32/api/minidumpapiset/ns-minidumpapiset-minidump_header)
* [minidump_format.h](https://chromium.googlesource.com/breakpad/breakpad/+/master/src/google_breakpad/common/minidump_format.h),
  by Google, 2006
* [Parsing Windows Minidumps](https://moyix.blogspot.com/2008/05/parsing-windows-minidumps.html),
  by Brendan Dolan-Gavitt, May 7, 2008
* [Format of a minidump (mdmp) file](http://web.archive.org/web/20110814041817/http://www.stackhash.com/blog/post/Format-of-a-minidump-(mdmp)-file.aspx),
  Internet Archive: StackHash blog, May 16, 2011

### Mach-O

* [Wikipedia: Mach-O](https://en.wikipedia.org/wiki/Mach-O)

## Tools

### MZ, PE/COFF

* [pefile](https://github.com/erocarrera/pefile), multi-platform Python
  module to read and work with Portable Executable (aka PE) files

### PDB

* [pdbparse](https://code.google.com/archive/p/pdbparse), Open-source parser
  for Microsoft debug symbols (PDB files)

### Minidump

* [Dumpchk.exe](https://support.microsoft.com/en-us/topic/how-to-use-dumpchk-exe-to-check-a-memory-dump-file-0d766a2d-efaf-cf41-989e-fa3169869abb),
  by [Microsoft](microsoft.md)
* [minidump](https://github.com/skelsec/minidump),
  Python library to parse and read Microsoft minidump file format
