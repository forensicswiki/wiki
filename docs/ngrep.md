---
tags:
  - Network Forensics
---
**Ngrep** is a tool that provides GNU grep's features
applying them to the network layer.

## Overview

Ngrep recognizes IPv4/6, TCP, UDP, ICMPv4/6, IGMP and Raw across
Ethernet, PPP, SLIP, FDDI, Token Ring and null interfaces.

## Examples

Example 1: dump all common HTTP requests on a live network (eth0):


ngrep -qd eth0 '^(GET\|POST\|HEAD\|CONNECT)' 'tcp'

Example 2: the same, but from a network dump (out.pcap):


ngrep -qI out.pcap '^(GET\|POST\|HEAD\|CONNECT)' 'tcp'

## Limitations

Ngrep cannot reconstruct data streams, it has no ability to match a
string that is broken across two or more packets.

## External Links

* [Project page](https://ngrep.sourceforge.net/)
* [IPv4 and IPv6 fragment reassembly patch](https://sourceforge.net/p/ngrep/patches/31/)
