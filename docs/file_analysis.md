---
tags:
  - Analysis Techniques
---
File analysis is the process of examining the contents of files on a
storage medium, as distinct from the analysis of the file system that
organizes them. It is an important part of
[computer forensics](computer_forensics.md), and spans the whole spectrum
from determining what a file actually is, via
[file format identification](file_format_identification.md), to extracting
and interpreting its content, to understanding the behavior of
[executable](executable.md) files, to the analysis of files shared over
peer-to-peer networks.

The term "file analysis" is frequently used to mean file format
identification or simple string searching, but it really covers the whole
range of techniques for examining what a file contains and what a program
contained in a file does.

More fundamentally, file analysis is **a process of inference**: the
investigator reconstructs the origin, content, and use of a file from its
observable features - the strings it contains, the structures it follows,
the calls it makes when it runs. Every recovered observation is therefore
a hypothesis, whose reliability grows the more independent observed
features corroborate it.

## File format identification

Determining the actual type of a file from its content - magic numbers,
headers and footers, internal structure - rather than from the name or
extension it carries, which its creator (or an adversary) supplied. This
is the foundation for all further analysis of an unknown file, and must
work even when the file system metadata is missing or unreliable.

See also [File Format Identification](file_format_identification.md) and
[File format identification
tools](tools_file_analysis.md#file-format-identification).

## Content analysis

Extracting meaningful content from a file: printable strings in text or
binary data, text and layout information inside documents, and embedded
or hidden data. Content analysis works on files of known or unknown
format and is often the first pass over a suspicious file.

See also [Strings analysis](strings_analysis.md) and [File analysis
tools: content
analysis](tools_file_analysis.md#content-analysis).

## Executable file analysis

Analysis of [executable](executable.md) files, both statically (headers,
formats, dependencies) and dynamically (tracing the system calls, library
calls, and other behavior a process makes when it runs). These same
techniques underpin [malware analysis](malware_analysis.md), where the
goal is to understand what a malicious program does.

See also [Portable Executable
format](portable_executable_format.md),
[Analyzing program execution](analyzing_program_execution.md) and [File
analysis tools: executable file
analysis](tools_file_analysis.md#executable-file-analysis).

## Code comparison

Comparing source code and object code to measure similarity, used to
detect copyright infringement and trade secret theft, and also of use in
attributing related code to a common origin.

See also [CodeSuite](codesuite.md).

## Artifact parsing

Parsing structured artifacts produced by applications - Recycle Bin
entries, browser cookies, mail, office documents - each in its own
documented or ad-hoc format, which often carry user data and traces of
activity even when the application itself is no longer in use.

See also [File formats](file_formats.md), [Residual data in document
files](residual_data_in_document_files.md), [Document metadata
extraction](document_metadata_extraction.md) and [Logfile
analysis](logfile_analysis.md).

## File sharing analysis

Examining the files and traces left by peer-to-peer file sharing
applications, including the files shared on disk and the metadata the
application records about them.

See also [P2P Marshal](p2pmarshal.md).

## Email and structured file viewers

Examining the files of structured stores used by mail and database
applications - [PST](personal_folder_file_(pab,_pst,_ost).md),
[EDB](extensible_storage_engine_(ese)_database_file_(edb)_format.md), OLM,
[MBOX](mbox.md), MSG - with dedicated viewers, converters and repair
tools; often the only way in when the application's own mailbox file is
corrupted.

See also [Email and structured file viewer
tools](tools_file_analysis.md#email-and-structured-file-viewers).

## Windows environments

Because so much evidence comes from Windows systems, Unix-like analysis
tools are frequently run under an emulated Unix environment on Windows.

See also [Cygwin](cygwin.md) and [File analysis tools: Windows
environments](tools_file_analysis.md#windows-environments).

## See also

* [Tools: File analysis](tools_file_analysis.md)
* [File Format Identification](file_format_identification.md)
* [File formats](file_formats.md)
* [Document metadata extraction](document_metadata_extraction.md)
* [Logfile analysis](logfile_analysis.md)
* [Strings analysis](strings_analysis.md)
* [Malware analysis](malware_analysis.md)
* [Executable](executable.md)
* [Analyzing program execution](analyzing_program_execution.md)
* [P2P Marshal](p2pmarshal.md)
* [Open Computer Forensics Architecture](open_computer_forensics_architecture.md)

## External Links

* [Wikipedia: File (data)](https://en.wikipedia.org/wiki/File_(data))
* [Wikipedia: prevx](https://en.wikipedia.org/wiki/Prevx)
