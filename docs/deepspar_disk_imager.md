---
tags:
  -  Disk Imaging
  -  Tools
  -  Hardware
---
The [DeepSpar](deepspar.md) Disk Imager is a hardware, drive to
drive, data recovery imaging device. It makes use of a fairly standard
PC system but connects directly to the source drive (the drive being
imaged.) Through this hardware connection, it is able to command the
source drive on a low ATA register level. It thus bypasses normal BIOS
calls to the hard drive. Standard BIOS / hard drive operations will not
allow the retrieval of damaged or corrupted sectors as it would
invariably cause a system (OS) failure. For data recovery purposes
however, it is important to be able to access any available data.

![](DeepSpardiskimager.jpg "DeepSpardiskimager.jpg")

Additionally, the DeepSpar Disk Imager controls the power input of the
source drive so that it can, if required, re-power the source without
rebooting the system. (This is significant with highly unstable drives
that will continually “hang.”)

To control and pre-configure the source drive, the DeepSpar Disk Imager
makes use of specific ATA commands [1](http://www.t13.org) as well as
some vendor specific commands. This includes the ability to read sectors
while ignoring [ECC errors](error_correction_code.md) as well as
the ability to send software and hardware reset commands to the drive
which creates the ability to control “read timeout.” (Read timeout is a
user defined amount of time in milliseconds that the hard drive will be
given to read any particular sector. If the read timeout is reached
before the sector is correctly read, it will be skipped. The imager then
marks in its “map” that the sector was skipped so that it can be
reprocessed on later passes.)

Through the tool’s software interface, the end user is able to configure
all parameters and commands that they wish the imager to use over
multiple imaging passes. As previously mentioned, the DeepSpar Disk
Imager stores a “map” of all the sectors from the source drive. This map
allows the imager to always remember which sectors have been imaged,
which were skipped, and which had errors etc. This in turn allows the
imager to run multiple passes without reprocessing sectors that had been
previous read correctly. It also allows the imager run imaging passes to
target specific sector errors.

Unlike forensics tools, the DeepSpar Disk Imager does not create an
[image file](raw_image_format.md). Instead, it uses commands and
techniques to image all sectors on the source drive directly to the
destination drive. The image drive can then be used by any data
retrieval or forensics software for file recovery or forensics
investigation.

## External Links

- [Official website](http://www.driveimager.com/)
- [Product data
  sheet](http://www.deepspar.com/pdf/DeepSparDiskImager.pdf)
- [Review of the DeepSpar Disk
  Imager](http://www.deepspar.com/mjm-ds-disk-imager.html) by Mike
  Montgomery of MJM Data Recovery in the UK.
- *[Disk Imaging: A Vital Step in Data
  Recovery](http://www.deepspar.com/pdf/DeepSparDiskImagingWhitepaper3.pdf)*,
  a whitepaper on the product
- [Interview on the
  imager](http://cyberspeak.libsyn.com/index.php?post_id=193897) on the
  [Cyberspeak podcast](cyberspeak_podcast.md)
