## Description and Review

Netstat is an extremely powerful tool that can be used to view the
network connection information on a machine. Netstat includes
information such as listening/active ports and which protocols they are
using. Established connections will also list the IP address
(potentially an attacker's) that the machine is connected to. Many
systems also allow you to specify a switch to view not only the PID of
the programs connected to those ports, but also their names. Because
many hacking attacks attempt to create backdoors on the victim machine
in order to establish another means of connecting back into the machine
later, being able to view open ports and the programs attached to them
can be very beneficial. Netstat can help you quickly identify any
suspicious network behavior on the machine and help point you in the
right direction to files and connections that may require additional
investigation.

Another great benefit to using the Netstat command is that it is one of
the few commands that uses, for the most part, the same syntax on
UNIX-like and Windows operating systems. Netstat also comes installed by
default on nearly all systems.

## Usage Instructions

To run Netstat, open the terminal/command shell and run the following
command for Windows:

` `***`netstat –anob`***

And the following command for UNIX systems:

` `***`netstat –anp`***

This will output all listening and active connections on the machine,
including the PID and name of the program attached to each connection.
This also tells Netstat to return the IP address of connections, rather
than trying to determine their host names. The -a parameter tells
netstat to display all active connections and the TCP and UDP ports on
which the computer is listening. The -n parameter tells netstat to show
all the TCP connections but to not resolve the host-name, this will
greatly increase the speed of the command. The -p parameter shows which
processes are using which sockets. (see
[here](http://pcsupport.about.com/od/commandlinereference/p/netstat-command.htm)
for detailed explanations of Netstat switches on Windows systems, and
[here](http://crybit.com/netstat-command-switches/) for detailed
explanations of Netstat switches on UNIX systems).

Below is an example of an excerpt from the Netstat output (taken from a
forensic investigation on a Windows machine for a class):

` Active Connections`
` `
` Proto  Local Address          Foreign Address        State           PID`
` TCP    0.0.0.0:135            0.0.0.0:0              LISTENING       712`
` ...`
` TCP    0.0.0.0:445            0.0.0.0:0              LISTENING       4`
` [System]`
` `
` `**`TCP 0.0.0.0:1337 0.0.0.0:0 LISTENING 1256`**
` `**`[srss.exe]`**

As you can see, the bolded line shows that the srss.exe program is
running with a PID of 1256 and is listening on TCP port 1337. Looking up
port 1337 and srss.exe on the internet did not reveal any
legitimate/standard programs by that name or port. Further review of the
srss.exe file revealed that it was a disguised version of Netcat,
running a backdoor on the system. Running Netstat helps us quickly
determine which program to investigate first, allowing us to efficiently
identify the intent of the attacker. If the attacker had been connected
to that listening backdoor, his IP address would've also been shown in
the "Foreign Address" column.

Netstat can also list out the routing table for the machine (which may
reveal attempts by the attacker to create alternate routes in order to
bypass firewalls and other restrictions) using the following command:

` `***`netstat –rn`***

This is an example output from the internal route table:

`   Kernel IP routing table`
`   Destination     Gateway         Genmask         Flags   MSS Window  irtt Iface`
`   0.0.0.0         172.16.10.2     0.0.0.0         UG        0 0          0 ens33`
`   169.254.0.0     0.0.0.0         255.255.0.0     U         0 0          0 ens33`
`   172.16.10.0     0.0.0.0         255.255.255.0   U         0 0          0 ens33`

[Category:Tools](Category:Tools "wikilink") [Category:Network
Forensics](Category:Network_Forensics "wikilink")