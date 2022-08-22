**Metadata** is data about data. Metadata plays a number of important
roles in [computer forensics](computer_forensics "wikilink"):

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

- [File system](File_system "wikilink") metadata (e.g. [MAC
  times](MAC_times "wikilink"), [access control
  lists](access_control_lists "wikilink"), etc.)
- Digital image metadata. Although information such as the image size
  and number of colors are technically metadata, [JPEG](JPEG "wikilink")
  and other file formats store additional data about the photo or the
  device that acquired it.
- Document metadata, such as the creator of a document, it's last print
  time, etc.

## File types that support metadata and extraction tools

Below are some common data and metadata formats, the files in which they
are found, and a collection of tools that can be used to extract
information.

[EXIF](EXIF "wikilink") ([JPEG](JPEG "wikilink") and [TIFF](TIFF "wikilink") image files; Music Files)
The [Exchangeable Image File](Exchangeable_Image_File "wikilink") format
describes a format for a block of data that can be embedded into JPEG
and TIFF image files, as well as [RIFF WAVE](RIFF_WAVE "wikilink") audio
files. Information includes date and time information, camera settings,
location information, textual descriptions, and copyright information.

- [PEL: PHP Exif Library](http://pel.sourceforge.net/)
- [LibExif](http://libexif.sourceforge.net/) (C)
- [Metadata extraction in Java](http://www.drewnoakes.com/code/exif/)
- [Adroit Photo
  Forensics](http://digital-assembly.com/products/adroit-photo-forensics/)

<!-- -->

[ID3](ID3 "wikilink") ([MP3](MP3 "wikilink") files)
Implemented as a small block of data stored at the end of MP3 files.
[ID3v1](ID3v1 "wikilink") is a 128-byte block in a specified format
allowing 30 bytes for song, artist and album, 4 bytes for year, 30 bytes
for comment, and 1 byte for genre. [ID3v1.1](ID3v1.1 "wikilink") adds a
track number. [ID3v2](ID3v2 "wikilink") is a general container
structure. For more information, see [1](http://www.id3.org/).

- [id3lib](http://id3lib.sourceforge.net/), a widely-used open source
  C/C++ ID3 implementation.
- [Java library MP3](http://www.vdheide.de/projects.html)
- [MP3::Info](http://search.cpan.org/dist/MP3-Info/) (Perl)
- [MPEG::ID3v2Tag](http://search.cpan.org/dist/MPEG-ID3v2Tag/) (Perl)

<!-- -->

[Microsoft](Microsoft "wikilink") [OLE Compound File](OLE_Compound_File "wikilink")
Microsoft Office document files contain a huge amount of metadata. They
are created as OLE Compound Files and mainly stored in the so called
property set streams. Here are some tools for processing them:

- [Jakarta POI](http://jakarta.apache.org/poi/index.html) Open Source
  implementation in Java.
- [Payne Consulting Metadata
  Assistant](http://www.thepaynegroup.com/products/metadata/) Metadata
  Analysis and cleanup.
- [Inforenz Forager](http://www.inforenz.com/software/forager.html)
  Inforenz Forager
- [OleDeconstruct](http://sandersonforensics.com/forum/content.php?120-OleDeconstruct)
  Free utility from Sanderson Forensics.
- [SquirrelGripper Perl
  script](https://cheeky4n6monkey.blogspot.com/2012/05/perl-script-plays-matchmaker-with.html)
  Extract fields into SQLite Database.
- [FOCA - Eleven
  Paths](https://www.elevenpaths.com/labstools/foca/index.html) Scan and
  group metadata information.

<!-- -->

[TIFF](TIFF "wikilink")
The [Tagged Image File Format](Tagged_Image_File_Format "wikilink")
allows one or more images to be bundled in a single file. Multiple
[compression](compression "wikilink") formats are supported.
[EXIF](EXIF "wikilink") files can be stored inside TIFFs.

- [LibTIFF](http://www.remotesensing.org/libtiff/)
- [TIFF FAQ](http://www.awaresystems.be/imaging/tiff/faq.html)

# See Also

[Document_Metadata_Extraction](Document_Metadata_Extraction "wikilink")

# External links

- [Wikipedia: Metadata](http://en.wikipedia.org/wiki/Metadata)
- [Automated Metadata
  Extraction](http://theses.nps.navy.mil/08Jun_Migletz.pdf),James
  Migletz, Master's Thesis, Naval Postgraduate School, June 2008
- [Why is Microsoft Office metadata what it
  is](https://journeyintoir.blogspot.com/2011/06/why-is-it-what-it-is.html),
  [Corey Harrell](Corey_Harrell "wikilink"), Journey Into Incident
  Response