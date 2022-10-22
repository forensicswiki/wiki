---
tags:
  -  Tools
  -  Windows
  -  Articles that need to be expanded
  -  System Analysis
  -  Open Source Software
---
## Description

The Regimented Potential Incident Examination Report (**RPIER** or
**RAPIER**) is script based [incident response](incident_response.md) tool released under the
[GPL](gpl.md) by [Intel](intel.md). It is a
modular framework.

RAPIER is a [Windows](windows.md) NT based information gathering
framework. It was designed to streamline the acquisition of information
off of systems in a large scale enterprise network. It was designed with
a pretty simple to use GUI so that end-users could be walked through
execution of the tool on a system.

Contact: rapier.securitytool@gmail.com

## Features

- Modular Design - all information acquired is through individual
  modules
- Fully configurable GUI
- [SHA1](sha1.md) verification checksums
- Auto-update functionality
- Results can be auto-zipped
- Auto-uploaded to central repository
- Email Notification when results are received
- 2 Default Scan Modes – Fast/Slow
- Separated output for faster analysis
- Pre/Post run changes report
- Configuration File approach
- Process priority throttling

### Information Acquired through RAPIER

- Complete list of running processes
- Locations of those processes on disk
- Ports those processes are using
- Checksums for all running processes
- Memory dumps for all running processes
- All DLLS currently loaded and their checksum
- Last Modify/Access/Create times ([MAC times](mac_times.md)
  for designated areas
- All files that are currently open
- Net (start/share/user/file/session)
- Output from nbtstat and [netstat](netstat.md)
- All open shares/exports on system
- Current routing tables
- List of all network connections
- Layer3 traffic samples
- Logged in users
- System Startup Commands
- [MAC address](mac_address.md)
- List of installed services
- Local account and policy information
- Current patches installed on system
- Current AV versions
- Files with alternate data streams (ADS)
- Files marked as hidden
- List of all installed software on system (known to registry)
- System logs
- AV logs
- Copies of application caches (temporary internet files) –
  [IE](internet_explorer.md), [FF](mozilla_firefox.md),
  [Opera](opera.md)
- Export entire registry
- Search/retrieve files based on search criteria.

## See Also

[List of Script Based Incident Response
Tools](list_of_script_based_incident_response_tools.md)

## External Links

- [Official website](http://code.google.com/p/rapier/)
- [Google Discussion
  Group](http://groups.google.com/group/rapier-development?hl=en)
- [Presentation at FIRST Conference
  2006](http://www.first.org/conference/2006/program/rapier_-_a_1st_responders_info_collection_tool.html)