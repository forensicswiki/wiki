---
tags:
  -  Articles that need to be expanded 
---
A disk image is a full disk copy of the data making up the partition
table, file allocation tables and data partitions without regard for
operating system.

A disk image should be made prior to performing any forensic analysis of
the disk. Creating a disk image is important in forensics for several
reasons:

1\. Ensure that disk information is not inadvertantly changed during
analysis.

2\. By performing an original disk image and storing the original disk,
it is possible to reproduce forensic test results with an exact
reproduction of analysis methods on the original evidence.

3\. Disk imaging will capture information invisible to the operating
system in use (e.g. hidden partitions, ext3 partitions on a Windows
machine, etc.)

## Software

Popular software used to create disk images includes [Norton
Ghost](norton_ghost.md) copy of the
original media should be done using the software, which may not be the
default settings on the software.

Other possible software, programs include [dd](dd.md),
[dcfldd](dcfldd.md), [EnCase](encase.md), and
[FTK](ftk.md)