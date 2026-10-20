---
tags:
  - Data Recovery
---
Data recovery is the process of restoring data that has become inaccessible because it was deleted,
the file system or partition table was damaged, or the storage media itself is failing. It spans the
whole spectrum from undeleting a file on a healthy [hard drive](hard_drive.md) to extracting
readable data from physically damaged platters, including lost partitions, broken [RAID](raid.md)
arrays, virtual disk files, and (attempts at) overwritten sectors.

The term "data recovery" is frequently used to mean forensic recovery, but it really should be
reserved for recovering data from damaged media, while the recovery of deleted or logically
corrupted data from healthy media is a forensic activity.

More fundamentally, data recovery is **a process of inference** rather than a direct reading of the
media: the investigator reconstructs what once existed from incomplete evidence - partially
overwritten directory entries, remnants of file headers, sectors that still hold older data. Every
recovered artifact is therefore a hypothesis, whose reliability grows the more independent
observed evidence corroborates it.

## Deleted file recovery

Recovering files whose pointers were removed at deletion - the directory entry, the
[FAT](fat.md) chain, or the [NTFS](ntfs.md) MFT record - but whose data sectors remain, a process
known as *undelete*. It is most reliable on [FAT](fat.md), and far less so on [NTFS](ntfs.md),
where fragmented files are generally beyond undelete.

See also [Recovering deleted data](recovering_deleted_data.md).

## Partition recovery

Recovering a disk whose partition table, [Master Boot Record](master_boot_record.md), or boot code
has been damaged by faulty software, certain viruses, or human error. Recovery may be as simple as
restoring the partition table from an intact copy, or may require guessing the table from remnants
of the file systems.

See also [Partition Recovery tools](tools_data_recovery.md#partition-recovery).

## Recovery from damaged media

Recovering data from drives that are malfunctioning - bad sectors, damaged firmware, failed read
heads, or physically damaged platters - using software approaches that bypass the drive's own
limitations, or hardware approaches (controller tools, spare parts, cleanroom work).

See also [Recovering bad data](recovering_bad_data.md) and
[Linux File Recovery](linux_file_recovery.md).

## Recovery of overwritten data

Whether data can be recovered after it has been overwritten - multiple passes of random data, or a
single pass of zeros - has been debated for decades, and published results remain thin.

See also [Recovering overwritten data](recovering_overwritten_data.md),
[Remnant data](remnant_data.md) and [Residual data](residual_data.md).

## File carving

Recovering files based on their content rather than on file system metadata; the
[file carving](file_carving.md) article covers the definition, the taxonomy of carving techniques,
and recovery of fragmented files (such as [SmartCarving](file_carving_smartcarving.md) and
[GuidedCarving](file_carving_guidedcarving.md)) as well as [zero storage
carving](zero_storage_carving.md).

See also the [File Carving
Bibliography](file_carving_bibliography.md) and [File Carving
Tools](tools_data_recovery.md#carving).

## RAID and virtual disk recovery

Recovering data from [RAID](raid.md) arrays that have failed (reconstructing the layout from the
member disks) and from virtual disk file formats - [VDI](virtual_disk_image_(vdi).md),
[VHD](virtual_hard_disk_(vhd).md), [VMDK](vmware_virtual_disk_format_(vmdk).md),
[QCOW](qcow_image_format.md) - of virtual machines, which themselves may be damaged or contain
deleted files.

## Recovery of structured data

Recovering records from structured stores - databases, mail stores, office documents - which are
often damaged or only partially recoverable even when the whole file is intact.

## Media-specific recovery

Recovery tailored to particular media types: damaged or dirty [SIM cards](sim_card_forensics.md),
memory cards (photo recovery from CF/SD/Smart Media/XD cards), and optical media (CD/DVD/Blu-ray).

See also [Damaged SIM Card Data Recovery](damaged_sim_card_data_recovery.md).

## See also

* [Tools: Data Recovery](tools_data_recovery.md)
* [File carving](file_carving.md)
* [Recovering deleted data](recovering_deleted_data.md)
* [Recovering bad data](recovering_bad_data.md)
* [Recovering overwritten data](recovering_overwritten_data.md)
* [Remnant data](remnant_data.md)
* [Forensic recovery of evidence device (FRED)](forensic_recovery_of_evidence_device.md)
* [Hard drive](hard_drive.md) (data recovery section)
* [Concepts](concepts.md#data-recovery)
* [Tools: data recovery](tools_data_recovery.md)

## External Links

* [Wikipedia: Data recovery](https://en.wikipedia.org/wiki/Data_recovery)

### Stories of data recovery

* [May 6, 2008 - Kroll Ontrack recovers over 90% of the data from a 400 MB hard drive that was on
  Shuttle Columbia when it burned up on reentry into Earth's
  atmosphere.](https://www.ontrack.com/en-us/ediscovery) This link to a page at Kroll contains links
  to journals covering the story, such as [Scientific American's article about the data that was
  recovered](https://www.scientificamerican.com/article/hard-drive-recovered-from-columbia/).
