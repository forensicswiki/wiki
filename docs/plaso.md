---
tags:
  -  Timeline Analysis
  -  Tools
  -  Open Source Software
  -  Disk Analysis
  -  Linux
  -  MacOS
  -  Windows
---
Plaso (Plaso langar að safna öllu) is the Python based back-end engine
used by tools such as log2timeline for automatic creation of a super
timelines. The goal of log2timeline (and thus Plaso) is to provide a
single tool that can parse various log files and forensic artifacts from
computers and related systems, such as network equipment to produce a
single correlated timeline. This timeline can then be easily analysed by
forensic investigators/analysts, speeding up investigations by
correlating the vast amount of information found on an average computer
system. Plaso is intended to be applied for creating super timelines but
also supports creating [targeted
timelines](http://blog.kiddaland.net/2013/02/targeted-timelines-part-i.html).

## Supported Formats

The information below is based of version 20221212. See [Plaso
documentation](https://plaso.readthedocs.io/en/latest/sources/Supported-formats.html)
for the most up to date information.

### Storage Media Image File Formats

Storage Media Image File Format support is provided by [dfVFS](dfvfs.md).

### Volume System Formats

Volume System Format support is provided by [dfVFS](dfvfs.md).

### File System Formats

File System Format support is provided by [dfVFS](dfvfs.md).

### File formats

* Android usage history (usage-history.xml) file
* Apple Spotlight store database (store.db) file
* [Apple System Log (asl)](apple_system_log_(asl).md) file
* AWS CloudTrail Log
* Azure Activity Log
* Azure Application Gateway access log
* [Basic Security Module (bsm)](basic_security_module_(bsm)_file_format.md)
  event auditing file
* Bencoded file
* Compound ZIP file
* CUPS IPP file
* [Custom destinations jump list](jump_lists.md) or .customDestinations-ms file
* Docker container configuration file
* Docker container log file
* Docker layer configuration file
* [Extensible Storage Engine (ESE) Database File (EDB)
  format](extensible_storage_engine_(ese)_database_file_(edb)_format.md)
  using [libesedb](libesedb.md)
* Fish history file
* [Google Chrome or Chromium cache file](chrome_disk_cache_format.md)
* Google Chrome Preferences file
* Google Cloud (GCP) log
* iOS Application Privacy report
* [Java WebStart Cache IDX file](java.md)
* JSON-L log file
* Linux libc6 utmp file
* Locate database file (updatedb)
* MacOS File System Events Disk Log Stream (fseventsd) file
* MacOS keychain database file
* Mac OS X 10.5 utmpx file
* McAfee Anti-Virus access protection log file
* Microsoft [Internet Explorer History File
  Format](internet_explorer_history_file_format.md) (also known
  as MSIE 4 - 9 Cache Files or index.dat) using
  [libmsiecf](libmsiecf.md)
* Microsoft (Office) 365 audit log
* Mozilla Firefox Cache version 1 file (version 31 or earlier)
* Mozilla Firefox Cache version 2 file (version 32 or later)
* NetworkMiner .fileinfos file
* NTFS $MFT metadata file using [libfsntfs](libfsntfs.md)
* NTFS USN change journal ($UsnJrnl:$J) file system metadata file
  using [libfsntfs](libfsntfs.md)
* [OLE Compound File](ole_compound_file.md) using
  [libolecf](libolecf.md)
* [Opera global history](opera.md) (global_history.dat) file
* Opera typed history (typed_history.xml) file
* PL SQL cache file (PL-SQL developer recall file) format
* Portable Executable (PE) file
* [Property list (plist) format](property_list_(plist).md) using
  [binplist](binplist.md)
* Safari Binary Cookie file
* [SleuthKit version 3 bodyfile](mactime.md)
* [SQLite database format](sqlite_database_format.md) using [SQLite](sqlite.md)
* Symantec AV Corporate Edition and Endpoint Protection log file
* Systemd journal file
* text-based log file
* Trend Micro Office Scan Virus Detection log file
* Trend Micro Office Web Reputation log file
* Windows Defender scan DetectionHistory file
* [Windows Event Log (evt)](windows_event_log_(evt).md) using
  [libevt](libevt.md)
* [Windows NT Registry File (regf)](windows_nt_registry_file_(regf).md)
  using [libregf](libregf.md)
* [Windows Prefetch files](windows_prefetch_file_format.md)
* [Windows $Recycle.Bin](windows#recycle_bin.md) $I file
* [Windows Recycler](windows#recycle_bin.md) INFO2 file
* Windows Restore Point log (rp.log) file
* [Windows Scheduled Task job](windows_job_file_format.md) (also known as "at jobs")
* [Windows Shortcut File (LNK) format](lnk.md) using [liblnk](liblnk.md)
* [Windows XML Event Log (evtx)](windows_xml_event_log_(evtx).md) using
  [libevtx](libevtx.md)

### Bencode file formats

* Transmission BitTorrent activity file
* uTorrent active torrent file

### Browser cookie formats

* Google Analytics `__utma` cookie
* Google Analytics `__utmb` cookie
* Google Analytics `__utmt` cookie
* Google Analytics `__utmz` cookie

### Compound ZIP file formats

* OpenXML (OXML) file

### ESE database file formats

* Internet Explorer WebCache ESE database (WebCacheV01.dat, WebCacheV24.dat) file
* System Resource Usage Monitor (SRUM) ESE database file
* Windows 8 File History ESE database file
* Windows User Access Logging ESE database file

### JSON-L log file formats

* [AWS CloudTrail logs](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/cloudtrail-log-file-examples.html)
* [Azure Activity logs](https://learn.microsoft.com/en-us/azure/azure-monitor/essentials/activity-log)
* Azure Application Gateway access log
* Docker container configuration file
* Docker container log file
* Docker layer configuration file
* Google Cloud (GCP) log
* iOS Application Privacy report
* Microsoft (Office) 365 audit log

### OLE Compound File formats

* [Automatic destinations jump list](jump_lists.md) OLE compound file or .automaticDestinations-ms file
* Document summary information (\0x05DocumentSummaryInformation)
* Summary information (\0x05SummaryInformation) (top-level only)

### Property list (plist) formats

* Airport plist file
* Apple account information plist file
* Apple iOS Car Play application plist file
* iPod, iPad and iPhone plist file
* Launchd plist file
* MacOS Bluetooth plist file
* MacOS installation history plist file
* MacOS software update plist file
* MacOS TimeMachine plist file
* MacOS user plist file
* [Safari history](apple_safari.md) plist file
* Spotlight searched terms plist file
* Spotlight volume configuration plist file

### SQLite database file formats

* Android call history SQLite database (contacts2.db) file
* Android text messages (SMS) SQLite database (mmssms.dbs) file
* Android WebViewCache SQLite database file
* Android WebView SQLite database file
* Dropbox sync history database (sync_history.db) file
* [Google Chrome browsing and downloads history](google_chrome.md)
  * Google Chrome 17 - 65 cookies SQLite database file
  * Google Chrome 27 and later history SQLite database file
  * Google Chrome 66 and later cookies SQLite database file
  * Google Chrome 8 - 25 history SQLite database file
* Google Chrome autofill SQLite database (Web Data) file
* [Google Chrome extension activity](google_chrome.md) SQLite database file
* [Google Drive](google_drive.md) snapshot SQLite database (snapshot.db) file
* Google Hangouts conversations SQLite database (babel.db) file
* iOS Kik messenger SQLite database (kik.sqlite) file
* iOS network usage SQLite database (netusage.sqlite) file
* iOS powerlog SQLite database (CurrentPowerlog.PLSQL) file
* iOS Screen Time SQLite database (RMAdminStore-Local.sqlite)
* Kodi videos SQLite database (MyVideos.db) file
* MacOS and iOS iMessage database (chat.db, sms.db) file
* MacOS application usage SQLite database (application_usage.sqlite) file
* MacOS document revisions SQLite database file
* MacOS Duet/KnowledgeC SQLites database file
* MacOS launch services quarantine events database SQLite database file
* MacOS MacKeeper cache SQLite database file
* MacOS Notes SQLite database (NotesV7.storedata) file
* MacOS Notification Center SQLite database file
* MacOS Transparency, Consent, Control (TCC) SQLite database (TCC.db) file
* Mozilla Firefox cookies SQLite database file
* [Mozilla Firefox browsing and downloads history](mozilla_firefox.md)
  * Mozilla Firefox downloads SQLite database (downloads.sqlite) file
  * Mozilla Firefox history SQLite database (places.sqlite) file
* Safari history SQLite database (History.db) file
* Skype SQLite database (main.db) file
* Tango on Android profile SQLite database file
* Tango on Android TC SQLite database file
* Twitter on Android SQLite database file
* Twitter on iOS 8 and later SQLite database (twitter.db) file
* Windows 10 Timeline SQLite database (ActivitiesCache.db) file
* Windows diagnosis EventTranscript SQLite database (EventTranscript.db) file
* [Zeitgeist activity](zeitgeist.md) SQLite database file

### Text-based log file formats

* Advanced Packaging Tool (APT) History log file
* Android logcat file
* Apache access log (access.log) file
* [AWS ELB Access log file](https://docs.aws.amazon.com/elasticloadbalancing/latest/application/load-balancer-access-logs.html#access-log-file-format)
* Bash history file
* Confluence access log (access.log) file
* Debian package manager log (dpkg.log) file
* Google Drive Sync log file
* Google-formatted log file
* iOS lockdown daemon log
* iOS sysdiag log
* iOS sysdiagnose logd file
* MacOS Application firewall log (appfirewall.log) file
* MacOS security daemon (securityd) log file
* MacOS Wi-Fi log (wifi.log) file
* Microsoft IIS log file
* OneDrive (or SkyDrive) version 1 log file
* OneDrive (or SkyDrive) version 2 log file
* Popularity Contest log file
* PostgreSQL application log file
* Santa log (santa.log) file
* SELinux audit log (audit.log) file
* Snort3/Suricata fast-log alert log (fast.log) file
* Sophos anti-virus log file (SAV.txt) file
* System Center Configuration Manager (SCCM) client log file
* System log (syslog) file
* Viminfo file
* vsftpd log file
* Windows Firewall log file
* Windows SetupAPI log file
* XChat log file
* XChat scrollback log file
* ZSH extended history file

### [Windows Registry](windows_registry.md) formats

* AMCache (AMCache.hve)
* [Application Compatibility Cache](windows_application_compatibility.md) or AppCompatCache Registry data
* Background Activity Moderator (BAM) Registry data
* BagMRU (or ShellBags) Registry data
* Boot Execution Registry data
* CCleaner Registry data
* [Microsoft Internet Explorer zone settings](internet_explorer.md) Registry
   data
* Microsoft Office MRU Registry data
* Microsoft Outlook search MRU Registry data
* Most Recently Used (MRU) Registry data
* [Run and RunOnce](windows_registry#run/runonce.md) Registry data
* Security Accounts Manager (SAM) users Registry data
* Terminal Server Client Connection Registry data
* Terminal Server Client Most Recently Used (MRU) Registry data
* User Assist Registry data
* Windows boot verification Registry data
* Windows drivers and services Registry data
* Windows Explorer mount points Registry data
* [Windows Explorer Programs Cache](https://github.com/libyal/winreg-kb/blob/master/documentation/Programs%20Cache%20values.asciidoc)
  Registry data
* Windows Explorer typed URLs Registry data
* Windows last shutdown Registry data
* Windows log-on Registry data
* Windows network drives Registry data
* Windows networks (NetworkList) Registry data
* Windows Task Scheduler cache Registry data
* Windows time zone Registry data
* Windows USB device Registry data
* Windows USB Plug And Play Manager USBStor Registry data
* Windows version (product) Registry data
* WinRAR History Registry data

## Analysis plugins

* file_hashes: Lists all the hashes for all files processed
* tagging: rule-based tagging
* virustotal: Looks up PE files using the VirusTotal API
* viper: Looks up PE files in a Viper instance

## History

Plaso is a Python-based rewrite of the Perl-based
[log2timeline](log2timeline.md) initially created by [Kristinn
Gudjonsson](kristinn_gudjonsson.md) and extended by the
contribution of various others.

Plaso builds upon the [SleuthKit](sleuthkit.md), [pytsk](pytsk.md),
[libyal](libyal.md), [dfVFS](dfvfs.md) and various other projects.

## Related tools

This section contains several tools that can help in analyzing Plaso's
timeline output:

* [4n6time](4n6time.md), formerly "l2t_Review", which is a
  cross-platform forensic tool for timeline creation and review. This
  tool appears to be abandoned.
* [Timesketch](timesketch.md) a collaborative forensic timeline
  analysis.

## See Also

- [dfVFS](dfvfs.md)
- [dfwinreg](dfwinreg.md)
- [log2timeline](log2timeline.md)
- [Timesketch](timesketch.md)

## External Links

- [Project site](https://github.com/log2timeline/plaso/)
- [Project documentation](https://plaso.readthedocs.io/en/latest/)
- [Project blog](https://osdfir.blogspot.com/search/label/plaso)
