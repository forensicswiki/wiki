---
tags:
  - No Category
---
**DMG** is the proprietary Apple Disk Image file recognized & primarily
associated with the Macintosh OS X operating system used for emulating a
hard disk or DVD. The Apple Disk Image file is created in various types
of volumes (HFSX, HFS+, & HFS). It is a raw disk image file consisting
of block data and metadata. Often one or more layers are applied to the
file (optionally) for its encryption and compression.

The image file was primarily used for replicating contents into a
different disk. The source disk is duplicated exactly in the process
including free & slack spaces. The files are mounted & treated as a disk
entirely on Macintosh operating systems. DMG is equivalent to the ISO
disk image file of Windows systems.

## Overview

Originally Apple created a disk image file as Mac applications used
Resource Fork which posed little difficulty while being transmitted over
unified networks. Files, especially applications, were earlier divided
into logical parts; Data Fork & Resource Fork. Data Fork is the general
consideration of a file while Resource Fork consisted of data collection
with standard method of organization which only a dedicated API could
access.

Even though the usage of latter declined with the arrival of Mac OS X,
disk image format continued to be a standard format for software
distribution, owing to its purpose earlier.

Particularly, Disk Copy for 10.2 & earlier versions of Mac OS X and Disk
Utility for 10.3 & later versions of Mac OS X are used for creating
Apple disk images. Disk images can also be managed using ‘hdiutil’; the
command based utility for Mac OS X.

## Types of Format

DMG files can be different types and formats:

- UDBZ; bzip2 compressed Universal Disk Image Format (UDIF) image
- UDCO; Apple Data Compression (ADC) compressed Universal Disk Image
  Format (UDIF) image
- UDIF; Read-write uncompressed Universal Disk Image Format (UDIF) image
- UDRO; Read-only uncompressed Universal Disk Image Format (UDIF) image
- UDxx; Uncompressed Universal Disk Image Format (UDIF) image
- UDZO; zlib/DEFLATE compressed Universal Disk Image Format (UDIF) image
- ULFO; LZFSE compressed Universal Disk Image Format (UDIF) image
- ULMO; LZMA compressed Universal Disk Image Format (UDIF) image

These are all variants of the Universal Disk Image Format (UDIF), where
older DMG files might use the New Disk Image Format (NDIF).

DMG files, typically contain a partition table (APM, GPT, MBR) and a
file system (HFS+, APFS)

Mac OS Extended or HFS+ (HFS Plus) as they are commonly known, are image
format for DMG files supported by Mac OS 8.1 & above versions. The
format is further available as Journaled, Case-sensitive and with a
combination of both. Journaled DMG is the default and most used format
out of the rest.

## Partition Systems

A DMG image file can be created for the CD/DVD or a Hard Disk Partition.
Six different types of partition schemes are generally found, i.e. Hard
Disk, No Partition Map, CD/DVD, and Single Partition for – Apple
Partition Map, CD/DVD, Master Boot Record Partition Map, CD/DVD ISO
data, & GUID Partition Map.

## MIME Type & Optional Layers

Apple DMG files have an MIME type and can be protected using different
encryption types. ‘application/x-apple-diskimage’ is the MIME type used
to publish DMG files.

This block data containing raw disk image files are optionally added
with a layer or two providing encryption and compression. In
command-line utility, hdiutil the layers are known as CEncryptedEncoding
and CUDIFEncoding respectively.

DMG files are encrypted either with the help of 128 bit or 256 bit
Advanced Encryption Standard (AES). User keychain by default stores the
encryption password unless the remember password check is un-checked on
DiskUtility.

## Support

### On Macintosh Machine

Mac Operating Systems of version 10.2.3 were introduced to Disk Images
of Internet Enabled and Compressed type by Apple. Usage limit of the
disk image was to be only accessed with Apple’s Disk Copy Utility. The
program was later integrated to Disk Utility version 10.3.

A multilingual software agreement was displayed before the Disk Copy
utility mounted an image. Mounting the image was only possible on user
agreement to the license.

Presently, on a Mac OS 9 a DMG (uncompressed) can be opened only by
using either the developer or beta version for Disk Copy utility.

### On Non-Macintosh Machine

No documentation has by far been released by Apple on the format though
the attempt of interpreting Mac OS proprietary disk image, on Windows
platform has been a success. Freeware instrumentation includes DMG
Viewer, DMGExtractor, and dmg2img. The latter are implementation of the
attempt at reverse engineering parts of DMG. The first, however, offers
a platform for interpretation of Mac Disk Image without inverting its
structure.

The encryption layer was acting as a deadlock in reversing the
engineering of DMG files. Thus, implementation of support for encrypted
disk images was supplied by DMG Viewer, DMGExtractor and dmg2img.

Ample of options render independent mounting and extraction of Apple DMG
file. The long-familiar licensed cross platform utilities are:

**For Mounting:**

`  DMG Viewer`

**For Conversion:**

`  dmg2img`

**For Extraction:**

`  DMGExtractor`
`  7zip`
`  PeaZip`

## External Links

- [Demystifying the DMG File Format](http://newosxbook.com/DMG.html), by
  Jonathan Levin, June 2013
- [Mac OS disk image
  types](https://github.com/libyal/libmodi/blob/main/documentation/Mac%20OS%20disk%20image%20types.asciidoc),
  by the libmodi project

### Tools

- [DMG Viewer](http://www.systoolsgroup.com/dmg-viewer/)