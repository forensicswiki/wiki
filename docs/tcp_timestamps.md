---
tags:
  -  Network Forensics
  -  Tools
  -  FreeBSD
  -  Linux
  -  Windows
  -  Solaris
  -  NetBSD
---
**TCP timestamps** are used to provide protection against wrapped
sequence numbers. It is possible to calculate system uptime (and boot
time) by analyzing TCP timestamps (see below).

These calculated uptimes (and boot times) can help in detecting hidden
network-enabled operating systems (see
[TrueCrypt](truecrypt.md), linking spoofed [IP](ip.md)
and [MAC](mac.md) addresses together, linking
[IP](ip.md) addresses with Ad-Hoc wireless APs, etc.

## Supported Operating Systems

- BSD/OS
- [FreeBSD](freebsd.md), but not the default configuration in
  versions 3 to 4.3
- HP-UX, recent versions
- IRIX
- [Linux](linux.md), kernel 2.1 and later
- NetApp NetCache
- Solaris 2.6 and later
- [Windows](windows.md) 2000, 2003, XP and Vista

## Limitations

Some operating systems do not send TCP timestamps unless incoming TCP
SYN packets will have this option enabled.

## Method

- Find all TCP packets with timestamp option (in
  [Wireshark](wireshark.md) use following display filter:
  *tcp.options.time_stamp*);
- Calculate target's clock frequency (e.g. 100 Hz or 1000 Hz) by
  analyzing two (or more) TCP timestamps in a certain period of time;
- Use this frequency to calculate uptime.

Following tools can automate this process:

- [Nmap](nmap.md)

## Links

- [RFC 1323](http://rfc.net/rfc1323.html)
- <http://uptime.netcraft.com/>

