---
tags:
  - No Category
---
## Aftertime

**Aftertime** is a Java software application that can be used to create
[time lines](timeline_analysis_bibliography.md) for forensic
investigators. Aftertime is based on [Snorkel](snorkel.md) to
provide access to a large number of image file formats, partition
schemes, file systems and file formats. Aftertime not only uses time
information contained in the file system but also extracts time
information from file contents, e.g. event logs, internet history,
e-mail and more. The winners of the [DFRWS](dfrws.md) [2009
Forensic Challenge](http://www.dfrws.org/2009/challenge/index.shtml)
used Aftertime to create the timeline.

## Features

With Aftertime it is possible to set the time zone per project, per
image, per scanner or change the time zone displayed. The file types
supported are summarized below.

|                  |                                                                                                                               |
|------------------|-------------------------------------------------------------------------------------------------------------------------------|
| E-mail           | [Mbox](mbox.md)                                                                                                       |
| Files            | [Shortcuts](lnk.md)                                                                                                   |
|                  | [MAC-times](mac_times.md)                                                                                             |
| Internet history | [Internet Explorer cookies](internet_explorer.md)                                                                     |
|                  | [Internet Explorer history](internet_explorer_history_file_format.md)                                                 |
|                  | [Safari history](apple_safari_history_file_format.md)                                                                 |
|                  | [Safari cookies](safari.md)                                                                                           |
|                  | [Opera cookies](opera.md)                                                                                             |
|                  | [Mozilla/Firefox cookies](firefox.md)                                                                                 |
|                  | [Mozilla](mozilla_firefox_history_file_format.md)/[Firefox](Mozilla_Firefox_3_History_File_Format "wikilink") history |
| Logs             | [MSN](msn.md)                                                                                                         |
|                  | WTMP                                                                                                                          |
|                  | Console kit                                                                                                                   |
|                  | Zone alarm                                                                                                                    |
|                  | Gator                                                                                                                         |
|                  | setupapi.log                                                                                                                  |
|                  | WBEM                                                                                                                          |
| Multimedia       | [Exif](exif.md)                                                                                                       |
| Operating System | [Windows Event log](evt.md)                                                                                           |
|                  | [Windows Prefetch](prefetch.md)                                                                                       |
|                  | Linux / Macintosh logs                                                                                                        |
|                  | [Windows Registry](windows_registry.md)                                                                               |
|                  | Windows Shadow-files                                                                                                          |

## Examples of use

Aftertime is used in a wide variety of cases:

- Was a person using this system at a specific time (alibi)?
- Are there traces of malicious activity at a given time?
- Are there any traces of other activity while this file was downloaded?
- When was this letter written?

Aftertime has two different views on the data. The first display is a
graphical view, where events are presented in a histogram. It is
possible to display the events in a logarithmic scale to not overlook
events that are only present a limited number of times. The second
display is a list of events with the details of each event presented by
highlighting the event.

## Screenshots

<img src="Aftertime1_large.png" title="Aftertime1_large.png" width="200"
alt="Aftertime1_large.png" />
<img src="Aftertime2_large.png" title="Aftertime2_large.png" width="200"
alt="Aftertime2_large.png" />
<img src="Aftertime3_large.png" title="Aftertime3_large.png" width="200"
alt="Aftertime3_large.png" />

## Links

[Aftertime website](http://www.holmes.nl/NFIlabs/Aftertime/index.html)