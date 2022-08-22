The Windows XML Event Log (EVTX) format was introduces in [Windows
Vista](Windows "wikilink") as a replacement for the [Windows Event Log
(EVT)](Windows_Event_Log_(EVT) "wikilink") format.

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
[1](http://msdn.microsoft.com/en-us/goglobal/bb964664.aspx).

## Location

    C:\Windows\system32\winevt\Logs

## See Also

- [Windows Event Log (EVT)](Windows_Event_Log_(EVT) "wikilink")
- [Windows](Windows "wikilink")

## External Links

- [Mute Sysmon - Silence Sysmon via event manifest
  tampering](https://securityjosh.github.io/2020/04/23/Mute-Sysmon.html),
  by SecurityJosh, April 23, 2020

### File Format

- \[<http://msdn.microsoft.com/en-us/library/cc231282(v=prot.10>).aspx
  EventLog Remoting Protocol Version 6.0 Specification\], by
  [Microsoft](Microsoft "wikilink")
- [Simple BinXml
  Example](http://msdn.microsoft.com/en-us/library/cc231354.aspx), by
  [Microsoft](Microsoft "wikilink")
- [int for(ensic){blog;} - results tagged
  Evtx](http://computer.forensikblog.de/mt/mt-search.cgi?IncludeBlogs=3&tag=Evtx&limit=20),
  by [Andreas Schuster](Andreas_Schuster "wikilink")
- [Introducing the Microsoft Vista Event Log File
  Format](http://www.dfrws.org/2007/proceedings/p65-schuster_pres.pdf),
  by [Andreas Schuster](Andreas_Schuster "wikilink"), in 2007
- [Linking Event Messages and Resource
  DLLs](http://computer.forensikblog.de/en/2010/10/linking-event-messages-and-resource-dlls.html),
  by [Andreas Schuster](Andreas_Schuster "wikilink"), in 2010
- [Windows XML Event Log (EVTX)
  format](https://googledrive.com/host/0B3fBvzttpiiSRnQ0SExzX3JjdFE/Windows%20XML%20Event%20Log%20(EVTX).pdf),
  by the [libevtx project](libevtx "wikilink")

### Event Identifiers

- [EventID.net](http://eventid.net/)

### Windows Vista/2008

- [Description of security events in Windows Vista and in Windows Server
  2008](http://support.microsoft.com/kb/947226)

### Windows 7

- [Core OS Events in Windows 7, Part
  1](http://msdn.microsoft.com/en-us/magazine/ee412263.aspx)
- [Core Instrumentation Events in Windows 7, Part
  2](http://msdn.microsoft.com/en-us/magazine/ee358703.aspx)

## Tools

- [Evtx
  Parser](http://computer.forensikblog.de/files/evtx/Parse-Evtx-current.zip)
- [libevtx](libevtx "wikilink")
- [log2timeline](log2timeline "wikilink")
- [wevtutil](http://technet.microsoft.com/en-us/library/cc749339.aspx)
- [LogParser](http://www.microsoft.com/en-us/download/details.aspx?id=24659)
- [python-evtx](http://www.williballenthin.com/evtx/)
- [winlast](https://github.com/pch3/winlast)
- [Event log explorer](https://eventlogxp.com/)
- [Event-Log Hunting tools collection by
  Renzon](https://twitter.com/r3nzsec/status/1463018324086988801)

[Category:File Formats](Category:File_Formats "wikilink")