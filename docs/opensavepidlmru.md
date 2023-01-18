---
tags:
  - Windows
---
The [OpenSaveMRU](opensavemru.md) Windows registry key was
renamed starting in Windows Vista to OpenSavePidlMRU

## Notable Changes from Windows XP

The \* sub-key of OpenSavePidlMRU was extended to track the last twenty
files opened or saved of any type via the Windows Common Dialog
[2](https://www.sans.org/digital-forensics-incident-response/).

Value data is stored as binary (REG_BINARY) and was previously stored as
a string value (REG_SZ) in [OpenSaveMRU](opensavemru.md).
