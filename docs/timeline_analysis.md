---
tags:
  - Papers
  - Research
  - Timeline Analysis
---
Timeline analysis is the process of collecting, correlating and ordering the date and time values
of artifacts found on a computer system into a single chronological record of its activity.

These date and time values comes from many sources:

* file system timestamps,
* [Windows Registry](windows_registry.md) keys,
* [event logs](windows_xml_event_log_(evtx).md),
* browser history,
* e-mail,
* application and system log files
* telemetry from supporting systems such as network equipment and proxies

Each source is parsed and normalized into one of the [timeline formats](#timeline-formats),
combined and sorted chronologically before it is examined to reconstruct what took place on the
system, and in which order it took place.

Timeline analysis is frequently used to describe a particular workflow, but at its core
it is a method: *ordering artifacts in time* and reading the resulting sequence.
Investigations are usually addressed by first building a *super timeline* - a single
timeline combining all the timestamped artifacts on the evidence - and then narrowing it
down; where the amount of material is too large, or the question too specific, a
*timeline is analyzed in a targeted manner* instead: the timeline is built from only
those artifacts that are relevant to a particular user, file, program or time frame.

More fundamentally, timeline analysis is **a matter of interpreting time** rather than
reading events: a timestamp is evidence of *when* something happened on a system, and on
its own it rarely proves *what* happened. Every conclusion drawn from a sequence of
entries - that a user logged in, that a program was executed, that a document was
opened - is a hypothesis, whose reliability grows the more independent sources
corroborate it.

The classic pitfalls are conflating a timestamp with the event it represents, ignoring
time zones and an unknown [system time](system_time.md), over-reading timestamps beyond
the [granularity of the file system](mac_times.md#time-resolution), or accepting tampered
timestamps ([timestomping](timestomp.md)) at face value. A single, isolated timestamp is
worth little; it is the pattern of *many* timestamps - across file systems, the registry,
log files and network evidence - that establishes the sequence of events.

## Timeline creation

Creating a timeline means identifying the timestamped artifacts on the evidence,
extracting them and normalizing their time, source and description into a common
[timeline format](#timeline-formats) such as [body file](body_file.md) or
[L2T CSV](l2t_csv.md). The work is done by purpose-built engines: [Plaso](plaso.md), for
example, parses file systems, the registry and a wide range of log and application
artifact formats into a single correlated timeline, while [mactime](mactime.md) from
[The Sleuth Kit](the_sleuth_kit.md) turns the [body file](body_file.md) of a file system
into a sorted timeline. Creation and analysis are normally kept apart: the timeline is
produced as a file - a *product* of the examination - and then examined with analysis
and visualization tools.

See also [Timeline creation tools](tools_timeline_analysis.md#timeline-creation).

## Timeline formats

A timeline is only as good as the format in which it is exchanged. Each format carries a
different set of fields (date/time, source, host, user, description), a different time
granularity and a known set of limitations - most commonly second-only resolution and no
indication of the time zone - that silently distort the interpretation if the
investigator does not know about them.

The timeline formats described in this wiki are:

* [body file](body_file.md) - pipe-separated "intermediate" timeline introduced by the
  grave-robber tool of The Coroner's Toolkit and adopted by [The Sleuth Kit](the_sleuth_kit.md);
  not sorted chronologically, but staged for post-processing with [mactime](mactime.md)
* [L2T CSV](l2t_csv.md) - the 17-field CSV introduced by [log2timeline](log2timeline.md),
  with the short and full description fields that visualization tools rely on
* [Mactime](mactime.md) - the chronologically sorted timeline output of [The Sleuth Kit](the_sleuth_kit.md)
* [TLN](tln.md) - the pipe-separated `Time|Source|Host|User|Description` format
  introduced by [Harlan Carvey](harlan_carvey.md), with the [l2tTLN](tln.md#variants)
  variant adding a time zone and a notes field

See also [Tools: Timeline analysis](tools_timeline_analysis.md).

## Analyzing timelines

Once a timeline has been created, the analysis means reading through it: filtering and
grouping entries by source, user or time of day, looking for the characteristic
signatures of log on, program execution, file operations and network connections, and
correlating the result with timelines from related systems - see for example the
[timeline correlation](tools_network_forensics.md#timeline-correlation) performed in
[network forensics](network_forensics.md). [Timesketch](timesketch.md) supports this
step with a collaborative, sketch-based workspace in which multiple investigators
organize, annotate, tag, star and comment on the same set of timelines.

See also [Timeline analysis tools](tools_timeline_analysis.md#analyzing-timelines).

## Interpreting timestamps

Before a timeline can be interpreted, the meaning of its timestamps must be
established. That means knowing *what* a value records - which of the [MAC(B) or
MACE](mac_times.md) values it is - *relative to which* [epoch](epoch.md), at *what
granularity* [the file system records](mac_times.md#time-resolution), and whether the
[system time](system_time.md) and time zone of the machine are known.

Equally important is being able to rule out deliberate manipulation:
[timestomping](timestomp.md) and other [anti-forensic
techniques](anti_forensic_techniques.md) can shift timestamps to misleading values,
while honest causes (time synchronization, time zone changes, daylight savings) can shift
them too. The rigorous way to deal with this is through model-based and hypothesis-based
approaches to the interpretation of timestamp evidence, including bounding the time of
an event between the values of multiple timestamps. Where the system time itself is in
question, the reference time can be established from independent sources, such as
estimating the boot time and uptime of a machine from [TCP
timestamps](tcp_timestamps.md).

## Visualizing timelines

Timelines in real cases contain thousands to millions of entries, and reading them as
text is not practical. Visualizations turn the timeline into a picture of its *density
and structure* - trends, clusters of activity, and at least as important the gaps of
inactivity between them - which is why visualization has been a central topic of
timeline analysis research; see the [Visualization](#visualization) section of the
bibliography below. Purpose-built [tools](tools_timeline_analysis.md#visualizing-timelines)
in this area are mostly discontinued, and current practice leans on the visualization
capabilities of [Timesketch](timesketch.md) and similar analysis tools.

## See also

* [Tools: Timeline analysis](tools_timeline_analysis.md)
* [epoch](epoch.md)
* [MAC(B) and MACE times](mac_times.md)
* [System time](system_time.md)
* [Timestomping](timestomp.md)
* [Anti-forensic techniques](anti_forensic_techniques.md)
* [Network forensics](network_forensics.md)
* [Digital evidence](digital_evidence.md) (temporal reconstruction)
* [Shell item](shell_item.md) (date and time values usable in timeline analysis)
* [Windows Update](windows_update.md) (reconstructing system timelines)
* [Zeitgeist](zeitgeist.md) (activity data consumed by [Plaso](plaso.md))
* [unpaired surrogates](unpaired_surrogates.md) (timeline tool rendering and export edge cases)
* [Concepts - Timeline Analysis](concepts.md#timeline-analysis)

## Bibliography

### Articles / Blogposts

* [Targeted timelines - Part I](http://blog.kiddaland.net/2013/02/targeted-timelines-part-i.html),
  by Kristinn Guðjónsson, February 22, 2013
* [Let's talk about time](https://osdfir.blogspot.com/2021/06/lets-talk-about-time.html),
  by Alexander Jäger, June 04, 2021
* [Pearls and pitfalls of timeline analysis](https://osdfir.blogspot.com/2021/10/pearls-and-pitfalls-of-timeline-analysis.html),
  by Joachim Metz, October 20, 2021

### Papers

* [Generating computer forensic supertimelines under Linux - A comprehensive guide for Windows-based
  disk
  images](https://www.forensicfocus.com/stable/wp-content/uploads/2012/08/generating-computer-forensic-supertimelines-under-linux-a-comprehensive-guide-for-windows-based-disk-images1.pdf),
  by R. Carbone, C. Bean, August 2012
* [Generating computer forensic supertimelines under Linux: A comprehensive guide for Windows-based
  disk images](https://apps.dtic.mil/dtic/tr/fulltext/u2/1003976.pdf),
  October 2011
* [Computer forensic timeline visualization tool](https://dfrws.org/presentation/computer-forensic-timeline-visualization-tool/),
  by J. Olsson, M. Boldt, ScienceDirect Digital Investigation, Volume 6,
  September 2009
* [Analysis of Time Information for Digital Investigation](https://ieeexplore.ieee.org/document/5331448),
  by Jewan Bang, BY Yoo, JS Kim, SJ Lee, NCM 2009, 5th International Joint
  Conference on INC, IMS, IDC, August 2009
* [A Model Based Approach to Timestamp Evidence Interpretation](https://www.igi-global.com/articles/details.asp?ID=33298),
  by S. Willassen, International Journal of Digital Crime and Forensics, 1:2,
  2009
* [Digital Evidence with an Emphasis on Time](https://www.diva-portal.org/smash/get/diva2:831086/FULLTEXT01.pdf),
  by Olsson, Jens Master's Thesis, Blekinge Institute of Technology, September
  2008.
* [The Use of File Timestamps in Digital Forensics](https://digifors.cs.up.ac.za/issa/2008/Proceedings/Full/43.pdf),
  by R. Koen, M. Olivier, ISSA 2008, Johannesburg, South Africa, July 2008
* [Methods for Enhancement of Timestamp Evidence in Digital Investigations](https://ntnuopen.ntnu.no/ntnu-xmlui/handle/11250/261472),
  by S. Willassen, PhD Dissertation, Norwegian University of Science and
  Technology, 2008
* [Finding Evidence of Antedating in Digital Investigations](https://ieeexplore.ieee.org/document/4529317),
  by S. Willassen, ARES 2008, Barcelona, Spain, March 2008
* Hypothesis Based Investigation of Digital Timestamp,
  by S. Willassen, January 2008
* Timestamp Evidence Correlation by model based clock hypothesis testing,
  by S. Willassen, January 2008
* An Improved Clock Model for Translating Timestamps,
  by F. Buchholz
* [A brief study of time](https://dfrws.org/sites/default/files/session-files/2007_USA_paper-a_brief_study_of_time.pdf),
  by F. Buchholz, B. Tjaden, Digital Investigation 2007:4S
* [The Rules of Time on NTFS File System](https://i.cs.hku.hk/~cisc/forensics/papers/RuleOfTime.pdf),
  by K. Chow, F. Law, M. Kwan, P. Lai, 2nd International Workshop on Systematic
  Approaches to Digital Forensic Engineering, Seattle, Washington, April 2007
* [A correlation method for establishing provenance of timestamps in digital evidence](https://dfrws.org/presentation/a-correlation-method-for-establishing-provenance-of-timestamps-in-digital-evidence/),
  by B. Schatz, G. Mohay, A. Clark, Digital Investigation 2006:3S
* Formalizing Event Time Bounding in Digital Investigation,
  by P. Gladyshev, A. Patel, International Journal of Digital Evidence, vol
  4:2, 2005
* Time and Date issues in forensic computing - a case study,
  by C. Boyd, P. Forster, Digital Investigation 2004:1
* Unification of relative time frames for digital forensics,
  by M.W. Stevens, Digital Investigation 2004:1
* [Dynamic Time &amp; Date Stamp Analysis](https://www.utica.edu/academic/institutes/ecii/publications/articles/A048B1E4-B921-1DA3-EB227EE7F61F2053.pdf),
  M. C. Weil, International Journal of Digital Evidence, vol 1:2, 2002

### Visualization

* ThemeRiver: In Search of Trends, Patterns, and Relationships,
  by Susan Havre, Beth Hetzler, and Lucy Nowell, Battelle Pacific Northwest
  Division, Richland, Washington, 1999
* [Visualizing gaps in time-based lists](https://well-formed-data.net/archives/26/visualizing-gaps-in-time-based-lists),
  by Moritz Stefaner, November 6, 2000

## External Links

* [Wikipedia: Computer forensics](https://en.wikipedia.org/wiki/Computer_forensics)
