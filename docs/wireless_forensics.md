---
tags:
  - Articles that need to be expanded
  - Network Forensics
---
**Wireless forensics** is the process of capturing information that
moves over a wireless network and trying to make sense of it in some
kind of forensics capacity.

## Wireless Local Area Networks

*WLANs are standardized under the IEEE 802.11 series.*

Common encryption technologies used by these networks are: WEP,
WPA/WPA2-PSK, some networks have no encryption at all.

In order to decrypt intercepted secured WLAN traffic you should crack
the encryption key. Note, that the only option for cracking WPA/WPA2-PSK
keys is to do a brute-force password guessing attack. There are several
WPA-PSK [rainbow tables](rainbow_tables.md)
[available](https://www.renderlab.net/projects/WPA-tables/).

Many commercial [network forensics](network_forensics.md)
systems can intercept and decrypt WLAN traffic, for example:

* Mera Systems [NetBeholder Mobile](https://videonadzor.net/)
* E-Detective [Wireless Detective System](https://www.edecision4u.com/PRODUCTS.html)
* Expert Team [3i Tactical System (3iTS)](http://expert-team.net/home/product/))

As well as some open-source tools:

* [aircrack-ng](http://aircrack-ng.org/doku.php)

WPA/WPA2-PSK cracking-only solutions with [GPU acceleration](forensics_on_gpus.md)
(15-100 times faster than in CPU-only mode):

* [ElcomSoft Distributed Password Recovery](https://www.elcomsoft.com/edpr.html)
* [Pyrit](https://code.google.com/archive/p/pyrit)
