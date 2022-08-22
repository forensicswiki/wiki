## Overview

**lsof** is a UNIX specific tool that LiSts Open Files. Everything in
Unix is a file: sockets, directories, processes, devices, pipes, etc.
Because of this lsof is able to display information about current
processes, network information and connections.

## Description and Review

lsof was developed by Victor Abell. Written in C, its main purpose is to
show information about files that are opened by running processes on the
system. It shares similar functionality with netstat, but also lists the
network port the service is using. This is a special tool in forensics
due to the amount of information you can receive from it. It could show
port redirections, sniffers, eggdrop IRC bots, or even some backdoors.
The lsof command is preinstalled on most UNIX and Linux distributions.
Other compressed versions of lsof can be found
[here](https://people.freebsd.org/~abe/).

## Usage Instructions

To run lsof open a terminal and type:

`   `**`lsof -n`**

This will display all the open files on the system. The -n option tells
lsof to not do a DNS record on the IP addresses, the purpose of this is
to speed up the process. The resulting output will look similar to:

`   COMMAND    PID       USER   FD      TYPE     DEVICE SIZE/OFF       NODE NAME`
`   init         1       root  cwd       DIR        8,1     4096          2 /`
`   init         1       root  rtd       DIR        8,1     4096          2 /`
`   init         1       root  txt       REG        8,1   190432     927934 /sbin/init`
`   init         1       root  mem       REG        8,1    47040     918484 /lib/i386-linux-gnu/libnss_files-2.15.so`
`   init         1       root  mem       REG        8,1    42652     918488 /lib/i386-linux-gnu/libnss_nis-2.15.so`
`   init         1       root  mem       REG        8,1    92016     918478 /lib/i386-linux-gnu/libnsl-2.15.so`
`   ksoftirqd    3       root  txt   unknown                                /proc/3/exe`
`   migration    6       root  cwd       DIR        8,1     4096          2 /`
`   migration    6       root  rtd       DIR        8,1     4096          2 /`
`   migration    6       root  txt   unknown                                /proc/6/exe`
`   watchdog/    7       root  cwd       DIR        8,1     4096          2 /`
`   watchdog/    7       root  rtd       DIR        8,1     4096          2 /`
`   watchdog/    7       root  txt   unknown                                /proc/7/exe`
`   cpuset       8       root  cwd       DIR        8,1     4096          2 /`
`   cpuset       8       root  rtd       DIR        8,1     4096          2 /`
`   cpuset       8       root  txt   unknown                                /proc/8/exe`
`   khelper      9       root  cwd       DIR        8,1     4096          2 /`
`   khelper      9       root  rtd       DIR        8,1     4096          2 /`
`   khelper      9       root  txt   unknown                                /proc/9/exe`
`   kdevtmpfs   10       root  cwd       DIR        0,5     4240          3 /`
`   kdevtmpfs   10       root  rtd       DIR        0,5     4240          3 /`
`   kdevtmpfs   10       root  txt   unknown                                /proc/10/exe`
`   netns       11       root  cwd       DIR        8,1     4096          2 /`
`   netns       11       root  rtd       DIR        8,1     4096          2 /`
`   netns       11       root  txt   unknown                                /proc/11/exe`
`   sync_supe   12       root  cwd       DIR        8,1     4096          2 /`

To have lsof find all the open sockets on the system the -i option can
be used

`   `**`lsof -i`**

An example of the resulting output is:

`   COMMAND    PID   USER   FD   TYPE DEVICE SIZE/OFF NODE NAME`
`   avahi-dae  689  avahi   12u  IPv4  14766      0t0  UDP *:mdns `
`   avahi-dae  689  avahi   13u  IPv6  14767      0t0  UDP *:mdns `
`   avahi-dae  689  avahi   14u  IPv4  14768      0t0  UDP *:54424 `
`   avahi-dae  689  avahi   15u  IPv6  14769      0t0  UDP *:39288 `
`   dnsmasq   1099 nobody    4u  IPv4  17859      0t0  UDP ubuntu:domain `
`   dnsmasq   1099 nobody    5u  IPv4  17860      0t0  TCP ubuntu:domain (LISTEN)`
`   cups-brow 3334   root    8u  IPv4  30678      0t0  UDP *:ipp `
`   dhclient  4133   root    6u  IPv4  33401      0t0  UDP *:bootpc `

Lsof can also be used to view which processes are listening to a given
port:

`     `**`lsof -i :[port#]`**

To show all the TCP and UDP connections

`     `**`Lsof -i tcp; lsof -i udp`**

To view which process opened a file

`     `**`Lsof /file/path`**

To view all the processes that opened files in a given directory

`     `**`Lsof +d /directory`**

To view all the processes opened by a user

`     `**`Lsof -u username`**

To view all the files opened by a process

`     `**`Lsof -p pid`**

## External Links

- [Useful lsof Primer](https://danielmiessler.com/study/lsof/)
- [Developer’s website for lsof](https://people.freebsd.org/~abe/)

## See Also

- [netstat](netstat "wikilink")

[Category:Network Forensics](Category:Network_Forensics "wikilink")
[Category:Tools](Category:Tools "wikilink")
[Category:Howtos](Category:Howtos "wikilink")