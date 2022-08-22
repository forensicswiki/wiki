The [Windows](Windows "wikilink") Logical Disk Manager, is commonly
abbreviated to LDM.

## On-disk structures

According to
[TECHNET](http://technet.microsoft.com/en-us/library/cc737048.aspx):

The location of the database is determined by the partition style of the
disk.

- On MBR disks, the database is contained in the last 1 megabyte (MB) of
  the disk.
- On GPT disks, the database is contained in a 1-MB reserved (hidden)
  partition known as the Logical Disk Manager (LDM) Metadata partition.

## Types of dynamic volumes

- Simple volume
- Spanned volume
- Striped volume
- Mirrored volume (Server editions of Windows 2000, Windows 2003)
- RAID-5 volume (Server editions of Windows 2003)

## Also see

- [File Systems](:Category:File_Systems "wikilink")

## External Links

- \[<http://msdn.microsoft.com/en-us/library/windows/desktop/aa363785(v=vs.85>).aspx
  Basic and Dynamic Disks\], by Microsoft
- [What Are Dynamic Disks and
  Volumes?](http://technet.microsoft.com/en-us/library/cc737048.aspx),
  by Microsoft, March 2003
- [Dynamic disks and
  volumes](http://technet.microsoft.com/en-us/library/cc757696.aspx), by
  Microsoft, January 2005
- [Logical Disk Manager documentation](http://www.ntfs.com/ldm.htm)

[Category:Volume Systems](Category:Volume_Systems "wikilink")