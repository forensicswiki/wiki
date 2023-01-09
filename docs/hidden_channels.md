---
tags:
  - Network Forensics
---
**Hidden channels** (covert channels) are communication channels that
transmit information without the authorization or knowledge of the
channel's designer, owner, or operator.

## Common Uses

- Bypassing network filters;
- Bypassing network [sniffers](sniffer.md).

## Techniques

Information can be hidden within:

- IP ID;
- TCP ISN;
- TCP options;
- DNS ID;
- HTTP cookie;
- etc.

## Detection of hidden channels

Generally, it is impossible to detect well-designed hidden channels by
means of traffic analysis. For example, information hidden within TLS
*Client/Server Hello* random bytes in encrypted form cannot be
distinguished from bytes produced by secure random number generator.

However, it is possible to detect hidden channels by detecting attendant
events, such as successful intrusion attempts. Some hidden channels
produce network anomalies, for example, hidden channels using DNS ID to
hide information may produce large number of DNS queries without further
communication between hosts.

## External Links

* [Wikipedia: Covert channel](https://en.wikipedia.org/wiki/Covert_channel)
* [Unusual firewall bypassing techniques, network and computer security](http://gray-world.net/)
* [SANS InfoSec Reading Room - Covert Channels](https://www.sans.org/white-papers/)
