---
tags:
  -  Tools
  -  Disk Analysis
  -  Open Source Software
  -  Windows
  -  Linux
  -  MacOS
---
## Overview

**bulk_extractor** is a computer forensics tool that scans a disk image,
a file, or a directory of files and extracts useful information without
parsing the file system or file system structures. The results can be
easily inspected, parsed, or processed with automated tools.
**bulk_extractor** also creates a histograms of features that it finds,
as features that are more common tend to be more important. The program
can be used for law enforcement, defense, intelligence, and
cyber-investigation applications.

bulk_extractor is distinguished from other forensic tools by its speed
and thoroughness. Because it ignores file system structure,
bulk_extractor can process different parts of the disk in parallel. In
practice, the program splits the disk up into 16MiByte pages and
processes one page on each available core. This means that 24-core
machines process a disk roughly 24 times faster than a 1-core machine.
bulk_extractor is also thorough. That’s because bulk_extractor
automatically detects, decompresses, and recursively re-processes
compressed data that is compressed with a variety of algorithms. Our
testing has shown that there is a significant amount of compressed data
in the unallocated regions of file systems that is missed by most
forensic tools that are commonly in use today.

Another advantage of ignoring file systems is that bulk_extractor can be
used to process any digital media. We have used the program to process
hard drives, SSDs, optical media, camera cards, cell phones, network
packet dumps, and other kinds of digital information.

## Output Feature Files

bulk_extractor now creates an output directory that includes:

- **ccn.txt** -- Credit card numbers
- **ccn_track2.txt** -- Credit card “track 2″ information
- **domain.txt** -- Internet domains found on the drive, including
  dotted-quad addresses found in text.
- **email.txt** -- Email addresses
- **ether.txt** -- Ethernet MAC addresses found through IP packet
  carving of swap files and compressed system hibernation files and file
  fragments.
- **exif.txt** -- EXIFs from JPEGs and video segments. This feature file
  contains all of the EXIF fields, expanded as XML records.
- **find.txt** -- The results of specific regular expression search
  requests.
- **ip.txt** -- IP addresses found through IP packet carving.
- **telephone.txt** --- US and international telephone numbers.
- **url.txt** --- URLs, typically found in browser caches, email
  messages, and pre-compiled into executables.
- **url_searches.txt** --- A histogram of terms used in Internet
  searches from services such as Google, Bing, Yahoo, and others.
- **wordlist.txt** --- :A list of all “words” extracted from the disk,
  useful for password cracking.
- **wordlist_\*.txt** --- The wordlist with duplicates removed,
  formatted in a form that can be easily imported into a popular
  password-cracking program.
- **zip.txt** --- A file containing information regarding every ZIP file
  component found on the media. This is exceptionally useful as ZIP
  files contain internal structure and ZIP is increasingly the compound
  file format of choice for a variety of products such as Microsoft
  Office

For each of the above, two additional files may be created:

- **\*_stopped.txt** --- bulk_extractor supports a stop list, or a list
  of items that do not need to be brought to the user’s attention.
  However rather than simply suppressing this information, which might
  cause something critical to be hidden, stopped entries are stored in
  the stopped files.
- **\*_histogram.txt** --- bulk_extractor can also create histograms of
  features. This is important, as experience has shown that email
  addresses, domain names, URLs, and other information that appear more
  frequently on a hard drive or in a cell phone’s memory can be used to
  rapidly create a pattern of life report.

Bulk extractor also creates a file that captures the provenance of the
run:

report.xml
A Digital Forensics XML report that includes information about the
source media, how the bulk_extractor program was compiled and run, the
time to process the digital evidence, and a meta report of the
information that was found.

## Post-Processing

We have developed four programs for post-processing the bulk_extractor
output:

bulk_diff.py
This program reports the differences between two bulk_extractor runs.
The intent is to image a computer, run bulk_extractor on a disk image,
let the computer run for a period of time, re-image the computer, run
bulk_extractor on the second image, and then report the differences.
This can be used to infer the user’s activities within a time period.

cda_tool.py
This tool, currently under development, reads multiple bulk_extractor
reports from multiple runs against multiple drives and performs a
multi-drive correlation using Garfinkel’s Cross Drive Analysis
technique. This can be used to automatically identify new social
networks or to identify new members of existing networks.

identify_filenames.py
In the bulk_extractor feature file, each feature is annotated with the
byte offset from the beginning of the image in which it was found. The
program takes as input a bulk_extractor feature file and a DFXML file
containing the locations of each file on the drive (produced with
Garfinkel’s fiwalk program) and produces an annotated feature file that
contains the offset, feature, and the file in which the feature was
found.

make_context_stop_list.py
Although forensic analysts frequently make “stop lists”—for example, a
list of email addresses that appear in the operating system and should
therefore be ignored—such lists have a significant problem. Because it
is relatively easy to get an email address into the binary of an open
source application, ignoring all of these email addresses may make it
possible to cloak email addresses from forensic analysis. Our solution
is to create context-sensitive stop lists, in which the feature to be
stopped is presented with the context in which it occurs. The
make_context_stop_list.py program takes the results of multiple
bulk_extractor runs and creates a single context-sensitive stop list
that can then be used to suppress features when found in a specific
context. One such stop list constructed from Windows and Linux operating
systems is available on the bulk extractor website.

## Download

The current version of **bulk_extractor** is 1.5.5.

- Downloads for Windows and Linux/Unix systems are available at:
  <https://downloads.digitalcorpora.org/downloads/bulk_extractor/>

Version 2.0 is under development.

## Bibliography

### Academic Publications

1.  Garfinkel, Simson, [Digital media triage with bulk data analysis and
    bulk_extractor](https://simson.net/clips/academic/2013.COSE.bulk_extractor.pdf).
    Computers and Security 32: 56-72 (2013)
2.  Beverly, Robert, Simson Garfinkel and Greg Cardwell, ["Forensic
    Carving of Network Packets and Associated Data
    Structures"](https://simson.net/clips/academic/2011.DFRWS.ipcarving.pdf),
    DFRWS 2011, Aug. 1-3, 2011, New Orleans, LA. BEST PAPER AWARD
    (Acceptance rate: 23%, 14/62)
3.  Garfinkel, S., [Forensic Feature Extraction and Cross-Drive
    Analysis,](https://simson.net/clips/academic/2006.DFRWS.pdf)The 6th
    Annual Digital Forensic Research Workshop Lafayette, Indiana, August
    14-16, 2006. (Acceptance rate: 43%, 16/37)

### YouTube

**[search
YouTube](https://www.youtube.com/results?search_query=bulk_extractor) for
bulk_extractor videos**

- [Simson Garfinkel speaking at CERIAS about
  bulk_extractor](https://www.youtube.com/watch?v=odvDTGA7rYI)
- [BackTrack 5 with
  bulk_extractor](https://www.youtube.com/watch?v=wTBHM9DeLq4)
- [Ubuntu 12.04 forensics with
  bulk_extractor](https://www.youtube.com/watch?v=QVfYOvhrugg)
- [Social Network forensics with
  bulk_extractor](https://www.youtube.com/watch?v=57RWdYhNvq8)

### Tutorials

1.  [Using bulk_extractor for digital forensics triage and cross-drive
    analysis](http://simson.net/ref/2012/2012-08-08%20bulk_extractor%20Tutorial.pdf),
    DFRWS 2012