---
tags:
  -  Data Recovery
  -  Articles that need to be expanded 
---
When the user requests to delete a file, most modern [operating
systems](operating_system.md) do not erase the actual data.
Instead, they merely erase a pointer to the file so that the file does
not appear in directory listings. These files can be recovered by simply
*undeleting* the file — that is, restoring the directory entry.

For some file systems, such as [FAT](fat.md), the deleted
directory entry itself is easily recovered. In these cases the files can
be recovered using an *undelete* program. In other cases, however, the
directory entry is not available — perhaps because it was overwritten.
In these cases the only way that the file can be recovered is through
the use of [File Carving](carving.md).

Using an undelete function on FAT32 can be very dangerous if any files
are fragmented. Deleting the file also removes the FAT entry and so the
locations of split fragments can no longer be assumed. Forensically,
making any changes to a disk is 'not allowed'.

# See Also

[Carving](carving.md)