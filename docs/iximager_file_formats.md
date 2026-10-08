---
tags:
  - File Formats
---
[ILook Investigator v8](ilook.md) and its disk-imaging
counterpart, [IXimager](iximager.md), offer three proprietary,
authenticated image formats:

* compressed (IDIF)
* non-compressed (IRBF)
* encrypted (IEIF)

Although few technical details are disclosed publicly, IXimager's online
documentation provides some insights: IDIF "includes protective mechanisms to
detect changes from the source image entity to the output form" and supports
"logging of user actions within the confines of that event;" IRBF is similar to
IDIF except that disk images are left uncompressed; IEIF, meanwhile, encrypts
said images.

For compatibility with ILook Investigator v7 and other forensic tools,
IXimager allows for the transformation of each of these formats into raw
format.

## Header

The header for these image formats appears to contain the string:
`RiPed_By_ILookImager` e.g.

```text
00000000  7f 52 69 50 65 64 5f 42  79 5f 49 4c 6f 6f 6b 49  |.RiPed_By_ILookI|
00000010  6d 61 67 65 72 00 01 70  03 00 dc 23 65 d6 15 19  |mager..p...#e...|
00000020  00 a1 81 87 d0 f4 69 a1  00 00 00 00 00 00 00 00  |......i.........|
00000030  00 00 00 00 00 00 00 00  00 00 00 00 00 00 00 00  |................|
*
```

## External Links

* [Sample image in EnCase, iLook, and dd format](https://cfreds.nist.gov/all/NIST/BasicMacImage),
  From the Computer Forensic Reference Data Sets Project
