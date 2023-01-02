---
tags:
  - No Category
---
**Metadata** is data about data. Metadata plays a number of important
roles in [computer forensics](computer_forensics.md):

- It can provide corroborating information about the document data
  itself.
- It can reveal information that someone tried to hide, delete, or
  obscure.
- It can be used to automatically correlate documents from different
  sources.

Since metadata is fundamentally data, it suffers all of the data quality
and pedigre issues as any other form of data. Nevertheless, because
metadata isn't generally visible unless you use a special tool, more
skill is required to alter or otherwise manipulate it.

## Kinds of Metadata

Some kinds of metadata that are interesting in computer forensics:

- File system metadata (e.g. [MAC times](mac_times.md), access control lists
- Digital image metadata. Although information such as the image size
  and number of colors are technically metadata, [JPEG](jpeg.md)
  and other file formats store additional data about the photo or the
  device that acquired it.
- Document metadata, such as the creator of a document, it's last print
  time, etc.

## File types that support metadata and extraction tools

Below are some common data and metadata formats, the files in which they
are found, and a collection of tools that can be used to extract
information.

[Exchangeable Image File (EXIF)](exif.md) ([JPEG](jpeg.md) and [TIFF](tiff.md) image files; Music Files)
The EXIF format describes a format for a block of data that can be embedded into JPEG
and TIFF image files, as well as RIFF WAVE audio
files. Information includes date and time information, camera settings,
location information, textual descriptions, and copyright information.

- [LibExif](http://libexif.sourceforge.net/) (C)
- [Metadata extraction in Java](http://www.drewnoakes.com/code/exif/)
- [Adroit Photo Forensics](http://digital-assembly.com/products/adroit-photo-forensics/)

<!-- -->

[ID3](id3.md) ([MP3](mp3.md) files)
Implemented as a small block of data stored at the end of MP3 files. ID3v1 is a
128-byte block in a specified format allowing 30 bytes for song, artist and
album, 4 bytes for year, 30 bytes for comment, and 1 byte for genre. ID3v1.1
adds a track number. ID3v2 is a general container structure.

- [id3lib](http://id3lib.sourceforge.net/), a widely-used open source
  C/C++ ID3 implementation.
- [MP3::Info](http://search.cpan.org/dist/MP3-Info/) (Perl)
- [MPEG::ID3v2Tag](http://search.cpan.org/dist/MPEG-ID3v2Tag/) (Perl)

<!-- -->

[Microsoft](microsoft.md) [OLE Compound File](ole_compound_file.md)
Microsoft Office document files contain a huge amount of metadata. They
are created as OLE Compound Files and mainly stored in the so called
property set streams. Here are some tools for processing them:

- [Jakarta POI](http://jakarta.apache.org/poi/index.html) Open Source
  implementation in Java.
- [SquirrelGripper Perl script](https://cheeky4n6monkey.blogspot.com/2012/05/perl-script-plays-matchmaker-with.html)
  Extract fields into SQLite Database.
- [FOCA - Eleven Paths](https://www.elevenpaths.com/labstools/foca/index.html)
  Scan and group metadata information.

<!-- -->

[TIFF](tiff.md)
The Tagged Image File Format allows one or more images to be bundled in a
single file. Multiple [compression](compression.md) formats are supported.
[EXIF](exif.md) files can be stored inside TIFFs.

- [LibTIFF](http://www.libtiff.org/)
- [TIFF FAQ](http://www.awaresystems.be/imaging/tiff/faq.html)

# See Also

* [Document_Metadata_Extraction](document_metadata_extraction.md)

# External links

- [Wikipedia: Metadata](http://en.wikipedia.org/wiki/Metadata)
- [Automated Metadata Extraction](https://simson.net/clips/students/08Jun_Migletz.pdf),
  by James Migletz, June 2008
- [Why is Microsoft Office metadata what it is](https://journeyintoir.blogspot.com/2011/06/why-is-it-what-it-is.html),
  by Corey Harrell
