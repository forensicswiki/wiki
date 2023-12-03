---
tags:
  - File Formats
---
The **Joint Photographic Experts Group** (**JPEG**) format is a
commonly-used lossy image format.

# Format

JPEG is a container file format that consist of a well defined
[header](header.md), some [metadata](metadata.md),
icons, a color table, compressed data, and a well defined
[footer](footer.md).

Common file extensions are .jpg, .jpeg, .JPG, .JPE, and .jfif.

# Metadata

JPEG files can contain lots of [metadata](metadata.md) in several formats, such
as Exif, IPTC, GPS, or Camera Raw.

The [exif](exif.md) and [jhead](jhead.md) command tools can extract and
manipulate some of that metadata. [Adroit Photo Forensics](adroit_photo_forensics.md)
can be used to extract, view and group metadata from jpeg and camera Raw files.
In iOS, the [Photo Investigator](photo_investigator.md) can extract, view, and
remove metadata from all images.

# Also see

* [exif](exif.md)

# Externals Links

- [JPEG File Interchange Format Version 1.02](https://www.w3.org/Graphics/JPEG/jfif3.pdf)
- [Adobe: XMP Specification](https://www.adobe.com/products/xmp/standards.html)
- [Extensible Metadata Platform (XMP)](https://www.adobe.com/products/xmp.html)
- [FlashPix Tags](https://exiftool.org/TagNames/FlashPix.html)
- [ISO/IEC 10918-1](https://www.w3.org/Graphics/JPEG/itu-t81.pdf),
  Section: Annex B contains a detailed description of the JPEG file
  structure.
- [Wikipedia: ICC profile](https://en.wikipedia.org/wiki/ICC_profile)
- [Wikipedia: JPEG](https://en.wikipedia.org/wiki/JPEG)
