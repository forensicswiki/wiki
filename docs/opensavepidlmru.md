---
tags:
  - No Category
---
The [OpenSaveMRU](opensavemru.md) Windows registry key was
renamed starting in Windows Vista to OpenSavePidlMRU
[1](http://www.forensicmag.com/articles/2012/04/windows-7-registry-forensics-part-4).

## Notable Changes from Windows XP

The \* sub-key of OpenSavePidlMRU was extended to track the last twenty
files opened or saved of any type via the Windows Common Dialog
[2](http://computer-forensics.sans.org/blog/2010/04/02/openrunsavemru-lastvisitedmru).

Value data is stored as binary (REG_BINARY) and was previously stored as
a string value (REG_SZ) in [OpenSaveMRU](opensavemru.md).