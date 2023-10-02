---
tags:
  - Digital Forensics XML
---
Forensic Disk Differencing is the process of taking two or more disk images
from the same computer and determining what changes in the first disk image
might have resulted in the changes that are observed in the second. One common
use of differencing is to determine what an attacker did during a break-in. To
be used for this purpose, it is necessary to have a forensic disk image of the
computer before the break-in and after the break-in.

## Differencing Tools

### idifference.py

idifference.py is part of the [Digital Forensics XML](digital_forensics_xml_schema.md)
Python Toolkit distributed with [fiwalk](fiwalk.md). This tool will compare two
different disk images and report changes in files between the first and the
second. It also produces a timeline of changes.

For example, using the **nps-2009-canon2** series of disk images:

    $ python idifference.py /nps-2009-canon2-gen2.raw nps-2009-canon2-gen3.raw
    >>> Reading nps-2009-canon2-gen2.raw
    >>> Reading nps-2009-canon2-gen3.raw

    Disk image:/corp/drives/nps/nps-2009-canon2/nps-2009-canon2-gen3.raw

    New Files:

    2008-12-23 14:26:12 1315993 DCIM/100CANON/IMG_0041.JPG

    Deleted Files:

    2008-12-23 14:12:38 855935  DCIM/100CANON/IMG_0001.JPG
    2008-12-23 14:22:38 1347778 DCIM/100CANON/IMG_0037.JPG

    Files with modified content (but size unchanged):

    Files with changed file properties:

    DCIM/CANONMSC/M0100.CTG SHA1 changed    69b30c352ee802f49b1ea25325af9fa05c3ffca1    ->  baa42c03a917b01b212fb7e538e5deb525995f31
    DCIM/CANONMSC/M0100.CTG crtime changed to   1230070924  ->  1230071142
    DCIM/CANONMSC/M0100.CTG mtime changed to    1230070924  ->  1230071142
    DCIM/CANONMSC/M0100.CTG resized 180 ->  188

    Timeline

    2008-12-23 14:25:42 DCIM/CANONMSC/M0100.CTG SHA1 changed    69b30c352ee802f49b1ea25325af9fa05c3ffca1    ->  baa42c03a917b01b212fb7e538e5deb525995f31
    2008-12-23 14:25:42 DCIM/CANONMSC/M0100.CTG crtime changed  1230070924  ->  1230071142
    2008-12-23 14:25:42 DCIM/CANONMSC/M0100.CTG mtime changed   1230070924  ->  1230071142
    2008-12-23 14:25:42 DCIM/CANONMSC/M0100.CTG resized 180 ->  188
    2008-12-23 14:26:12 DCIM/100CANON/IMG_0041.JPG  created
    $

Here are some more examples:

- ![<File:Idifference-demo1.txt>](Idifference-demo1.txt "File:Idifference-demo1.txt")
  --- idifference.py run on two disks from the 2009-M57 Patents scenario
  (Jo's November 23 vs. November 24th disk)

## See Also

* [A general strategy for differential forensic analysis](https://www.sciencedirect.com/science/article/pii/S174228761200028X)
