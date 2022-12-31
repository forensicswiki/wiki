---
tags:
  -  File Formats
  -  Windows
  -  Linux
  -  FreeBSD
  -  NetBSD
  -  OpenBSD
  -  Solaris
  -  ChromeOS
  -  MacOS
  -  Binary
---
An executable file is used to perform tasks according to encoded
instructions. Executable files are sometimes also referred to as
binaries which technically can be considered a sub class of executable
files.

There are multiple families of executable files:

- Scripts; e.g. shell scripts, batch scripts (.bat)
- DOS, Windows executable files (.exe) which can be of various formats
  like: MZ, PE/COFF, NE
  - EFI fat binary; roughly a 48-byte header and 2x MZ-PE/COFF
- ELF
- Mach-O

## External Links

- [Wikipedia: Executable](http://en.wikipedia.org/wiki/Executable)
- [Anatomy of a Program in
  Memory](http://duartes.org/gustavo/blog/post/anatomy-of-a-program-in-memory/),
  by Gustavo Duarte, January 27, 2009
- [Extracting Compiler Provenance from Program
  Binaries](ftp://ftp.cs.wisc.edu/paradyn/papers/Rosenblum10prov.pdf),
  by Nathan E. Rosenblum, Barton P. Miller, Xiaojin Zhu, June 2010
- [Journey to the Stack, Part
  I](http://duartes.org/gustavo/blog/post/journey-to-the-stack/), by
  Gustavo Duarte, March 10, 2014

### ELF

- [Manually Creating an ELF
  Executable](http://robinhoksbergen.com/papers/howto_elf.html), by
  Robin Hoksbergen

### MZ, PE/COFF

- [Wikipedia: Portable
  Executable](http://en.wikipedia.org/wiki/Portable_Executable)
- [Microsoft PE and COFF
  Specification](http://msdn.microsoft.com/en-us/windows/hardware/gg463119.aspx)
- [Peering Inside the PE: A Tour of the Win32 Portable Executable File
  Format](http://msdn.microsoft.com/en-us/magazine/ms809762.aspx), by
  Matt Pietrek, March 1994
- [Under the Hood](http://www.microsoft.com/msj/0797/hood0797.aspx), by
  Matt Pietrek, July 1997
- [An In-Depth Look into the Win32 Portable Executable File
  Format](http://msdn.microsoft.com/en-us/magazine/cc301805.aspx), by
  Matt Pietrek, February 2002
- [MZ, PE-COFF executable file format
  (EXE)](https://googledrive.com/host/0B3fBvzttpiiSd1dKQVU0WGVESlU/Executable%20(EXE)%20file%20format.pdf),
  by the [libexe project](libexe.md), October 2011
- [Carving up EFI fat
  binaries](http://ho.ax/posts/2012/02/carving-up-efi-fat-binaries/), by
  snare, February 24, 2012
- [The Internal of Reloc
  .text](http://seclists.org/fulldisclosure/2013/Oct/157), Full
  Disclosure Mailing list, October 21, 2013

### DBG, PDB

- [Wikipedia: Program
  database](http://en.wikipedia.org/wiki/Program_database)
- [Matching Debug
  Information](http://www.debuginfo.com/articles/debuginfomatch.html),
  by debuginfo.com
- [Description of the .PDB files and of the .DBG
  files](http://support.microsoft.com/kb/121366), by
  [Microsoft](microsoft.md)
- \[<http://msdn.microsoft.com/en-us/library/ff553493(v=vs.85>).aspx
  Public and Private Symbols\], by [Microsoft](microsoft.md)
- \[<http://msdn.microsoft.com/en-us/library/windows/desktop/ms679293(v=vs.85>).aspx
  DbgHelp Structures\], by [Microsoft](microsoft.md)
- [Internet Archive: Microsoft Symbol and Type
  Information](http://web.archive.org/web/20070915060650/http://www.x86.org/ftp/manuals/tools/sym.pdf),
  by [Microsoft](microsoft.md)
- [Microsoft Symbol and Type
  Information](http://pierrelib.pagesperso-orange.fr/exec_formats/MS_Symbol_Type_v1.0.pdf)
- [Stream
  Descriptions](https://code.google.com/p/pdbparse/wiki/StreamDescriptions),
  [pdbparse project](https://code.google.com/p/pdbparse/)
- [libmsdebug](https://sourceforge.net/p/mingw-w64/code/HEAD/tree/experimental/tools/libmsdebug/),
  by the [MinGW project](mingw.md)
- [The Types
  Stream](http://moyix.blogspot.com/2007/10/types-stream.html), by
  [Brendan Dolan-Gavitt](brendan_dolan-gavitt.md), October 4,
  2007

### Minidump

- \[<http://msdn.microsoft.com/en-us/library/windows/desktop/ms680378(v=vs.85>).aspx
  MSDN: MINIDUMP_HEADER structure\]
- [minidump_format.h](https://code.google.com/p/google-breakpad/source/browse/trunk/src/google_breakpad/common/minidump_format.h),
  by [Google](google.md), 2006
- [Parsing Windows
  Minidumps](http://moyix.blogspot.com/2008/05/parsing-windows-minidumps.html),
  by [Brendan Dolan-Gavitt](brendan_dolan-gavitt.md), May 7,
  2008
- [Format of a minidump (mdmp)
  file](http://web.archive.org/web/20110814041817/http://www.stackhash.com/blog/post/Format-of-a-minidump-(mdmp)-file.aspx),
  Internet Archive: StackHash blog, May 16, 2011

### Mach-O

- [Wikipedia: Mach-O](http://en.wikipedia.org/wiki/Mach-O)

### Packers

- [Packers & Unpackers](http://www.woodmann.com/crackz/Packers.htm)

## Tools

### MZ, PE/COFF

- [pefile](https://code.google.com/p/pefile/), multi-platform Python
  module to read and work with Portable Executable (aka PE) files

### PDB

- [pdbparse](https://code.google.com/p/pdbparse/), Open-source parser
  for Microsoft debug symbols (PDB files)

### Minidump

- [Dumpchk.exe](http://support.microsoft.com/kb/315271), by
  [Microsoft](microsoft.md)
- [minidump.py](http://amnesia.gtisc.gatech.edu/~moyix/minidump.py), by
  [Brendan Dolan-Gavitt](brendan_dolan-gavitt.md)