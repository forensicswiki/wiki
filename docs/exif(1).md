---
tags:
  - No Category
---
The **Exchangeable image file format** (Exif) is an image [file
format](file_format.md) which adds lots of
[metadata](metadata.md) to existing image formats, mainly
[JPEG](jpeg.md).

To read the Date/Time tag do:

` exif --tag=0x132 filename.jpg       (reveals Date & Tag) `
` exif --tag=0x9003 filename.jpg      (reveals Date and Time (original))`
` exif --tag=0x9004 filename.jpg      (reveals Date and Time (digitized))`

To set the Date/Time tag:

` exif  --tag=0x132 --set-value="1975:01:01 12:01:01" --ifd=0 filename.jpg`

For tools that extract Exif meta data look here -
[Document_Metadata_Extraction#Images](document_metadata_extraction#images.md)

## External Links

- [exif.org](http://exif.org/)
- [Exif 2.2 specification](media:exif2-2.pdf.md)
- [Exif](http://en.wikipedia.org/wiki/Exif) article in the Wikipedia.