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
[dfvfs](dfvfs "wikilink").

### Volume System Formats

Volume System Format support is provided by [dfvfs](dfvfs "wikilink").

### File System Formats

File System Format support is provided by [dfvfs](dfvfs "wikilink").

### File formats

- [Apple System Log (ASL)](Apple_System_Log_(ASL) "wikilink")
- Android usage-history (app usage)
- [Basic Security Module
  (BSM)](Basic_Security_Module_(BSM)_file_format "wikilink")
- Bencode files
- [Chrome cache files](Chrome_Disk_Cache_Format "wikilink")
- Chrome preferences file
- CUPS IPP
- [Extensible Storage Engine (ESE) Database File (EDB)
  format](Extensible_Storage_Engine_(ESE)_Database_File_(EDB)_format "wikilink")
  using [libesedb](libesedb "wikilink")
- Firefox Cache
- [Java IDX](Java "wikilink")
- [Jump Lists](Jump_Lists "wikilink") .customDestinations-ms files
- MacOS-X Application firewall
- MacOS-X Keychain
- MacOS-X Securityd
- MacOS-X Wifi
- [mactime logs](mactime "wikilink")
- McAfee Anti-Virus Logs
- Microsoft [Internet Explorer History File
  Format](Internet_Explorer_History_File_Format "wikilink") (also known
  as MSIE 4 - 9 Cache Files or index.dat) using
  [libmsiecf](libmsiecf "wikilink")
- Microsoft IIS log files
- NTFS \$MFT using [libfsntfs](libfsntfs "wikilink")
- NTFS \$UsnJrnl:\$J using [libfsntfs](libfsntfs "wikilink")
- [OLE Compound File](OLE_Compound_File "wikilink") using
  [libolecf](libolecf "wikilink")
- [Opera Browser history](Opera "wikilink")
- OpenXML
- Pcap files
- PL SQL cache file (PL-SQL developer recall files)
- Popularity Contest log
- Portable Executable (PE) file
- [Property list (plist) format](Property_list_(plist) "wikilink") using
  [binplist](binplist "wikilink")
- Restore points log file (rp.log)
- Safari Binary cookie
- SCCM client logs
- SELinux audit logs
- SkyDrive log and error log files
- [SQLite database format](SQLite_database_format "wikilink") using
  [SQLite](SQLite "wikilink")
- Symantec AV Corporate Edition and Endpoint Protection log
- Syslog
- UTMP
- UTMPX
- [Windows Event Log (EVT)](Windows_Event_Log_(EVT) "wikilink") using
  [libevt](libevt "wikilink")
- Windows Firewall
- [Windows Job files](Windows_Job_File_Format "wikilink") (also known as
  "at jobs")
- [Windows Prefetch files](Windows_Prefetch_File_Format "wikilink")
- [Windows Recycle bin](Windows#Recycle_Bin "wikilink") (INFO2 and
  \$I/\$R)
- [Windows NT Registry File
  (REGF)](Windows_NT_Registry_File_(REGF) "wikilink") using
  [libregf](libregf "wikilink")
- [Windows Shortcut File (LNK) format](LNK "wikilink") using
  [liblnk](liblnk "wikilink") (including shell item support)
- [Windows XML Event Log
  (EVTX)](Windows_XML_Event_Log_(EVTX) "wikilink") using
  [libevtx](libevtx "wikilink")
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
- [Jump Lists](Jump_Lists "wikilink") .automaticDestinations-ms files

### Property list (plist) formats

- Airport
- Apple Account
- Bluetooth
- Install History
- iPod/iPhone
- Mac User
- [Safari history](Apple_Safari "wikilink")
- Software Update
- Spotlight
- Spotlight Volume Information
- Timemachine

### SQLite database file formats

- Android call logs
- Android SMS
- Chrome cookies
- [Chrome browsing and downloads history](Google_Chrome "wikilink")
- [Chrome Extension activity](Google_Chrome "wikilink")
- Firefox cookies
- [Firefox browsing and downloads history](Mozilla_Firefox "wikilink")
- [Google Drive](Google_Drive "wikilink")
- Launch services quarantine events
- MacKeeper cache
- Mac OS X document versions
- Skype text conversations
- [Zeitgeist activity database](Zeitgeist "wikilink")

### [Windows Registry](Windows_Registry "wikilink") formats

- [AppCompatCache](Windows_Application_Compatibility "wikilink")
- BagMRU (or ShellBags)
- CCleaner
- [Explorer
  ProgramsCache](https://github.com/libyal/winreg-kb/blob/master/documentation/Programs%20Cache%20values.asciidoc)
- Less Frequently Used (LFU)
- MountPoints2
- Most Recently Used (MRU) MRUList and MRUListEx (including shell item
  support)
- [MSIE Zones](Internet_Explorer "wikilink")
- Office MRU
- Outlook Search
- [Run and RunOnce keys](Windows_Registry#Run/RunOnce "wikilink")
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
[log2timeline](log2timeline "wikilink") initially created by [Kristinn
Gudjonsson](Kristinn_Gudjonsson "wikilink") and extended by the
contribution of various others.

Plaso builds upon the [SleuthKit](SleuthKit "wikilink"),
[pytsk](pytsk "wikilink"), [libyal](libyal "wikilink"),
[dfvfs](dfvfs "wikilink") and various other projects.

## Related tools

This section contains several tools that can help in analyzing plaso's
timeline output:

- [4n6time](4n6time "wikilink"), formerly "l2t_Review", which is a
  cross-platform forensic tool for timeline creation and review. This
  tool appears to be abandoned.
- [Timesketch](Timesketch "wikilink") a collaborative forensic timeline
  analysis.

## See Also

- [dfvfs](dfvfs "wikilink")
- [dfwinreg](dfwinreg "wikilink")
- [log2timeline](log2timeline "wikilink")
- [Timesketch](Timesketch "wikilink")

## External Links

- [Project site](https://github.com/log2timeline/plaso/)
- [Project documentation](https://plaso.readthedocs.io/en/latest/)
- [Project blog](https://osdfir.blogspot.com/search/label/plaso)