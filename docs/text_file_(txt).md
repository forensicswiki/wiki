---
tags:
  -  File Formats
  -  Text
  -  Windows
  -  FreeBSD
  -  Linux
  -  OpenBSD
  -  NetBSD
  -  MacOS
---
The **Text file (TXT)** format consist of 8-, 16- or 32-bit characters
that use printable characters along with some control data such as tabs
and line feeds. [1](http://en.wikipedia.org/wiki/Text_file) Text files
are split into several major types:

- DOS/Windows format ends each line using Carriage Return (CR) or
  char(13) and a Line Feed (LF) or char(10) byte sequence,
- Unix format includes only the Carriage Return (CR) or char (13) at the
  end of the line.
- Macintosh format includes only the Line Feed (LF) or char(10) at the
  end of the line.
- Unicode includes an optional encoding in the first two bytes Byte
  Order Mark (BOM) that identifies the Unicode encoding. This is used to
  identify little endian or big endian byte order. Unicode defines an
  8-bit encoding UTF-8, a 16-bit encoding UTF-16 and a 32-bit encoding
  UTF-32. Earlier equivalent encodings are respectively UCS-1, UCS-2 and
  USC-4
- EBCIDIC used char(15) for a new line.
  [2](http://en.wikipedia.org/wiki/EBCDIC)

They are usually [ASCII](ascii.md) encoded, although other
encodings are possible to allow various language scripts to be used.
Other encodings include EBCIDIC from the old IBM mainframe. Text files
can have the [MIME type](mime_type.md) "text/plain", often with
suffixes indicating an encoding (e.g. "text/plain;charset=UTF-8".) Any
basic text reader can be used to view the contents of a simple text
file, however some (notably Notepad) have issues with certain less
popular encodings. Wordpad is included with
[Windows](windows.md) and may display the files properly.

Translation of a DOS/Windows text file to Unix is performed by removing
the Carriage Return from the end of the line. The reverse is simply the
addition of the Carriage Return to the Line Feed. Files that have double
spaces between the lines may have been improperly translated from one
system to another.

Text files usually have the **.txt** extension. A number of file formats
is actually "text files", but bear different extensions. For example is
web documents ([html](html.md) text files but is written
with a specific syntax so the applications the files are designed to
work with can read i correctly. Other kinds of files that can be seen as
text files are source code files, xml, etc.

