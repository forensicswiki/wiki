---
tags:
  - File Systems
---
There are many ways to identify a file system inside a partition.

When an operating system attempts to mount a partition, it may use the
ID from the partition table.

There are several tools that can identify the partition from the data it
contains, including:

- blkid
- [file](file.md)
- parted
- [testdisk](testdisk.md)

In general you should not rely on the partition record for determining
the partition type.

Some of the test images created for the [Honeynet
Challenges](http://wiki.sleuthkit.org/index.php?title=Case_Studies) have
multiple file systems contained in a single partition.

