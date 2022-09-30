---
tags:
  - No Category
---
log2timeline is designed as a framework for artifact timeline creation
and analysis. The main purpose is to provide a single tool to parse
various log files and artifacts found on suspect systems (and supporting
systems, such as network equipment) and produce a body file that can be
used to create a timeline, using tools such as mactime from TSK, for
forensic investigators.

The tool is written in Perl for Linux but has been tested using Mac OS X
(10.5.7 and 10.5.8). Parts of it should work natively in Windows as well
(with ActiveState Perl installed).

## Description

log2timeline takes a log file (or a directory) and parses it to produce
a body file that can be imported into other tools for timeline analysis.
The tool has both a modular based approach to the input file as well as
the output file. The default behavior of the current version is to
export the timeline in a body format readable by TSK's (The SleuthKit)
[mactime](http://wiki.sleuthkit.org/index.php?title=Body_file) (although
this can be easily changed). log2timeline is build as a series of
scripts, this one being the front-end, which uses other scripts to
actually parse the log files (called modules). The tool is build to be
easily extended for anyone that wants to create a new module.

The tool contains (current version of 0.51 nightly build (20102608))
three front-ends:

- **log2timeline** - The main front-end. A tool capable of parsing a
  single log file/directory pointed to the tool using a selected input
  module.
- **timescanner** - A recursive front-end capable of parsing a directory
  passed to the tool and recursively go through each and every file/dir
  and try to parse it with every or selected input modules (to provide
  an automatic method of creating a super timeline).
- **glog2timeline** - A simple GUI front-end, with similar capabilities
  as log2timeline (the main front-end)

## Currently Supported Input Modules

The currently supported input modules (as of version 0.51 nightly build
(20102608)) are:

- **apache2_access** - Parse the content of a Apache2 access log file
- **apache2_error** - Parse the content of a Apache2 error log file
- **chrome** - Parse the content of a Chrome history file
- **evt** - Parse the content of a [Windows 2k/XP/2k3 Event
  Log](windows_event_log_(evt).md)
- **evtx** - Parse the content of a [Windows XML Event Log
  (evtx)](windows_xml_event_log_(evtx).md) file
- **exif** - Extract metadata information from files using ExifTool
- **ff_bookmark** - Parse the content of a Firefox bookmark file
- **firefox2** - Parse the content of a Firefox 2 browser history
- **firefox3** - Parse the content of a Firefox 3 history file
- **iehistory** - Parse the content of an index.dat file containg IE
  history
- **iis** - Parse the content of a IIS W3C log file
- **isatxt** - Parse the content of a ISA text export log file
- **mactime** - Parse the content of a body file in the mactime format
- **mcafee** - Parse the content of a log file
- **opera** - Parse the content of an Opera's global history file
- **oxml** - Parse the content of an OpenXML document (Office 2007
  documents)
- **pcap** - Parse the content of a PCAP file
- **pdf** - Parse some of the available PDF document metadata
- **prefetch** - Parse the content of the Prefetch directory
- **recycler** - Parse the content of the recycle bin directory
- **restore** - Parse the content of the restore point directory
- **setupapi** - Parse the content of the SetupAPI log file in Windows
  XP
- **sol** - Parse the content of a .sol (LSO) or a Flash cookie file
- **squid** - Parse the content of a Squid access log (http_emulate off)
- **syslog** - Parse the content of a Linux Syslog log file
- **tln** - Parse the content of a body file in the TLN format
- **userassist** - Parses the NTUSER.DAT registry file
- **volatility** - Parse the content of a Volatility output files
  (psscan2, sockscan2, ...)
- **win_link** - Parse the content of a Windows shortcut file (or a link
  file)
- **wmiprov** - Parse the content of the wmiprov log file
- **xpfirewall** - Parse the content of a XP Firewall log

## Currently Supported Output Modules

The currently supported output modules (as of version 0.51 nightly build
(20102608)) are:

- **beedocs** - Output timeline using tab-delimited file to import into
  BeeDocs
- **cef** - Output timeline using the ArcSight Commen Event Format (CEF)
- **cftl** - Output timeline in a XML format that can be read by CFTL
- **csv** - Output timeline using CSV (Comma Separated Value) file
- **mactime** - Output timeline using mactime format
- **mactime_l** - Output timeline using legacy version of the mactime
  format (version 1.x and 2.x)
- **simile** - Output timeline in a XML format that can be read by a
  SIMILE widget
- **sqlite** - Output timeline into a SQLite database
- **tab** - Output timeline using TDV (Tab Delimited Value) file
- **tln** - Output timeline using H. Carvey's TLN format
- **tlnx** - Output timeline using H. Carvey's TLN format in XML

## Plaso - The next generation

Version 0.x Log2timeline has been extremely useful but it was written in
Perl and has performance limitations. A major effort to re-write it in
Python, named [plaso](plaso.md) is underway and alpha releases
have been released.

For version 1.x the [plaso](plaso.md) engine has been created
and front-ends have been written.

## See Also

- [plaso](plaso.md)

## External Links

- [log2timeline web site](http://log2timeline.net)
- [plaso web site](http://plaso.kiddaland.net)
- [SANS GCFA Gold paper about the
  tool](http://www.sans.org/reading_room/whitepapers/logging/mastering-super-timeline-log2timeline_33438)
- [A quick run on how to create a super
  timeline](http://blogs.sans.org/computer-forensics/2010/03/19/digital-forensic-sifting-super-timeline-analysis-and-creation/)
- [Blog posts about the tool](http://blog.kiddaland.net/?s=log2timeline)
- [Part 1 of the SANS Forensic blog post about the
  tool](https://blogs.sans.org/computer-forensics/2009/08/13/artifact-timeline-creation-and-analysis-tool-release-log2timeline/)
- [Part 2 of the SANS forensic blog post about the
  tool](https://blogs.sans.org/computer-forensics/2009/08/14/artifact-timeline-creation-and-analysis-part-2/)