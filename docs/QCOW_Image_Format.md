[QEMU](QEMU "wikilink") uses the **QEMU Copy-On-Write (QCOW)** files to
store a disk image.

## MIME types

## File signature

QCOW files start with hexadecimal: 0x51 0x46 0x49 0xfb (ASCII: "QFI.")

## File types

Currently there are three versions of the QCOW1 format; namely QCOW
(version 1) and QCOW2 (version 2). Version 3 is considered an extended
variant of QCOW2.

## Contents

The QCOW format is used to store storage media data, e.g. disk images.

The QCOW image file consists of:

- the file header
- the L1 table (cluster aligned)
- the reference count table (cluster aligned)
- reference count blocks
- snapshot headers (8-byte aligned on cluster boundary)
- clusters containing:
  - L2 tables
  - storage media data

The clusters are 512 bytes of size

## Encryption

The QCOW2 format supports optional AES encryption

## See Also

- [Disk Images](Disk_Images "wikilink")

## External Links

- [The QCOW Image
  Format](http://people.gnome.org/~markmc/qcow-image-format-version-1.html),
  by [Mark McLoughlin](Mark_McLoughlin "wikilink"), June 2006
- [The QCOW2 Image
  Format](http://people.gnome.org/~markmc/qcow-image-format.html), by
  [Mark McLoughlin](Mark_McLoughlin "wikilink"), September 2008
- [QEMU Copy-On-Write file
  format](https://github.com/libyal/libqcow/blob/master/documentation/QEMU%20Copy-On-Write%20file%20format.asciidoc),
  by the [libqcow project](libqcow "wikilink"), December 2010

## Tools

- [libqcow](libqcow "wikilink")
- [QCOW Data
  Recovery](http://www.bitrecover.com/virtual-drive-recovery-software/) -
  Recover data from corrupt or crashed QCOW, QCOW2 virtual image files.

[Category:File Formats](Category:File_Formats "wikilink")