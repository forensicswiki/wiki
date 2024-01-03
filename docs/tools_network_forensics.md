---
tags:
  - Network Forensics
  - Tools
---
# Network Forensics Packages and Appliances

[E-Detective](https://www.edecision4u.com/)

[CapAnalysis](https://www.capanalysis.net/ca/)

**Open Source** web visual tool for information security specialists,
system administrators and everyone who needs to analyze large amounts of
captured network traffic.

CapAnalysis performs indexing of data set of PCAP files and presents
their contents in many forms, starting from a list of TCP, UDP or ESP
streams/flows, passing to the geo-graphical representation of the
connections.

[Demo](https://pcap.capanalysis.net/)

[chkrootkit](https://www.chkrootkit.org/)

[cryptcat](https://farm9.org/Cryptcat/)

[Enterasys Dragon](https://www.extremenetworks.com/)

Instrusion Detection System, includes session reconstruction.

[MNIS Collector](https://www.mantaro.com)
MNIS Collector is an IPFIX collector which also supports legacy Netflow.
It was designed to be used with the MNIS Exporter, which is a Deep
Packet Inspection probe that can be used to decode 300+ protocols on up
to 20 Gbps and report the information in IPFIX.

[Mantaro Network Intelligence Solutions (mnis)](https://www.mantaro.com)

MNIS is a comprehensive and scalable network intelligence platform for
network forensics and various other applications. It is built on high
speed Deep Packet Inspection and metadata alerting. It can be used to
understand network events before and after an event. It scales from LAN
environments to 20 Gbps service provider networks.

[MaxMind](https://www.maxmind.com/en/home)

[IP geolocation](ip_geolocation.md) services and data provider
for offline geotagging. Free GeoLite country database. Programmable
APIs.

[netcat](netcat.md)

[SiLK](https://tools.netsa.cert.org/silk/index.html)

[Netstat](netstat.md)

NetworkMiner

NetworkMiner is a Network Forensic Analysis Tool (NFAT) for Windows.
NetworkMiner can be used as a passive network sniffer/packet capturing
tool in order to detect operating systems, sessions, hostnames, open
ports etc. without putting any traffic on the network. NetworkMiner can
also parse PCAP files for off-line analysis and to regenerate/reassemble
transmitted files and certificates from PCAP files. The purpose of
NetworkMiner is to collect data (such as forensic evidence) about hosts
on the network rather than to collect data regarding the traffic on the
network. The main view is host centric (information grouped per host)
rather than packet centric (information showed as a list of
packets/frames). NetworkMiner has, since the first release in 2007,
become popular tool among incident responce teams as well as law
enforcement. NetworkMiner is today used by companies and organizations
all over the world.

NetworkMiner is available both as a [free open source
tool](https://sourceforge.net/projects/networkminer/) and as a
[commercial network forensics
tool](https://www.netresec.com/?page=NetworkMiner).

[pcap2wav](https://pcap2wav.xplico.org/)

VoIP/RTP decoder. pcap2wav is part (a sub-project) of
[Xplico](xplico.md) and it supports and decodes the following
audio codecs: G711ulaw, G711alaw, G722, G729, G723, G726 and MSRTA
(x-msrta: Real Time Audio).

[rkhunter](https://rkhunter.sourceforge.net/)

[ngrep](ngrep.md)

[nslookup](https://en.wikipedia.org/wiki/Nslookup)

Name Server Lookup command line tool used to find IP address from domain
name.

[Sguil](http://bammv.github.io/sguil/index.html)

[Snort](snort.md)

[ssldump](https://ssldump.sourceforge.net/)

[tcpdump](tcpdump.md)

[tcpxtract](tcpxtract.md)

[tcpflow](tcpflow.md)

[truewitness](http://www.nature-soft.com/forensic.html)

Linux/open-source. Based in India.

[OmniPeek](omnipeek.md) by [WildPackets](wildpackets.md)

OmniPeek is a network forensics tool used to capture, store, and analyze
historical network traffic.

[Whois](https://en.wikipedia.org/wiki/WHOIS)

Web service and command line tool to look up registry information for internet
domain.

[American Registry for Internet Numbers (ARIN)](https://www.arin.net/)

[African Network Information Center (AfriNIC)](https://www.afrinic.net/)

[Asia Pacific Network Information Centre (APNIC)](https://www.apnic.net/)

[Latin American and Caribbean IP Address Regional Registry (LACNIC)](https://www.lacnic.net/)

[RIPE Network Coordination Centre (RIPE NCC)](https://www.ripe.net/)

[Wireshark](wireshark.md) / Ethereal

Open Source protocol analyzer previously known as ethereal.

[Kismet](kismet.md)

Kismet is an 802.11 layer2 wireless network detector, sniffer, and
intrusion detection system.

[kisMAC](kismac.md)

KisMAC is an open-source and free sniffer/scanner application for Mac OS
X.

[Xplico](xplico.md)

Open Source Network Forensic Analysis Tool (NFAT). Protocols supported:
HTTP, SIP, FTP, IMAP, POP, SMTP, TCP, UDP, IPv4, IPv6, ...

VoIP sniffer and decoder. Audio codec supported: G711ulaw, G711alaw,
G722, G729, G723, G726 and MSRTA

[Expert Team - 3i System](http://expert-team.net/home/)

Expert Team 3i System provides real-time data traffic reconstruction
which allows raw data packet stream to be decoded, reassemble and
reconstruct back to the original content view receive/compose/sent by
the target users. Supported layer 7 protocols and applications include
HTTP (Web URL and Content, Web Video, Web File Upload and Download,
Email - POP3, IMAP, SMTP, Webmail, Social Networking Sites, FTP File
Upload and Download, Instant Messaging, VoIP etc....

[fmadio 10G Packet Capture](https://www.fmad.io/)

Cost effective full line rate 10G packet capture to disk appliance.
Featuring a slim 1U solution with 4 hot swap drives and 16TB of raw disk
space, generating nanosecond PCAP files that can be downloaded for
further processing at 10Gbit speed. This is a commercial appliance by a
small independent vendor.

# Command-line tools

arp- view the contents of your ARP cache

ifconfig - view your mac and IP address

ping - send packets to probe remote machines

[SplitCap](https://www.netresec.com/?page=SplitCap)

SplitCap is a free open source pcap file splitter.

[tcpdump](tcpdump.md) - capture packets

snoop - captures packets from the network and
displays their contents ([solaris](solaris.md)

nemesis - create arbitrary packets

tcpreplay - replay captured packets

traceroute - view a network path

gnetcast - GNU rewrite of netcat

packit - packet generator

[nmap](nmap.md) - utility for network exploration and security
auditing

[Xplico](xplico.md) Open Source Network Forensic Analysis Tool
(NFAT)

[pcap_latency_analyzer](https://github.com/fmadio/pcap_latency_analyzer)
Analyze packet latency between 2 PCAPs or between 2 MAC addresses or any
packets with the same payloads.

## ARP and Ethernet MAC Tools

arping - transmit ARP traffic

arpdig - probe LAN for MAC addresses

arpwatch - watch ARP changes

arp-sk - perform denial of service attacks

macof - CAM table attacks

ettercap - performs various low-level Ethernet
network attacks

## CISCO Discovery Protocol Tools

cdpd - transmit and receive CDP announcements;
provides forgery capabilities

## ICMP Layer Tests and Attacks

icmp-reset

icmp-quench

icmp-mtu

ish

isnprober

## IP Layer Tests

iperf - IP multicast test

fragtest - IP fragment reassembly test

## UDP Layer Tests

udpcast - includes UDP-receiver and UDP-sender

## TCP Layer

[Layer Four Traceroute (LFT) and WhoB](https://pwhois.org/lft/) - TCP tracing
