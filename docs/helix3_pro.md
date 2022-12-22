---
tags:
  - No Category
---
**Helix3 Pro** is a [Live CD](live_cd.md) built on top of
[Ubuntu](ubuntu.md). It focuses on [incident
response](incident_response.md) and [computer
forensics](computer_forensics.md).

## Tools Included

- Live side for [Mac OS X](mac_os_x.md),
  [Windows](windows.md) and [Linux](linux.md)
- A bootable forensically sound environment based on
  [Ubuntu](ubuntu.md)

Open source forensic tools include:

- [dc3dd](dc3dd.md)
- [aimage](aimage.md)
- [The Sleuth Kit](the_sleuth_kit.md) (3.0.1, with "light"
  version of [Autopsy](autopsy.md), with
  [libewf](libewf.md)
- [foremost](foremost.md)
- [Volatility](volatility.md)
- Several tools for mobile phone forensics

Other tools include:

- [LinEn](linen.md)

## Forensic Issues

- Helix3 Pro can automount some storage devices like firewire devices
  and MMC in read/write mode;
- Helix3 Pro relies on file system drivers to provide write protection,
  mounting some file system types (e.g. [XFS](xfs.md) will
  result in several data writes to the original media.

## See Also

Free version: [Helix3](helix3.md)
