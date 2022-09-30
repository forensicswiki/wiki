---
tags:
  -  Windows Analysis
---
On Windows XP the Restore Points can be found in:

    C:\System Volume Information_restore{%GUID%}\

Where %GUID% is the machine GUID, for which the Restore Point was
created.

This directory contains:

- fifo.log; Restore Point deletion information
- Restore Point data sub directories, named 'RP\[1-9\]\[0-9\]\*', e.g.
  'RP1'

A Restore Point data sub directory contains:

- change.log or change.log.\[1-9\];
- rp.log; restore point information log file

## External Links

- [Wikipedia: System
  Restore](http://en.wikipedia.org/wiki/System_Restore)
- \[<https://msdn.microsoft.com/en-us/library/windows/desktop/bb395209(v=vs.85>).aspx
  MSDN: Legacy System Restore Reference\]
- [Restore Point
  Forensics](http://www.stevebunting.org/udpd4n6/forensics/restorepoints.htm),
  by [Steve Bunting](steve_bunting.md)
- [Forensic Analysis of System Restore Points in Microsoft Windows
  XP](http://citeseerx.ist.psu.edu/viewdoc/download?doi=10.1.1.84.4474&rep=rep1&type=pdf),
  by Kris Harms, July 2006
- [Restore Point
  Forensics](http://windowsir.blogspot.ch/2006/10/restore-point-forensics.html),
  by [Harlan Carvey](harlan_carvey.md), October 20, 2006
- [ProScript to parse rp.log file from XP System Restore Points (PD/IR
  4.85+)](https://web.archive.org/web/20090828023053/http://toorcon.techpathways.com/cs/forums/thread/95.aspx),
  by [Harlan Carvey](harlan_carvey.md), October 26, 2006
- [Restore Point
  Analysis](http://windowsir.blogspot.ch/2007/06/restore-point-analysis.html),
  by [Harlan Carvey](harlan_carvey.md), June 16, 2007
- [Enscript Tutorial 1 - Parse XP System Restore
  Logs](http://www.swiftforensics.com/2012/03/enscript-tutorial-1-parse-xp-system.html),
  by Yogesh Khatri, March 2, 2012
- [The Windows Restore Point
  formats](https://github.com/libyal/dtformats/blob/master/documentation/Restore%20point%20formats.asciidoc),
  by [Joachim Metz](joachim_metz.md), April 2015

## Tools

- [plaso](plaso.md) as of version 1.3.0 has support for rp.log
- [rp_change_log.py](https://github.com/libyal/dtformats/blob/master/scripts/rp_change_log.py),
  tool to analyze the change.log files

