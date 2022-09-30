---
tags:
  - No Category
---
The **System Acquisition Forensic Environment (SAFE) Block XP** software
is a software-based write blocker designed for the Windows XP 32 and 64
bit operating system. Because it is software based it allows for disk
imaging speeds that are significantly faster than imaging in Windows
using commercially available hardware-based write blockers. It also
allows you to write block as many devices as are connected to the
computer. It is application independent and works with all forensic
acquisition and analysis software that works on Windows. In order to
ensure that you are working forensically sound environment **SAFE Block
XP** provides automatic write blocking of all directly attached media,
including IDE (PATA & SATA), SCSI, FC, SAS, USB, and IEEE1394.

**SAFE Block XP** identifies and provides access to Host Protected Areas
(HPAs) and Device Configuration Overlay (DCOs) on IDE (PATA and SATA)
disks, connected directly via PATA or SATA controllers. HPAs are
temporarily removed and make no permanent modification to the disk
configuration, using volatile HPA commands. Since a DCO cannot be
removed temporarily, SAFE Block XP preserves all DCO information,
allowing safe removal of the DCO or HPA/DCO combination, then upon
completion of the acquisition, replacement of the DCO or HPA/DCO
combination back to its original state.

## Notes

- **SAFE Block XP** has passed all of NIST's Mandatory and Optional Test
  Assertions, including not allowing a protected drive to be changed,
  not preventing obtaining any information from or about any drive and
  not preventing any operations to a drive that is not protected.