---
tags:
  -  Tools
  -  Opensource
---
## About

Barnyard2 is an open source interpreter for Snort unified2 binary output
files. Its primary use is allowing Snort to write to disk in an
efficient manner and leaving the task of parsing binary data into
various formats to a separate process that will not cause Snort to miss
network traffic.

Barnyard2 has 3 modes of operation:

` 1. batch (or one-shot),`
` 2. continual, and`
` 3. continual w/ bookmark.`

In batch (or one-shot) mode, barnyard2 will process the explicitly
specified file(s) and exit.

In continual mode, barnyard2 will start with a location to look and a
specified file pattern and continue to process new data (and new spool
files) as they appear.

Continual mode w/ bookmarking will also use a checkpoint file (or waldo
file in the snort world) to track where it is. In the event the
barnyard2 process ends while a waldo file is in use, barnyard2 will
resume processing at the last entry as listed in the waldo file.

The "-f", "-w", and "-o" options are used to determine which mode
barnyard2 will run in. It is legal for both the "-f" and "-w" options to
be used on the command line at the same time, however any data that
exists in the waldo file will override the command line data from the
"-f" and "-d" options. See the command directives section below for more
detail.

Barnyard2 processing is controlled by two main types of directives:
input processors and output plugins. The input processors read
information in from a specific format ( currently the spo_unified2
output module of Snort ) and output them in one of several ways.

## History

Barnyard is a critical tool for the parsing of Snort's unified binary
files, processing and on-forwarding to a variety of output plugins.
Unfortunately it has not seen an updated in over 4 years and is not
going to be maintained by the original developers. With the new version
of the unified format (ie. unified2) arriving we need something to
bridge this gap. To quote directly from the Snort FAQ:

- "Barnyard is an output system for Snort. Snort creates a special
  binary output format called unified. Barnyard reads this file, and
  then resends the data to a database backend. Unlike the database
  output plug-in, Barnyard is aware of a failure to send the alert to
  the database, and it stops sending alerts. It is also aware when the
  database can accept connections again and will start sending the
  alerts again."

The SXL team love barnyard. So much so that we want it to stay and have
been tinkering around with the code to give it a breath of new life.
Here is what we have achieved to far for this reinvigorated code base:
Parsing of the new unified2 log files.

- Maintaining majority of the command syntax of barnyard.
- Addressed all associated bug reports and feature requests arising
  since barnyard-0.2.0.
- Completely rewritten code based on the GPLv2 Snort making it entirely
  GPLv2.

## Sources

- [Github About page](https://github.com/firnsy/barnyard2/)
- [securixlive.com](https://firnsy.com/)