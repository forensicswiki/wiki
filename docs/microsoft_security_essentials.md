---
tags:
  -  Applications
  -  Anti Virus
---
## Quarantine directory

On Windows XP:

    C:\Documents and Settings\All Users\Application Data\Microsoft\Microsoft Antimalware\Quarantine

On Windows 7:

    C:\ProgramData\Microsoft\Microsoft Antimalware\Quarantine

## Scan cache

    C:\ProgramData\Microsoft\Microsoft Antimalware\Scans\History\CacheManager\MpScanCache-0.bin

## File system cache (Windows Defender)

    C:\ProgramData\Microsoft\Windows Defender\Scans\History\CacheManager\MpSfc.bin

To build run:

    "%programfiles%\Windows Defender\MpCmdRun.exe" –BuildSFC

## External Links

* [Microsoft Security Essentials](https://support.microsoft.com/en-us/windows/what-is-microsoft-security-essentials-c25ad47a-7d15-8072-1438-b07dffcbbb20),
  by [Microsoft](microsoft.md)
* [Endpoint Protection](https://learn.microsoft.com/en-us/previous-versions/system-center/system-center-2012-R2/hh508836(v=technet.10)),
  by [Microsoft](microsoft.md)

### Quarantined files

* [hardcoded key obtained from mpengine.dll](https://github.com/brad-sp/cuckoo-modified/blob/00ad13c94cc7453c40ed6152d16009ca1c8ed6f2/lib/cuckoo/common/quarantine.py)
