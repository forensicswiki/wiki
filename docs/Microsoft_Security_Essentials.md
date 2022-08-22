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

- [Microsoft Security
  Essentials](http://windows.microsoft.com/en-us/windows/security-essentials-download),
  by [Microsoft](Microsoft "wikilink")
- [Endpoint
  Protection](http://technet.microsoft.com/en-us/library/hh508836.aspx),
  by [Microsoft](Microsoft "wikilink")

### Quarantined files

- [hardcoded key obtained from
  mpengine.dll](https://github.com/brad-accuvant/cuckoo-modified/blob/00ad13c94cc7453c40ed6152d16009ca1c8ed6f2/lib/cuckoo/common/quarantine.py#L186)

[Category:Applications](Category:Applications "wikilink") [Category:Anti
Virus](Category:Anti_Virus "wikilink")