---
tags:
  -  Data Recovery
  -  Articles that need to be expanded 
---
A [forensic investigator](forensic_investigator.md) uses
techniques that can **recover bad data** in order to recover data from a
[disk drive](disk_drive.md) that is malfunctioning.

One popular program for recovering bad data is
[SpinRite](spinrite.md). This program works by turning off the
disk drive's own data recovery technology and repeatedly re-reading each
*bad* sector, with the hope that a good read may eventually happen.

The [dd_rescue](dd_rescue.md) program can't recover from *bad*
sectors, but it can skip around a disk and recover data that is still
mostly good. [dd_rescue](dd_rescue.md) reads the disk forwards
until it finds an error; it then goes to the end of the disk and reads
backwards. The [aimage](aimage.md) advanced disk imager
implements a similar algorithm.