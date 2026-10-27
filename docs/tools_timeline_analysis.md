---
tags:
  - Timeline Analysis
  - Tools
---
Timeline analysis tooling for creating, exchanging, analyzing and visualizing timelines
from the timestamped artifacts found on a computer system. The tools below are grouped
according to the [categories of timeline analysis](timeline_analysis.md) described in
[Timeline analysis](timeline_analysis.md).

> **Warning:** The tools listed below are not necessarily forensic tooling in the sense of
> [Forensic tooling](forensic_tooling.md).

## Timeline creation

See also [Timeline creation](timeline_analysis.md#timeline-creation).

* [Plaso](plaso.md)

Plaso (Plaso Langar Að Safna Öllu), or *super timeline all the things*, is a
Python-based engine used by several tools for automatic creation of timelines. Plaso
default behavior is to create super timelines but it also supports creating more targeted
timelines. It parses file systems, [Windows Registry](windows_registry.md) data, log
files and application artifacts into a single correlated timeline, whose
output is then imported into [Timesketch](timesketch.md) for collaborative
analysis.

* [The Sleuth Kit](the_sleuth_kit.md)

The [body file](body_file.md) output of `fls` can be used as the input of the
[mactime](mactime.md) sorting program, which produces a chronologically sorted
[mactime](mactime.md) timeline of a file system.

* [fiwalk](fiwalk.md)

fiwalk is a batch forensics analysis program built on [The Sleuth Kit](the_sleuth_kit.md).
It walks a disk image and outputs a [Digital Forensics XML](digital_forensics_xml_schema.md)
record of every file with its MAC times; the companion `idifference.py`
([forensic disk differencing](forensic_disk_differencing.md)) compares two images of
the same disk and produces a *timeline of changes* between them.

* [Recon for Mac OS X](sumuri_llc.md)

RECON for Mac OS X is a commercial triage suite for [Mac OS X](mac_os_x.md) developed by
[SUMURI](sumuri_llc.md) that automatically finds, parses and unifies important
artifacts into a refined timeline; advertised features include advanced timeline
analysis and automatic chat timeline construction for Messages and Skype.

* [ExifTool](exiftool.md)

ExifTool is a general-purpose metadata extraction tool used to pull timestamped EXIF
metadata out of images; [log2timeline](log2timeline.md) used it in its `exif` input
module. It is also the common cross-check for timestamped image metadata produced
by tools such as [EXIF Hound](exif_hound.md).

* [Sticky Notes Parser](https://code.google.com/archive/p/winforensicaanalysis/downloads)

A Win32 command line tool that parses [Sticky Notes](sticky_notes.md)
(`stickynotes.snt`) files; its output can be a listing of the available notes, or in
CSV and [TLN](tln.md) format for inclusion in a timeline of system activity.

* [Browser History Examiner](https://www.foxtonforensics.com/browser-history-examiner/)

A browser history extraction tool - it is listed in the
[Firefox 3 history file format](mozilla_firefox_3_history_file_format.md) article
alongside [log2timeline](log2timeline.md) and [Plaso](plaso.md) - that extracts
visit histories with timestamps into a format suitable for timeline analysis.

* [graverobber (The Coroner's Toolkit)](https://en.wikipedia.org/wiki/The_Coroner%27s_Toolkit)

graverobber, a tool of [The Coroner's Toolkit](https://en.wikipedia.org/wiki/The_Coroner%27s_Toolkit)
(TCT), is the origin of the [body file](body_file.md) format, which was adopted by
[The Sleuth Kit](the_sleuth_kit.md). TCT was superseded by [The Sleuth Kit](the_sleuth_kit.md),
and graverobber's role in timeline creation was taken over by TSK's `fls`/`mactime` and
later by [Plaso](plaso.md). Discontinued.

* [log2timeline](log2timeline.md)

Log2timeline is an artifact timeline creation and analysis framework, with modular
input and output support for [body file](body_file.md), [TLN](tln.md),
[l2t CSV](l2t_csv.md) and more. Log2timeline has been superseded by
[Plaso](plaso.md) and is no longer maintained.

## Analyzing timelines

See also [Analyzing timelines](timeline_analysis.md#analyzing-timelines).

* [Timesketch](timesketch.md)

Timesketch is a tool for collaborative forensic timeline analysis. Using sketches you
and your collaborators can easily organize your timelines and analyze them all at the
same time. Add meaning to your raw data with rich annotations, comments, tags and stars.

* [logstash](https://www.elastic.co/logstash)

logstash is a tool for managing events and logs: it collects, parses and stores logs
for later use, and includes a web interface for searching and drilling into them. It
is listed under [timeline correlation](tools_network_forensics.md#timeline-correlation)
in the [network forensics tools](tools_network_forensics.md) article.

* [MailXaminer](mailxaminer.md)

MailXaminer is a commercial Windows-based e-mail and messaging data analysis tool
whose feature list includes timeline analysis of searches - chats, mails and more.

* [PALADIN](sumuri_llc.md)

PALADIN is a free, "live" Linux forensic toolkit from [SUMURI](sumuri_llc.md) that
bundles 100+ open source tools in toolboxes that include timeline analysis, log
analysis and [The Sleuth Kit](the_sleuth_kit.md).

* [EXIF Hound](exif_hound.md)

EXIF Hound is a free, open source desktop application for inspecting
[EXIF](exif.md) metadata in images and plotting GPS coordinates; it supports
reconstructing where and in what order photos were taken, and exports metadata as CSV
or JSON "for timelines and reports".

* [4n6time](4n6time.md)

4n6time, formerly "l2t_Review", was a free, cross-platform forensic tool for timeline
creation and review. It appears to be abandoned.

## Visualizing timelines

See also [Visualizing timelines](timeline_analysis.md#visualizing-timelines).

* [Zeitline](https://sourceforge.net/projects/zeitline/)

Zeitline is a forensic timeline editor, a desktop tool for reviewing, filtering and
annotating timelines. The project appears to be abandoned.

* [TimeFlow](https://github.com/FlowingMedia/TimeFlow/wiki/)

TimeFlow produces visual timelines for an investigation; its source is freely
available. The project appears to be abandoned.

* [Simile Timeline and Timeplot](https://github.com/simile-widgets/ancient-simile-widgets)

Simile provides browser-based widgets (timeline, timeplot) that sort and render
timeline data. The project has been archived.
