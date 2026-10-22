---
tags:
  - Network Forensics
  - Tools
---
Network forensics tooling for capturing, analyzing, and reconstructing
network traffic. The tools below are grouped according to the
[categories of analysis](network_forensics.md) described in
[Network forensics](network_forensics.md).

> **Warning:** The tools listed below are not necessarily forensic tooling in the sense of
> [Forensic tooling](forensic_tooling.md).

## Deep Analysis - Full Packet Capture (FPC) and Deep Packet Inspection (DPI)

* [fmadio 10G Packet Capture](https://www.fmad.io/)

Cost effective full line rate 10G packet capture to disk appliance.
Featuring a slim 1U solution with 4 hot swap drives and 16TB of raw disk
space, generating nanosecond PCAP files that can be downloaded for
further processing at 10Gbit speed. This is a commercial appliance by a
small independent vendor.

* [NetWitness](https://www.netwitness.com/)

NetWitness Corporation - Freeware/Commercial, Enterprise-Wide, Real-Time
Network Forensics.

* [OmniPeek](omnipeek.md) by WildPackets

OmniPeek is a network forensic tool used to capture, store, and analyze
historical network traffic.

* PacketMotion

Full Packet Capture and Deep Packet Inspection appliance (acquired by
VMware).

* snoop - captures packets from the network and displays their contents
  ([solaris](solaris.md))

* [SplitCap](https://www.netresec.com/?page=SplitCap)

SplitCap is a free open source pcap file splitter.

* [tcpdump](tcpdump.md) - capture packets

* [Wireshark](wireshark.md)

Graphical packet capture and protocol dissection (analysis) tool.

* [Xplico](xplico.md)

Network Forensic Analysis Tool (NFAT) that extracts application-layer
data (emails, web content, files) from pcaps using Deep Packet
Inspection; see also [pcap2wav](https://pcap2wav.xplico.org/).

## Session reconstruction

See also [Session reconstruction](session_reconstruction.md).

* [Chaosreader](chaosreader.md)

Takes tcpdump/snoop capture files and fetches the application data
(tcp sessions, HTTP transfers, FTP files, SMTP emails), producing an
HTML index that links to each reconstructed session.

* E-Detective

Web and email forensic tool for reconstructing web pages and email
content.

* [Expert Team - 3i System](http://expert-team.net/home/)

Expert Team 3i System provides real-time data traffic reconstruction
which allows raw data packet stream to be decoded, reassemble and
reconstruct back to the original content view receive/compose/sent by
the target users. Supported layer 7 protocols and applications include
HTTP (Web URL and Content, Web Video, Web File Upload and Download,
Email - POP3, IMAP, SMTP, Webmail, Social Networking Sites, FTP File
Upload and Download, Instant Messaging, VoIP etc....

* [NetworkMiner](networkminer.md)

Network Forensic Analysis Tool (NFAT) for passive sniffing and PCAP
analysis that recovers sessions, hostnames, open ports, and
reassembles transmitted files and certificates.

* [pcap2wav](https://pcap2wav.xplico.org/)

VoIP/RTP decoder. pcap2wav is part (a sub-project) of
[Xplico](xplico.md) and it supports and decodes the following
audio codecs: G711ulaw, G711alaw, G722, G729, G723, G726 and MSRTA
(x-msrta: Real Time Audio).

* [tcpflow](tcpflow.md)

Captures data transmitted as part of TCP connections (flows) and stores
each flow in its own file for protocol analysis and debugging; can also
process stored 'tcpdump' packet flows.

* [tcpxtract](tcpxtract.md)

Recovers files from network traffic based on content signatures
(inspired by [foremost](foremost.md)).

## Flow-based analysis

See also [Flow-based analysis](flow_based_analysis.md).

* [Argus](argus.md)

Flow-based network monitor that records network transactions (5-tuple
flows with byte and packet counts) for later analysis and replay.

* [CapAnalysis](https://www.capanalysis.net/ca/)

**Open Source** web visual tool for information security specialists,
system administrators and everyone who needs to analyze large amounts of
captured network traffic.

CapAnalysis performs indexing of data set of PCAP files and presents
their contents in many forms, starting from a list of TCP, UDP or ESP
streams/flows, passing to the geo-graphical representation of the
connections.

* [Mantaro Network Intelligence Solutions (mnis)](https://www.mantaro.com)

MNIS is a comprehensive and scalable network intelligence platform for
network forensics and various other applications. It is built on high
speed Deep Packet Inspection and metadata alerting. It can be used to
understand network events before and after an event. It scales from LAN
environments to 20 Gbps service provider networks.

* [MNIS Collector](https://www.mantaro.com)

MNIS Collector is an IPFIX collector which also supports legacy Netflow.
It was designed to be used with the MNIS Exporter, which is a Deep
Packet Inspection probe that can be used to decode 300+ protocols on up
to 20 Gbps and report the information in IPFIX.

* [netfse](netfse.md)

Net/FSE (Network Forensic Search Engine): capture, indexing and search
service for high-volume IP-based network log data (firewalls, intrusion
detection systems, routers and other network devices).

* [ntop](ntop.md)

libpcap-based network traffic probe that shows per-host network usage,
similar to the `top` Unix command.

* [pcap_latency_analyzer](https://github.com/fmadio/pcap_latency_analyzer)

Analyze packet latency between 2 PCAPs or between 2 MAC addresses or any
packets with the same payloads.

* [SiLK](https://tools.netsa.cert.org/silk/index.html)

Toolkit for collecting, storing and analyzing flow records (Compact
NetFlow-style traffic metadata) at scale.

## Intrusion and anomaly detection

See also [Intrusion detection](intrusion_detection.md).

* [chkrootkit](https://www.chkrootkit.org/)

Checks a local system for signs of rootkit intrusion (tampered kernel,
hidden processes, suspicious open ports).

* [OSSEC](ossec.md)

Open source host-based intrusion detection system (HIDS) with log
monitoring and compliance features.

* [rkhunter](https://rkhunter.sourceforge.net/)

Rootkit Hunter - scans a local system for rootkits, tampered binaries
and hidden backdoors.

* [Sguil](https://github.com/bammv/sguil)

Web-based dashboard for collecting and correlating IDS alerts and host
logs.

* [Snort](snort.md)

Open source network intrusion prevention and detection system (IDS/IPS).

## Data leakage analysis

* [InfoWatch Traffic Monitor](https://infowatch.com/)

Network data loss prevention (DLP) tool that inspects network traffic
for leaking of sensitive information.

## DNS analysis

* [nslookup](https://en.wikipedia.org/wiki/Nslookup)

Name Server Lookup command line tool used to find IP address from domain
name.

## Wireless and Radio Frequency (RF) analysis

See also [Wireless forensics](wireless_forensics.md).

* [kisMAC](kismac.md)

Free, open source 802.11 sniffer and security tool (passive scanning and
monitor mode), for Mac OS X.

* [kismet](kismet.md)

802.11 layer2 wireless network detector, sniffer, and intrusion
detection system.

## TLS/SSL analysis

See also [SSL forensics](ssl_forensics.md).

* [ssldump](https://ssldump.sourceforge.net/)

Captures and analyzes SSL/TLS sessions: handshake records, certificate
metadata and - when session keys are available - the cleartext payload.

## Geolocation and path analysis

See also [IP geolocation](ip_geolocation.md).

* [Layer Four Traceroute (LFT) and WhoB](https://pwhois.org/lft/) - TCP
  tracing; a layer-4 traceroute that maps the route using TCP handshake
  segments, useful where ICMP traceroute is filtered.

* [MaxMind](https://www.maxmind.com/en/home)

[IP geolocation](ip_geolocation.md) services and data provider
for offline geotagging. Free GeoLite country database. Programmable
APIs.

* [Whois](https://en.wikipedia.org/wiki/WHOIS)

Web service and command line tool to look up registry information for
internet domain.

* [American Registry for Internet Numbers (ARIN)](https://www.arin.net/)

* [African Network Information Center (AfriNIC)](https://www.afrinic.net/)

* [Asia Pacific Network Information Centre (APNIC)](https://www.apnic.net/)

* [Latin American and Caribbean IP Address Regional Registry (LACNIC)](https://www.lacnic.net/)

* [RIPE Network Coordination Centre (RIPE NCC)](https://www.ripe.net/)

## Timeline correlation

See also [Timeline analysis](timeline_analysis.md) and
[Logfile analysis](logfile_analysis.md).

* [logstash](https://www.elastic.co/logstash)

logstash is a tool for managing events and logs. You can use it to
collect logs, parse them, and store them for later use (like, for
searching). Speaking of searching, logstash comes with a web interface
for searching and drilling into all of your logs.

## Generic tooling

* [Bulk Extractor](bulk_extractor.md)

Computer forensic tool that scans disk images (and other data sources)
recovering artifacts - strings, files, emails and more - in a single
pass.

* [cryptcat](https://farm9.org/Cryptcat/)

Network stream utility with encryption support (Twofish, base64,
SSL/TLS), similar to [netcat](netcat.md).

* Mera Systems NetBeholder

* [netcat](netcat.md)

Reads and writes data over network connections (TCP/UDP); used for
ad-hoc transfers and port testing.

* [Netstat](netstat.md)

Shows the network connections, listening ports, and routing information
of a machine.

* [ngrep](ngrep.md)

Applies grep-style pattern matching to live or captured network traffic
(TCP and UDP).

* [nmap](nmap.md) - utility for network exploration and security auditing

## See Also

* [Network forensics](network_forensics.md)
* [Forensic tooling](forensic_tooling.md)

## External Links

* [Wikipedia: Network forensics](https://en.wikipedia.org/wiki/Network_forensics)
