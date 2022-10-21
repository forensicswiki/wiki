---
tags:
  -  Network Forensics
  -  Wireless
  -  Tools
  -  Open Source Software
  -  Linux
---
**Kismet** is an 802.11 layer2 wireless network detector,
[sniffer](sniffer.md), and intrusion detection system.

## Overview

- [Wireshark](wireshark.md)/[Tcpdump](tcpdump.md)
  compatible data logging;
- [Airsnort](airsnort.md) compatible weak-iv packet logging;
- Network IP range detection;
- Built-in channel hopping and multicard split channel hopping;
- Hidden network SSID decloaking;
- Graphical mapping of networks;
- Client/server architecture allows multiple clients to view a single
  Kismet server simultaneously;
- Manufacturer and model identification of access points and clients;
- Detection of known default access point configurations;
- Runtime decoding of WEP packets for known networks;
- Named pipe output for integration with other tools, such as a layer3
  IDS like [Snort](snort.md);
- Multiplexing of multiple simultaneous capture sources on a single
  Kismet instance;
- Distributed remote drone sniffing;
- [XML](xml.md) output;
- Over 20 supported card types.

## Intrusion Detection

Kismet will detect following events:

- Active network scanning (NetStumbler, PocketStumbler, etc);
- SSID brute force attempts;
- Broadcast disconnect/deauthenticate attacks;
- Deauthenticate/disassociate flood;
- Fake APs (new AP on another channel, invalid BSS timestamps);
- Many DoS attacks (zero-length SSID, over-long SSID, etc).

