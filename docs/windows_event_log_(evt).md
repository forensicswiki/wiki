---
tags:
  -  File Formats
  -  Windows
  -  Binary
---
MS Windows 2000, XP and 2003 typically maintain three Event Log files:
Application, System, and Security. They are generally found in the
C:\Windows\system32\config directory. Server versions of the OS may
maintain additional Event Logs (DNS Server.evt, Directory Service.evt,
File Replication Service.evt) depending upon the functionality of the
server.

Note that Windows Vista and later use the [Windows XML Event Log
(evtx)](windows_xml_event_log_(evtx).md) format.

Each log file consists of a Header record and the Body. The body again
consists of Event records, the Cursor record and unused space. The body
could form a ring buffer, where the cursor record will mark the border
between the oldest and the newest event record. Unused space could be
empty, slack and padding.

## Header Record

The Header Record defined as
[ELF_LOGFILE_HEADER](http://msdn.microsoft.com/en-us/library/bb309024%28VS.85%29.aspx)
on MSDN consists of:

1.  uint32 length of record in bytes, fixed 0x30
2.  char magic\[4\], fixed 'LfLe' (for Event log file)
3.  uint32 unknown, fixed 0x0100 0x0000, possibly indicates version
4.  uint32 unknown, fixed 0x0100 0x0000, possibly indicates version
5.  uint32 offset of first event record
6.  uint32 offset of next event record
7.  uint32 number of next event record
8.  uint32 number of first event record
9.  uint32 filesize (see below)
10. uint32 flags (see below)
11. uint32 retention period in seconds
12. uint32 length of record in bytes (again), fixed 0x30

Offsets and record numbers are updated only during a file close
operation, that is if the DIRTY flag (see below) is unset. Consult the
cursor record in that case.

Filesize is updated only during some recovery operations.

### Flags

- 0x0001 DIRTY if set, flag is set after first first write after an open
  operation.
- 0x0002 WRAPPED is set, flag is set if the log wrapped around.
- 0x0004 FULL if set, flag is set if an event record could not be
  written because of size limitations and the retention policy in
  effect.
- 0x0008 PRIMARY if set, BACKUP if unset. This flag possibly depends on
  the origin of a log file, usage seems change between earlier (pre SP1)
  and later versions (SP4) of Windows 2000.

## Cursor Record

1.  uint32 length of record in bytes, fixed 0x28
2.  uint32 magic\[4\], fixed 0x11111111 0x22222222 0x33333333 0x44444444
3.  uint32 offset of first event record
4.  uint32 offset of next event record
5.  uint32 number of next event record
6.  uint32 number of first event record
7.  uint32 length of record in bytes, fixed 0x28

## Event Record

Details of the Event record can be found in Microsoft's MSDN library
under
[EVENTLOGRECORD](http://msdn.microsoft.com/library/default.asp?url=/library/en-us/eventlog/base/eventlogrecord_str.asp).

## Padding

If

- a log file has reached its configured size limit
- and the retention policy allows wrapping
- and the remaining size is larger than 0x38 but smaller than the event
  record to be written,

then

- the event log service writes the first part of the event record (to
  record offset 0x38)
- fills the remaining space with a padding of 0x0027
- continues to write the second part of the event record (starting at
  record offset 0x38) at the top of the body (immediately after the
  header, that is at file offset 0x30).

## Message Templates

When written to disk, EVT log records contain very little human-readable
context. Log entries are made human-readable at analysis time through
tools such as the event viewer, by combining pre-defined log templates
(stored in system DLLs and EXEs) with variable data stored in the EVT
file. The templates and variable data are combined with a call to
FormatMessage(), which means the templates look similar to printf()'s
format strings.

When event viewer (or other log viewing tools) displays log records, it
has to determine which DLLs store the message templates. This linking
information is stored in the registry, and is specific to each type of
log (System, Security, Application, etc). These entries ultimately point
out a list of DLLs which contain the message templates. Each log record
contains a relative virtual address (RVA) to reference the associated
message template. The lower 16 bits of this RVA is typically displayed
as the Message ID, but this alone generally isn't enough to uniquely
reference a message template.

All of this means that EVT files aren't really complete on their own.
The files which store the core meaning of the log entry are separate
from the logs themselves and this creates several analysis problems.
First of all, an attacker could modify DLLs or the registry in order to
change the meaning of logs without having to touch the EVT file at all.
Secondly, when software is uninstalled in the future, it could cause
some EVT records to lose their context. Finally, EVT files aren't
particularly portable to other systems, since some log records could
rely on message templates which don't exist on other systems. One must
be careful to keep these issues in mind when analyzing EVT logs.

## See Also

- [Windows XML Event Log
  (evtx)](windows_xml_event_log_(evtx).md)
- [Windows](windows.md)

## External Links

### File Format

- [Windows Event Log (EVT)
  format](http://code.google.com/p/libevt/downloads/detail?name=Windows%20Event%20Log%20%28EVT%29.pdf),
  by the [libevt project](libevt.md)

### Event identifiers

- [EventID.net](http://eventid.net/)

### Windows 2000

- [Correlation of Windows Process Tracking
  Events](http://www.eventreporter.com/common/en/securityreference/win-eventcorrelation-processtracking.php)

## Tools

- [GrokEVT](http://projects.sentinelchicken.org/grokevt) is a set of
  forensics scripts designed to make sense of EVT logs for
  investigations. Along with RegLookup, it is able to combine registry
  information and event log templates to place EVT data in context.
  (UN\*X platforms only.)
- [<File::ReadEVT>](http://www.cpan.org/modules/by-authors/id/H/HC/HCARVEY/)
  is a Perl module that parses event log files for the purpose of
  forensics.
- [Windows Eventlog
  Viewer](http://www.tzworks.net/prototype_page.php?proto_id=4) Free
  tool that can be run on Windows, Linux or Mac OS-X. Parses Windows XP,
  Vista and Windows 7 eventlogs.
- [evtwalk](http://www.tzworks.net/prototype_page.php?proto_id=25)
  Command line tool to pull events and generate reports (password
  changes, logons, clock changes, system start/stop, and credential
  changes) from Windows event logs.
- [libevt](libevt.md)
- [lfle.py](https://github.com/williballenthin/LfLe), by [Willi
  Ballenthin](willi_ballenthin.md)
- [evtkit - fix broken evt files](https://github.com/yarox24/evtkit)

