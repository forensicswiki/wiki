**VPN** (Virtual Private Network) is a class of technology that allows
remote machines to interconnect by creating a virtual network layer, on
top of the physical network connection, that in practice is used to
maintain the privacy of data shared over this virtual network connection
(essentially all VPN toolsets use some form of packet-level
[encryption](encryption "wikilink")). There are many different modern
implementations of the VPN concept itself, to the point where
categorizing them together becomes somewhat questionable.

## Overview

Virtual Private Networks are deployed by organizations and individuals
for different purposes:

- Protecting confidential information in organizations (for example,
  when connecting geographically distant office networks);
- Providing "work from home" or traveling employees with secure remote
  access to office network resources;
- Securing general Internet traffic in particularly insecure network
  usage settings (e.g. open wireless networks);
- Encrypting all internet traffic to and from a home connection, to
  prevent ISP packet shaping and/or surveillance (i.e. [Torrentfreedom
  Privacy](http://www.torrentfreedom.net)).

When used for Internet connectivity, VPN service also acts as a form of
proxy and protects the user's real IP address from public display. As a
result, they are an increasingly popular form of anonymity protection
for ordinary internet users and criminals.

## VPNs and anonymity

- Log files: VPN services may maintain usage logs which could then be
  used to track the activities of the user of those services, after the
  fact. However some commercial consumer-oriented VPN services
  specifically configure their servers not to retain any logfile
  information of this type. Example are [Cryptocloud
  VPN](Cryptocloud_VPN "wikilink") or [iVPN](iVPN "wikilink").

<!-- -->

- Protocol stack: [TCP timestamps](TCP_timestamps "wikilink") and IP ID
  values may be used in correlating incoming (encrypted) and outgoing
  (unencrypted) network streams. This type of "traffic analysis" can, in
  theory, be used to gather information about a fully-encrypted VPN
  connection - in practice, there are no known public examples of
  traffic analysis being used against commercial VPN service providers.

## See Also

- [iVPN](iVPN "wikilink")
- [Cryptocloud VPN](Cryptocloud_VPN "wikilink")
- [Tor](Tor "wikilink")
- [Proxy server](Proxy_server "wikilink")

[Category:Anti-Forensics](Category:Anti-Forensics "wikilink")
[Category:Network Forensics](Category:Network_Forensics "wikilink")
[Category:Encryption](Category:Encryption "wikilink")