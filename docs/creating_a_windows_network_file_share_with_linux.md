---
tags:
  -  Howtos
---
## Description and Review

For large files and other instances in which it isn't feasible to use
[Netcat](netcat.md) to transfer evidence from the victim machine
to your forensic workstation, a network file share can be established
between the two machines in order to transfer files. This is especially
useful when since the output of some commands (such as when gathering a
process memory dump in Windows) can't be transferred directly using
Netcat. However, by creating a network file share, we can still minimize
the impact of our actions on the victim machine by saving to the file
share, rather than to victim machine.

It is important to note that creating a network file share with write
permissions can present a security vulnerability on your forensic
workstation, especially if the victim machine is infected with malware
or if the attacker is currently on the victim machine. Therefore, it is
crucial to be wary of this risk and to frequently scan and check your
forensic workstation to maintain its integrity and security. Make sure
to also protect your file share with a strong password.

## Usage Instructions

As the forensic workstation I use primarily runs Linux, and due to the
complexity of creating a network file share between Windows and Linux, I
have included instructions below (these instructions could easily be
adapted to create a network file share between two Linux machines,
assuming that the victim machine was already running Samba (see
[here](http://www.howtogeek.com/176471/how-to-share-files-between-windows-and-linux/)
for additional instructions) (be wary whenever relying on the victim
machine's potentially-compromised built-in programs/services for your
forensic investigation)):

Ensure that Samba is running on your forensic workstation by running the
following command in the terminal (if it's already installed it will
tell you):

` sudo apt-get install samba`

Next, create a Samba username and password to use to access the Samba
share, by running the following command (replacing <username> with the
username on your machine that you want to use (e.g., root)):

` sudo smbpasswd -a `<username>

You should be prompted to enter a password for the user. The prompts
should look similar to those in the screenshot below:

Next, create a directory to share (replace <share> with whatever you
want the shared directory to be named):

` mkdir Desktop/`<share>

Next, the Samba configuration file needs to be edited to include the
share. To do this, run the following command (you may decide to replace
"vi" with a different editor):

` sudo vi /etc/samba/smb.conf`

Once you have the smb.conf file open in your editor, go down to the very
bottom and add the following lines (replacing <share> with the name of
your shared directory, <pathToShare> with the path to the shared
directory you created above, and <user> with the Samba user you created
above):

` [`<share>`]`
`      path = `<pathToShare>
`      available = yes`
`      valid users = `<user>
`      read only = no`
`      browsable = yes`
`      public = yes`
`      writeable = yes`

After adding the text listed above, the bottom of the *smb.conf* file
should look something like this:

Save the changes you've made to the smb.conf file.

Next, the Samba service needs to be restarted in order to reflect these
changes. To do so, run the following command:

` sudo service samba restart`

After Samba restarts, you should be able to access the share using your
Windows machine. To do so through the command line, type the following
command (replacing "Z" with the drive letter you want to map the network
file share to on the Windows machine (choose one that is not already in
use), <sharingMachineIPAddress> with the IP address of the machine you
created the share on, and <share> with the name of the shared directory
you created above):

` net use Z: \\`<sharingMachineIPAddress>`\`<share>

If you have set things up correctly, you should be prompted for the
Samba username and password you created above. Once, the network file
share has been established, you can access and copy information to it
using the drive letter you specified in the "net use" command above.
