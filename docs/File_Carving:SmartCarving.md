**SmartCarving** is a [file carving](File_Carving "wikilink") technique
to recover fragmented files first proposed by [A.
Pal](User:PashaPal "wikilink"), T. Sencar and [N.
Memon](User:NasirMemon "wikilink") in DFRWS 2008. The term **smart
carving** was already proposed in 2006 in [Analysis of 2006 DFRWS
forensic carving challenge - A smart carving
approach](http://sandbox.dfrws.org/2006/mora/dfrws2006.pdf).

SmartCarving utilizes a combination of structure based validation along
with validation of each file's unique content. Results for the
SmartCarving technique were demonstrated on fragmented jpegs in the
DFRWS 2006 and DFRWS 2007 challenges. From these two challenges
SmartCarving was able to recover all but one fragmented jpeg file.

## History

[Memon](User:NasirMemon "wikilink") et al.\[1\] presented an efficient
algorithm based on a greedy heuristic and alpha-beta pruning for
reassembling fragmented images. Building on this work,
[Memon](User:NasirMemon "wikilink") et al.\[2\] researched and
introduced sequential hypothesis testing as a an effective mechanism for
detecting fragmentation points of file. This paper won the best paper
award for DFRWS 2008. The techniques presented in the paper were the
foundation for the overall SmartCarving design.

## Details

After identifying a header block of a specific file type, for example,
jpeg, a SmartCarver will analyze each subsequent block to determine if
it belongs or does not belong to the starting block. If a block is
determined not to belong, then the file is assumed to be fragmented and
the SmartCarving algorithm looks for the next fragment by matching the
data of other available blocks with the first fragment. This process can
be done in parallel for many files.

## Applications

There are currently two commercial applications available that utilize
SmartCarving, both produced by Digital Assembly:

- [Adroit Photo Forensics](Adroit_Photo_Forensics "wikilink")
- Adroit Photo Recovery

Further there is one open-source solution under development:

- [Multimedia File Carver](https://github.com/rpoisel/mmc) -
  Implementation that focuses on the recovery of fragmented movies and
  images (JPEG)

## References

- A. Pal and N. Memon, ["Automated reassembly of file fragmented images
  using greedy
  algorithms"](http://digital-assembly.com/technology/research/pubs/ieee-trans-2006.pdf)
  in IEEE Transactions on Image processing, February 2006, pp 385­393
- A. Pal, T. Sencar and N. Memon, ["Detecting File Fragmentation Point
  Using Sequential Hypothesis
  Testing"](http://digital-assembly.com/technology/research/pubs/dfrws2008.pdf),
  Digital Investigations, Fall 2008

## External links

- [Adroit Photo
  Recovery](http://digital-assembly.com/products/adroit-photo-recovery/)
- [Adroit Photo
  Forensics](http://digital-assembly.com/products/adroit-photo-forensics/)
- [Link to SmartCarving Technology and
  Research](http://digital-assembly.com/technology/)
- [Digital Assembly](http://digital-assembly.com)