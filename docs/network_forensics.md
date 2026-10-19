---
tags:
  - Network Forensics
---
Network forensics is the process of identifying, capturing, and preserving volatile data
transmitted across a network to reconstruct events, establish timelines, and uncover actionable
digital evidence.

The scope of network forensics encompasses the monitoring, interception, and analysis of network
traffic across internal and external boundaries to identify security anomalies, trace policy
violations, and reconstruct information security incidents. This operational domain extends from
localized local area network (LAN) activity and wide area network (WAN) perimeters to virtualized
cloud environments and software-defined networks. Rather than focusing on static storage media,
investigators target data in motion using two primary methodologies:

* Deep-Analysis Systems: Utilize Full Packet Capture (FPC) and Deep Packet Inspection (DPI) to
  record every byte passing through a network monitoring point (via TAPs or SPAN ports), allowing
  investigators to reconstruct entire transmissions down to the application layer.
* Flow-Based Systems: Aggregate traffic into compact, structured metadata records based on a unique
  "5-tuple" identity (Source/Destination IP, Source/Destination Port, and Protocol) to provide
  long-term behavioral visibility without inspecting payload contents.

By combining these packet-level and flow-level capture capabilities with the evaluation of network
device logs (such as firewall and IDS records), advanced hybrid systems establish an authenticated,
end-to-end timeline of how an attacker accessed, navigated, and exfiltrated data from an enterprise
ecosystem.

## Categories of Analysis

The analysis of captured network data is commonly broken down into the following categories:

* **Session reconstruction** - Rebuilding complete user sessions by
  recovering application-layer content (files, email, web pages) from
  captured packets; see also [Session reconstruction](session_reconstruction.md).
* **Flow-based analysis** - Examining compact 5-tuple records (volume,
  duration, timing) to find unusual peers, tunneling, exfiltration, and
  beaconing patterns; see also [Flow-based analysis](flow_based_analysis.md).
* **Intrusion and anomaly detection** - Matching traffic against
  signature rules or behavioral baselines to identify attacks and
  malware; see also [Intrusion detection](intrusion_detection.md).
* **Data leakage analysis** - Combining flow volumes with inspection of
  unencrypted payloads and DNS queries to identify sensitive data
  leaving the network.
* **DNS analysis** - Inspecting queries and responses for tunneling,
  domain generation algorithms, and indicators of compromise.
* **Wireless and Radio Frequency (RF) analysis** - Analysis of 802.11 and other
  radio-based traffic; see also [Wireless forensics](wireless_forensics.md).
* **TLS/SSL analysis** - Examining handshake and certificate metadata,
  or the payload when keys are available; see also
  [SSL forensics](ssl_forensics.md).
* **Geolocation and path analysis** - Using TTL values, traceroutes,
  and address data to map routes; see also
  [IP geolocation](ip_geolocation.md).
* **Timeline correlation** - Aligning network events with host and log
  evidence to build an end-to-end incident timeline; see also
  [Timeline analysis](timeline_analysis.md) and
  [Logfile analysis](logfile_analysis.md).

## Overview

| System | License | User Interface | Supported Platform | Supported Protocols | Refs |
| --- | --- | --- | --- | --- | --- |
| [Argus](argus.md) | Open Source | Command Line, GUI via [ArgusEye](http://www.datenspionage.de/arguseye/) | Mac OS X, Linux, Solaris, FreeBSD, OpenBSD, NetBSD, AIX, IRIX, Windows (under Cygwin) and OpenWrt | L2 addresses, tunnel identifiers (MPLS, GRE, ESP, etc...), protocol ids, SAP's, hop-count, options, L4 transport identification (RTP, RTCP detection), host flow control indication; netflow | |
| [Chaosreader](chaosreader.md) | Open Source | Command Line, GUI | Solaris, RedHat, Windows | FTP files, HTTP transfers (HTML, GIF, JPEG, ...), SMTP emails, ... from the captured data inside network traffic logs | |
| Junkie | Open Source | GUI | unknown | unknown | |
| [kisMAC](kismac.md) | Open Source | GUI | Mac OS X, Linux, Solaris, FreeBSD, OpenBSD, NetBSD, AIX, IRIX, Windows (under Cygwin) and OpenWrt | L2 addresses, tunnel identifiers (MPLS, GRE, ESP, etc...), protocol ids, SAP's, hop-count, options, L4 transport identification (RTP, RTCP detection), host flow control indication; netflow | |
| [kismet](kismet.md) | Open Source | Command Line /GUI via [ArgusEye](http://www.datenspionage.de/arguseye/) | Mac OS X | unknown | |
| n2disk | Open Source | Command Line, GUI | Ubuntu, CentOS | unknown | |
| net-sniff-ng | Open Source | unknown | unknown | unknown | |
| [netfse](netfse.md) | Open Source | GUI | unknown | TCP/IP, UDP | |
| netsleuth | Open Source | Command Line, GUI | Windows, [Backtrack](backtrack.md) | Apple MDNS / Bonjour, SMB / CIFS / NetBios, DHCP (using the www.fingerbank.org resource), SSDP (as used in Microsoft Zero Config) | |
| [NetworkMiner](networkminer.md) | Open Source | Windows GUI, Commandline | Linux / Mac OS X / FreeBSD, Windows | http, smb, ftp, tfpt, ssl , tls, tor | |
| [ntop](ntop.md) | Open Source | Command Line, GUI | Unix (including Linux, \*BSD, Solaris, and Mac OS X), Linux, Windows | DPI via OpenDPI Library; FTP POP SMTP IMAP DNS IPP HTTP MDNS NTP NFS SSDP BGP SNMP XDMCP SMB SYSLOG DHCP PostgreSQL MySQL TDS DirectDownloadLink I23V5 AppleJuice DirectConnect Socrates WinMX MANOLITO PANDO Filetopia iMESH Kontiki OpenFT Kazaa/Fasttrack Gnutella eDonkey Bittorrent (Extended) OFF AVI Flash OGG MPEG QuickTime RealMedia Windowsmedia MMS XBOX QQ MOVE RTSP Feidian Icecast PPLive PPStream Zattoo SHOUTCast SopCast TVAnts TVUplayer VeohTV QQLive Thunder/Webthunder Soulseek GaduGadu IRC Popo Jabber MSN Oscar Yahoo Battlefield Quake Second Life Steam Halflife2 World of Warcraft Telnet STUN IPSEC GRE ICMP IGMP EGP SCTP OSPF IP in IP RTP RDP VNC PCAnywhere SSL SSH USENET MGCP IAX TFTP | |
| [OSSEC](ossec.md) | Open Source | Command Line, GUI | Windows 7, XP, 2000 and Vista Windows Server 2003 and 2008 VMWare ESX 3.0,3.5 (including CIS checks) FreeBSD (all versions) OpenBSD (all versions) NetBSD (all versions) Solaris 2.7, 2.8, 2.9 and 10 AIX 5.3 and 6.1 HP-UX 10, 11, 11i Mac OS X 10 remote syslog: Cisco PIX, ASA and FWSM (all versions) Cisco IOS routers (all versions) Juniper Netscreen (all versions) SonicWall firewall (all versions) Checkpoint firewall (all versions) Cisco IOS IDS/IPS module (all versions) Sourcefire (Snort) IDS/IPS (all versions) Dragon NIDS (all versions) Checkpoint Smart Defense (all versions) McAfee VirusScan Enterprise (v8 and v8.5) Bluecoat proxy (all versions) Cisco VPN concentrators (all versions) Database monitoring is available for the following systems: MySQL (all versions) PostgreSQL (all versions) Oracle, MSSQL (to be available soon)" | Unknown | |
| [Snort](snort.md) | Open Source | Command Line, GUI | Linux, Windows | Unknown | |
| [Wireshark](wireshark.md) | Open Source | Command Line, GUI | Windows, Linux, Mac OS X, Solaris, FreeBSD, NetBSD, and others | IPsec, ISAKMP, Kerberos, SNMPv3, SSL/TLS, WEP, and WPA/WPA2; Wireshark can decrypt IEEE 802.11 WLAN data with user specified encryption keys, and others | |
| [xplico](xplico.md) | Open Source | Command Line, GUI | Linux | ARP Radiotap Ethernet PPP VLAN L2TP IPv4 IPv6 TCP UDP DNS HTTP SMTP POP IMAP SIP MGCP H323 RTP RTCP SDP FB chat FTP IPP CHDLC PJL NNTP MSN IRC YAHOO GTALK EMULE SSL/TLS IPsec 802.11 LLC MMSE Linux cooked TFTP SNOOP PPPoE Telnet WebMail Paltalk Exp. Paltalk NetBIOS SMB PPI syslog G711ulaw, G711alaw, G722, G729, G723, G726 and RTAudio (x-msrta: Real Time Audio). | Unknown |

## See also

* [Flow-based analysis](flow_based_analysis.md)
* [Intrusion detection](intrusion_detection.md)
* [IP geolocation](ip_geolocation.md)
* [Logfile Analysis](logfile_analysis.md#tools)
* [Session reconstruction](session_reconstruction.md)
* [SSL forensics](ssl_forensics.md)
* [Tools: Network Forensics](tools_network_forensics.md)
* [Wireless forensics](wireless_forensics.md)

## External Links

* [http2 explained](https://daniel.haxx.se/http2/), by Daniel Stenberg,
  February 18, 2015
