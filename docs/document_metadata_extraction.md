---
tags:
  - Tools
---
Here are tools that will extract metadata from document files.

## Tools

[antiword](https://en.wikipedia.org/wiki/Antiword)

[Belkasoft](belkasoft.md) Evidence Center

Extracts metadata from various [Microsoft](microsoft.md) Office
files (both 97-2003 and 2007-2013 formats), as well as Open Office
documents. Besides, can extract plain texts (combining all texts from
all XLS/XLSX/ODS pages and PPT/PPTX/ODP slides) and embedded objects.
The tool can visualize pictures embedded in a document.

[catdoc](https://github.com/petewarden/catdoc)

[word2x](https://word2x.sourceforge.net/)

[wvWare](https://wvware.sourceforge.net/)

Extracts metadata from various [Microsoft Word](microsoft_office.md) (doc)
files. Can also convert doc files to other formats such as HTML or plain text.

[FI Tools](https://www.fid3.com/)

More than 100 file types.

# PDF Files

[Belkasoft](belkasoft.md) Evidence Center

Extracts metadata from [PDF](pdf.md) files. Besides, can extract
texts and embedded objects. For pictures, embedded into a PDF document,
the tool can visualize them all right in its user interface.

[pdfinfo](pdfinfo.md) (part of the [xpdf](xpdf.md)
package) displays some metadata of [PDF](pdf.md) files.

[XpdfReader](https://www.xpdfreader.com/index.html)

# Images

[Belkasoft](belkasoft.md) Evidence Center

Extracts [EXIF](exif.md) metadata from [JPEG](jpeg.md)
files as well as many digital camera raw files. The tool allows a user
to create complex filters based on various criteria on EXIF properties.
Photos with GPS coordinates can be shown on Google Maps and Google
Earth. Evidence Center can analyze existing Thumbs.db files and Thumbs
Cache as well as carve deleted thumbnails.

[Exiftool](exiftool.md)

Free, cross-platform tool to extract metadata from many different file
formats. Also supports writing

[jhead](jhead.md)
<https://www.sentex.ca/~mwandel/jhead/>

Displays or modifies [Exif](exif.md) data in
[JPEG](jpeg.md) files.

[vinetto](vinetto.md)
<https://vinetto.sourceforge.net/>

Examines [Thumbs.db](thumbs.db.md) files.

[libexif](libexif.md)
<https://sourceforge.net/projects/libexif> EXIF tag Parsing Library

[Adroit Photo Forensics](adroit_photo_forensics.md)

Displays meta data and uses date and camera meta-data for grouping,
timelines etc.

[exiftags](https://johnst.org/sw/exiftags/)

open source utility to parse and edit [exif](exif.md) data in
[JPEG](jpeg.md) images. Found in many Debian based
distributions.

[exifprobe](https://www.virtual-cafe.com/~dhh/tools.d/exifprobe.d/exifprobe.html)

Open source utility that reads [exif](exif.md) data in
[JPEG](jpeg.md) and some "RAW" image formats. Found in many
Debian based distributions.

[Exiv2](https://exiv2.org/)

Open source C++ library and command line tool for reading and writing
metadata in various image formats. Found in almost every GNU/Linux
distribution

[pngmeta](https://sourceforge.net/projects/pmt/files/)

Open source command line tool that extracts metadata from PNG images. Found in
many Debian based distributions.

# General

These general-purpose programs frequently work when the special-purpose
programs fail, but they generally provide less detailed information.

[Metadact-e](https://www.litera.com/products/metadact)
"Patented server-based metadata cleaning software that previews, cleans
and converts documents in Microsoft Outlook, Web Access email, tablets
and smartphones, as well as desktop-based documents."

[Metadata Extraction Tool](https://meta-extractor.sourceforge.net/)
"Developed by the National Library of New Zealand to programmatically
extract preservation metadata from a range of file formats like PDF
documents, image files, sound files Microsoft office documents, and many
others."

[hachoir-metadata](hachoir.md)
Extraction tool, part of **[Hachoir](hachoir.md)** project

[file](file.md)
The UNIX **file** program can extract some metadata

[GNU libextractor](https://www.gnunet.org/en/)
The libextractor library is a plugable system for extracting metadata

[Directory Lister Pro](https://www.krksoft.com/)
Directory Lister Pro is a Windows tool which creates listings of files
from selected directories on hard disks, CD-ROMs, DVD-ROMs, floppies,
USB storages and network shares. Listing can be in HTML, text or CSV
format (for easy import to Excel). Listing can contain standard file
information like file name, extension, type, owner and date created, but
especially for forensic analysis file meta data can be extracted from
various formats: 1) executable file information (EXE, DLL, OCX) like
file version, description, company, product name. 2) multimedia
properties (MP3, AVI, WAV, JPG, GIF, BMP, MKV, MKA, MPEG) like track,
title, artist, album, genre, video format, bits per pixel, frames per
second, audio format, bits per channel. 3) Microsoft Office files (DOC,
DOCX, XLS, XLSX, PPT, PPTX) like document title, author, keywords, word
count. For each file and folder it is also possible to obtain its CRC32,
MD5, SHA-1 and Whirlpool hash sum. Extensive number of options allows to
completely customize the visual look of the output. Filter on file name,
date, size or attributes can be applied so it is possible to limit the
files listed.

[Apache Tika](https://tika.apache.org/)
Apache Tika extracts metadata from a wide range of file formats and
normalizes metadata keys to Dublin Core when possible. In recent
versions of Tika, we have focused on extracting more information about
"authors" (original author, comment authors, last-saved-by, editors,
etc.) in general formats and more granular information for to/from/bcc
info in .msg files. We've also added extraction of "original paths,"
when available, that might allow examiners to see the full path that the
file or its attachments were stored. Finally, we've enriched extraction
from XMP to allow identification of uuids and ancestor uuids. Tika can
run in batch mode from input directory to output directory, and we
recommend the RecursiveParserWrapper (-J -t options in the commandline
app or /rmeta endpoint in
[tika-server](https://cwiki.apache.org/confluence/display/tika/TikaJAXRS)) to capture
metadata from embedded documents.
