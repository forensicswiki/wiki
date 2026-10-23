---
tags:
  - Open Source Software
  - Tools
---
Strings is a program that prints out any [ASCII](ascii.md) or Unicode strings
in the input file. Forensic examiners can use strings to get a sense of the
functionality of an unknown program. User prompts, error messages, and status
messages can give hints, but should not be used as proof or lack of any
functionality.

Analyzing files such as executables and process memory dumps for strings is
very useful in identifying what these files were up to behind the scenes.
For example, a malicious process memory dump may contain clues as to what
other files and/or starting parameters the malicious process used. String
analyzers are able to sift through files and pull out only the strings that
are most likely to include pertinent information, using the criteria given
to them. The [strings analysis](strings_analysis.md) article describes the
analysis technique in more detail.

Most [Linux](linux.md) distributions and other UNIX-like operating systems
have a strings program included. If you want to use strings on Windows, check
out [Cygwin](cygwin.md) and make sure to install the binutils package as
part of the setup process.

There is a [Windows](windows.md) version of strings by
[Mark Russinovich](mark_russinovich.md). Note that the Windows version
prints an output header and searches for both ASCII and Unicode strings by
default.

## Use

One of the most useful features of strings is the ability to specify the
minimum string length for it to gather. For example, if you are not
interested in short strings in a file and only want to see strings that are
made up of at least 8 characters (since they are more likely to contain
filenames or start parameters that the process used), you would run the
following command (replacing &lt;sourcefilename&gt; with the name of the file you
want to analyze strings in, and "&lt;outputfilename&gt;" with the name of the file
you want to output the results to):

```bash
strings -8 <sourcefilename> > <outputfilename>.txt
```

The resulting .txt file will contain a list of all strings made up of at
least 8 consecutive characters found within the source file. The "8" can be
replaced with any other number you choose to specify.

When using strings on a suspicious process memory dump obtained during a
digital forensics investigation, the following strings can be found:

```text
...
C:\Windows\system32\srss.exe -l -p 1337 -e cmd.exe
...
Cmd line:
port numbers can be individual or ranges: m-n [inclusive]
       -u            UDP mode
       -v            verbose [use twice to be more verbose]
       -w secs              timeout for connects and final net reads
       -z            zero-I/O mode [used for scanning]
       -t            answer TELNET negotiation
       -g gateway    source-routing hop point[s], up to 8
       -G num        source-routing pointer: 4, 8, 12, ...
       -h            this cruft
       -i secs              delay interval for lines sent, ports scanned
       -l            listen mode, for inbound connects
       -L            listen harder, re-listen on socket close
       -n            numeric-only IP addresses, no DNS
       -o file              hex dump of traffic
       -p port              local port number
       -r            randomize local and remote ports
       -s addr              local source address
       -e prog              inbound program to exec [dangerous!!]
       -d            detach from console, stealth mode
[v1.10 NT]
connect to somewhere:      nc [-options] hostname port[s] [ports] ...
listen for inbound:  nc -l -p port [options] [hostname] [port]

critsvc32:
...
C:\Windows\critsvc32.exe
...
Secure Resource Selection Service
C:\Windows\system32\srss.exe -l -p 1337 -e cmd.exe
C:\Windows\system32\srss.exe
```

The file the process was attached to is the *srss.exe* file, seen in the
text above. Performing this strings analysis makes it easy to quickly
identify this *srss.exe* file as simply a disguised version of
[Netcat](netcat.md), acting as a backdoor to the victim machine. As can be
seen in the text above, the entire "-h" (help) output, including the version
("v1.10 NT"), is contained in the process memory dump. The Netcat backdoor
is set up to listen ("-l") on port 1337 ("-p 1337") and is configured to
execute any commands sent to it using the command line ("-e cmd.exe"). This
presents a huge security concern on the victim machine. String analysis made
it much quicker and simpler to gather the data needed and to react
accordingly.

Note that by default, strings will only analyze the file for ASCII and
equivalent characters. Additional "-e" arguments will need to be used to
search for Unicode characters.

## See Also

* [Strings analysis](strings_analysis.md)
* [Netcat](netcat.md)
* [Memory analysis](memory_analysis.md)

## External Links

* [Strings - Sysinternals](https://learn.microsoft.com/en-us/sysinternals/downloads/strings)
