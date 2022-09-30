---
tags:
  -  Timeline Analysis
---
log2timeline (or L2T) CSV is a timeline format introduced by
[log2timeline](log2timeline.md) tool.

## Format

The following information was copied from the [log2timeline project
wiki](http://code.google.com/p/log2timeline/wiki/l2t_csv) with
permission:

By default log2timeline uses the l2t_csv output format. It is a simple
CSV (comma separated) file with 17 fields.

The first line of the CSV file is a header, containing the name of each
field, followed by each timestamped entry. Each line in the CSV file
refers to one timestamped entry, which means that each timestamp object
may be expanded to several lines.

The header is:

    date,time,timezone,MACB,source,sourcetype,type,user,host,short,desc,version,filename,inode,notes,format,extra

The comma is not allowed as character in fields and is typically
replaced with a space

### More Detailed Description

A more detailed description of each of the fields and their meaning:

1.  <b>date</b>: The date of the event, in the format of "MM/DD/YYYY"
    (n.b this might get changed in a future version to YYYY-MM-DD, but
    for now this will stay this way).
2.  <b>time</b>: time of day, expressed in a 24h format, HH:MM:SS (in
    future versions this may change to include ms values in the format
    of HH:MM:SS.ms)
3.  <b>timezone</b>: The name of the timezone used as the output
    timezone, or the chosen timezone of the input file if no output
    timezone was chosen.
4.  <b>MACB</b>: MACB or legacy meaning of the fields, mostly for
    compatibility with the mactime format.
5.  <b>source</b>: Short name for the source. This may be something like
    LOG, WEBHIST, REG, etc. This field name should correspond to the
    type field in the TLN output format and describes the nature of the
    log format on a high level (all log files are marked as LOG, all
    registry as REG, etc.)
6.  <b>sourcetype</b>: More comprehensive description of the source.
    This field further describes the format, such as "Syslog" instead of
    simply "LOG", "NTUSER.DAT Registry" instead of "REG", etc.
7.  <b>type</b>: type of the timestamp itself, such as “Last Accessed”,
    “Last Written” or “Last modified”, etc.
8.  <b>user</b>: username associated with the entry, if one is
    available.
9.  <b>host</b>: hostname associated with the entry, if one is
    available.
10. <b>short</b>: short description of the entry, usually contains less
    text than the full description field. This is created to assist with
    tools that try to visualize the event. In those output the short
    description is used as the default text, and further information or
    the full description can be seen by either hovering over the text or
    clicking on further details about the event.
11. <b>desc</b>: description field, this is where most of the
    information is stored. This field is the full description of the
    field, the interpreted results or the content of the actual log
    line.
12. <b>version</b>: version number of the timestamp object. Current
    version is 2.
13. <b>filename</b>: filename with the full path of the filename that
    contained the entry. In most input modules this is the name of the
    logfile or file being parsed, but in some cases it is a value
    extracted from it, in the instance of \$MFT this field is populated
    as the name of the file in question, not the \$MFT itself.
14. <b>inode</b>: inode number of the file being parsed, or in the case
    of \$MFT parsing and possibly some other input modules the inode
    number of each file inside the \$MFT file.
15. <b>notes</b>: Some input modules insert additional information in
    the form of a note, which comes here. This might be some hints on
    analysis, indications that might be useful, etc. This field might
    also contain URL's that point to additional information, such as
    information about the meaning of events inside the EventLog, etc.
16. <b>format</b>: name of the input module that was used to parse the
    file. If this is a log2timeline input module that produced the
    output it should be of the format Log2t::input::NAME where name is
    the name of the module. However other tools that produce l2t_csv
    output may put their name here.
17. <b>extra</b>: additional information parsed is joined together and
    put here. This 'extra' field may contain various information that
    further describe the event. Some input modules contain additional
    information about events, such as further divide the event into
    source IP's, etc. These fields may not fit directly into any other
    field in the CSV file and are thus combined into this 'extra' field.

## Known issues

- date and time values are in second-only granularity and therefore
  limit the usefulness of the format for timelines with a vast amount of
  sub-second activity
  - Note that second-only granularity is known to affect MACB grouping
    behavior of certain tools, also see
    <https://github.com/sleuthkit/sleuthkit/issues/2015>
- timezone can be used for both the output and input time zone, it is
  strongly encouraged to only use it for the output time zone

## External Links

- [log2timeline project wiki:
  l2t_csv](http://code.google.com/p/log2timeline/wiki/l2t_csv)

