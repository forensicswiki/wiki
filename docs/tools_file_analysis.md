---
tags:
  - Analysis Techniques
  - Tools
---
File analysis tooling for examining what a file contains and does -
identifying file types from content, extracting and analyzing strings and
documents, parsing structured artifacts, and observing the behavior of
executables. The tools below are grouped according to the
[categories of analysis](file_analysis.md) described in
[File analysis](file_analysis.md). Related tool categories include
[Document metadata
extraction](document_metadata_extraction.md#tools) and [Logfile
analysis](logfile_analysis.md#tools).

> **Warning:** The tools listed below are not necessarily forensic tooling in the sense of
> [Forensic tooling](forensic_tooling.md).

## File format identification

See also [File Format Identification](file_format_identification.md).

* [libmagic](https://sourceforge.net/projects/libmagic)

Written in C. Rules in /usr/share/file/magic and compiled at runtime.
Powers the Unix "file" command, but you can also call the library
directly from a C program.

* [file](file.md)

The file command determines the file type of a given file, depending on
its contents and not on e.g. its extension or filename. In order to do
that, it uses a magic configuration file that identifies filetypes.

* [Hachoir](hachoir.md)

Python framework for binary file manipulation. Determines the file type
using file header/footer (hachoir-metadata --type), able to list strings
in Unicode (hachoir-grep), etc. Support more than 60 file formats.

* [PRONOM](https://www.nationalarchives.gov.uk/PRONOM/Default.aspx)

Project of the National Archives of the United Kingdom to develop a
registry of file types.

* [JHOVE](https://jhove.openpreservation.org/)

JSTOR/Harvard Object Validation Environment, a similar registry of file
formats started by JSTOR and Harvard. Attempts are now underway to merge
these two efforts in the [GDFR](https://www.gdfr.info/) and the
[UDFR](https://cdlib.org/cdlinfo/2012/07/03/unified-digital-format-registry-udfr-now-available/).

* [DROID](https://github.com/digital-preservation/droid)

Digital Record Object Identification, an "automatic file format
identification tool" developed by the UK National Archives. Written in
Java.

* [TrID - File Identifier](https://mark0.net/soft-trid-e.html)

Recognizes over 9,000 file formats with XML format definitions,
compiled to a single container. New file types can be added in an
automated way, simply scanning a group of files. Win32, Linux/x86 &
x86-64; closed source; free for non-commercial use.

* [Detect-it-Easy](https://github.com/horsicq/Detect-It-Easy)

File and format identification tool with ECMAScript (JS) format
definitions; reliably detects many weak/zero-magic formats by content
only. Supports YARA rules, looks inside many compression formats, has
extensive support of executable formats, disassembly that supports
dozens of silicones, a file visualizer, a string finder, entropy
analysis and a file extractor. Has a Telegram bot to send files to, and
is one of the VirusTotal tools for executables. The engine is a
separate project that can be easily reused. C++ and JS open source;
Windows x32/64, Linux x32/64, Mac x64 GUI and CLI.

* Forensic Innovations File Investigator TOOLS

Proprietary, but free trial available. Available as consumer
applications and OEM API. Identifies 3,000+ file types, using multiple
methods to maintain high accuracy. Extracts metadata for many of the
supported file types.

* [Stellent/Oracle Outside-In](https://www.oracle.com/content-management/webcenter-content/technologies/webcenter/outside-in-technology.html)

Proprietary but free demo.

* [Toolsley File Identifier](https://www.toolsley.com/file.html)

Free. Runs in the browser. HTML5/JS port of the UNIX "file" tool and
libmagic.

* Falstaff

Free, online. Based on machine learning techniques, uses multiple file
features and novel signatures computed from file format samples.
Identifications are linked to the [file formats
archive](http://fileformats.archiveteam.org/wiki/Main_Page) ontology.

* [Apache Tika](https://tika.apache.org/)

Free (Apache v2.0 License). The Apache Tika™ toolkit detects and
extracts metadata and text from over a thousand different file types.

* [Wikipedia: prevx](https://en.wikipedia.org/wiki/Prevx)

Web-based file analysis service (see the Wikipedia article).

## Content analysis

See also [Strings analysis](strings_analysis.md).

* [strings](strings.md)

Strings will print the strings of printable characters in files. It
allows choosing different charactersets (ASCII, UNICODE). It is a quick
way to browse through files/partitions/... in order to look for words,
filenames, keywords etc.

* [PDF Miner](https://www.unixuser.org/~euske/python/pdfminer/index.html)

"...suite of programs that aims to help analyzing text data from PDF
documents. It includes a PDF parser, a PDF renderer (though only
rendering text is supported for now), and a couple of nice tools to
extract texts. Unlike other PDF-related tools, it allows to obtain the
exact location of texts in a page, as well as other layout information
such as font size or font name, which could be useful for analyzing the
document. It also infers text running within a page by using clustering
technique."

* [Dstrings](dstrings.md)

Part of the [Live-Forensics](live-forensics.md) project: a command line
tool that searches for strings in a given file, able to compare the
output against a dictionary to either exclude dictionary terms from the
output or only output files that match the dictionary. Also able to
search for IP addresses and URLs/email addresses.

* [bless](bless.md)

Free hex editor for Linux. Efficient editing of large data files and
block devices, multilevel undo-redo, customizable data views, fast find
and replace, a data conversion table, and highlighting of selection
pattern matches in the file.

## Executable file analysis

See also [Executable](executable.md) and
[Analyzing program execution](analyzing_program_execution.md).

* [ldd](https://linux.die.net/man/1/ldd)

List dynamic dependencies of executable files.

* [Ghidra](ghidra.md)

Software reverse engineering (SRE) framework created and maintained by
the National Security Agency Research Directorate. The framework
includes a suite of full-featured software analysis tools that enable
users to analyze compiled code on Windows, Mac OS and Linux:
disassembly, decompilation, graphing, and scripting. Supports a wide
variety of processor instruction sets and executable formats, runs in
user-interactive and automated modes, and can be extended with Java or
Python plug-in components.

* [PEiD](peid.md)

GUI-based program that runs under Windows and identifies more than 600
different signatures in [portable
executable](portable_executable_format.md) files; supports custom plugins
via its plugin interface.

* [truss](https://docs.oracle.com/cd/E88353_01/html/E37839/truss-1.html)

Solaris tool used to trace the system/library calls (not user calls) and
signals made/received by a new or existing process. It sends the output
to stderr.

* [ltrace](https://linux.die.net/man/1/ltrace)

Library call tracer.

* [strace](https://sourceforge.net/projects/strace/)

System Call Tracer.

* [xtrace](https://sourceforge.net/projects/xtrace/)

eXtended trace utility, similar to strace, ptrace, truss, but with
extended functionality and unique features, such as dumping function
calls (dynamically or statically linked), dumping call stack and more.

* ktrace

Enables kernel process tracing on OpenBSD.

* [Valgrind](https://valgrind.org/)

Executes a program under emulation, performing analysis according to one
of the many plug-in modules as desired. You can write your own plug-in
module as desired.

* [DTrace](https://www.oracle.com/it-infrastructure/)

Comprehensive dynamic tracing framework for Solaris (also ported to
Mac OS X - XRays and FreeBSD). DTrace provides a powerful infrastructure
to permit analysis of the behavior of the operating system and user
programs.

## Code comparison

* [CodeSuite](codesuite.md)

CodeSuite by Software Analysis & Forensic Engineering comprises BitMatch,
CodeCross, CodeDiff, CodeMatch, and SourceDetective for comparing and
analyzing source code and object code to find copyright infringement and
trade secret theft. It can be used for free on small sets of code.

CodeSuite also includes FileCount and FileIsolate for counting file
attributes and quickly copying or deleting entire file trees. Both are
free utilities.

## Artifact parsing

See also [File formats](file_formats.md).

* [dumpster_dive.pl](https://jafat.sourceforge.net/files.html)

MS Windows Recycle Bin INFO2 parser.

* [cookie_cruncher.pl](https://jafat.sourceforge.net/files.html)

MS IE cookie file parser.

* [binplist](binplist.md)

Python-based parser for [binary property list
(plist)](property_list_(plist).md) files (macOS).

* [libagdb](libagdb.md)

Library and applications to read the [Windows SuperFetch
Format](windows_superfetch_format.md); the project currently only
provides documentation.

* [EXIF Hound](exif_hound.md)

Free, open source desktop application for inspecting [Exif](exif.md)
metadata in image files and plotting the GPS coordinates stored in that
metadata on a map. Local-first: parsing runs on the examiner's computer,
with no user account or telemetry.

* [Timestomp](timestomp.md)

Utility that deletes or modifies [timestamp-related
information](mac_times.md) on files (MACE values); useful for
understanding [anti-forensic
techniques](anti_forensic_techniques.md) that hide when a file was
modified.

* [analyzeMFT](analyzemft.md)

Parses the $MFT file system metadata of a [NTFS](new_technology_file_system_(ntfs).md)
file system and presents the results in multiple formats. Written in
Python 2 and no longer maintained; a Python 3 fork is also unmaintained.

## File sharing analysis

* [P2P Marshal](p2pmarshal.md)

Tools to discover and analyze peer-to-peer files for Windows.

## Email and structured file viewers

See also [Personal folder file (PAB,
PST, OST)](personal_folder_file_(pab,_pst,_ost).md) and [Extensible
Storage Engine (ESE) database file (EDB)
format](extensible_storage_engine_(ese)_database_file_(edb)_format.md).

* [DataHelp](datahelp.md)

Offers free viewers for [AOL PFC](aol_pfc.md), [EDB](extensible_storage_engine_(ese)_database_file_(edb)_format.md),
OST, [PST](personal_folder_file_(pab,_pst,_ost).md) and [MBOX](mbox.md)
email files.

* [FreeViewer](freeviewer.md)

Offers free viewers for MBOX, MSG and [Opera](opera.md) MBS email files,
plus a forensic analysis tool for [SQLite](sqlite.md) database files.

* [Aryson Outlook PST Repair](aryson_outlook_pst_repair.md)

Repairs, recovers and restores corrupt Outlook PST files; recovered
data can be saved as PST, EML, DBX, MBOX or MSG, preserving folder
hierarchy and integrity of the data.

* [SysInfoTools](sysinfotools_software.md)

Products include an NSF Merge Tool, PST and OST file viewers, a DBX
recovery tool, a DBX to PST converter, and SQL database, BKF and OST
recovery tools. (Also see its [data recovery
tools](tools_data_recovery.md).)

* [SysTools](systools.md)

Products include viewers for E01, BKF, OST, Outlook PST, Exchange EDB,
OLM, EML, SQL MDF and DXL files, the MailPro+ email viewer (14 desktop
email clients), an [NTFS log](new_technology_file_system_(ntfs).md) analyzer, and
PST/OST reporters. (Also see its [data recovery
tools](tools_data_recovery.md).)

* [Kernel Data Recovery](kerneldatarecovery.md)

Products include viewers for Outlook PST, Exchange EDB, OST, MBOX, OLM
and EML files, an Outlook PST Reporter that generates file analysis
reports (total item types, mail flow density by date or sender, user
interactions), and password recovery tools.

## Windows environments

See also [Cygwin](cygwin.md).

* [Cygwin](cygwin.md)

Linux like environment for Windows.

* [UnxUtils](https://unxutils.sourceforge.net/)

Common unix utilities compiled for a Windows environment.

* [GnuWin32](https://gnuwin32.sourceforge.net/)

Common GNU utilities compiled for a Windows Environment.
