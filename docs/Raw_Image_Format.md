The RAW Image Format is used to store a disk or volume image.

## File types

Some variants of the RAW Image Format split the data among multiple
segment files, which is also known as split RAW.

There are various naming schemes for RAW Image Format files, some of the
more common used for disk or volume images are:

- PREFIX.dd
- PREFIX.dmg
- PREFIX.img
- PREFIX.raw
- PREFIX.0 - PREFIX.#; variations: starting with either 0 or 1,
  consisting of multiple digits e.g. PREFIX.000
- PREFIX0 - PREFIX#; variations: starting with either 0 or 1, consisting
  of multiple digits e.g. PREFIX000
- PREFIXaa - PREFIXzz; variations: consisting of more letters e.g.
  PREFIX.aaa
- PREFIX.1of5 - PREFIX.5of5; variations: consisting of multiple segment
  files
- PREFIX001.asb - PREFIX###.asb
- PREFIX-f001.vmdk - PREFIX-f###.vmdk; variations: starting with 001

Note that there are also RAW Image Formats specific to the storage
media, e.g. RAW optical disc image.

These often are accompanied by a table of contents file often in the
[CUE Sheet format](CUE_Sheet_format "wikilink"), e.g.

- BIN/CUE
- ISO/CUE

## Contents

The RAW Image Format is basically a bit-for-bit copy of the RAW data of
either the disk or the volume, without any additions or deletions.

There is no [metadata](metadata "wikilink") stored in RAW Image Format
files. However sometimes the metadata is stored in additional files.

The RAW Image Format was originally used by [dd](dd "wikilink"), but is
supported by most of the computer forensics applications.

## See Also

- [Disk Images](Disk_Images "wikilink")

## Tools

- [dd](Dd "wikilink")
- [dc3dd](dc3dd "wikilink")
- [dcfldd](dcfldd "wikilink")
- [dd_rescue](dd_rescue "wikilink")
- [ddrescue](ddrescue "wikilink")

[Category:Forensics File
Formats](Category:Forensics_File_Formats "wikilink")