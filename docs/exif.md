---
tags:
  - Articles that need to be expanded
  - File Formats
---
The Exchangeable image file format (Exif) is an image [file format](file_formats.md)
which adds [metadata](metadata.md) to existing image formats, such as [JPEG](jpeg.md).

To read the Date/Time tag do:

* `exif --tag=0x132 filename.jpg` (reveals Date & Tag)
* `exif --tag=0x9003 filename.jpg` (reveals Date and Time (original))
* `exif --tag=0x9004 filename.jpg` (reveals Date and Time (digitized))

To set the Date/Time tag:

```bash
exif --tag=0x132 --set-value="1975:01:01 12:01:01" --ifd=0 filename.jpg
```

## See also

* [Document Metadata Extraction](document_metadata_extraction.md)

## External Links

* [Exif 2.2 specification](https://www.loc.gov/preservation/digital/formats/fdd/fdd000146.shtml)
* [Wikipedia: Exif](https://en.wikipedia.org/wiki/Exif)
