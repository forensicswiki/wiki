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
Body file is a timeline format introduced by the
[SleuthKit](sleuthkit.md).

Version 2 (used by SleuhtKit 2):

    MD5 | path/name | device | inode | mode_as_value | mode_as_string | num_of_links | UID | GID | rdev | size | atime | mtime | ctime | block_size | num_of_blocks

Version 3 (used by SleuhtKit 3 and later):

    MD5|name|inode|mode_as_string|UID|GID|size|atime|mtime|ctime|crtime

The times are reported in a POSIX (or UNIX) timestamp.

### Shortcomings

Known shortcomings with body file format are:

- Undocumented granularity of timestamp, current implementation by
  [Sleuthkit](sleuthkit.md) appears to be seconds
  [1](https://github.com/sleuthkit/sleuthkit/issues/1810)
- Undocumented extended file mode of "-/-rwxrwxrwx"
- Undocumented and inconsistent application of TSK metadata addresses
  [2](https://github.com/sleuthkit/sleuthkit/issues/1809)
- Undocumented and inconsistent application of owner UID
  [3](https://github.com/sleuthkit/sleuthkit/issues/1830)

This limits the portability of the body file format between tools.

### Observed behavior Sleuthkit

Sleuthkit 4.7.0 was used to create the examples below:

From the body file:

`0|/$BadClus|8-128-2|r/rr-xr-xr-x|0|0|0|1580550524|1580550524|1580550524|1580550524`
`0|/$BadClus:$Bad|8-128-1|r/rr-xr-xr-x|0|0|7270400|1580550524|1580550524|1580550524|1580550524`
`0|/$BadClus ($FILE_NAME)|8-48-3|r/rr-xr-xr-x|0|0|82|1580550524|1580550524|1580550524|1580550524`

Corresponding MFT entry:

`MFT Entry Header Values:`
`Entry: 8        Sequence: 8`
`$LogFile Sequence Number: 1069751`
`Allocated File`
`Links: 1`
``
`$STANDARD_INFORMATION Attribute Values:`
`Flags: Hidden, System`
`Owner ID: 0`
`Security ID: 256  ()`
`Created:    2020-02-01 10:48:44.857384500 (CET)`
`File Modified:  2020-02-01 10:48:44.857384500 (CET)`
`MFT Modified:   2020-02-01 10:48:44.857384500 (CET)`
`Accessed:   2020-02-01 10:48:44.857384500 (CET)`
``
`$FILE_NAME Attribute Values:`
`Flags: Hidden, System`
`Name: $BadClus`
`Parent MFT Entry: 5     Sequence: 5`
`Allocated Size: 0       Actual Size: 0`
`Created:    2020-02-01 10:48:44.857384500 (CET)`
`File Modified:  2020-02-01 10:48:44.857384500 (CET)`
`MFT Modified:   2020-02-01 10:48:44.857384500 (CET)`
`Accessed:   2020-02-01 10:48:44.857384500 (CET)`
``
`Attributes: `
`Type: $STANDARD_INFORMATION (16-0)   Name: N/A   Resident   size: 72`
`Type: $FILE_NAME (48-3)   Name: N/A   Resident   size: 82`
`Type: $DATA (128-2)   Name: N/A   Resident   size: 0`
`Type: $DATA (128-1)   Name: $Bad   Non-Resident   size: 7270400  init_size: 0`

Behavior of the TSK Metadata Address:

- 8-128-2 references the \$DATA attribute in MFT entry 8, note that this
  \$DATA attribute on-disk is the 3rd attribute in the MFT entry.
- 8-128-1 references the \$DATA attribute in MFT entry 8, note that this
  \$DATA attribute on-disk is the 4th attribute in the MFT entry.
- 8-48-3 references the first \$FILE_NAME attribute in MFT entry 8, note
  that the \$FILE_NAME attribute on-disk is the 2nd attribute in the MFT
  entry.

From the body file:

`0|/$Extend|11-144-4|d/dr-xr-xr-x|0|0|552|1580550524|1580550524|1580550524|1580550524`
`0|/$Extend ($FILE_NAME)|11-48-3|d/dr-xr-xr-x|0|0|80|1580550524|1580550524|1580550524|1580550524`

Corresponding MFT entry:

`MFT Entry Header Values:`
`Entry: 11        Sequence: 11`
`$LogFile Sequence Number: 1070011`
`Allocated Directory`
`Links: 1`
``
`$STANDARD_INFORMATION Attribute Values:`
`Flags: Hidden, System`
`Owner ID: 0`
`Security ID: 257  ()`
`Created:    2020-02-01 10:48:44.857384500 (CET)`
`File Modified:  2020-02-01 10:48:44.857384500 (CET)`
`MFT Modified:   2020-02-01 10:48:44.857384500 (CET)`
`Accessed:   2020-02-01 10:48:44.857384500 (CET)`
``
`$FILE_NAME Attribute Values:`
`Flags: Directory, Hidden, System`
`Name: $Extend`
`Parent MFT Entry: 5     Sequence: 5`
`Allocated Size: 0       Actual Size: 0`
`Created:    2020-02-01 10:48:44.857384500 (CET)`
`File Modified:  2020-02-01 10:48:44.857384500 (CET)`
`MFT Modified:   2020-02-01 10:48:44.857384500 (CET)`
`Accessed:   2020-02-01 10:48:44.857384500 (CET)`
``
`Attributes: `
`Type: $STANDARD_INFORMATION (16-0)   Name: N/A   Resident   size: 72`
`Type: $FILE_NAME (48-3)   Name: N/A   Resident   size: 80`
`Type: $INDEX_ROOT (144-4)   Name: $I30   Resident   size: 552`

Behavior of the TSK Metadata Address:

- 11-144-4 references the \$INDEX_ROOT attribute in MFT entry 11, note
  that this \$INDEX_ROOT attribute on-disk is the 3rd attribute in the
  MFT entry. Note that the size of a corresponding \$INDEX_ALLOCATION is
  not included in the "size" in the body file.
  [4](https://github.com/sleuthkit/sleuthkit/issues/1831)

## Also see

- [mactime](mactime.md)

## External Links

- [Body file -
  SleuthKit](http://wiki.sleuthkit.org/index.php?title=Body_file)

