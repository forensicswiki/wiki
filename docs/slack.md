---
tags:
  - Anti-Forensics
  - Articles that need to be expanded
---
## Definition

In [computer forensics](computer_forensics.md) **slack** refers
to the bytes after the logical end of a file and the end of the cluster
wherein the final byte of the valid file resides.

## File Slack Types

### RAM Slack

The data storage space that exists from the end of a file to the end of
the last sector assigned to a file.

### Drive Slack

The data storage space that exists from the end of the last sector
assigned to a file to the end of the last cluster assigned to a file.

### Hibernation Slack

Previous hibernation data that has not yet been overwritten in a
hibernation file.

## See Also

* [FAT#File_Slack](fat.md#file-slack)

## External Links

* <http://www.forensics-intl.com/def6.html>
