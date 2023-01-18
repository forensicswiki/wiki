---
tags:
  - Open Source Software
  - Registry Analysis
  - Tools
  - Windows
---
RegRipper is an open source forensic software application developed by
[Harlan Carvey](harlan_carvey.md). RegRipper, written in Perl,
is a [Windows Registry](windows_registry.md) data extraction
tool.

RegRipper can be customized to the examiner's needs through the use of
available plugins or by users writing plugins to suit specific needs.

## Technical Background and Forensic Soundness

RegRipper uses James McFarlane’s Parse::Win32Registry module
[1](https://metacpan.org/release/JMACFARLA/Parse-Win32Registry-0.40) to
access a Windows Registry hive file in an object-oriented manner,
bypassing the Win32API. This module is used to locate and access
Registry key nodes within the hive file, as well as value nodes and
their data. When accessing a key node, the LastWrite time is retrieved,
parsed and translated into something the examiner can understand. Data
is retrieved in much the same manner…if necessary, the plugin that
retrieves the data will also perform translation of that data into
something readable.

## Also see

[Windows Registry](windows_registry.md)

## External Links

- [Using RegRipper](http://windowsir.blogspot.com/2011/03/using-regripper.html)
- [RegRipper GitHub Repo](https://github.com/keydet89/RegRipper3.0)
- [RegRipper Blog](https://regripper.wordpress.com/)
- [Windows Forensics Analysis](https://code.google.com/archive/p/winforensicaanalysis)
- [RegRipper Supplemental Plugins](https://code.google.com/archive/p/regripperplugins)
- [Developers blog (Windows Incident Response)](http://windowsir.blogspot.com/)
- [RegRipper Google Code](https://code.google.com/archive/p/regripper)
