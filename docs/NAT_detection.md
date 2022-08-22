**NAT detection** is the process of determining hosts running [Network
Address Translators](Network_Address_Translator "wikilink") (NATs).

## Approaches

### Active detection

#### Port scanning

Some software [NAT](Network_Address_Translator "wikilink") solutions
(such as [Kerio WinRoute
Firewall](http://www.kerio.com/kwf_firewall.html)), as well as many
hardware solutions, provide a control port, which allows users to
monitor and control their server (e.g. using a web browser). These
control ports can be easily detected by means of port scanning (see
[Nmap](Nmap "wikilink")).

#### Routing test

Some improperly configured [NATs](Network_Address_Translator "wikilink")
allow IP packets to be translated from an external network. Routing test
can detect these translators by trying to contact external server (e.g.
*forensicswiki.org:80*) with modified routing tables.

### Passive detection

#### IP TTL

[Network Address Translators](Network_Address_Translator "wikilink")
decrement IP TTL values of all translated packets.

#### Leaked real IP address

Some network protocols leak real IP address of a client. These protocols
include:

- SMTP, HELO/EHLO commands:

<!-- -->

       These commands are used to identify the SMTP client to the SMTP
       server.  The argument field contains the fully-qualified domain name
       of the SMTP client if one is available.  In situations in which the
       SMTP client system does not have a meaningful domain name (e.g., when
       its address is dynamically allocated and no reverse mapping record is
       available), the client SHOULD send an address literal (see section
       4.1.3), optionally followed by information that will help to identify
       the client system.

(see RFC 2821)

- DNS, reverse lookups to an external DNS server:

Reverse DNS lookups made to an external DNS server can leak information
about hosts in an internal network.

- Oscar (ICQ), MSN, MRA (Mail.Ru Agent), direct connections.

#### Strict source port translation

Some network protocols use strict source ports for communication. These
protocols include: NTP, Valve.

Non-heuristic port translators (such as ICS in
[Windows](Windows "wikilink")) always translate source port numbers.

#### [OS fingerprinting](OS_fingerprinting "wikilink")

[Network Address Translators](Network_Address_Translator "wikilink") can
be detected by passively fingerprinting all transferred IP packets.

Generally, single host will not produce different OS fingerprints in a
short period of time. However, this method can be extended to
fingerprinting different hosts running the same [OS](OS "wikilink") by
using IP IDs and [TCP timestamps](TCP_timestamps "wikilink").

## Tools

- [p0f](http://lcamtuf.coredump.cx/p0f.shtml) can do NAT detection using
  passive [OS fingerprinting](OS_fingerprinting "wikilink"). It uses a
  variety of identifiers to create a score on the confidence level of
  device doing NAT.

<!-- -->

- [AntiNAT](http://itdefence.ru/content/pages/antinat/) (GPLv2):
  performs NAT detection based on:

<!-- -->

- - SMTP HELO/EHLO commands;
  - Oscar direct connections;
  - DNS reverse lookup requests;
  - NTP time synchronization;
  - Routing test.

## Links

- [TCP Timestamp to count hosts behind
  NAT](http://phrack.org/issues.html?issue=63&id=3#article), Phrack

### Non-English

- [Обнаружение NAT и
  proxy](http://itdefence.ru/content/articles/obnaruzhenie_nat_i_proxy/),
  ITDefence, 2007
- [Охота на сетевых
  партизан](http://www.xakep.ru/magazine/xa/111/150/1.asp), Kris
  Kaspersky

[Category:Network Forensics](Category:Network_Forensics "wikilink")