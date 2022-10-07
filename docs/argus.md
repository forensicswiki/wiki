---
tags:
  -  Network Forensics
  -  Tools
  -  Linux
  -  Windows
  -  MacOS
  -  FreeBSD
  -  OpenBSD
  -  NetBSD
  -  Opensource Software
---
## Overview

**argus** is a network flow monitor that is used to establish network
activity audits. The audits are the basis of Network Forensics for many
universities and corporations, providing data mining for historical
network activity. Many sites use contemporary IDS technology like snort
and/or Bro to generate events and alarms, and then use the Argus network
audit data to provide context for those alarms to decide if the alarms
are real problems. In many DIY efforts, snort, Bro and argus run on the
same high performance device. The audit data that Argus generates is
great for network forensics, non-repudiation, network asset and service
inventory, behavioral baselining of server and client relationships,
detecting very slow scans, and supporting Zero day events. The network
transaction audit data that Argus generates has also been used for a
wide range of other tasks including Network Billing and Accounting,
Operations Management and Performance Analysis.

Argus uses libpcap and it has been ported to virtually every
[Unix](unix.md) platform, OpenWRT and on
[Win32](windows.md) using Cygwin.

## Argus/Ra 3.0.8 Installation Instructions

The Argus/Ra packages installed when using apt-get install are the old
2.0.6 versions, which may have problems with filter-expressions.

In order to build Argus/Ra 3.0.8 on your UNIX machine follow these
commands/steps:

- sudo apt-get install libpcap0.8 libpcap0.8-dev flex bison rrdtool
- wget <http://qosient.com/argus/src/argus-3.0.8.tar.gz>
- tar -xzvf argus-3.0.8.tar.gz
- cd argus-3.0.8
- ./configure
- make && make install
- cd ..
- wget <http://qosient.com/argus/src/argus-clients-3.0.8.tar.gz>
- tar -xzvf argus-clients-3.0.8.tar.gz
- cd argus-clients-3.0.8
- ./configure
- make && make install
- the ./argus and ./ra programs can be run from the “bin” directories
  within the argus-3.0.8 and argus-clients-3.0.8 directories,
  respectively

**NOTE:** If you already have a different version of argus/ra installed
(e.g., if you installed v2.0.6 using apt-get install), you’ll likely
need to rename/remove the “/etc/ra.conf” file or else you’ll get a
syntax error when trying to run ra. I just renamed it using the
following command (to keep a backup just in case):

- cd /etc/
- mv ra.conf ra.conf.bak

## Usage Instructions

Argus is set up as a client server relationship. Running the argus
command runs the server. It will retrieve that packets from the network
interface. Then argus assembles this information into binary data. Thus
it is not human readable when just running the argus command. One needs
an argus client in order to analyze it.

There are a few clients for argus, but the most common is ra. It reads
the output steam and prints the binary records to stdout in ASCII. Then
this information can be used for incident analysis and intrusion
research

A typical use for argus would be to run it as a daemon and have it write
the reports to an output file:

`   argus -d -e ‘hostname‘ -w output-file`

Argus supports filtering. One can specify to include or exclude certain
ports in the report. Below is an example of filtering out ICMP traffic:

`   argus -w output-file - ip and not icmp`

When using ra to get valuable data out, one can filter the argus data
even further. Below is an example of reporting only the TCP
transactions:

`   ra -r argus.data - tcp`

## External Links

- [Argus website](http://qosient.com/argus)
- [Argus Wiki](http://nsmwiki.org/index.php?title=Argus)

## See Also

- [tcpdump](tcpdump.md)

