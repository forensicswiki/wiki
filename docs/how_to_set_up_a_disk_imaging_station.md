---
tags:
  -  Howtos
---
# FreeBSD

This section describes how to set up a [FreeBSD](freebsd.md)
system as a disk imaging system.

## Install FreeBSD 6.2 on a new computer

1.  Boot the FreeBSD 6.2 CDROM
2.  Hit return to boot the Default
3.  Hit return to select "United States" (or choose your country)
4.  Hit down-arrow and hit return to select "standard install"

Setting up the partition table:

1.  Enter to select "OK." If the geometry is incorrect, enter "OK" to
    accept.
2.  If there are any partitions, use the up and down arrows to select
    them and press "d" to delete them.
3.  press "a" to use All of the disk.
4.  press "q" to finish
5.  press the down arrow and hit Enter to select the Standard MBR (no
    boot manager)

Setting up the FreeBSD partitions:

1.  Press "enter" at the OK prompt.
2.  Press "a" for auto-defaults
3.  Press "q" to accept

Choosing what to install:

1.  Press the down arrow and Enter to select "all" software
2.  Press Enter at the "yes"
3.  Press the up arrow and press Enter to Exit
4.  Press Enter to select CD/DVD
5.  Press Enter to confirm

FreeBSD 6.2 will be installed. Now you need to configure it.

1.  Press Enter at the OK prompt when installation is complete.
2.  Press \[Yes\] Enter to configure an Ethernet address.
3.  Press \[Ok\] Enter to configure the first ethernet card.
4.  Press \[No\] Enter when asked if you want to configure an IPv6
    interface.
5.  Press \[Yes\] Enter when asked if you want to configure with DHCP.
6.  Press \[No\] Enter when asked if you want to be a network gateway.
7.  Press \[No\] Enter when asked if you want to configure inetd.
8.  Press \[No\] Enter when asked if you want to enable SSH login.
9.  Press \[No\] Enter when asked if you want to have anonymous FTP.
10. Press \[No\] Enter when asked if you want to configure the machine
    as an NFS server.
11. Press \[No\] Enter when asked if you want to configure the machine
    as an NFS client.
12. Press \[No\] Enter when asked if you want to customize the system
    console settings.
13. Press \[Yes\] Enter when asked if you want to set the machine's time
    zone.
14. Press \[No\] Enter when asked if the machine's system clock is in
    UTC.
15. Select your region and press \[OK\] Enter
16. Select your country and press \[OK\] Enter
17. If you are in the US, Select your time zone and press \[OK\] Enter
18. Press \[Yes\] Enter to confirm the time zone.
19. Select \[No\] Enter when asked if you need Linux compatibility.
20. Select \[No\] Enter when asked if you have a mouse (even if you have
    one).
21. Select \[No\] Enter when asked if you wish to browse the ports
    collection.
22. Select \[No\] Enter when asked if you wish to add any user accounts.
23. Press \[OK\] Enter when told you will be setting the Root password
24. Press \[Enter\] for the Root password; we will use no password.
25. Press \[Enter\] to confirm the empty root password.

# Getting Your Forensics Software Working for local analysis

Note that the order you do this matters: Sleuth Kit won't compile with
AFFLIB support unless AFFLIB is installed on your system.

1.  Download and install [libewf](libewf.md) if you want EnCase support.
2.  Download and install [AFFLIB](aff.md
3.  Download and install [The Sleuth Kit](the_sleuth_kit.md) from
    <http://www.sleuthkit.org/>
4.  Download and install [fiwalk](fiwalk.md)
