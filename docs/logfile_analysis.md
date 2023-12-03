---
tags:
  - Analysis
---
Log files are used to maintain a record of activities, e.g. activities
of the operating system, certain applications, etc.

Log files come in various formats, in general these formats can be
divided in the following categories:

- Binary formats
- Text-based formats
- in-database

## Binary formats

- [Windows Event Log (evt)](windows_event_log_(evt).md)
- [Windows XML Event Log (evtx)](windows_xml_event_log_(evtx).md)

## Text-based formats

- [Apache HTTP Server access log format](http://httpd.apache.org/docs/1.3/logs.html#accesslog)

## Tools

### Windows

[Log Parser 2.2](https://www.microsoft.com/en-us/download/details.aspx?id=24659)

From Microsoft, claims to parse a variety of log files, including XML
and CSV, as well as Windows Event Log, Registry, and Active Directory

Also see: Microsoft Log Parser Toolkit, by Gabriele Giuseppini, Mark
Burnett, ISBN: 1-93226-652-6

[Logpresso Mini](https://github.com/logpresso/community)

From Logpresso, claims to parse a variety of log files, including CSV,
JSON, XML, CEF, LEEF, and WELF, as well as Windows Event Log, Registry

### Web Logfile Analytics

Web logfile analytics software can process a log file and print a
report. Normally this software is used by organizations that host the
website. It can also be used for analysis of webserver logfiles.

[phpMyVisites](http://www.phpmyvisites.us/)

New "clicks heatmap" shows where people are clicking on your website;
depends on JavaScript. (on the other hand, doesn't need access to your
logfiles)

[AWStats](https://awstats.sourceforge.io/)

*"Free powerful and featureful tool that generates advanced web,
streaming, ftp or mail server statistics, graphically."*

[JasperReports](https://community.jaspersoft.com/)

Java reporting tool.

[Open Web Analytics](http://wiki.openwebanalytics.com/index.php?title=Main_Page)

*"An open source web analytics framework written in PHP."*

[Breadboard BI Web Analytics](https://sourceforge.net/projects/web-analytics/)

*"Uses open source tools to collect and distribute web analytics data."*
