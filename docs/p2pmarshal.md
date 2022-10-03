---
tags:
  -  Windows 
  -  Tools
  -  Peer to Peer Forensics 
---
P2P Marshal is a program that helps an investigator discover and analyze
[file sharing](file_sharing.md) software on a disk.

The Forensic Edition of P2P Marshal operates on a logically mounted
drive (i.e., a restored image of a disk, mounted as D:, E:, etc. or with
Mount Image Pro, EnCase's Physical Disk Emulator, or similar). The Field
Edition can also analyze a live computer's disk. P2P Marshal is designed
to run under Windows, though as a Java-based program, it should be able
to run on other platforms.

When run, it first detects the presence of P2P client programs. Then,
for each program detected, it presents various information, such as
downloaded and shared files, peer servers, and log messages. For some
clients, additional information may be displayed, such as host ID
numbers, total runtime, and other parameters tracked by the client. P2P
Marshal displays the information either on a per-user basis or for all
users. It also provides an extensive search capability, produces
customizable summary reports in PDF, HTML, and RTF formats, and
maintains an audit log of all actions performed by the investigator.

The Forensic Edition must be installed on a computer; the Field Edition
runs from a USB drive.

It currently supports LimeWire and several BitTorrent clients, and Ares,
and detects the presence of KaZaA.

As of March 2010, the 2.1.1 version is current. The Forensic Edition of
P2P Marshal is available to US law enforcement at no cost. ATC-NY
distributes the tools to US law enforcement and for educational use.
Cyber Security Technology distributes the tool commercially.

# Authors

P2P Marshal was developed by ATC-NY through a US National Institute of
Justice (NIJ) grant. The project was originally named File Marshal.

# External Links

- [DFRWS'07 File Marshal paper
  (pdf)](http://dfrws.org/2007/proceedings/p43-adelstein_pres.pdf)
- [p2pmarshal.com](http://www.p2pmarshal.com/)
- [ATC-NY](http://atc-nycorp.com)

[Category:Peer-to-peer forensics
tools](category:peer-to-peer_forensics_tools.md)