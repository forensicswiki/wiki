---
tags:
  -  File Formats
---
Microsoft Windows Shortcut Files

## File Format

The Windows Shortcut file has the extension .lnk. It basically is a
metadata file, specific for the Microsoft Windows platform and is
interpreted by the Windows Shell. The file format indicates that these
files contain a specific signature, 0x4C (4C 00 00 00) at offset 0
within the file/stream. Further, the GUID (CLSID)
00021401-0000-0000-c000-000000000046 stored at byte offset 4 makes a
good identifier.

Understanding this file format can be extremely useful for an analyst,
as not only are shortcut files employed from (at least) Windows 95
through Windows 10, but the binary format is also used in the numbered
streams within \*.automaticDestinations-ms and \*.customDestinations-ms
[Jump Lists](jump_lists.md) files on [Windows
7](windows_7.md) and later.

## Metadata

- [MAC times](mac_times.md) of the target. These are a snapshot
  of the target date and timestamps before it was last opened. The
  target can be several things like for example a (linked) file;

<!-- -->

    Linked file information:
        Creation time       : Jul 26, 2009 14:44:34 UTC
        Modification time   : Jul 26, 2009 14:44:34 UTC
        Access time     : Aug 12, 2010 06:41:50 UTC
        Local path      : C:\Program Files (x86)\Windows Live\Mail\wlmail.exe

- The [Shell Item](shell_item.md) list of the target;
- The size of the target when it was last accessed;
- Serial number of the volume where the target was stored;
  - Useful for correlating a USB drive or other removable media (if you
    can get the volume serial number off it) to a particular user or
    system.
- Network volume share name;
- Read-only, hidden, system, volume label, encryption, sparse,
  compressed, offline and several other target attributes;
- MAC address of the host computer (sometimes);
- Distributed link tracking information, e.g.

<!-- -->

    Distributed link tracker information:
        Machine identifier string           : mysystem
        Droid volume identifier             : 11111111-2222-3333-4444-555555555555
        Droid file identifier               : aaaaaaaa-bbbb-cccc-dddd-eeeeeeeeeeee
        Birth droid volume identifier       : 11111111-2222-3333-4444-555555555555
        Birth droid file identifier         : aaaaaaaa-bbbb-cccc-dddd-eeeeeeeeeeee

## Notes

Windows Shell commands:

    %windir%\explorer.exe ::{7007ACC7-3202-11D1-AAD2-00805FC1270E}

    %windir%\explorer.exe shell:::{3080F90D-D7AD-11D9-BD98-0000947B0257}

<http://docs.rainmeter.net/tips/launching-windows-special-folders>

## External Links

- [The Meaning of Linkfiles In Forensic
  Examinations](http://computerforensics.parsonage.co.uk/downloads/TheMeaningofLIFE.pdf),
  by [Harry Parsonage](harry_parsonage.md), September 2008
- [MS-SHLLINK](http://msdn.microsoft.com/en-us/library/dd871305%28PROT.13%29.aspx)
- [Windows Shortcut File (LNK)
  format](https://github.com/libyal/liblnk/blob/master/documentation/Windows%20Shortcut%20File%20(LNK)%20format.asciidoc),
  by the [liblnk project](liblnk.md)
- [Evidentiary Value of Link
  Files](http://www.forensicfocus.com/link-file-evidentiary-value), by
  Nathan Weilbacher
- [LNK Parsing: You’re doing it wrong
  (I)](http://blog.0x01000000.org/2010/08/10/lnk-parsing-youre-doing-it-wrong-i/),
  by [Jordi Sánchez López](jordi_sánchez_lópez.md), August 10,
  2010
- [LNK Parsing: You’re doing it wrong
  (II)](http://blog.0x01000000.org/2010/08/13/lnk-parsing-youre-doing-it-wrong-ii/),
  by [Jordi Sánchez López](jordi_sánchez_lópez.md), August 13,
  2010

## Tools

## Commercial tools

- [Windows LNK Parsing Utility
  (lp)](http://www.tzworks.net/prototype_page.php?proto_id=11), \$210.00
  tool that can be run on Windows, Linux or Mac OS-X

## Free (Non Open Source)

- [Windows File Analyzer](http://mitec.cz/wfa.html), free tool that is
  capable of reading and reporting on Windows shortcut files

## Open Source

- [jafat](http://jafat.sourceforge.net/files.html), free tool (in PERL)
  that is capable of reading and reporting on Windows shortcut files
- [liblnk](liblnk.md)
- [lnk-parser](http://code.google.com/p/lnk-parser/)
- [lnk parser in C# that parses all
  structures](https://github.com/EricZimmerman/Lnk/)
- [LECmd command line tool](https://github.com/EricZimmerman/LECmd/)

