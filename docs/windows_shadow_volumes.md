---
tags:
  - Disk Analysis
  - Windows
---
## Volume Shadow Copy Service

Windows has included the Volume Shadow Copy Service in it's releases
since Windows XP. The Shadow Copy Service creates differential backups
periodically to create restore points for the user. Windows 7
Professional and Ultimate editions include tools to work with and manage
the Volume Shadow Copy Service, including the ability to mount shadow
volumes on disk images. In Windows 8 the shadow volumes seem to have
been superseded by File History. For now it looks like it uses similar
structures as its predecessors.

Windows Shadow Copy is a service that either manually or automatically
creates backup copies of disk volumes. These backups are automatically
created when Windows performs either a scheduled backup or a system
restore point. This happens before Windows Updates are installed, or
when Windows determines that it is time to create a new system restore
point, which is determined by both system idle time and the time since a
previous system restore point was created. In Windows Vista, this is one
day. On Windows 7 and newer, this is seven days. Windows XP creates them
every 24 hours regardless of system activity.

Shadow copies are initially created as block-level clones of entire
drives. From there, only the changes to the drive are tracked. This
means that in a forensic investigation, not all relevant information may
be in the same Shadow Copy.

## History

Shadow copies were first available in the Windows XP and Server 2003
operating systems, and are still present in each subsequent Windows and
Server operating systems, including the present day Windows 10.

Although all present Windows and Server operating systems contain shadow
volume capability, the process in which each operating system creates
and accesses them varies, and is explained below.

### Windows XP and Server 2003

Windows first added Volume Snapshot Service to windows XP, which is used
by NTBackup. The creation of persistent snapshots has been added within
Windows Server 2003. This addition gives the ability of having up to 512
snapshots to exist for a single volume. Windows 2003 is used to create
incremental snapshots of the data that have changed.

In Windows XP, the process of system restore, or the creation of the
shadow copies is different from the more recent versions of windows.
Windows XP uses a simple mechanism- the moment an application attempts
to overwrite any system file, Windows XP makes a copy of the file and
saves that file to a separate folder. That way, in windows XP, system
restore will not affect a user's documents, but only files such as dll,
exe, and registry files, along with a few others.

### Windows Vista, Windows 7, and Server 2008

Many of the components of Windows have been updated to make use of
Shadow copies in these versions. The backup and restore utility within
these windows versions, use both shadow copies of files in both
file-based and sector-by -sector backups. VSS is used by the System
Protection components, which creates and maintains periodic copies of
system and user data on the same local volume, allows it to be locally
accessed by the System Restore Utility.

### Windows 8 and Server 2012

These versions of Microsoft’s operating systems support persistent
shadow copies. However, Windows 8 is lacking a GUI portion that is
necessary to easily browse the shadow copies. So, within Windows 8 the
Previous versions tab of the properties dialog of files was removed for
local volumes, so the ability to browse, search or recover older
versions of files is not present.

### Windows 10

This version of Microsoft Windows has restored the Previous versions tab
within the properties dialog of files. However, it now depends on the
the File History feature instead of Volume shadow Copy.

## Shadow Volume Copies in Digital Forensics

### Why Shadow Copies are Important to Forensics

Windows Shadow Volumes are important to digital forensics because they
can provide additional data that otherwise would not be available. They
can allow a forensic investigator to recover deleted files, and to learn
what was taking place on a system before he/she began the investigation.
They are an excellent tool for discovering data that was previously
deleted by a system user.

### Limitations of Shadow Copies in forensic investigations

Although Shadow Copies can provide forensic investigators with files
that have been deleted between the time the Shadow Copy was made and the
time the investigation began, they only provide one previous version of
files. If previous changes to files were made before the Shadow Copy was
created, those changes will not be known. Because Shadow Copies clone on
a block-level rather than a file-level, changes to individual files may
not be enough to cause Windows to make the changes in a corresponding
Shadow Copy.

Additionally, depending on the user’s individual settings, the Shadow
Copy service might be turned off, resulting in no Shadow Copies being
stored. Other times, the disk space settings might be set too low for
multiple Shadow Copies to be saved, or even for one Shadow Copy to be
saved if it is larger than what the settings allow. Windows
automatically overwrites Shadow Copies when the disk space limit is
reached. For these reasons, Shadow Copies should be an aid in a forensic
investigation, but they are not guaranteed as a means to discover useful
information.

## Also see

* [Windows](windows.md)
* [File History](windows_file_history.md)
* How to: [Mount shadow volumes on disk images](mount_shadow_volumes_on_disk_images.md)

## External Links

### How to analyze Shadow Volumes

* [VISTA and Windows 7 Shadow Volume Forensics](https://www.sans.org/digital-forensics-incident-response/),
  by [Rob Lee](rob_lee.md), October 2008
* [Accessing Volume Shadow Copies](https://windowsir.blogspot.com/2011/01/accessing-volume-shadow-copies.html),
  by [Harlan Carvey](harlan_carvey.md), January 2011
* [More VSCs](https://windowsir.blogspot.com/2011/01/more-vscs.html),
  by [Harlan Carvey](harlan_carvey.md), January 2011
* [A Little Help with Volume Shadow Copies](http://journeyintoir.blogspot.com/2011/04/little-help-with-volume-shadow-copies.html),
  by Corey Harrell, April 2011
* [HowTo: Mount and Access VSCs](https://windowsir.blogspot.com/2011/09/howto-mount-and-access-vscs.html),
  by [Harlan Carvey](harlan_carvey.md), September 2011
* [Shadow Timelines And Other VolumeShadowCopy Digital Forensics Techniques with the Sleuthkit on Windows](https://www.sans.org/digital-forensics-incident-response/),
  by [Rob Lee](rob_lee.md), September 2011
* [Ripping Volume Shadow Copies – Introduction](http://journeyintoir.blogspot.com/2012/01/ripping-volume-shadow-copies.html),
  by Corey Harrell, January 2012
* [Ripping VSCs – Practitioner Method](http://journeyintoir.blogspot.com/2012/02/ripping-vscs-practitioner-method.html),
  by Corey Harrell, February 2012
* [Ripping VSCs – Practitioner Examples](http://journeyintoir.blogspot.com/2012/02/ripping-vscs-practitioner-examples.html),
  by Corey Harrell, February 2012
* [Ripping VSCs – Developer Method](http://journeyintoir.blogspot.com/2012/02/ripping-vscs-developer-method.html),
  by Corey Harrell, February 2012
* [Ripping VSCs – Developer Examples](http://journeyintoir.blogspot.com/2012/02/ripping-vscs-developer-examples.html),
  by Corey Harrell, February 2012
* [Examining VSCs with GUI Tools](http://journeyintoir.blogspot.com/2012/02/examining-vscs-with-gui-tools.html),
  by Corey Harrell, February 2012
* [VSC Toolset: A GUI Tool for Shadow Copies](https://dfstream.blogspot.com/2012/03/vsc-toolset-gui-tool-for-shadow-copies.html),
  by Jason Hale, March 2012
* [Examining Volume Shadow Copies – The Easy Way!](http://encase-forensic-blog.guidancesoftware.com/2012/06/examining-volume-shadow-copies-easy-way.html),
  by Simon Key, June 2012
* Getting Ready for a Shadow Volume Exam,
  by Jimmy Weg, June 2012
* Mounting Shadow Volumes,
  by Jimmy Weg, July 2012
* Examining the Shadow Volumes with X-Ways Forensics,
  by Jimmy Weg, July 2012
* Weg, I’m afraid that I don’t have VMware. How do I Examime Shadow Volumes?,
  by Jimmy Weg, August 2012
* Examining shadow copies with Reconnoitre (and without vssadmin), it's as easy as 1, 2, 3,
  by [Paul Sanderson](paul_sanderson.md), January 2013

<!-- -->

### Shadow Volumes in depth

* [Reliably recovering evidential data from Volume Shadow Copies in Windows Vista and Windows 7](http://www.qccis.com/docs/publications/WP-VSS.pdf),
  by James Crabtree and Gary Evans, 2010
* [Into The Shadows](https://forensic4cast.com/2010/04/into-the-shadows/) and
  [Presentation](https://forensic4cast.com/2010/04/presentation-into-the-shadows/),
  by [Lee Whitfield](lee_whitfield.md), April 2010
* [Volume Shadow Snapshot format](https://github.com/libyal/libvshadow/blob/main/documentation/Volume%20Shadow%20Snapshot%20(VSS)%20format.asciidoc),
  by the [libvshadow project](libvshadow.md), March 2011
* [Windowless Shadow Snapshots - Analyzing Volume Shadow Snapshots (VSS) without using Windows](https://github.com/libyal/documentation/blob/main/Paper%20-%20Windowless%20Shadow%20Snapshots.pdf)
  and [OSDFC 2012 Slides](https://github.com/libyal/documentation/blob/main/Slides%20-%20Windowless%20Shadow%20Snapshots.pdf),
  by [Joachim Metz](joachim_metz.md), October 2012

### Other

* [Volume Shadow Copies - The Lost Post](https://www.scmagazine.com/security-weekly),
  by Mark Baggett, October 2012

## Tools

* [EnCase](encase.md) with VSS Examiner Enscript (available from
  the downloads section of the GSI Support Portal)
* [libvshadow](libvshadow.md)
* [ProDiscover](prodiscover.md)
* [ShadowExplorer](https://www.shadowexplorer.com/)
* [VSC Toolset](https://dfstream.blogspot.com/p/vsc-toolset.html)
* [X-Ways Forensics](x-ways_ag.md)
* Vssadmin - Command Line utility included in Windows XP and later,
  which can list, create, or delete volume shadow copies. This utility
  will also list the installed shadow copy writers and providers.
* [Forensic Tool Kit](forensic_toolkit.md)

## Sources

* [What you should know about Volume Shadow Copy/System Restore in Windows 7 & Vista (FAQ)](https://blog.szynalski.com/2009/11/volume-shadow-copy-system-restore/)
* [Restore points](https://learn.microsoft.com/en-us/windows/win32/sr/restore-points)
