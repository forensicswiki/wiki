---
tags:
  - Libyal
  - Analysis
  - LGPL
  - Tools
---
The **libuna** package contains a library and application to read and
write the [Text File (txt)](text_file_(txt).md) format in
different characters encodings.

Libuna currently supports:

- 7-bit ASCII
- ISO 8859-1, 8859-2, 8859-3, 8859-4, 8859-5, 8859-6, 8859-7, 8859-8,
  8859-9, 8859-10, 8859-11, 8859-13, 8859-14, 8859-15
- [Windows](windows.md) 874, 932, 936, 949, 950, 1250, 1251,
  1252, 1253, 1254, 1255, 1256, 1257, 1258
- Kod Obmena Informatsiey 8-bit; KOI8-R, KOI8-U
- UTF-7, UTF-8, UTF-16, UTF-32

## History

Libuna was created by [Joachim Metz](joachim_metz.md) in 2008,
while working for Hoffmann Investigations.

The codepages are based on
[libiconv](http://www.gnu.org/software/libiconv/) and documentation
available by [Microsoft](microsoft.md).

Currently libuna mainly supports the Windows codepages to be able to
convert these when encountered in file formats that use them.

Libuna is intended as a character encoding support library and is used
in:

- [libewf](libewf.md)
- [libnk2](libnk2.md)
- [libpff](libpff.md)

## Tools

The **libuna** package contains the following tools:

- **unaexport**, which exports the plain text files in different
  encodings. It also allows end of line conversion and control over the
  byte order mark (BOM).

## External Links

- [project site](https://github.com/libyal/libuna/)
