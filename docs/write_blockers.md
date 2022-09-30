---
tags:
  -  Disk Imaging
---
**Write blockers** are devices that allow acquisition of information on
a [drive](hard_drive.md) without creating the possibility of
accidentally damaging the drive contents. They do this by allowing read
commands to pass but by blocking write commands, hence their name.

There are two ways to build a write-blocker: the blocker can allow all
commands to pass from the computer to the drive except for those that
are on a particular list. Alternatively, the blocker can specifically
block the write commands and let everything else through.

Write blockers may also include drive protection which will limit the
speed of a drive attached to the blocker. Drives that run at higher
speed work harder (the head moves back and forth more often due to read
errors). This added protection could allow drives that can not be read
at high speed (UDMA modes) to be read at the slower modes (PIO).

There are two types of write blockers, Native and Tailgate. A Native
device uses the same interface on for both in and out, for example a IDE
to IDE write block. A Tailgate device uses one interface for one side
and a different one for the other, for example a Firewire to SATA write
block.

Steve Bress and Mark Menz invented hard drive write blocking (US Patent
6,813,682).

There are both hardware and software write blockers. Some software write
blockers are designed for a specific operating system. One designed for
Windows will not work on Linux. Most hardware write blockers are
software independent.

# Hardware Write Blockers

**Hardware write blockers** can be either [IDE](ide.md)-to-IDE
or [Firewire](firewire.md)/[USB](USB "wikilink")-to-IDE. Simson
prefers the IDE-to-IDE because they deal better with errors on the drive
and make it easier to access special information that is only accessible
over the IDE interface. You may feel differently.

NIST test results are here:
<http://www.cftt.nist.gov/hardware_write_block.htm>

## Commercial

[ICS Drive Lock](ics_drive_lock.md)
<http://www.ics-iq.com/Super-DriveLock-Write-Blocker-Write-Protector-p/f.gr-0028-0000.htm>

<!-- -->

MyKey Technology, Inc. NoWrite FPU and FlashBlock II
1.8"/2.5"/3.5"/ IDE to IDE, FireWire/USB to IDE & SATA, all media
types - NIST Ver. 2 accepted

<http://www.mykeytech.com/>

<!-- -->

[Tableau](tableau.md) write blockers for IDE, SATA, SCSI, USB NIST Ver. 1 accepted
<https://www.guidancesoftware.com/products/Pages/tableau/overview.aspx>

<!-- -->

WiebeTech write-blockers for almost any disk drive: 2.5"/3.5" IDE, SCSI, SATA, ...
<http://www.cru-inc.com/products/wiebetech/> NIST Ver. 1 accepted

<!-- -->

EPOS WriteProtector
<http://www.epos.ua/view.php/en/products_epos_write_protector>

# Software Write Blockers

**Software write blockers** can be either tailored to an individual
operating system or can be an independent boot disk. Their main upsides
are with ease of use, since they are on a CD and do not require you to
open up the case, and speed since they do not become a bottle neck.

## Open Source

[Linux software write blocker](linux_software_write_blocker.md)
<https://github.com/msuhanov/Linux-write-blocker>

## Commercial

[SAFE Block XP](safe_block_xp.md)
SAFE Block XP is a software-based write blocker designed for the Windows
XP Operating System. It comes in both 32 and 64 bit options. NIST Ver.
1.2 accepted

<http://www.forensicsoft.com/>

<!-- -->

[MacForensicsLab Write Controller](macforensicslab_write_controller.md)
MacForensicsLab Write Controller is a software-based write blocker
designed for the Mac OS X operating system. It runs on both 32 and 64
bit versions of Mac OS X 10.4 or later.

<http://www.macforensicslab.com/ProductsAndServices/index.php?main_page=product_info&cPath=1&products_id=339>

