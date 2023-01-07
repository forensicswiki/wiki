---
tags:
  -  Network Forensics
  -  Tools
  -  Linux
  -  Open Source Software
---
Snort® is an open source network intrusion prevention and detection
system (IDS/IPS) developed by [Sourcefire](https://www.cisco.com/site/us/en/products/security/index.html).

## History

Originally released in 1998 by Sourcefire founder and CTO Martin Roesch,
Snort is a free, open source network intrusion detection and prevention
system capable of performing real-time traffic analysis and packet
logging on IP networks. Initially called a “lightweight” intrusion
detection technology, Snort has evolved into a mature, feature-rich IPS
technology that has become the de facto standard in intrusion detection
and prevention. With over 4 million downloads and nearly 400,000
registered users, it is the most widely deployed intrusion prevention
technology in the world.

## Capabilities

Snort can perform protocol analysis and content searching/matching. It
can be used to detect a variety of attacks and probes, such as buffer
overflows, stealth port scans, CGI attacks, SMB probes, OS
fingerprinting attempts, and much more. It uses a flexible rules
language to describe traffic that it should collect or pass, as well as
a detection engine that utilizes a modular plug-in architecture. Snort
has a real-time alerting capability as well, incorporating alerting
mechanisms for syslog, a user specified file, a UNIX socket, or WinPopup
messages to Windows clients. Snort has three primary uses: a straight
packet sniffer like tcpdump, a packet logger (useful for network traffic
debugging, etc), or a full-blown network intrusion prevention system.

## Requirements

The Snort Engine is distributed both as source code and binaries for
popular Linux distributions and Windows

### Windows

Note to Windows users: If you’re downloading Snort binaries the only
requirements are WinPcap and Barnyard.

### \*nix

Libpcap In the field of computer network administration, [pcap](pcap.md)
consists of an application programming interface (API) for capturing network
traffic. Unix-like systems implement pcap in the libpcap library; Windows uses
a port of libpcap known as WinPcap.

Monitoring software may use libpcap and/or WinPcap to capture packets
traveling over a network. libpcap and WinPcap also support saving
captured packets to a file and reading files containing saved packets.
Snort uses these files to read network traffic and analyze it.

For more information and to download please visit
[tcpdump](http://www.tcpdump.org/)

#### PCRE

Perl Compatible Regular Expressions (PCRE) is a regular expression C
library inspired by Perl’s external interface, written by Philip Hazel.
The PCRE library is incorporated into a number of prominent open-source
programs such as the Apache HTTP Server, the PHP and R scripting
languages, and Snort.

For more information and to download please visit [PCRE](http://www.pcre.org/).

#### [Libdnet](libdnet.md)

Libdnet is a generic networking API that provides access to several
protocols.

For more information and to download please visit [libdnet](https://github.com/ofalk/libdnet)

#### [Barnyard2](barnyard2.md)

Barnyard is an output system for Snort. Snort creates a special binary
output format called unified. Barnyard2 reads this file, and then
resends the data to a database back-end. Unlike the database output
plugin, Barnyard2 manages the sending of events to the database and
stores them when the database temporarily cannot accept connections.

For more information and to download please visit
[barnyard2](http://www.securixlive.com/barnyard2/download.php/)

#### DAQ

DAQ is the Data-Acquisition API that is necessary to use Snort version
2.9.0 and above.

For more information and to download please visit [DAQ](https://snort.org/downloads)

## See Also

* [Network Forensics](network_forensics.md)

## External Links

* [Offical Snort Website](https://snort.org/)
* [Snort Documentation](https://snort.org/documents)
* [Build an IPS Virtual Appliance with Snort](https://s3.amazonaws.com/snort-org-site/production/document_files/files/000/000/069/original/Snort-IPS-Tutorial.pdf)
