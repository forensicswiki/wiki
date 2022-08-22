**hiberfil.sys** is the file used by default by Microsoft Windows to
save the machine's state as part of the
[hibernation](hibernation "wikilink") process. The operating system also
keeps an open file handle to this file, so no user, including the
Administrator, can read the file while the system is running.

Although often presumed, the size of the hiberfil.sys is *not*
one-to-one in size to the available, or total RAM of the machine.

The data structures required to parse the file format are available in
the [Microsoft Windows](Microsoft_Windows "wikilink") debug symbols,
including some of the various compression methods used.

The Xpress compression was reverse engineered by [Matthieu
Suiche](Matthieu_Suiche "wikilink"). He created with [Nicolas
Ruff](Nicolas_Ruff "wikilink") a project called
[Sandman](http://sandman.msuiche.net/) is the only open-source tool that
can read and write the Windows Vista and 7 hibernation files.

In early 2008, as part of the [Windows Server Protocol
Program](http://msdn.microsoft.com/en-us/library/cc197979.aspx),
Microsoft released documentation on the Xpress compression algorithm in
the [Directory Replication Service (DRS) Remote
Protocol](http://download.microsoft.com/download/a/e/6/ae6e4142-aa58-45c6-8dcf-a657e5900cd3/%5BMS-DRSR%5D.pdf)
specification (section 4.1.10.6.15, "DecompressWin2k3"). However, the
pseudocode given contains numerous errors, as documented by [Matthieu
Suiche](Matthieu_Suiche "wikilink") in a [blog
entry](http://www.msuiche.net/2008/04/06/few-words-about-microsoft-interoperability-initiative/).

| Windows Version | Compression               |
|-----------------|---------------------------|
| ME and earlier  | none                      |
| 2000            | LZNT1 (LZ77 variant)      |
| Vista, 7        | Xpress (LZ77 and direct2) |

[Hibernation Recon](Arsenal_Recon#Hibernation_Recon "wikilink") is a
commercial digital forensics tool [launched in late
2016](https://arsenalrecon.com/apps/hibernation-recon/). In addition to
memory reconstruction from Windows XP, Vista, 7, 8/8.1, and 10
hibernation files, Hibernation Recon also identifies and extracts data
from the multiple levels of slack space within them.

## External Links

- [Sandman
  Project](http://sandman.msuiche.net/docs/SandMan_Project.pdf), by
  [Matthieu Suiche](Matthieu_Suiche "wikilink"), February 2008
- [Windows hibernation file for fun &
  profit](http://msuiche.net/con/bhusa2008/Windows_hibernation_file_for_fun_%27n%27_profit-0.6.pdf),
  by [Matthieu Suiche](Matthieu_Suiche "wikilink")
- [Enter SandMan](http://www.msuiche.net/pres/PacSec07-slides-0.4.pdf),
  by [Nicolas Ruff](Nicolas_Ruff "wikilink"), [Matthieu
  Suiche](Matthieu_Suiche "wikilink")
- [Hibernation File
  Format](http://web17.webbpro.de/downloads/Hibernation%20File%20Attack/Hibernation%20File%20Format.pdf),
  by [Peter Kleissner](Peter_Kleissner "wikilink"), 2009
- [<http://jessekornblum.livejournal.com/254105.html>](http://jessekornblum.livejournal.com/254105.html),
  by [Jesse Kornblum](Jesse_Kornblum "wikilink"), August 18, 2009
- [Microsoft Hibernation
  Files](http://code.google.com/p/volatility/wiki/HiberAddressSpace), by
  [the Volatility project](Volatility "wikilink")
- [Hibernation Recon](https://arsenalrecon.com/apps/hibernation-recon/)
- [Parsing hibernation slack
  space](https://diablohorn.com/2014/12/10/parsing-the-hiberfil-sys-searching-for-slack-space/)

### LZ XPRESS

- [DIRECT2 Encoding
  Algorithm](http://msdn.microsoft.com/en-us/library/ee441458.aspx), by
  [Microsoft](Microsoft "wikilink")
- [Few words about Microsofts interoperability
  initiative](http://www.msuiche.net/2008/04/06/few-words-about-microsoft-interoperability-initiative/),
  by [Matthieu Suiche](Matthieu_Suiche "wikilink")
- [C implementation of LZ
  XPRESS](http://www.msuiche.net/codes/xpress.c.txt), by [Matthieu
  Suiche](Matthieu_Suiche "wikilink")