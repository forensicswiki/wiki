---
tags:
  - No Category
---
Interested in getting involved in computer forensics research? Here's
how to start.

## Recommended Reading

1. Read the proceedings for the past four years of the [DFRWS](https://dfrws.org/)
   conference.
1. Review the proceedings from the past few years of the IEEE/SADFE
   (Systematic Approaches to Digital Forensics Engineering) workshops.
1. Review the [IFIP Working Group 11.9 on Digital Forensics](http://www.ifip119.org/)
   website and look at the proceedings from the past conferences (unfortunately,
   you can't download the papers and the book costs more than \$100, but if you
   see something interesting it can usually be requested via
   interlibrary loan) (Some higher education libraries subscribe to
   SpringerLink which makes full text of these proceedings available to
   students and faculty as part of the school subscription)
   - [IFIP WG 11.9 publications](http://www.ifip119.org/Publications/)
1. Search for interesting forensic terms at the [ACM Digital Library](https://dl.acm.org/)
   and [CiteSeer](https://citeseer.ist.psu.edu/)
1. Review the [Sleuth Kit Website](http://www.sleuthkit.org/). In particular,
   review the issues of [The Sleuth Kit Informer](http://www.sleuthkit.org/informer/index.php)
   and download a copy of Sleuth Kit for your computer.

## Recommended Mailing Lists

- [sleuthkit-users](https://sourceforge.net/projects/sleuthkit/lists/sleuthkit-users)
- [computer forensic tool testing (cftt)](https://www.nist.gov/itl/ssd/software-quality-group/computer-forensics-tool-testing-program-cftt)

## Setting up a C++ development environment

Many people working in forensics find it useful to be able to compile
their tools from source code. Most of the tools compile on Linux, Mac,
and within the Cygwin environment under Windows.

Because all of these tools build upon one another, it is important to
compile and install them in the order specified below.

1. Download a copy of [libewf](https://github.com/libyal/libewf-legacy)
   and install it on your computer. This will allow your forensic tools
   to read and process [EnCase E01 disk images](encase_image_file_format.md).
1. Download a copy of [Sleuthkit](http://www.sleuthkit.org/sleuthkit/)
   and install it. Sleuth Kit is the basic open source computer
   forensics tool that allows the extraction of files from disk images.
   You can use it to recover deleted files.

If you are interested in doing file recovery, you may also wish to
explore:

- Sleuth Kit, above
- [PhotoRec](https://www.cgsecurity.org/wiki/PhotoRec), a file carver.
- [Adroit Photo Recovery](adroit_photo_forensics.md), a commercial
  photo recovery tool that's pretty amazing.

If you want to experiment with automated computer forensics research,
try these:

- [Bulk Extractor](bulk_extractor.md), a program from the Naval
  Postgraduate School that searches a disk image for email addresses and
  prints a histogram.
- [fiwalk](fiwalk.md), a program that processes a disk image and
  outputs an XML or ARFF file containing information about all of the
  file system metadata. fiwalk is now part of Sleuth Kit.

## Exercises for the Reader

1. Download the file
   [nps-2009-canon2-gen6.raw](http://digitalcorpora.org/corp/images/nps/nps-2009-canon2/nps-2009-canon2-gen6.raw)
   from the Digital Corpora website and try to recover as many files as
   you can. Some of the JPEGs can only be found using file carving, and
   some can only be found with fragment recovery file carving.
   - Can you determine when the photos were taken?
   - Can you determine *where* the photos were taken?
   - Can you determine the username of the person who took the photos?
   - Can you determine the clock offset of the camera from real time?

<!-- -->

1. Download the file
   [usbnist1.gen3.aff](http://digitalcorpora.org/corp/images/nps/nps-2009-ubnist1/ubnist1.gen3.aff)
   and find the government documents that were stored on the USB
   device.
