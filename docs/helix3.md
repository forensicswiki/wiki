---
tags:
  - Disk Imaging
  - Linux
  - Live CD
  - System Analysis
  - Tools
---
## Helix3

Helix3 is a [Live CD](live_cd.md) built on top of [Ubuntu](ubuntu.md). It
focuses on [incident response](incident_response.md) and [computer forensics](computer_forensics.md).

According to Helix3 Support Forum, e-fense is no longer planning on
updating the free version of Helix.

### Tools Included

Helix focuses on Incident Response and forensics tools. It is meant to
be used by individuals who have a sound understanding of Incident
Response and forensic techniques.

#### Bootable Side

* [aimage](aimage.md)
* [dc3dd](dc3dd.md)
* [dcfldd](dcfldd.md)
* [LinEn](linen.md)
* [The Sleuth Kit](the_sleuth_kit.md)

*and others.*

#### Windows Side

* [FTK Imager](ftk_imager.md)
* IRCR
* [mdd](mdd.md)
* WFT
* [win32dd](windd.md)
* winen

*and others.*

Windows side can be used to scan for pictures on a live system.

### Forensic Issues

* Helix3 will automount ext3 and ext4 file systems during the boot process and
  recover them if required (bug in *initrd* scripts);
* Helix3 can automount some storage devices like firewire devices and
  MMC in read/write mode;
* Helix3 relies on file system drivers to provide write protection,
  mounting some file system types (e.g. [XFS](xfs.md) will
  result in several data writes to the original media.

## Helix3 Pro

Helix3 Pro is a [Live CD](live_cd.md) built on top of
[Ubuntu](ubuntu.md). It focuses on [incident
response](incident_response.md) and [computer
forensics](computer_forensics.md).

### Tools Included

* Live side for [Mac OS X](mac_os_x.md),
  [Windows](windows.md) and [Linux](linux.md)
* A bootable forensically sound environment based on
  [Ubuntu](ubuntu.md)

Open source forensic tools include:

* [dc3dd](dc3dd.md)
* [aimage](aimage.md)
* [The Sleuth Kit](the_sleuth_kit.md) (3.0.1, with "light"
  version of Autopsy, with [libewf](libewf.md)
* [foremost](foremost.md)
* [Volatility](volatility_framework.md)
* Several tools for mobile phone forensics

Other tools include:

* [LinEn](linen.md)

### Forensic Issues

* Helix3 Pro can automount some storage devices like firewire devices
  and MMC in read/write mode;
* Helix3 Pro relies on file system drivers to provide write protection,
  mounting some file system types (e.g. [XFS](xfs.md) will
  result in several data writes to the original media.
