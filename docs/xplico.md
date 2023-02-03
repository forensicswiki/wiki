---
tags:
  - Analysis
  - GPL
  - Linux
  - Tools
---
The **Xplico** is a Network Forensic Analysis Tool (NFAT). The main
scope of Xplico is to extract all application data content from a
network capture (pcap file or real-time acquisition). For example,
Xplico is able to extract all e-mails carried by the POP and SMTP
protocols, and all content carried by HTTP protocol from a pcap file.

## Features

- Protocols supported: [HTTP, SIP, FTP, IMAP, POP, SMTP, TCP, UDP, IPv4,
  IPv6, ...;
- VoIP audio codecs supported: G711ulaw, G711alaw, G722, G729, G723,
  G726 and MSRTA (x-msrta:Real Time Audio)
- Port Independent Protocol Identification (PIPI) for each application
  protocol;
- Multithreading;
- Output data and information in SQLite database or MySQL database
  and/or files;
- At each data reassembled by Xplico is associated a
  [XML](xml.md) file that uniquely identifies the flows and the
  pcap containing the data reassembled;
- Realtime elaboration (depends on the number of flows, the types of
  protocols and by the performance of computer ---RAM, CPU, HD access
  time, ...--- );
- TCP reassembly with ACK verification for any packet or soft ACK
  verification;
- Reverse DNS lookup from DNS packages contained in the inputs files
  (pcap), not from external DNS server;
- No size limit on data entry or the number of files entrance (the only
  limit is HD size).

## Demo and Cloud computing

* Demo with full features: [Demo](https://demo.xplico.org/)
* VoIP decoding, from pcap to wav file:
  [pcap2wav](https://pcap2wav.xplico.org/)

## External links

* [Official website](https://www.xplico.org/)
