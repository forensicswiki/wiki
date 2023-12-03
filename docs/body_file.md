---
tags:
  -  File Formats
  -  Linux
  -  Windows
  -  MacOS
  -  Timeline Analysis
  -  Text
  -  Articles that need to be expanded
---

# Body File

_Body file may also be referred to as "bodyfile", however official
documentation refers to it as body file (two separate words)._

The **body file** format is a delimiter-separated output timeline format (as
far as known) introduced by the [The Sleuth Kit](the_sleuth_kit.md). Body files are pipe
(`|`) delimited and are referred to as an "intermediate file", as they are not
sorted chronologically and are often staged for post-processing. Subsequent
timeline sorting is done via the [mactime](mactime.md) tool.

## Data & Fields

All times within a body file are reported in UNIX time format. Lines that start
with `#` are ignored and treated as comments.

There was a rewrite of body file output with The Sleuth Kit 3.0. However, some
tools may still utilize version 2.x.

Default output fields are as follows:

### Version 2.x

```ascii
MD5 | path/name | device | inode | mode_as_value | mode_as_string | num_of_links | UID | GID | rdev | size | atime | mtime | ctime | block_size | num_of_blocks
```

### Version 3.x

```ascii
MD5 | name | inode | mode_as_string | UID | GID | size | atime | mtime | ctime | crtime
```

_Note: Outputs do not include spaces between values and pipes; we have inserted them here for easier readability._

---

## Known Issues
<!-- Issues have been merged from multiple files. Also, issues may apply to The Sleuth Kit more than body files - must reconcile. 
NOTE: Nov/Dec 2022, validate if each is still an issue -->
Known shortcomings with body file format are:

* Undocumented granularity of timestamp, current implementation by
  [The Sleuth Kit](the_sleuth_kit.md) appears to be seconds. See [here](https://github.com/sleuthkit/sleuthkit/issues/1810).
* Undocumented extended file mode of `-/-rrwxrwxrwx`. Characters `-/-` are appended to the body file entry and `r` file entry type indication, presumably to indicate a "regular file".
* Undocumented and inconsistent application of TSK metadata addresses. See [here](https://github.com/sleuthkit/sleuthkit/issues/1809)
* Undocumented and inconsistent application of owner identifier (UID). See [here](https://github.com/sleuthkit/sleuthkit/issues/1830).
* Date and time values do not indicate a time zone or if daylight savings applies. Timestamps can be in either UTC or local time depending on the original file system.
* Body file encoding is not specified, UTF-8 is assumed.
  * It is unclear how "invalid" Unicode characters should be handled, such as unpaired surrogates in NTFS file names.
* The name field can contain `($FILE_NAME)` to indicate the body file entry was derived from a NTFS `$FILE_NAME` attribute instead of `$STANDARD_INFORMATION` and `$DATA` attributes. Note that the exact behavior is not documented by the Sleuth Kit project.
* The `name` field can contain `-> symbolic_link_target` but `fls` does not appear to support this for NTFS. Also see [here](https://github.com/sleuthkit/sleuthkit/issues/2645).
* It is unclear if the symbolic link target can be used in combination with the `($FILE_NAME)` suffix.
* It is unclear which characters should be escaped, by observation `|`
  and `\` are both escaped with `\` in the name field by `fls` but `mactime`
  is unable to handle a name that contains the `|` character. See [here](https://github.com/sleuthkit/sleuthkit/issues/2124). _Note: Other implementations are known to not escape `\`._
* It is unclear from the specification if control characters should be
  escaped. See [here](https://github.com/sleuthkit/sleuthkit/issues/1989). Other implementations are known to escape control characters as `x##` where `##` contains the hexadecimal byte value of the control character.
* The format of the `inode` field is unclear for file systems like NTFS, the documentation indicates that it uses [a TSK Metadata Address](https://wiki.sleuthkit.org/index.php?title=Metadata_Address), however by observation the implementation is TSK specific and does not seem to match what is documented. Also see [here](https://github.com/sleuthkit/sleuthkit/issues/1809). Other implementations are known to store the 64-bit NTFS file reference value as the `inode` field.
* The format of the `mode_as_string` field is unclear for file systems like NTFS, this likely can be derived from the source code. Also see [here](https://github.com/sleuthkit/sleuthkit/issues/1810).
* The Sleuth Kit currently does not correctly identify symbolic links for NTFS in the body file output. Also see [here](https://github.com/sleuthkit/sleuthkit/issues/2645).
* The `atime`, `mtime`, `ctime`, and `crtime` typically contain the number of seconds since January 1, 1970. It is unknown if a fractional part is allowed by specification. The corresponding mactime tool does allow for a fractional part to be present but ignores it. Also see [here](https://github.com/sleuthkit/sleuthkit/issues/1810). _This limits the usefulness of the format for timelines with a vast amount of sub-second activity._
* The format of the MD5 field is undefined, however documentation indicates:
  * If hashing is disabled, the value will be `0`.
  * If hashing is enabled, but no MD5 was calculated, the value will be `00000000000000000000000000000000`. See [here](https://github.com/sleuthkit/sleuthkit/issues/2058).

### NTFS

* Duplicate entries for the same NTFS ADS. Also see [here](https://github.com/sleuthkit/sleuthkit/issues/2644).

### HFS+ and HFSX

* On HFS+ and HFSX the `/` character in a file name will be replaced by `:`, which
  corresponds with the behavior of Mac OS Terminal. Also see [here](https://github.com/sleuthkit/sleuthkit/blob/3d16b8bc293ba13a5674fe9ce6a35f867ccc945d/tsk/fs/hfs_dent.c).
* For hard links on HFS+ the Catalog Node Identifier (CNID) of the link target (indirect node) file record is used instead as the `inode` value instead of the CNID of the (hard link) file record itself. This matches the behavior of Mac OS (file) stat as described [here](https://developer.apple.com/library/archive/technotes/tn/tn1150.html), in the section "Hard Links".
* For HFS+ the MD5 calculation of `fls` includes:
  * Regular files
  * symbolic links (content of the data stream of the symbolic link not its target)
  * "Virtual metadata files" like `$CatalogFile`

### ext2, ext3 and ext4

* For ext2, ext3 and ext4 the MD5 calculation of `fls` includes:
  * Regular files
  * Directories (contents of the directory entries data stream)
  * Symbolic links (content of the data stream of the symbolic link not its
  target)
  * "Virtual metadata files/directories" like `$OrphanFiles`

## Output Format

Sleuthkit 4.7.0 was used to create the example below from a sample NTFS MFT file entry:

Body file data:

```ascii
0|/$BadClus|8-128-2|r/rr-xr-xr-x|0|0|0|1580550524|1580550524|1580550524|1580550524
0|/$BadClus:$Bad|8-128-1|r/rr-xr-xr-x|0|0|7270400|1580550524|1580550524|1580550524|1580550524
0|/$BadClus ($FILE_NAME)|8-48-3|r/rr-xr-xr-x|0|0|82|1580550524|1580550524|1580550524|1580550524
```

Corresponding NTFS MFT entry:

```ascii
MFT Entry Header Values:
Entry: 8        Sequence: 8
$LogFile Sequence Number: 1069751
Allocated File
Links: 1

$STANDARD_INFORMATION Attribute Values:
Flags: Hidden, System
Owner ID: 0
Security ID: 256  ()
Created:    2020-02-01 10:48:44.857384500 (CET)
File Modified:  2020-02-01 10:48:44.857384500 (CET)
MFT Modified:   2020-02-01 10:48:44.857384500 (CET)
Accessed:   2020-02-01 10:48:44.857384500 (CET)

$FILE_NAME Attribute Values:
Flags: Hidden, System
Name: $BadClus
Parent MFT Entry: 5     Sequence: 5
Allocated Size: 0       Actual Size: 0
Created:    2020-02-01 10:48:44.857384500 (CET)
File Modified:  2020-02-01 10:48:44.857384500 (CET)
MFT Modified:   2020-02-01 10:48:44.857384500 (CET)
Accessed:   2020-02-01 10:48:44.857384500 (CET)

Attributes: 
Type: $STANDARD_INFORMATION (16-0)   Name: N/A   Resident   size: 72
Type: $FILE_NAME (48-3)   Name: N/A   Resident   size: 82
Type: $DATA (128-2)   Name: N/A   Resident   size: 0
Type: $DATA (128-1)   Name: $Bad   Non-Resident   size: 7270400  init_size: 0
```

Behavior of the TSK Metadata Address:

* `8-128-2` references the `$DATA` attribute in MFT entry 8, note that this
  `$DATA` attribute on-disk is the 3rd attribute in the MFT entry.
* `8-128-1` references the `$DATA` attribute in MFT entry 8, note that this
  `$DATA` attribute on-disk is the 4th attribute in the MFT entry.
* `8-48-3` references the first `$FILE_NAME` attribute in MFT entry 8, note
  that the `$FILE_NAME` attribute on-disk is the 2nd attribute in the MFT
  entry.

_Note that due to an issue within The Sleuth Kit, NTFS metadata addresses for `$FILE_NAME` attributes in an `$ATTRIBUTE_LIST` are not unique, and it is not deterministic as to what the "first" MFT attribute is. See [here](https://github.com/sleuthkit/sleuthkit/issues/1809)._

## Also see

* [mactime](mactime.md)
* [The Sleuth Kit](the_sleuth_kit.md)

## External Links

* [Body file - Sleuth KitWiki](http://wiki.sleuthkit.org/index.php?title=Body_file)
* [Bodyfile format](https://dfimagetools.readthedocs.io/en/latest/sources/Bodyfile-format.html), by dfImageTools project
