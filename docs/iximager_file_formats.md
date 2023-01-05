---
tags:
  - No Category
---
[ILook Investigator v8](ilook.md) and its disk-imaging
counterpart, [IXimager](iximager.md), offer three proprietary,
authenticated image formats: compressed (IDIF), non-compressed (IRBF),
and encrypted (IEIF). Although few technical details are disclosed
publicly, IXimager's online documentation provides some insights: IDIF
"includes protective mechanisms to detect changes from the source image
entity to the output form" and supports "logging of user actions within
the confines of that event;" IRBF is similar to IDIF except that disk
images are left uncompressed; IEIF, meanwhile, encrypts said images.

For compatibility with ILook Investigator v7 and other forensic tools,
IXimager allows for the transformation of each of these formats into raw
format.

## Header

The header for these image formats appears to contain the string:

    RiPed_By_ILookImager

## External Links

- [Sample image in EnCase, iLook, and dd
  format](https://cfreds.nist.gov/v2/Basic_Mac_Image.html) - From the
  [Computer Forensic Reference Data
  Sets](computer_forensic_reference_data_sets.md) Project