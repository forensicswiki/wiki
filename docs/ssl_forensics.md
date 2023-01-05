---
tags:
  -  Network Forensics
---
**SSL (TLS) forensics** is the process of capturing information
exchanged through SSL (TLS) connections and trying to make sense of it
in some kind of forensics capacity.

## Overview

TLS (*Transport Layer Security*) provides authentication and
[encryption](encryption.md) for many network protocols, such as:
*POP*, *IMAP*, *SMTP*, *HTTP*. However, it is possible to tunnel almost
every TCP-based protocol through TLS using such tools as
[stunnel](http://stunnel.mirt.net/).

Generally, many TLS realizations require only server to be authenticated
using signed certificate.

## Data decryption

Data exchanged through SSL (TLS) connections can be decrypted by
performing *man-in-the-middle* attack. Attacker can modify TLS handshake
and provide new certificates (with attacker's encryption keys).

Some commercial [network forensics](network_forensics.md)
systems can perform such an attack:

- Mera Systems [Sleek
  Buster](https://videonadzor.net/)
  (supports signed by a trusted CA forged certificates)
- [E-Detective HTTPS/SSL Network Packet Forensics Device](https://www.edecision4u.com/PRODUCTS.html)
- Expert Team [3i Tactical System](http://expert-team.net/home/product/)

As well as some open-source tools:

- [ettercap](http://ettercap.sourceforge.net/) (unsupported, last
  version - 2005/05/29)
- [dsniff](http://monkey.org/~dugsong/dsniff/) (obsolete, last stable
  version - 2000/12/17)

## Other information

The TLS protocol also leaks some significant information:

- Current date and time on a TLS client and server (old versions of
  [Firefox](firefox.md) and
  [Thunderbird](thunderbird.md);
- Hostname being accessed ("server_name" extension);
- Original data size.

## [The Onion Router](the_onion_router.md)

Tor tunnels application data through TLS connections
and it is not possible to decrypt such connections by performing
traditional *man-in-the-middle* attack. Tor also sends
application data in chunks to make it harder to guess exactly how many
bytes users are communicating.

## Links

- [RFC 2246 (TLS 1.0)](http://rfc.net/rfc2246.html)
- [RFC 4346 (TLS 1.1)](http://rfc.net/rfc4346.html)

