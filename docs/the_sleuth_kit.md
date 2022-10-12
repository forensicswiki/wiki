---
tags:
  -  Tools
  -  Windows
  -  Linux
  -  MacOS
  -  Disk Analysis
  -  Data Carving
  -  Data Recovery 
  -  Opensource Software
---
**The Sleuth Kit** (**TSK**) is a collection of
[UNIX](unix.md)-based command line tools that allow you to
investigate a computer. The current focus of the tools is the file and
volume systems and TSK supports multiple [file
systems](file_system.md).

[Autopsy](autopsy.md) is a front-end for TSK which allows
browser-based access to the TSK tools.

# Features

The Sleuth Kit is arranged in layers. There is a *data layer* which is
concerned with how information is stored on a disk and a *metadata
layer* which is considered with information such as
[inodes](inode.md) and [directories](directory "wikilink"). The
commands that deal with the data layer are prefixed with the letter *d*,
which the commands that deal with the metadata layer are prefixed with
the letter *i*.

Some of the commands in Sleuth Kit are:

blkcat
Views the contents of a [block](block.md).

<!-- -->

blkls
Lists [unallocated blocks](unallocated_block.md). Makes keyword
searches more efficient. Gets a list of unallocated blocks.

<!-- -->

blkcalc
Tells you where an unallocated blocks are.

<!-- -->

blkstat
Details about a given block.

<!-- -->

icat
View contents of a file given its inode value or [cluster
number](cluster_number.md). Doesn't list directories, lists the
contents.

<!-- -->

ils
Lists the files extents on a disk.

<!-- -->

istat
Information about an inode number.

## Supported File Systems

- [NTFS](ntfs.md)
- [FAT](fat.md)
- [Ext2](ext2.md), [Ext3](ext3.md),
  [Ext4](ext4.md)
- [UFS](ufs.md)
- ISO 9660
- [HFS+](hfs+.md)/HFSX
- [Yaffs](yaffs.md)

Note that several several of the file systems supported have known
shortcomings. Check [issue
tracker](https://github.com/sleuthkit/sleuthkit/issues) for details.

## File Search Facilities

- Lists allocated and unallocated files.
- Lists and sorts by file type.
- Shows a time of creation and change.

## Historical Reconstruction

**fls** and **ils** can be used to create a full listing of file system
timestamps. The output of these commands can be inputted into
**mactimes** which will generate a timeline of the file system
timestamps.

Note that there are numerous known issues with the
[Bodyfile](bodyfile.md) format used by **fls** and **ils**.

## Searching Abilities

- Searches for keywords.
- Builds an index.

## Hash Databases

- Uses [MD5](md5.md) or [SHA-1](sha-1.md).
- Interfaces with NIST [NSRL](nsrl.md),
  [Hashkeeper](hashkeeper.md) and customer databases.

## Evidence Collection Features

- Tracks forensic activity.

# History

## License Notes

The SleuthKit uses a mix of various licenses. Its core library, libtsk,
is predominantly licensed under IBM Public License version 1.0 and
Common Public License version 1.0. For more information see:
<https://github.com/sleuthkit/sleuthkit/blob/develop/licenses/README.md>

## Ext4 support

In 2011 [Willi Ballenthin](willi_ballenthin.md) provided
[patches](http://www.williballenthin.com/ext4/) for the SleutKit to add
ext4 support. These patches were integrated by [Kevin
Fairbanks](kevin_fairbanks.md) into a separate [fork of the
SleuthKit](https://github.com/kfairbanks/sleuthkit/tree/Ext4_Dev). This
fork was integrated in the 4.1.0 version.

Note that ext4 format features introduced after SleutKit 4.1.0 might not
be supported and SleutKit tools might incorrectly represent these
[1](https://github.com/sleuthkit/sleuthkit/issues/2488).

# See Also

- [The Sleuth Kit How-To](the_sleuth_kit_how-to.md)
- [Bodyfile](bodyfile.md)
- [tsk-cp](tsk-cp.md)
- The mmls [OCFA treegraph API](ocfa_treegraph_api.md) example
  module.

# External Links

- [Autopsy website](http://www.sleuthkit.org/autopsy/desc.php)

## External Reviews