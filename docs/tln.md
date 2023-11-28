---
tags:
  -  Timeline Analysis
---
TLN is a timeline format (as far known) introduced in a [blog
post](https://windowsir.blogspot.com/2009/02/timeline-analysis-pt-iii.html)
by [Harlan Carvey](harlan_carvey.md).

He specifies the following 5 \| separated fields:

    Time|Source|Host|User|Description

Time - 32-bit POSIX (or Unix) epoch timestamp

<b>It is unclear if negative timestamps are supported or how values that
overflow the 32-bit should be represented.</b>

<b>Since the author has been, so far, unable provide the actual
representation this field it is assumed to be a (decimal) numeric string
of the number of seconds since Jan 1, 1970 00:00:00 (both positive and
negative) in an externally defined time zone. This would make it
equivalent to that of the (Linux) date command e.g.</b>

    date -u -d@0
    Thu Jan  1 00:00:00 UTC 1970

    date -u -d@$(( 1 << 31 ))
    Tue Jan 19 03:14:08 UTC 2038

    date -u -d@$(( -1 * ( 1 << 31 ) ))
    Fri Dec 13 20:45:52 UTC 1901

<b>Note that the 32-bit size of the value is only an artificial
limitation and modern versions of (Linux) date have support for signed
64-bit values.</b>

Source - fixed-length field for the source of the data (i.e., file
system, Registry, EVT/EVTX file, AV or application log file, etc.) and
may require a key or legend.

According to the author the field is approx 8 char in length.

Host - The host system, defined by IP or MAC address, NetBIOS or DNS
name, etc. (may also require a key or legend)

User - User, defined by user name, SID, email address, IM screenname,
etc. (may also require a key or legend)

Description - The description of what happened; this is where context
comes in...

In addition the Description field seems to be allowed to be overloaded
with ; separated values. An example from the same blog post:

    1123619888|EVT|PETER|S-1-5-18|Userenv/1517;EVENTLOG_WARNING_TYPE;PETER\Harlan

Where it looks like the separated fields in the Description are not
pre-defined.

## Variants

Known variants of TLN are:

- l2tTLN (log2timeline TLN); which extends the format with a TZ (time
  zone) and Notes field.

## Known issues

- it is unclear if \| (the pipe-character) can be used in the fields,
  currently it assumed that it is not
- date and time values do not indicate a time zone or if daylight
  savings applies
- date and time values are in second-only granularity and therefore
  limit the usefulness of the format for timelines with a vast amount of
  sub-second activity
- As far known there is no list of predefined common sources. The author
  indicates there is none but there might be an implicit one in the
  tools by the same author.

## External Links

- [TimeLine Analysis, pt
  III](https://windowsir.blogspot.com/2009/02/timeline-analysis-pt-iii.html),
  by [Harlan Carvey](harlan_carvey.md), February 28, 2009
- [Timeline Analysis...do we need a
  standard?](https://windowsir.blogspot.com/2010/02/timeline-analysisdo-we-need-standard.html),
  by [Harlan Carvey](harlan_carvey.md), February 08, 2010

