---
tags:
  - BSD
  - LGPL
  - Linux
  - MacOS
  - Tools
  - Windows
---
**libexif** is an [open source](open_source.md) library for reading and editing
[Exif](exif.md) metadata, commonly found in digital pictures. It is written in
C and released under the LGPL. The library runs under GNU/Linux, BSD, MacOS,
and Windows. The library is developed by the "libexif project." The project
also includes command-line and graphical front-ends.

## Examples

The use of the command-line front end is typical of many Unix or Linux commands.

` exif example.jpg`

This command will write all tags and values contained in the file to standard
output. It will also indicate if the file contains an embedded thumbnail.

Other common options for the exif command:

* -e extracts the thumbnail. You can use the --output option to a specified file
* -r removed the thumbnail from the image. Will write a new image. You can
  specify the file with the --output option
* -l lists all known tags
* --remove removes a specified tag or entire IFD (Image File Directory) is no
  tag is given

## External Links

* [libexif project documentation](https://libexif.sourceforge.net/docs.html)
* [man page for exif command line tool](https://libexif.sourceforge.net/man/exif.html)
