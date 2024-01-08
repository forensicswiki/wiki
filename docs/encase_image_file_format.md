---
tags:
  -  File Formats
  -  Disk Image
---
The Encase image file format is used by [EnCase](encase.md) used
to store various types of digital evidence e.g.

- disk image (physical bitstream of an acquired disk)
- volume image
- memory
- logical files

## History

Expert Witness (for Windows) was the original name for EnCase (dating
back to 1998). More info about this can be found on the Internet Archive
[1](http://web.archive.org/web/19980504153628/http://guidancesoftware.com/)
including a demo of the original software
[2](http://web.archive.org/web/19980504153952/http://guidancesoftware.com/data/ewsetup.exe).

(presumably) the product was renamed because it intruded the Expert
Witness trademark held by ASR Data
[3](http://www.asrdata.com/wp-content/themes/asr/pdf/ruling.pdf).

The Encase image file format therefore is also referred to as the Expert
Witness (Compression) Format.

Currently there are 2 versions of the format:

- version 1 is (reportedly) based on [ASR Data's Expert Witness
  Compression
  Format](asr_data's_expert_witness_compression_format.md)
- version 2 was introduced in EnCase 7, for which a format specification
  (at least non-encrypted Ex01) is available, but requires registration.

The libewf project indicates that the January 2012 version of the
version 2 format specification, besides Lx01 not being specified, is
sufficient to read non-encrypted Ex01 files.

Although the format specification is not complete, at the moment
Guidance Software is working on an update. This will not include:

- encrypted Ex01
- Lx01

So in contrast to other claims both versions of the EWF file format are:

- proprietary
- partially open specification

For more information about these definitions see: [File formats](file_formats.md)

## Version 1

The media data can be stored in multiple evidence files, which are
called segment files. Each segment file consist of multiple sections,
which has a distinct section start definition containing a section type.
Up to EnCase 5 the segment file were limited to 2 GiB, due to the
internal 31-bit file offset representation. This limitation was lifted
by adding a base offset value in EnCase 6.

EnCase allows to store the data compressed either using a fast or best
level of the deflate compression method. EnCase 7 no longer
distinguishes between fast or best compression and just provides for
either uncompressed or compressed.

Besides digital evidence the evidence files, or segment files, contain a
header containing case information. The case information which entails
date and time of acquisition, an examiner's name, notes on the
acquisition, and an optional password.

- In EnCase 3 the case information header is stored in the "header"
  section, which is defined twice within the file and contain the same
  information.
- As of EnCase 4 an additional "header2" section was added. The "header"
  section now appears only once, but the new "header2" section twice.

The format adds error detection by storing the data with checksums
(Adler32), for both the metadata as the data blocks, which are by
default 64 x 512 byte sectors (32 KiB). As of EnCase 5 the number of
sectors per block (chunk) can vary. EnCase 3F introduced an "error2"
section that it uses to record the location and number of bad sector
chunks. The way it handles the sections it can't read is that those
areas are filled with zero. Then EnCase displays to the user the areas
that could not be read when the image was acquired. The granularity of
unreadable chunks appears to be 32K. As of EnCase 5 the granularity of
unreadable chunks can vary.

EnCase 3 can store a one-way hash of the data. For a bitstream it does
so by calculating e.g. a MD5 hash of the original media data and adds a
hash section to the last of the segment file. As of EnCase 6 the option
to store a SHA1 hash was added.

EnCase 5 and later have the option to store **single files** into the
EnCase Logical Evidence File (LEF) or EWF-L01. This format changed
slightly in EnCase 6 and 7.

## Version 2

In EnCase 7 the EWF format was succeeded by the EnCase Evidence File
Format Version 2 (EWF2-EX01 and EWF2-LX01). EWF2-EX01 is at it's lower
levels a different format then EWF-E01 and provides support for:

- bzip2 compression
- direct encryption (AES-256) of the section data

The same features are added to the new logical evidence file format
(EWF2-LX01) with the exception of encryption. The actual encryption
method and corresponding key derivation are, currently, not open.

EWF2-EX01, EWF2-LX01 are not backwards compatible with previous EnCase
products.

## See Also

- [ASR Data's Expert Witness Compression Format](asr_data's_expert_witness_compression_format.md)
- [EnCase](encase.md)

### Tools

- [E01 Viewer](e01_viewer.md)

## External Links

- [Sample image in EnCase, iLook, and dd format](https://cfreds.nist.gov/all/NIST/BasicMacImage) -
  From the Computer Forensic Reference Data Sets Project, the E01 sample image
  dates from January 2005
- [Expert Witness Compression Format (EWF)](https://github.com/libyal/libewf/blob/main/documentation/Expert%20Witness%20Compression%20Format%20(EWF).asciidoc),
  by the [libewf project](libewf.md), March 2006
- [Expert Witness Compression Format (EWF) version 2](https://github.com/libyal/libewf/blob/main/documentation/Expert%20Witness%20Compression%20Format%202%20(EWF2).asciidoc),
  by the [libewf project](libewf.md), July 2012
- [Validation of forensic images for assurance of digital evidence integrity](https://researchportal.murdoch.edu.au/esploro/outputs/graduate/Validation-of-forensic-images-for-assurance/991005544234707891),
  by James Michael McCutcheon, November, 2014
