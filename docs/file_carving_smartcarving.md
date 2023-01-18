---
tags:
  - Data Carving
  - Data Recovery
---
**SmartCarving** is a [file carving](file_carving.md) technique to recover
fragmented files first proposed by A.  Pal, T. Sencar and N. Memon in DFRWS
2008.

The term **smart carving** was already proposed in 2006 in
[Analysis of 2006 DFRWS forensic carving challenge - A smart carving approach](http://sandbox.dfrws.org/2006/mora/dfrws2006.pdf).

SmartCarving utilizes a combination of structure based validation along
with validation of each file's unique content. Results for the
SmartCarving technique were demonstrated on fragmented JPEGs in the
DFRWS 2006 and DFRWS 2007 challenges. From these two challenges
SmartCarving was able to recover all but one fragmented JPEG file.

## History

Memon et al. presented an efficient algorithm based on a greedy heuristic and
alpha-beta pruning for reassembling fragmented images. Building on this work,
Memon et al. researched and introduced sequential hypothesis testing as an
effective mechanism for detecting fragmentation points of file. This paper won
the best paper award for DFRWS 2008. The techniques presented in the paper were
the foundation for the overall SmartCarving design.

## Details

After identifying a header block of a specific file type, for example,
JPEG, a SmartCarver will analyze each subsequent block to determine if
it belongs or does not belong to the starting block. If a block is
determined not to belong, then the file is assumed to be fragmented and
the SmartCarving algorithm looks for the next fragment by matching the
data of other available blocks with the first fragment. This process can
be done in parallel for many files.

## Applications

There are currently two commercial applications available that utilize
SmartCarving, both produced by Digital Assembly:

- [Adroit Photo Forensics](adroit_photo_forensics.md)
- Adroit Photo Recovery

Further there is one open-source solution under development:

- [Multimedia File Carver](https://github.com/rpoisel/mmc) -
  Implementation that focuses on the recovery of fragmented movies and
  images (JPEG)

## References

* Automated reassembly of file fragmented images using greedy algorithms,
  by A. Pal and N. Memon, in IEEE Transactions on Image processing, February 2006, pp 385­393
* Detecting File Fragmentation Point Using Sequential Hypothesis Testing,
  by A. Pal, T. Sencar and N. Memon, Digital Investigations, Fall 2008
