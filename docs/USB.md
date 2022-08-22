USB is an acronym for the *Universal Serial Bus*, a method for attaching
a wide variety of devices to a host system. USB provides for hot-swap of
devices, and network-like communications that allow for additional ports
to be added to a system by way of internal or external hubs, often
mitigating the need to physically open a host system in order to add
more device capacity. There also exist some ways to [redirect
USB](http://www.eltima.com/usb-redirector/), which was already plugged
to PC. Software solutions and additional steps may help to make [USB
device accessible over IP](http://www.eltima.com/share-usb-over-ip/).

## History of Past Devices

Microsoft [Windows](Windows "wikilink") operating systems are known to
record information about each USB device when it is connected. Such
information can be used by an examiner to show that a person had
possession of a USB device, a device was used on a machine, or that data
exfiltration was conducted, for example.

# USB Monitoring Tools

Windows:

- [usbsnoop](usbsnoop "wikilink")

Linux

- enable CONFIG_USB_STORAGE_DEBUG and monitor syslog
- [usbmon](usbmon "wikilink")
- Turn on [usbfs_snoop](usbfs_snoop "wikilink") and monitor syslog and
  the kernel buffer ring.

[Category:Computer Bus](Category:Computer_Bus "wikilink")
[Category:Hardware](Category:Hardware "wikilink")