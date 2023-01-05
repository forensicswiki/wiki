---
tags:
  - No Category
---
The First Responder's Evidence Disk, or FRED, is a script based
[incident response](incident_response.md) tool. It was designed
to capture volatile information from a computer system for later
analysis without modifying anything on the victim. It consists of a
batch file used to execute a set of known good tools that gather the
state of a victim computer system. It was similar to the
IRCR program and has been widely imitated by other
tools. Many other incident response tools used names similar to FRED.

## Usage

The program was distributed as a compressed 1.44 MB floppy image. The
examiner runs this image on a safe system and writes the FRED program
out to a piece of removable media such as a floppy disk or USB device.
The examiner then connects this device to the victim machine. When run,
the FRED program writes information out to an audit file on the
removable device. The examiner takes this audit file back to the safe
system for later analysis. The audit file can also be sent to other
investigators if desired.

## History

FRED was developed by [Jesse Kornblum](jesse_kornblum.md) for
the [Air Force Office of Special
Investigations](air_force_office_of_special_investigations.md)
starting in the fall of 2000 and was first released in 2001. The tool
was publicly unveiled the following year at the [DFRWS
Conference](digital_forensic_research_workshop.md). Although the
component parts of FRED were not released, mostly due to licensing
restrictions, Kornblum did present a paper, *[Preservation of Fragile
Digital Evidence by First
Responders](http://dfrws.org/2002/papers/Papers/Jesse_Kornblum.pdf)*,
that included the FRED script.

A version of the FRED script was later incorporated into the
[Helix](helix3.md) disk.

There was a proposal for a program to process the audit files into
[HTML](html.md), but this never came to fruition.

Since 2004 FRED has been maintained by the [Air Force Computer Emergency
Response Team](air_force_computer_emergency_response_team.md).
The current version of FRED (version 4) has been redesigned as a single
executable, with remote collection capabilities, and uses Native API
functions. The audit file uses PKI for encryption to protect the
contents from tampering and disclosure. The publicly available version
has the remote functionality as well as the PKI encryption capabilities
turned off.

## Trivia

The desire for a recursive [MD5](md5.md) program for FRED
inspired the development of [md5deep](md5deep.md).

## See Also

- [COFEE](cofee.md)

## External Links

- [Project site](http://darkparticlelabs.com/projects)
