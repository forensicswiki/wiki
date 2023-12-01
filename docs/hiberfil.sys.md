---
tags:
  - File Formats
---
**hiberfil.sys** is the file used by default by Microsoft Windows to
save the machine's state as part of the
hibernation process. The operating system also
keeps an open file handle to this file, so no user, including the
Administrator, can read the file while the system is running.

Although often presumed, the size of the hiberfil.sys is *not*
one-to-one in size to the available, or total RAM of the machine.

The data structures required to parse the file format are available in
the [Microsoft Windows](microsoft_windows.md) debug symbols,
including some of the various compression methods used.

The Xpress compression was reverse engineered by Matthieu
Suiche. He created with Nicolas
Ruff a project called
Sandman is the only open-source tool that
can read and write the Windows Vista and 7 hibernation files.

In early 2008, as part of the [Windows Server Protocol Program](https://learn.microsoft.com/en-us/openspecs/dev_center/ms-devcentlp/5f4fc8ba-f448-4b05-968e-df51c60eaef8),
Microsoft released documentation on the Xpress compression algorithm in
the [Directory Replication Service (DRS) Remote Protocol](https://learn.microsoft.com/en-us/openspecs/windows_protocols/ms-drsr/f977faaa-673e-4f66-b9bf-48c640241d47)
specification (section 4.1.10.6.15, "DecompressWin2k3").

| Windows Version | Compression               |
|-----------------|---------------------------|
| ME and earlier  | none                      |
| 2000            | LZNT1 (LZ77 variant)      |
| Vista, 7        | Xpress (LZ77 and direct2) |

[Hibernation Recon](arsenal_recon.md#hibernation-recon) is a
commercial digital forensics tool launched in late 2016. In addition to
memory reconstruction from Windows XP, Vista, 7, 8/8.1, and 10
hibernation files, Hibernation Recon also identifies and extracts data
from the multiple levels of slack space within them.

## External Links

* [Microsoft Hibernation Files](https://code.google.com/archive/p/volatility/wikis/HiberAddressSpace.wiki),
  by [the Volatility project](volatility_framework.md)
* [Parsing hibernation slack space](https://diablohorn.com/2014/12/10/parsing-the-hiberfil-sys-searching-for-slack-space/)

### LZ XPRESS

* [DIRECT2 Encoding Algorithm](https://learn.microsoft.com/en-us/openspecs/windows_protocols/ms-drsr/07815956-1375-4148-b33e-39c31f988ec8),
  by [Microsoft](microsoft.md)
