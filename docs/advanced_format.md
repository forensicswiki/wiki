---
tags:
  - Hard Drives
  - Hardware
---
# The Technology

Hard drive manufacturers have moved to a new standard: 4KB (4,096 bytes)
sectors, replacing 512B sectors. This is a good thing; it means that the
signal-to-noise ratio improves, and less space is needed for error
correction. Long-term improvements in speed, density, and overall
capacity. Western Digital has started releasing drives with 4KB sectors
under the name "Advanced Format" (not to be confused with the [Advanced
Forensics Format](aff.md).

# The Standard

ATA 7 (T13/D1532, INCITS 397-2005) introduced Long Physical Sector (LPS)
and Long Logical Sector (LLS) feature sets. Drives with large sector
sizes shall report the actual physical/logical size in words 106 and
117-118 of the ATA IDENTIFY data.

Some Western Digital drives with "Advanced Format" reportedly do not
provide the information about physical sector size (see [External
Links](#external-links)).

# The Problem: Death of LBA 63

Operating systems written before the transition, particularly XP, have
trouble with the new drives. XP makes an assumption about where the
format should start (LBA 63), but this doesn't work well with the
translation software that maps from logical 512B blocks to physical 4K
blocks.

The nutshell is that XP should not be used to format these drives, and
some assumptions made by tools and users need to be corrected. For
analysis purposes, note that you can't assume that an NTFS partition
starts at LBA 63. If you are used to using, for example, the Sleuthkit
command "fls -o 63 <image>", this may need to change. Hopefully more
information about these drives will come forth as time progresses.

LBA 63 was dying anyway. Windows Vista and Windows 7 both align to LBA
2048 by default. This change happened before the Advanced Format 512e
drives hit the marketplace.

# The Solution

To format one of these drives properly for Windows XP, use the following
utility (this applies only to drives from Western Digital):

[Western Digital Advanced Drive Format Utility](http://www.wdc.com/en/products/advancedformat/)

# External Links

* [A Good Overview at AnandTech](http://www.anandtech.com/storage/showdoc.aspx?i=3691)
* [PDF White Paper](http://www.wdc.com/wdproducts/library/WhitePapers/ENG/2579-771430.pdf)
* [A Tom's Hardware Review of the WD Caviar Green Drives](http://www.tomshardware.com/reviews/green-terabyte-1tb,2078-2.html)
* [ATA 4 KiB sector issues (good summary from Linux ATA wiki)](https://ata.wiki.kernel.org/index.php/ATA_4_KiB_sector_issues)
* [4K-sector drives and Linux (LWN.net)](http://lwn.net/Articles/377895/)
* [WD6400AARS-00Y5B1 does not provide sector size info (smartmontools ticket)](http://sourceforge.net/apps/trac/smartmontools/ticket/62)
