---
tags:
  - No Category
---
The *system time* of a computer is typically the time and date of the
computer's real time clock. Typically this information is not stored in
a disk image but must be recovered separately when a computer is
acquired.

It is a good idea to determine the system time so that you can state
that the times in the file system are aligned with the times of a
correct wall clock.

## Determine the System Time

### PC

The system time of most PCs can be determined by booting into the BIOS
and reading the system clock.

### Macintosh

The system time of most Intel-based Macintoshes can be determined by
booting a USB device equipped with [rEFIt](refit.md). This gives
access to an EFI shell. You can now issue the **date** and **time**
commands. Note that the time will be in GMT and the date will be in
**mm/dd/yy** format.