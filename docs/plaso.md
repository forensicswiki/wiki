---
tags:
  - No Category
---
Plaso (plaso langar að safna öllu) is the Python based back-end engine
used by tools such as log2timeline for automatic creation of a super
timelines. The goal of log2timeline (and thus plaso) is to provide a
single tool that can parse various log files and forensic artifacts from
computers and related systems, such as network equipment to produce a
single correlated timeline. This timeline can then be easily analysed by
forensic investigators/analysts, speeding up investigations by
correlating the vast amount of information found on an average computer
system. Plaso is intended to be applied for creating super timelines but
also supports creating [targeted
timelines](http://blog.kiddaland.net/2013/02/targeted-timelines-part-i.html).

## Supported Formats

The information below is based of version 1.4.0. See [plaso
documentation](https://plaso.readthedocs.io/en/latest/sources/Supported-formats.html)
for the most up to date information.

### Storage Media Image File Formats

Storage Media Image File Format support is provided by
[dfvfs](dfvfs.md).

### Volume System Formats

Volume System Format support is provided by [dfvfs](dfvfs.md).

### File System Formats

File System Format support is provided by [dfvfs](dfvfs.md).

### File formats

- [Apple System Log (asl)](apple_system_log_(asl).md)
- Android usage-history (app usage)
- [Basic Security Module
  (bsm)](basic_security_module_(bsm)_file_format.md)
- Bencode files
- [Chrome cache files](chrome_disk_cache_format.md)
- Chrome preferences file
- CUPS IPP
- [Extensible Storage Engine (ESE) Database File (EDB)
  format](extensible_storage_engine_(ese)_database_file_(edb)_format.md)
  using [libesedb](libesedb.md)
- Firefox Cache
- [Java IDX](java.md)
- [Jump Lists](jump_lists.md) .customDestinations-ms files
- MacOS-X Application firewall
- MacOS-X Keychain
- MacOS-X Securityd
- MacOS-X Wifi
- [mactime logs](mactime.md)
- McAfee Anti-Virus Logs
- Microsoft [Internet Explorer History File
  Format](internet_explorer_history_file_format.md) (also known
  as MSIE 4 - 9 Cache Files or index.dat) using
  [libmsiecf](libmsiecf.md)
- Microsoft IIS log files
- NTFS \$MFT using [libfsntfs](libfsntfs.md)
- NTFS \$UsnJrnl:\$J using [libfsntfs](libfsntfs.md)
- [OLE Compound File](ole_compound_file.md) using
  [libolecf](libolecf.md)
- [Opera Browser history](opera.md)
- OpenXML
- Pcap files
- PL SQL cache file (PL-SQL developer recall files)
- Popularity Contest log
- Portable Executable (PE) file
- [Property list (plist) format](property_list_(plist).md) using
  [binplist](binplist.md)
- Restore points log file (rp.log)
- Safari Binary cookie
- SCCM client logs
- SELinux audit logs
- SkyDrive log and error log files
- [SQLite database format](sqlite_database_format.md) using
  [SQLite](sqlite.md)
- Symantec AV Corporate Edition and Endpoint Protection log
- Syslog
- UTMP
- UTMPX
- [Windows Event Log (evt)](windows_event_log_(evt).md) using
  [libevt](libevt.md)
- Windows Firewall
- [Windows Job files](windows_job_file_format.md) (also known as
  "at jobs")
- [Windows Prefetch files](windows_prefetch_file_format.md)
- [Windows Recycle bin](windows#recycle_bin.md) (INFO2 and
  \$I/\$R)
- [Windows NT Registry File
  (regf)](windows_nt_registry_file_(regf).md) using
  [libregf](libregf.md)
- [Windows Shortcut File (LNK) format](lnk.md) using
  [liblnk](liblnk.md)
- [Windows XML Event Log
  (evtx)](windows_xml_event_log_(evtx).md) using
  [libevtx](libevtx.md)
- Xchat and Xchat scrollback files

### Bencode file formats

- Transmission
- uTorrent

### ESE database file formats

- Internet Explorer WebCache format
- Windows 8 File History

### OLE Compound File formats

- Document summary information
- Summary information (top-level only)
- [Jump Lists](jump_lists.md) .automaticDestinations-ms files

### Property list (plist) formats

- Airport
- Apple Account
- Bluetooth
- Install History
- iPod/iPhone
- Mac User
- [Safari history](apple_safari.md)
- Software Update
- Spotlight
- Spotlight Volume Information
- Timemachine

### SQLite database file formats

- Android call logs
- Android SMS
- Chrome cookies
- [Chrome browsing and downloads history](google_chrome.md)
- [Chrome Extension activity](google_chrome.md)
- Firefox cookies
- [Firefox browsing and downloads history](mozilla_firefox.md)
- [Google Drive](google_drive.md)
- Launch services quarantine events
- MacKeeper cache
- Mac OS X document versions
- Skype text conversations
- [Zeitgeist activity database](zeitgeist.md)

### [Windows Registry](windows_registry.md) formats

- [AppCompatCache](windows_application_compatibility.md)
- BagMRU (or ShellBags)
- CCleaner
- [Explorer
  ProgramsCache](https://github.com/libyal/winreg-kb/blob/master/documentation/Programs%20Cache%20values.asciidoc)
- Less Frequently Used (LFU)
- MountPoints2
- Most Recently Used (MRU) MRUList and MRUListEx (including shell item
  support)
- [MSIE Zones](internet_explorer.md)
- Office MRU
- Outlook Search
- [Run and RunOnce keys](windows_registry#run/runonce.md)
- SAM
- Services
- Shutdown
- Task Scheduler Cache (Task Cache)
- Terminal Server MRU
- Timezone information
- Typed URLS
- USB
- USBStor
- UserAssist
- WinRar
- Windows version information

## Analysis plugins

- file_hashes: Lists all the hashes for all files processed
- tagging: rule-based tagging
- virustotal: Looks up PE files using the VirusTotal API
- viper: Looks up PE files in a Viper instance

## History

Plaso is a Python-based rewrite of the Perl-based
[log2timeline](log2timeline.md) initially created by [Kristinn
Gudjonsson](kristinn_gudjonsson.md) and extended by the
contribution of various others.

Plaso builds upon the [SleuthKit](sleuthkit.md),
[pytsk](pytsk.md), [libyal](libyal "wikilink"),
[dfvfs](dfvfs.md) and various other projects.

## Related tools

This section contains several tools that can help in analyzing plaso's
timeline output:

- [4n6time](4n6time.md), formerly "l2t_Review", which is a
  cross-platform forensic tool for timeline creation and review. This
  tool appears to be abandoned.
- [Timesketch](timesketch.md) a collaborative forensic timeline
  analysis.

## See Also

- [dfvfs](dfvfs.md)
- [dfwinreg](dfwinreg.md)
- [log2timeline](log2timeline.md)
- [Timesketch](timesketch.md)

## External Links

- [Project site](https://github.com/log2timeline/plaso/)
- [Project documentation](https://plaso.readthedocs.io/en/latest/)
- [Project blog](https://osdfir.blogspot.com/search/label/plaso)