---
tags:
  -  Windows
---
**Jump Lists** are a feature found in Windows 7.

## Jump Lists

Jump Lists are a new Windows 7 Taskbar feature that gives the user quick
access to recently accessed application files and actions.

Jump Lists come in multiple flavors:

* automatic (autodest, or \*.automaticDestinations-ms) files
* custom (custdest, or \*.customDestinations-ms) files
* Explorer StartPage2 ProgramsCache Registry values

### AutomaticDestinations

The AutomaticDestinations Jump List files are located in the user
profile path:

Path:
C:\Users\\%USERNAME%\AppData\Roaming\Microsoft\Windows\Recent\AutomaticDestinations

Files: \*.automaticDestinations-ms

#### Structure

The AutomaticDestinations Jump List files are [OLE Compound
Files](ole_compound_file.md) containing multiple streams of
which:

* hexadecimal numbered, e.g. "1a"
* DestList

Each of the hexadecimal numbered streams contains data similar of that
of a [Windows Shortcut (lnk)](lnk.md). One could extract all the
streams and analyze them individually with a LNK parser.

The "DestList" stream acts as a most recently/frequently used (MRU/MFU)
list. This stream consists of a 32-byte header, followed by the various
structures that correspond to each of the individual numbered streams.
Each of these structures is 114 bytes in size, followed by a variable
length Unicode string. The first 114 bytes of the structure contains the
following information at the corresponding offsets:

| Offset | Size     | Description                                                                                                     |
|--------|----------|-----------------------------------------------------------------------------------------------------------------|
| 0x48   | 16 bytes | NetBIOS name of the system; padded with zeros to 16 bytes                                                       |
| 0x58   | 8 bytes  | Stream number; corresponds to the numbered stream within the jump list                                          |
| 0x64   | 8 bytes  | Last modification time, contains a [FILETIME](http://msdn2.microsoft.com/en-us/library/ms724284.aspx) structure |
| 0x70   | 2 bytes  | Path string size, the number of characters (UTF-16 words) of the path string                                    |
| 0x72   | ...      | Path string                                                                                                     |
|        |          |                                                                                                                 |

### CustomDestinations

The CustomDestinations Jump List files are located in the user profile
path:

Path:
C:\Users\\%USERNAME%\AppData\Roaming\Microsoft\Windows\Recent\CustomDestinations

Files: \*.customDestinations-ms

#### Structure

CustomDestinations Jump List files reportedly follow a structure of sequential
[MS-SHLLINK](https://learn.microsoft.com/en-us/openspecs/windows_protocols/ms-sh llink/16cb4ca1-9339-4d0c-a68d-bf1d6cc0f943)
binary format segments.

## See also

* [List of Jump List IDs](list_of_jump_list_ids.md)
* [OLE Compound File](ole_compound_file.md)
* [Windows](windows.md)

## External Links

* [Windows 7 Goodies in C++: Jump Lists](https://www.codeproject.com/Articles/36561/Windows-7-Goodies-in-C-Jump-Lists),
  by Michael Dunn, May 19, 2009
* [Jump Lists in Windows 7 and Possible Forensic Implementations](http://mikeahrendt.blogspot.ch/2011/04/jump-lists-in-windows-7-and-possible.html),
  by Mike Ahrendt, April 3, 2011
* [The Forensic Value of the Windows 7 Jump List](http://www.alexbarnett.com/jumplistforensics.pdf),
  by Alexander G Barnett, April 18, 2011
* [Forensic Examination of Windows 7 Jump Lists](https://www.slideshare.net/ctin/windows-7-forensics-jump-listsrv3public),
  by Troy Larson, June 6, 2011
* [Jump List Analysis](http://windowsir.blogspot.ch/2011/08/jump-list-analysis.html),
  by [Harlan Carvey](harlan_carvey.md), August 17, 2011
* [Jump List Analysis, pt II](http://windowsir.blogspot.ch/2011/08/jump-list-analysis-pt-ii.html),
  by [Harlan Carvey](harlan_carvey.md), August 24, 2011
* [Jump List Analysis](http://windowsir.blogspot.ch/2011/12/jump-list-analysis.html),
  by [Harlan Carvey](harlan_carvey.md), December 28, 2011
* [Forensic Analysis of Windows 7 Jump Lists](https://www.forensicfocus.com/articles/forensic-analysis-of-windows-7-jump-lists/),
  by Rob Lyness, October 2012
* [Jump lists format](https://github.com/libyal/dtformats/blob/main/documentation/Jump%20lists%20format.asciidoc),
  by the [libyal project](libyal.md), July 2014
* [Jump lists in depth (includes changes from Windows 10)](https://binaryforay.blogspot.com/2016/02/jump-lists-in-depth-understand-format.html),
  by [Eric Zimmerman](eric_zimmerman.md), Feb 2016

## Tools

* [Belkasoft Evidence Center](belkasoft_evidence_center.md). One
  of functions of this tool is search (including carving) and analysis
  of jumplists. A wide list of applications is supported (Jump list
  IDs).
* TZWorks LLC: Windows Jump List Parser (jmp). Also has a
  tool that can parse both the custom and automatic Destinations type
  files. For automaticDestinations it associates the MRU/MFU metadata
  with that of the SHLLINK metadata. There are versions of the tool that
  can run in Windows, Linux or Mac OS-X.
* [Woanware: JumpLister](https://github.com/woanware). Tool to view
  the information within the numbered streams of each autodest file.
* [plaso](plaso.md)
* [JumpList](https://github.com/EricZimmerman/JumpList). Parser written
  in C# with support thru Windows 10 jump lists
* [JLECmd](https://github.com/EricZimmerman/JLECmd). Command line tool
  using the above parser

