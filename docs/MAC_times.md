The term **MAC times** refers to the timestamps of the latest
*modification* (mtime) or last written time, *access* (atime) or
*change* (ctime) of a certain file.

[Windows](Windows "wikilink") systems use *birth* (btime) or creation
(crtime) time (e.g. 'This file was created on 05/05/02 12:15pm'). Hence
MACB; Modification, Access, Change and Birth.

[Unix](Unix "wikilink") systems maintain the historical interpretation
of *ctime* as the time when certain file metadata, not its contents,
were last changed, such as the file's permissions or owner (e.g. 'This
files metadata was changed on 05/05/02 12:15pm'). Though POSIX only
specifies *mtime*, *atime* and *ctime*, some Unix-like systems also
implement *btime* on compatible file systems (for instance ext4 on Linux
distributions, UFS2 on FreeBSD).

In both [NTFS](NTFS "wikilink") and
[ReFS](Resilient_File_System_(ReFS) "wikilink") each file has a time
stamp for 'Create', 'Modify', 'Access', and 'Entry Modified'. The latter
refers to the time when the MFT entry itself was modified. These four
values are commonly abbreviated as the 'MACE' values.

Other file systems like [HFS](HFS+ "wikilink") include different
timestamps like e.g. a backup time.

## Time resolution

When dealing with MAC times it's important to know and understand the
concept of time resolution.

On [FAT](FAT "wikilink") file system (in Windows NT):

- the creation time has a resolution of 10 milliseconds,
- the last written time has a resolution of 2 seconds,
- and the access time has a resolution of 1
  day.[1](http://msdn.microsoft.com/en-us/library/ms724284.aspx)

On NTFS file system:

- the creation time and the last written time have a resolution of 100
  nanoseconds.
- the access time also has a resolution of 100 nanoseconds, but updates
  to access time could be held in memory by up to an hour before being
  flushed to the
  disk.[2](https://msdn.microsoft.com/en-us/library/ms724290.aspx)

Tampering of filetimes can usually be detected by an absence of
sub-second resolution on any of the
timestamps.[3](http://www.meridiandiscovery.com/articles/date-forgery-analysis-timestamp-resolution/)

## Access Time Update

On various operating systems the update of the access time can be
disabled. This means when a file is accessed the atime in the
corresponding file system entry is not updated.

### [Windows](Windows "wikilink")

In Windows the access time behavior is controlled by the Registry key:

    HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Control\FileSystem\NtfsDisableLastAccessUpdate

Where a value of *1* indicates the access time update being disabled.

In Windows XP and earlier, the default value is 0 (enabled), and in
Windows Vista onwards, the default value is 1 (disabled).

Note that in Windows 10 “Redstone 4” (April 2018 Update) the behavior of
this setting was extended
[1](https://dfir.ru/2018/12/08/the-last-access-updates-are-almost-back/amp/)

When disabled, the access time is usually initialized to the time the
file was first written to the disk, following the rules seen below:

| Condition                                      | Modified         | Accessed                                               | Created          |
|------------------------------------------------|------------------|--------------------------------------------------------|------------------|
|                                                |                  |                                                        |                  |
| When renaming a file                           | Preserved        | Preserved                                              | Preserved        |
| When moving a file between folders             | Preserved        | Preserved                                              | Preserved        |
| When moving a file between disks or partitions | Preserved        | Time of move                                           | Preserved        |
| When copying a file                            | Preserved        | Time of copy                                           | Time of copy     |
| When writing a new file                        | Time of creation | Time of creation                                       | Time of creation |
| When modifying an existing file                | Time modified    | Preserved                                              | Preserved        |
| When accessing an existing file                | Preserved        | Updated within an hour if enabled, otherwise Preserved | Preserved        |

### [Linux](Linux "wikilink")

In Linux the *noatime* mount option indicates the access time update
should be disabled.

## See Also

- [Timestomp](Timestomp "wikilink")

## External Links

- [Wikipedia: MAC times](http://en.wikipedia.org/wiki/MAC_times)
- [What Are
  MACtimes?](http://www.drdobbs.com/what-are-mactimes/184404275), by Dan
  Farmer, Oct 2000

### NTFS

- [Disable the NTFS Last Access Time
  Stamp](http://www.winguides.com/registry/display.php/50/)
- [Microsoft KB 299648: Description of NTFS date and time stamps for
  files and folders](http://support.microsoft.com/kb/299648)