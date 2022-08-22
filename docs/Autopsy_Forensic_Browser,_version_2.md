The **Autopsy Forensic Browser** (**Autopsy**) is a graphical interface
to the command line digital investigation analysis tools in [The Sleuth
Kit](The_Sleuth_Kit "wikilink"). Together, they can analyze
[Windows](Windows "wikilink") and [UNIX](UNIX "wikilink") disks and
[file systems](file_systems "wikilink") ([NTFS](NTFS "wikilink"),
[FAT](FAT "wikilink"), [UFS1](UFS1 "wikilink")/[UFS2](UFS2 "wikilink"),
[Ext2](Ext2 "wikilink")/[Ext3](Ext3 "wikilink")).

The [Sleuthkit](Sleuthkit "wikilink") and Autopsy are both Open Source
and run on UNIX platforms. As Autopsy is [HTML](HTML "wikilink")-based,
you can connect to the Autopsy server from any platform using a web
browser. Autopsy provides a "File Manager"-like interface and shows
details about deleted data and file system structures.

## Current state

As of 2014, Autopsy 2.24 is the last version of Autopsy that supports
non-Windows platforms. Since Autopsy 2.24 was released in 2010, it
cannot support all features introduced in latest
[Sleuthkit](Sleuthkit "wikilink") versions. Various modifications
introduced in Sleuthkit since 2010 break Autopsy 2.24.

There are several known conflicts between Autopsy 2.24 and Sleuthkit
4.1.3:

- Autopsy cannot normally jump through directories on HFS.
- Autopsy cannot handle Sun VTOC.
- Autopsy cannot view timelines in most cases.

Also, Ext4 file creation timestamps cannot be viewed in the Autopsy
"File Manager"-like interface. Unofficial
[patch](https://github.com/msuhanov/autopsy-2.24-patch/blob/master/autopsy-2.24-1.patch)
exists to fix or "hack around" these issues.

## See also

- [Autopsy Forensic Browser, version
  3](Autopsy_Forensic_Browser "wikilink") (Windows only)