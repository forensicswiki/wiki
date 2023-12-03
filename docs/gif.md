---
tags:
  - File Formats
---
The **Graphics Interchange Format** (**GIF**) (SM) format is a lossless image
format. GIF images use internal LZW compression to reduce file size. CompuServe
created this format, which is a bitmap image format allowing 256 different
colors to be selected from a 24-bit color palette (RGB). GIF also allows for
animations by sequencing through multiple GIF image data inside a single file.

"The Graphics Interchange Format(c) is the Copyright property of
CompuServe Incorporated. GIF(sm) is a Service Mark property of
CompuServe Incorporated."

## Format

GIF files consist of a [header](header.md), image data, optional
[metadata](metadata.md), and a [footer](footer.md). The
header consists of a signature and a version, each 3 bytes long. The
signature is `47 49 46` (hex) / `GIF` (text). The versions are either
`38 37 61` or `38 39 61` (hex) / `87a` or `89a` (text) respectively. The
footer or trailer (as identified in the format specification) is usually
`3B` (hex).

Common file extensions are .gif and .GIF

## Metadata

GIF89a files can contain [metadata](metadata.md) in text format. GIF metadata
is contained in sections identified as a Comment Extension, a Plain Text
Extension, and an Application Extension. All extension sections begin with the
Extension Introducer `21` (hex).

Comment Extensions are optional and more than one may be present. They
were designed to allow including comments about the graphic, credits,
descriptions or other types of non-control/non-graphic data. The
beginning of this block has the Extension Introducer and a Comment Label
`FE` (hex). Comment data has a sequence of sub-blocks between 1 and 255
bytes in length, with the size in a byte before the data. Comment
Extensions should appear either before or after the control and graphic
data blocks.

Plain Text Extensions are optional and more than one may be present.
They were designed to allow rendering of textual data as a graphic. The
beginning of this block has the Extension Introducer and a Comment Label
`01` (hex). Plain text data has a sequence of sub-blocks between 1 and
255 bytes in length, with the size in a byte before the data.

Application Extensions are optional. They were designed to allow
applications to insert application specific data inside a GIF. The
beginning of this block has the Extension Introducer and an Application
Extension Label `FF` (hex).

## External Links

- [Wikipedia: GIF](https://en.wikipedia.org/wiki/GIF)
- [W3.Org: GRAPHICS INTERCHANGE FORMAT SPECIFICATION](https://www.w3.org/Graphics/GIF/spec-gif89a.txt)
