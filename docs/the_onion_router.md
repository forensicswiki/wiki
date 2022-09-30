---
tags:
  -  Anti-Forensics
---
**Tor** (**The Onion Router**) is an implementation of second-generation
onion routing.

## Overview

Tor is a distributed censorship-resistant network designed to anonymize
TCP-based applications.

## Attacks

**Timing attacks**

Tor fails when the attacker can correlate timing patterns on both ends
of the communications channel.

**Misconfigured software**

- DNS leaks

Some applications do name resolution directly (bypassing Tor proxy). In
this case lookup requests leak significant information (e.g. web site
being visited).

- Web browsers
  - Enabled scripts: Java and Flash applets may leak real IP address
    (see [Metasploit Decloaking Engine](http://decloak.net/));
  - Enabled cookies: web server can identify clients using unique
    cookies.

<!-- -->

- Direct connections in [Instant
  Messaging](instant_messaging.md) also leak
  real IP address

**TLS attacks**

Various deviations of system time can be detected in TLS traffic (e.g.
HTTPS traffic). Attacker can modify system time of the target computer
(or group of them) via NTP and easily trace TLS connections from
anonymous network.

**Eavesdropping by exit nodes**

Tor doesn't encrypt traffic between an exit node and the target server,
so exit nodes are able to capture all unencrypted traffic. Malicious
exit nodes can perform man-in-the-middle attacks on encrypted protocols.

## Hidden services

Location hidden services are also vulnerable to timing correlation
attack.

## External Links

- [Official website](https://www.torproject.org/)
- [Article in
  Wikipedia](http://en.wikipedia.org/wiki/Tor_(anonymity_network))
- [Tor Unreliable Datagram Extension
  Proposal](https://www.torproject.org/svn/trunk/doc/spec/proposals/100-tor-spec-udp.txt)

<!-- -->

- [Low-Cost Traffic Analysis of Tor (University of
  Cambridge)](http://www.cl.cam.ac.uk/~sjm217/papers/oakland05torta.pdf)

[Category:Anti-Forensics](category:anti-forensics.md)
[Category:Anti-forensics
tools](category:anti-forensics_tools.md) [Category:Network
Forensics](category:network_forensics.md)
