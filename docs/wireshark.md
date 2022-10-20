---
tags:
  -  Network Forensics
  -  Open Source Software
  -  Windows
  -  Linux
  -  Windows
  -  Solaris
  -  NetBSD
  -  FreeBSD
  -  MacOS
  -  OpenBSD
---
**Wireshark** is a popular [network protocol analyzer](sniffer.md).

## Overview

Wireshark has a rich feature set which includes the following:

- Deep inspection of hundreds of protocols;
- Live capture and offline analysis;
- Standard three-pane packet browser;
- Multi-platform: runs on [Windows](windows.md),
  [Linux](linux.md), [Mac OS X](mac_os_x.md),
  [Solaris](solaris.md), [FreeBSD](freebsd.md),
  [NetBSD](netbsd.md), and many others;
- Captured network data can be browsed via a GUI, or via the TTY-mode
  TShark utility;
- Powerful display filters;
- Rich [VoIP](voip.md) analysis;
- Read/write many different capture file formats: tcpdump (libpcap),
  Catapult DCT2000, Cisco Secure IDS iplog, [Microsoft Network
  Monitor](microsoft_network_monitor.md), Network General
  Sniffer® (compressed and uncompressed), Sniffer® Pro, and NetXray®,
  Network Instruments Observer, Novell LANalyzer, RADCOM WAN/LAN
  Analyzer, Shomiti/Finisar Surveyor, Tektronix K12xx, Visual Networks
  Visual UpTime, WildPackets EtherPeek/TokenPeek/AiroPeek, and many
  others;
- Capture files compressed with gzip can be decompressed on the fly;
- Live data can be read from [Ethernet](ethernet.md), [IEEE
  802.11](wireless_forensics.md), PPP/HDLC, ATM,
  [Bluetooth](bluetooth.md), [USB](usb.md), Token Ring,
  Frame Relay, FDDI, and others (depending on your platfrom);
- Decryption support for many protocols, including
  [IPsec](ipsec.md), ISAKMP, Kerberos, SNMPv3,
  [SSL/TLS](ssl_forensics.md), [WEP, and
  WPA/WPA2](wireless_forensics.md);
- Coloring rules can be applied to the packet list for quick, intuitive
  analysis;
- Output can be exported to [XML](xml.md), PostScript®,
  [CSV](csv.md), or plain text.

## Network Forensics

Wireshark can be used in the [network
forensics](network_forensics.md) process. There are some
limitations:

- Wireshark is packet-centric (not data-centric);
- Wireshark doesn't work well with large network capture files (you can
  turn all packet coloring rules off to increase performance).

### Wireless Forensics

Wireshark can decrypt IEEE 802.11 WLAN data with user specified
encryption keys.

## Usage

The following YouTube video provides a brief overview of how to use
Wireshark to capture and analyze network-based evidence:

<https://www.youtube.com/watch?v=bbT0zDIfjWw>

Another helpful utility in Wireshark is "Follow TCP Stream", this will
bring up a new window that will show all the communications between the
server and the client. To get to this feature left click on a packet and
hover over "follow", then click on "TCP STREAM".

## External Links

- [Wireshark Wiki](http://wiki.wireshark.org/)

## See Also

- [tcpdump](tcpdump.md)

