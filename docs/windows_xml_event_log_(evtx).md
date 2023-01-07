---
tags:
  - File Formats
  - Windows
  - XML
---
The Windows XML Event Log (EVTX) format was introduces in [Windows
Vista](windows.md) as a replacement for the [Windows Event Log
(evt)](windows_event_log_(evt).md) format.

## Event Viewer

On Windows the event logs can be managed with "Event Viewer"
(eventvwr.msc) or "Windows Events Command Line Utility" (wevtutil.exe).
Event Viewer can represent the EVTX files in both "general view" (or
formatted view) and "details view" (which has both a "friendly view" and
"XML view"). Note that the formatted view can hide significant event
data that is stored in the event record and can be seen in the detailed
view.

If you export an event log from Event Viewer additional "display
information" can be exported. This display information is stored in a
corresponding file named:

    LocaleMetaData\%FILENAME%_%LCID%.MTA

Where LCID is the "locale identifier"
[1](https://learn.microsoft.com/en-us/openspecs/windows_protocols/ms-lcid/a9eac961-e77d-41a6-90a5-ce1a8b0cdb9c).

## Location

    C:\Windows\system32\winevt\Logs

## See Also

* [Windows Event Log (evt)](windows_event_log_(evt).md)
* [Windows](windows.md)

## External Links

* [Mute Sysmon - Silence Sysmon via event manifest tampering](https://securityjosh.github.io/2020/04/23/Mute-Sysmon.html),
  by SecurityJosh, April 23, 2020

### File Format

* [EventLog Remoting Protocol Version 6.0 Specification](http://msdn.microsoft.com/en-us/library/cc231282(v=prot.10>).aspx)
  by [Microsoft](microsoft.md)
* [Simple BinXml Example](https://learn.microsoft.com/en-us/openspecs/windows_protocols/ms-even6/7cdd0c95-2181-4794-a094-55c78b389358),
  by [Microsoft](microsoft.md)
* [int for(ensic){blog;} - results tagged Evtx](http://computer.forensikblog.de/mt/mt-search.cgi?IncludeBlogs=3&tag=Evtx&limit=20),
  by Andreas Schuster
* [Introducing the Microsoft Vista Event Log File Format](http://www.dfrws.org/2007/proceedings/p65-schuster_pres.pdf),
  by Andreas Schuster, in 2007
* [Linking Event Messages and Resource DLLs](http://computer.forensikblog.de/en/2010/10/linking-event-messages-and-resource-dlls.html),
  by Andreas Schuster, in 2010
* [Windows XML Event Log (EVTX) format](https://github.com/libyal/libevtx/blob/main/documentation/Windows%20XML%20Event%20Log%20(EVTX).asciidoc),
  by the [libevtx project](libevtx.md)

### Event Identifiers

* [EventID.net](http://eventid.net/)

### Windows Vista/2008

* [Description of security events in Windows Vista and in Windows Server 2008](http://support.microsoft.com/kb/947226)

### Windows 7

* [Core OS Events in Windows 7, Part 1](https://learn.microsoft.com/en-us/)
* [Core Instrumentation Events in Windows 7, Part 2](https://learn.microsoft.com/en-us/archive/msdn-magazine/2009/october/core-instrumentation-events-in-windows-7-part-2)

## Tools

* [Evtx Parser](http://computer.forensikblog.de/files/evtx/Parse-Evtx-current.zip)
* [libevtx](libevtx.md)
* [log2timeline](log2timeline.md)
* [wevtutil](https://learn.microsoft.com/en-us/previous-versions/windows/it-pro/windows-server-2008-R2-and-2008/cc749339(v=ws.11))
* [LogParser](http://www.microsoft.com/en-us/download/details.aspx?id=24659)
* [python-evtx](http://www.williballenthin.com/evtx/)
* [winlast](https://github.com/pch3/winlast)
* [Event log explorer](https://eventlogxp.com/)
* [Event-Log Hunting tools collection by Renzon](https://twitter.com/r3nzsec/status/1463018324086988801)
