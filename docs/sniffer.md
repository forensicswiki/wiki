---
tags:
  -  Network Forensics
---
**Sniffer** (network sniffer) is a tool that can intercept, log and
sometimes parse traffic passing over a network or part of a network.

## Common Uses

- Analyze network problems;
- Detect intrusion attempts;
- Monitor network usage;
- Spy on other users and collect sensitive information such as
  passwords.

## Detection of network sniffers

### Passive sniffing

Generally, it is impossible to detect passive sniffing programs.

- Detecting promiscuous mode

It is possible to detect network interfaces in promiscuous mode by
sending requests (ICMP, ARP, etc) with destination IP address of a
suspect machine and wrong destination MAC address. Network interfaces in
promiscuous mode will pass this request and a suspect machine will reply
(network interfaces in non-promiscuous mode will drop this packet).

- Detecting reverse DNS lookup requests

Some sniffing programs do automatic reverse DNS lookups on the IP
addresses they see. It is possible to detect such programs by
correlating network traffic and reverse DNS lookup requests.

- Detecting network sniffers using a [honeypot](honeypot.md)
  (monitoring connections to fake accounts)

### Active sniffing

Many sniffing programs provide special techniques to intercept traffic
on a switched network:

- ARP spoofing;
- Fake DHCP server;
- ICMP redirection.

As well as the ability to sniff encrypted data:

- Man-in-the-middle attacks.

These active sniffing techniques can be detected in various ways.

## Cheating network sniffers

- IP fragmentation

Some sniffing programs cannot handle IP fragmentation correctly.

- Shortcomings in TCP reassemblers

It is possible to cheat some TCP reassemblers by sending TCP packets
with low IP TTL values (this TCP packet may not reach the destination
host, but will be analysed by a network sniffer). This will break the
resulting TCP stream.

- [Encryption](encryption.md): [VPN](vpn.md) tunnels,
  SSH tunnels, Tor.

<!-- -->

- [Hidden channels](hidden_channels.md)

## Sniffers

- [tcpdump](tcpdump.md)
- [Wireshark](wireshark.md)
- [Xplico](xplico.md)
- [NetworkMiner](networkminer.md)
- [Cain & Abel](http://www.oxid.it/cain.html)
- [ettercap](https://ettercap.sourceforge.net/) (unsupported, last
  version - 2005/05/29)
- [dsniff](https://monkey.org/~dugsong/dsniff/) (obsolete, last stable
  version - 2000/12/17)
- [justniffer](http://justniffer.sourceforge.net/)

