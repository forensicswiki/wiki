---
tags:
  -  Tools
  -  Howtos
---
## Description and Review

Analyzing files such as executables and process memory dumps for strings
can be very useful in identifying what these files were up to behind the
scenes. For example, a malicious process memory dump may contain clues
as to what other files and/or starting parameters the malicious process
used. String analyzers are able to sift through files and pull out only
the strings that are most likely to include pertinent information, using
the criteria we give them. Strings is a well-known program on UNIX-like
systems that makes a great strings analyzer.

The Strings program comes installed by default on most UNIX-like
systems. If you want to use Strings on Windows, check out
[Cygwin](https://www.cygwin.com/) and make sure to install the binutils
package as part of the setup process.

## Usage Instructions

One of the most useful features of Strings is the ability to specify the
minimum string length for it to gather. For example, if I'm not
interested in short strings in a file and only want to see strings that
are made up of at least 8 characters (since they're more likely to
contain filenames or start parameters that the process used), I would
run the following command (replacing <sourcefilename> with the name of
the file I want to analyzing strings on, and "<outputfilename>" with the
name of the file I want to output the results to):

` strings -8 `<sourcefilename>` > `<outputfilename>`.txt`

The resulting .txt file will contain a list of all strings made up of at
least 8 consecutive characters found within the source file. The "8" can
be replaced with any other number you choose to specify.

When using Strings on a suspicious process memory dump I obtained during
a digital forensics investigation, I found the following strings:

` …`
` C:\Windows\system32\srss.exe -l -p 1337 -e cmd.exe`
` …`
` Cmd line:`
` port numbers can be individual or ranges: m-n [inclusive]`
`        -u            UDP mode`
`        -v            verbose [use twice to be more verbose]`
`        -w secs              timeout for connects and final net reads`
`        -z            zero-I/O mode [used for scanning]`
`        -t            answer TELNET negotiation`
`        -g gateway    source-routing hop point[s], up to 8`
`        -G num        source-routing pointer: 4, 8, 12, ...`
`        -h            this cruft`
`        -i secs              delay interval for lines sent, ports scanned`
`        -l            listen mode, for inbound connects`
`        -L            listen harder, re-listen on socket close`
`        -n            numeric-only IP addresses, no DNS`
`        -o file              hex dump of traffic`
`        -p port              local port number`
`        -r            randomize local and remote ports`
`        -s addr              local source address`
`        -e prog              inbound program to exec [dangerous!!]`
`        -d            detach from console, stealth mode`
` [v1.10 NT]`
` connect to somewhere:      nc [-options] hostname port[s] [ports] ...`
` listen for inbound:  nc -l -p port [options] [hostname] [port]`
` `
` critsvc32:`
` …`
` C:\Windows\critsvc32.exe`
` …`
` Secure Resource Selection Service`
` C:\Windows\system32\srss.exe -l -p 1337 -e cmd.exe`
` C:\Windows\system32\srss.exe`

The file the process was attached to was the *srss.exe file*, seen in
the text above. By performing this strings analysis, I was quickly able
to identify this *srss.exe* file as simply a disguised version of
Netcat, acting as a backdoor to the victim machine. As you can see in
the text above, the entire "-h" (help) output, including the version
("v1.10 NT"), was contained in the process memory dump. I was also able
to identify that the Netcat backdoor was set up to listen ("-l") on port
1337 ("-p 1337") and was configured to execute any commands sent to it
using the command line ("-e cmd.exe"). This presented a huge security
concern on the victim machine! The strings analysis made it much quicker
and simpler to gather the data I needed and react accordingly.

**NOTE:** By default, Strings will only analyze the file for ASCII and
equivalent characters. Additional "-e" arguments will need to be used to
search for Unicode characters. See
[here](http://linux.about.com/library/cmd/blcmdl1_strings.htm) for a
list of them.