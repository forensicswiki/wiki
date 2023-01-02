---
tags:
  -  Network Forensics
---
[NetworkMiner](http://www.netresec.com/?page=NetworkMiner) is a Network
Forensic Analysis Tool (NFAT) for Windows.
[NetworkMiner](https://sourceforge.net/apps/mediawiki/networkminer/index.php?title=NetworkMiner)
can be used as a passive network [sniffer](sniffer.md)/packet
capturing tool in order to detect operating systems, sessions,
hostnames, open ports etc. without putting any traffic on the network.
NetworkMiner can also parse PCAP files for off-line analysis and to
regenerate/reassemble transmitted files and certificates from PCAP
files.

The purpose of NetworkMiner is to collect data (such as forensic
evidence) about hosts on the network rather than to collect data
regarding the traffic on the network. The main view is host centric
(information grouped per host) rather than packet centric (information
showed as a list of packets/frames).

NetworkMiner performs [OS fingerprinting](os_fingerprinting.md)
based on TCP SYN and SYN+ACK packet by using [OS
fingerprinting](os_fingerprinting.md) databases from p0f (by
Michal Zalewski) and Ettercap (by Alberto Ornaghi and Marco Valleri).
NetworkMiner can also perform [OS
fingerprinting](os_fingerprinting.md) based on DHCP packets
(which usually are broadcast packets) by making use of the Satori (by
Eric Kollmann) [OS fingerprinting](os_fingerprinting.md)
database from FingerBank. NetworkMiner also uses the MAC-vendor list
from Nmap (by Fyodor).

NetworkMiner can extract files and certificates transferred over the
network by parsing a PCAP file or by sniffing traffic directly from the
network. This is a neat function that can be used to extract and [save
media
files](https://sourceforge.net/apps/mediawiki/networkminer/index.php?title=Save_media_files)
(such as audio or video files) which are streamed across a network.
Supported protocols for file extraction are FTP, HTTP and SMB.

User credentials (usernames and passwords) for supported protocols are
extracted by NetworkMiner and displayed under the "Credentials" tab.
Please be considerate when displaying the contents of this tab to the
public.

Another very useful feature is that the user can [search sniffed or
stored data for
keywords](https://sourceforge.net/apps/mediawiki/networkminer/index.php?title=Keyword_Search).
NetworkMiner allows the user to insert arbitrary string or byte-patterns
that shall be searched for with the keyword search functionality.

Version 0.84 (and newer) of NetworkMiner support [sniffing and parsing
of WLAN (IEEE 802.11)
traffic](https://sourceforge.net/apps/mediawiki/networkminer/index.php?title=WiFi_Sniffing).
NetworkMiner does however currently only support WiFi sniffing with
AirPcap adapters.

There is also a commercial version available of NetworkMiner from
[Netresec](http://www.netresec.com/). The commercial version is called
[NetworkMiner Professional](http://www.netresec.com/?page=NetworkMiner)
and has additional features such as:

- Port Independent Protocol Identification (PIPI)
- Export results to CSV / Excel
- Configurable file output directory
- Geo IP localization
- Host coloring support
- Command line scripting support

