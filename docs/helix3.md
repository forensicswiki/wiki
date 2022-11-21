---
tags:
  -  Live CD
  -  Tools
  -  Linux
  -  Disk Imaging
  -  System Analysis
---
**Helix3** is a [Live CD](live_cd.md) built on top of
[Ubuntu](ubuntu.md). It focuses on [incident
response](incident_response.md) and [computer
forensics](computer_forensics.md).

According to Helix3 Support Forum, e-fense is no longer planning on
updating the free version of Helix.

## Tools Included

Helix focuses on Incident Response and forensics tools. It is meant to
be used by individuals who have a sound understanding of Incident
Response and forensic techniques.

### Bootable Side

- [The Sleuth Kit](the_sleuth_kit.md)
- [dc3dd](dc3dd.md)
- [dcfldd](dcfldd.md)
- [LinEn](linen.md)
- [aimage](aimage.md)

*and others.*

### Windows Side

- [FTK Imager](ftk_imager.md)
- [mdd](mdd.md)
- [win32dd](windd.md)
- [winen](winen.md)
- [WFT](wft.md)
- [IRCR](ircr.md)

*and others.*

Windows side can be used to scan for pictures on a live system.

## Forensic Issues

- Helix3 will automount [Ext3](ext3.md) /
  [Ext4](ext4.md) file systems during the boot process and
  recover them if required (bug in *initrd* scripts);
- Helix3 can automount some storage devices like firewire devices and
  MMC in read/write mode;
- Helix3 relies on file system drivers to provide write protection,
  mounting some file system types (e.g. [XFS](xfs.md) will
  result in several data writes to the original media.

## See Also

- [Helix3 Pro](helix3_pro.md)

## External Links

- [Helix3 CE Forum](http://forum.charlestendell.com)