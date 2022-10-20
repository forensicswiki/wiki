---
tags:
  -  Tools
  -  Windows
  -  Linux
  -  FreeBSD
  -  OpenBSD
  -  NetBSD
  -  Open Source Software
  -  File Analysis
  -  Articles that need to be expanded
---
**Hachoir** is a generic framework for binary file manipulation. Written
in Python, it's operating system independent and has many text/graphic
user interfaces (ncurses, wxWidget, Gtk+). Although it contains a few
functions to modify files, it is generally intended for examining
existing files. Hachoir currently supports more than sixty file formats.
File format recognition is based on the headers and footers in a disk
image of file. It has a fault tolerant parser designed to handle
truncated or buggy files. The framework also automatically adjusts for
endian or character set issues. The framework can be scripted and
extended.

The package includes several sample programs based on the core framework
and parser:

- hachoir-metadata: extract metadata
- hachoir-strip: remove metadata and other "useless" informations
- hachoir-grep: find substring in a binary file (using hachoir parsers:
  so search is Unicode aware)
- hachoir-subfile: find all subfiles in a file

The current version of hachoir-core is 1.3.4 and was released in
February 2010. Precompiled packages are available for the Debian,
Gentoo, Mandriva, and Arch [Linux](linux.md) distributions along
with FreeBSD'''. There are Python egg files which can be used to install
it in Windows.

## External Links

- [Official website](http://bitbucket.org/haypo/hachoir/wiki/Home/)

Python egg files :

- [hachoir-core](http://pypi.python.org/pypi/hachoir-core)
- [hachoir-parser](http://pypi.python.org/pypi/hachoir-parser)
- [hachoir-metadata](http://pypi.python.org/pypi/hachoir-metadata)
- [hachoir-urwid](http://pypi.python.org/pypi/hachoir-urwid)
- [hachoir-wx](http://pypi.python.org/pypi/hachoir-wx)