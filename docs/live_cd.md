---
tags:
  -  Live CD
  -  Opensource Software 
  -  Tools
  -  Linux
---
A **live CD** is a CD containing a bootable computer [operating
system](operating_system.md). Live CDs are widely used in
[computer forensics](computer_forensics.md) and [incident
response](incident_response.md).

## Advantages

- [Physical memory](physical_memory.md) of a computer can be
  imaged by performing cold boot attack without running tools on an
  untrusted [OS](os.md);
- Acquisition over a network connection without running tools on an
  untrusted [OS](os.md);
- No need to reconstruct [RAID](raid.md) arrays;
- etc.

## Disadvantages

- Out-of-date software;
- No simple way to reconfigure Live CD: you cannot easily rebuild *foo*
  to support *bar* (e.g. rebuild [Sleuthkit](sleuthkit.md) to
  support [AFF](aff.md).

## See Also

- [Forensics Live CDs](live_cd.md)
- [Forensic Live CD issues](forensic_live_cd_issues.md)