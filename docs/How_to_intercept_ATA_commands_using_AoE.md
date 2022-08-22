ATA over Ethernet (*AoE*) is a network protocol designed for accessing
ATA storage devices over Ethernet networks.

This "How To" explains the process of using ATA over Ethernet protocol
to intercept ATA commands from a Linux system (called Linux client)
using [Wireshark](Wireshark "wikilink") for diagnostic and testing
purposes.

## Linux server - Linux client configuration

First, make sure that Linux server and Linux client are connected to the
same network and can exchange packets with each other.

### Server configuration

Make sure that your server has
[*vblade*](http://packages.debian.org/en/lenny/vblade) tool installed.
Then run the following command:

`# vblade 0 0 eth0 /dev/sda`

Where:

- eth0 - your network interface;
- /dev/sda - a block device you want to be accessible through a network.

### Client configuration

Make sure that your Linux client has [*aoe
tools*](http://packages.debian.org/en/lenny/aoetools) installed. Then
run the following command:

`# modprobe aoe`

Make sure your vblade device is available on the client by running:

`# aoe-stat`

The following block devices would be available:

- /dev/etherd/e0.0 - the whole disk (corresponds to /dev/sda on the
  server);
- /dev/etherd/e0.0p1 - first partition on the disk (corresponds to
  /dev/sda1 on the server);
- /dev/etherd/e0.0p2 - second partition on the disk (corresponds to
  /dev/sda2 on the server);
- etc.

## Intercepting ATA commands

Launch [Wireshark](Wireshark "wikilink") on a client and start a capture
on *eth0*. You can apply the following display filter to analyse AoE
packets only:

`eth.type == 0x88a2`

Here is a screenshot of [grml](grml "wikilink") client running in
VirtualBox:

![](Ataoe.png "Ataoe.png") to capture ATA commands\]\]

## External Links

- [Vblade - ATA over
  Ethernet](http://buffalo.nas-central.org/index.php/Vblade_-_ATA_over_Ethernet)

[Category:Howtos](Category:Howtos "wikilink")