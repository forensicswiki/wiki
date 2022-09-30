---
tags:
  -  Libyal
---
The **libsmraw** package contains a library and applications to read and
write (split) RAW storage media bitstream copies. Libsmraw contains
supports for multiple (split) RAW naming schemes.

## History

Libsmraw was created by [Joachim Metz](joachim_metz.md) in 2010,
while working for [Hoffmann Investigations](http://en.hoffmannbv.nl/).
Libsmraw is a rewrite of earlier work for the proof-of-concept
multi-threaded imager: GNOME Forensic Imager.

## Tools

The **libsmraw** package contains the following tools:

- **smrawmount**, which FUSE mounts (split) RAW image files.

The **libsmraw** package also contains the following bindings:

- **pysmraw**, bindings for Python (libsmraw 20140621 or later).

## Examples

FUSE mounting a split RAW image (libsmraw 20110916 or later)

    smrawmount image.raw.000 mount_point

Or:

    smrawmount image.raw.??? mount_point

## Also See

[RAW Image format](raw_image_format.md)

## External Links

- [Project site](https://github.com/libyal/libsmraw/)

