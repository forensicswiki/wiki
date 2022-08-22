## Description and Review

A crucial concept in digital forensics is to write to any mediums being
investigated as little as possible. This becomes a little more
complicated when performing a live analysis of a machine since each
command that is run to investigate the machine can affect memory,
registers, and even the disk. In order to save the output of forensic
tools and commands without writing to the disk of the victim machine, a
tool such as Netcat can be used. Netcat is a small utility that allows
output and even files to be immediately transferred from one machine to
another over the network, rather than first having to save to the source
machine's disk. This allows files and output to be saved and hashed on
your forensic workstation for future use as evidence and to provide
validation for your findings.

Although small, Netcat is very powerful and simple to use. It also comes
installed by default on many UNIX-like operating systems and can also be
used on Windows systems. For use on systems that don't already contain
Netcat, it's recommended to use the Netcat binaries that come with the
free [Nmap](Nmap "wikilink") utility.

It is important to note that because running Netcat creates on open
listening port on your machine, the use of Netcat can present a
significant security risk if used improperly. Be sure not to leave
Netcat running when not in use, and avoid using switches (such as -e)
that allow commands received by Netcat to be run on your machine. See
[here](http://www.sans.org/security-resources/sec560/netcat_cheat_sheet_v1.pdf)
for a list of Netcat switches.

## Usage Instructions

**NOTE:** When running Netcat on a UNIX-like operating system, the
conventional name of the binary is *nc*. When running Netcat on a
Windows-like operating system using the version that comes with nmap
(see above), the default name of the binary is *ncat*. The instructions
below use the *nc* name--make sure to replace it with ncat or whatever
else your Netcat binary is named, if it is different.

To use Netcat, you first need to set it up on your forensic workstation
to listen for incoming information. This can be accomplished by running
the following command in the terminal or command line:

` `***`nc -v -l -p 2222 > `<command>`.txt`***

The "-v" tells Netcat to be verbose, meaning that it will print out more
details about what is going on. The "-l" tells Netcat to listen for
connections. The "-p" tells Netcat which port to listen for connections
on (it's best to use a port above 1024, in order to avoid conflicting
with "well-known" ports that may already be in use by your system). The
"\>" tells the shell to redirect any of the information that Netcat
receives to the specified file (we usually give it the name of the
command that we are about to run on the victim machine (e.g.,
date.txt)). The file will be saved to the current working directory of
the shell you are running Netcat in.

After running the command listed above, you should see a screen that
looks like the following on your forensic workstation:
![<File:netcat1.png>](netcat1.png "File:netcat1.png")

Next, on the victim machine, run a command such as the following in the
terminal or command line:

` `***<command>` | nc `<forensicWS IP>` 2222`***

Replace "<command>" with whatever command you are running on the victim
machine (e,g., "date", "ifconfig", etc.). Replace "<forensicWS IP>" with
the IP address of your forensic workstation (this can be identified by
running the "ifconfig" command on UNIX-like systems and the "ipconfig"
on Windows systems). The "\|" tells the shell to
["pipe"](http://en.wikipedia.org/wiki/Pipeline_(computing)) the standard
output from the command as input to Netcat. Netcat will then send this
information to the IP address and port specified (**NOTE:** by default
only the "standard output" stream will be piped to Netcat. If you need
the "standard error" stream piped to Netcat as well (see
[here](http://en.wikipedia.org/wiki/Standard_streams) for a refresher on
the differences between streams), add the following text just after your
command: **2\>&1**). Make sure you replace "2222" with whatever port you
specified for Netcat to use on your forensic workstation above.

The victim machine screen should look something like this:
![<File:netcat2.png>](netcat2.png "File:netcat2.png")

If the command is taking longer to run that it should, try pressing the
"CTRL" and "C" keys simultaneously on the forensic workstation to
force-stop Netcat from listening.

Back on the forensic workstation, we can see that the listening Netcat
received a connection from our victim machine (in this example we used
the same machine to fill the role of forensic workstation and victim
machine, which is why the "from" name and IP address match our forensic
workstation). Then we used the "cat" command to view the contents of the
*date.txt* file that was created by Netcat, which contained the output
from the "date" command that we ran on the victim machine.
![<File:netcat3.png>](netcat3.png "File:netcat3.png")

When using Netcat to transfer file contents and binary files to your
forensic workstation, commands such as the following can instead be used
on your victim machine:

` `***`type `<fileDir>` | nc `<forensicWS IP>` 2222`***

` `***`cat `<fileDir>` | nc `<forensicWS IP>` 2222`***

## Video Demonstration

The following YouTube video provides a brief tutorial on how to use
Netcat to transfer data from a victim machine to a forensic machine:

<https://www.youtube.com/watch?v=OcSS34Lw910>

## Other Resources

Netcat can also be used to capture network traffic. See
[here](Tcpdump#Using_Tcpdump_with_Netcat "wikilink") for instructions on
how to use Netcat in conjunction with Tcpdump.

[Category:Tools](Category:Tools "wikilink") [Category:Network
Forensics](Category:Network_Forensics "wikilink")
[Category:Howtos](Category:Howtos "wikilink")