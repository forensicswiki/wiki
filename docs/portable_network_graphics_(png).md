---
tags:
  - File Formats
  - Photo
---
**Portable Network Graphics** (aka PNG) is an image file format
developed to replace GIF images on the web. It uses lossless compression
and is thus not ideal for photographs. The types of images ideally
suited for PNG are line-art, text, other graphics that have sharp
transitions.

# Format

A PNG file comprises "chunks" of data, some of which are mandatory and
others of which are ancillary. Some ancillary chunks can contain
metadata text or timestamps, but does not contain nearly as much
metadata as [exif](exif.md) images.

PNG files begin with the following 8-byte (hexadecimal) signature:

    89 50 4E 47 0D 0A 1A 0A

# See Also

* [Tools for extracting image metadata](document_metadata_extraction.md)

# External Links

* [Wikipedia article](https://en.wikipedia.org/wiki/Portable_Network_Graphics)
* [W3C Recommendation](https://www.w3.org/TR/2003/REC-PNG-20031110/)
