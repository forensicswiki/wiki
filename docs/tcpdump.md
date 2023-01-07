---
tags:
  -  Network Forensics
---
**tcpdump** is a common packet [sniffer](sniffer.md) for
[Unix](unix.md)-like operating systems
([linux](linux.md), [BSD](bsd.md), etc).

## Overview

tcpdump prints out a description of the contents of packets on a network
interface that match the boolean expression. It can also save the packet
data to a file for later analysis.

## Using Tcpdump with Netcat

When gathering network-based evidence, Tcpdump is an extremely useful
tool. It is a widely-known program that offers a myriad of options to
gather exactly the information that you want from the network. The
output of Tcpdump can also be formatted as a PCAP file, which can then
be opened and investigated using many different packet analyzing tools,
including Wireshark. Tcpdump also comes installed by default on many
UNIX-like system distributions. If not installed, binaries can be
downloaded using apt-get (or an equivalent) or compiled using the source
code from [here](http://www.tcpdump.org/).

Below you will find some of the Tcpdump switches most useful in typical
digital forensic investigations, including the ability to transfer
Tcpdump output in binary form (which creates a PCAP file) to a forensic
workstation using Netcat. See
[here](https://www.tcpdump.org/manpages/tcpdump.1.html) for a complete
list of Tcpdump switches, along with other information on the Tcpdump
manpage.

In order to transfer the output of Tcpdump on the victim machine to a
PCAP file on your forensic workstation using Netcat, you will first need
to set Netcat up to listen on your forensic workstation using the
following command (see [here](netcat.md) for a refresher on
using Netcat for digital forensic investigations (note that here we use
the extension ".pcap" instead of ".txt" because we are creating a binary
PCAP file, rather than just text ouptut)):

` `***`nc -v -l -p 2222 > `<command>`.pcap`***

Next, run a command similar to the following one on your victim machine:

` `***`tcpdump -s 0 -U -n -i eth0 not host `<forensicWS IP>` -w - | nc `<forensicWS IP>` 2222`***

The "-s 0" tells Tcpdump to use the default snapshot-length bytes of
data from each packet (65535 bytes) to ensure that packets aren't
truncated. The "-U', when used with "-w" tells Tcpdump to write the
packet information to the output immediately, rather than waiting for
the output buffer to fill. The "-n" tells Tcpdump to use the IP
addresses in the packets, rather than trying to resolve them into host
names using DNS. The "-i eth0" tells Tcpdump to listen for all packets
on the "eth0" interface (information about different interfaces can be
located using the "ifconfig" command; using "-i any" instead will tell
Tcpdump to listen on all interfaces). The "not host <forensicWS IP>" is
the filter syntax for Tcpdump, and tells it not to gather packets
involving the specified host IP address--in this case, our forensic
workstation. This is very important when using Tcpdump with Netcat
because otherwise Tcpdump would get stuck in an endless loop of sending
the same packet data as output through Netcat since each transmission
from Netcat would then immediately be recaptured by Tcpdump and sent to
Netcat again and again until either the program crashes or we run out of
disk space on a forensic workstation. There are also many other filters
you can use with Tcpdump (see the manpage link above). The "-w" tells
Tcpdump to redirect the output to a file, but since we have included a
"-" after it ("-w -"), Tcpdump knows to output the binary data so that
we can pipe it to whatever we want (in this case, Netcat). This allows
the data to be sent to our forensic workstation in a full PCAP file so
that we can perform various analyses on it.

## Video Demonstration

The following YouTube video provides a tutorial on how to conduct a
basic packet capture with tcpdump:
<https://www.youtube.com/watch?v=1AFjQv5jhyM>

## External Links

- [WinDump - tcpdump for Windows](https://www.winpcap.org/windump/)