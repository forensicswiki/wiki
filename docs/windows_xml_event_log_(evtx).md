---
tags:
  - File Formats
  - Windows
  - XML
---
The Windows XML Event Log (EVTX) format was introduced in [Windows Vista](windows.md)
as a replacement for the [Windows Event Log (evt)](windows_event_log_(evt).md) format.

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

```text
LocaleMetaData\%FILENAME%_%LCID%.MTA
```

Where LCID is the [locale identifier](https://learn.microsoft.com/en-us/openspecs/windows_protocols/ms-lcid/).

## Location

```text
C:\Windows\system32\winevt\Logs
```

## See Also

* [Windows Event Log (evt)](windows_event_log_(evt).md)
* [Windows](windows.md)

## External Links

* [Mute Sysmon - Silence Sysmon via event manifest tampering](https://securityjosh.github.io/2020/04/23/Mute-Sysmon.html),
  by SecurityJosh, April 23, 2020

### File Format

* [EventLog Remoting Protocol Version 6.0 Specification](https://learn.microsoft.com/en-us/openspecs/windows_protocols/ms-even6/18000371-ae6d-45f7-95f3-249cbe2be39b),
  by [Microsoft](microsoft.md)
* [Simple BinXml Example](https://learn.microsoft.com/en-us/openspecs/windows_protocols/ms-even6/7cdd0c95-2181-4794-a094-55c78b389358),
  by [Microsoft](microsoft.md)
* [Introducing the Microsoft Vista Event Log File Format](https://www.sciencedirect.com/science/article/pii/S1742287607000424),
  by Andreas Schuster, in 2007
* [Windows XML Event Log (EVTX) format](https://github.com/libyal/libevtx/blob/main/documentation/Windows%20XML%20Event%20Log%20(EVTX).asciidoc),
  by the [libevtx project](libevtx.md)

### Windows Vista/2008

* [Description of security events in Windows Vista and in Windows Server 2008](https://mskb.pkisolutions.com/kb/947226)

### Windows 7

* [Core OS Events in Windows 7, Part 1](https://learn.microsoft.com/en-us/)
* [Core Instrumentation Events in Windows 7, Part 2](https://learn.microsoft.com/en-us/archive/msdn-magazine/2009/october/core-instrumentation-events-in-windows-7-part-2)

## Parsing considerations

Most EVTX parsers read the binary XML (BinXml) of the event records and
output the event data. They do not render the event message that Event
Viewer shows in its "general view". Keep the following in mind when
interpreting their output. See also [Common misconceptions about Windows
EventLogs](https://osdfir.blogspot.com/2021/10/common-misconceptions-about-windows.html).

### Event data versus event message

* The event message is not stored in the EVTX file. It is looked up in
  the message resource files (DLL and MUI files) of the event provider on
  the system that renders it, and it can differ between Windows versions
  and languages. Output of a parser that does not use these resources
  contains the event data, but not the message.
* An event is identified by the provider and the event identifier, not
  the event identifier alone. The Qualifiers and Version of the event can
  change how the event data should be interpreted.
* A message can contain parameter references (`%%N`), for example
  `%%1833`, that are resolved using the provider's parameter message
  file. Without that file the reference is output as-is.
* Not all event data is used in the message, and the message can contain
  information that is not in the event data.

### Conversion to XML, JSON or JSONL

Converting records to XML, JSON or JSONL keeps most of the event data,
and JSON(L) is convenient to query with tools such as jq or to ingest in
a SIEM. However:

* The XML produced is not always valid XML 1.0. Event data can contain
  characters that are not allowed in XML or that are not escaped.
* Data element names within EventData are not guaranteed to be unique.
  JSON objects cannot hold duplicate keys, so a converter has to rename
  them (the Rust evtx crate appends `_1`, `_2`, …), keep only one value
  or store them as a list. Check which behavior a tool uses before
  searching on a field name.
* Events without named data elements (for example events written through
  the legacy ReportEvent API) have positional values only, which are
  output as a list without field names.
* Data types can be flattened. For example binary data is output as a
  hexadecimal string and a SID or GUID as a string.
* EventData and UserData are structured differently; converters and
  queries that only handle EventData miss UserData events.

### Normalization to CSV or JSON with per-event maps

Tools such as EvtxECmd flatten each record into a fixed set of columns
(for example user name, remote host and executable) using per-event maps
that select fields from the event XML. This makes records from different
providers comparable in a single timeline. However:

* A map only extracts the fields its author selected. Other event data
  is only available in the raw payload column.
* Events for which no map exists are only available as raw payload.
* A map is keyed on provider, channel and event identifier. It can be
  wrong when the event layout differs between versions of the event or
  of Windows.
* The column names are the map author's interpretation of the data. The
  same column can hold different kinds of values for different events.

### Rule-based hunting

Chainsaw and Hayabusa match Sigma (and tool specific) rules against the
event data. Field names in rules have to match the field names produced
by the tool's parser, including renamed duplicate fields. A rule not
matching does not mean that the activity did not occur, for example when
the log was cleared, rolled over or the relevant audit policy was not
enabled.

### Corrupted and recovered records

Parsers differ in how they handle corrupted chunks and records. For
example the Rust evtx crate skips the remainder of a chunk after an
invalid record, while [libevtx](libevtx.md) can also recover records.
When a file is dirty or partially overwritten, compare record counts and
event record identifiers between tools.

## Tools

* [libevtx](libevtx.md)
* [evtx](https://github.com/omerbenamram/evtx), Rust parser and `evtx_dump` CLI (XML, JSON, JSONL output)
* [EvtxECmd](https://github.com/EricZimmerman/evtx), by Eric Zimmerman, normalizes events to CSV/JSON using per-event maps
* [Chainsaw](https://github.com/WithSecureOpenSource/chainsaw), hunts EVTX files with Sigma rules
* [Hayabusa](https://github.com/Yamato-Security/hayabusa), Sigma-based EVTX timeline and threat-hunting tool
* [EVTX parser](https://www.evtxparser.com/), browser-based EVTX viewer (the Rust evtx crate compiled to WebAssembly; files are parsed locally and not uploaded)
* [log2timeline](log2timeline.md)
* [wevtutil](https://learn.microsoft.com/en-us/previous-versions/windows/it-pro/windows-server-2008-R2-and-2008/cc749339(v=ws.11))
* [LogParser](https://www.microsoft.com/en-us/download/details.aspx?id=24659)
* [python-evtx](https://github.com/williballenthin/python-evtx)
* [winlast](https://github.com/pch3/winlast)
* [Event log explorer](https://eventlogxp.com/)
* [Event-Log Hunting tools collection by Renzon](https://twitter.com/r3nzsec/status/1463018324086988801)
