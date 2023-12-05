---
tags:
  - Operating Systems
---
**Windows** is a widely-spread [operating
system](operating_system.md) from
[Microsoft](microsoft.md).

There are 2 main branches of Windows:

* the DOS-branch: i.e. Windows 95, 98, ME
* the NT-branch: i.e. Windows NT 4, XP, Vista

## Features

* [Basic and Dynamic Disks](https://learn.microsoft.com/en-us/windows/win32/fileio/basic-and-dynamic-disks)

### Introduced in Windows NT

* [NTFS](ntfs.md)

### Introduced in Windows 2000

### Introduced in Windows XP

* [Prefetch](prefetch.md)
* System Restore ([Restore Points](windows_restore_points.md);
  also present in Windows ME

#### SP2

* Windows Firewall

### Introduced in Windows Server 2003

* Volume Shadow Copies (see [Windows Shadow Volumes](windows_shadow_volumes.md)

### Introduced in [Windows Vista](windows_vista.md)

* [BitLocker](bitlocker_disk_encryption.md)
* [Boot Configuration Data](windows_boot_configuration_data.md)
* [Search](windows_desktop_search.md) integrated in operating
  system
* [ReadyBoost](readyboost.md)
* [SuperFetch](superfetch.md)
* [Transactional NTFS (TxF)](ntfs.md)
* [Transactional Registry (txr)](windows_nt_registry_file_(regf).md)
* [Shadow Volumes](windows_shadow_volumes.md); the volume-based
  storage of the Volume Shadow Copy data
* \$Recycle.Bin
* [Windows XML Event Log (evtx)](windows_xml_event_log_(evtx).md)
* [User Account Control (uac)](user_account_control_(uac).md)

### Introduced in Windows Server 2008

### Introduced in [Windows 7](windows_7.md)

* [BitLocker To Go](bitlocker_disk_encryption.md)
* [Jump Lists](jump_lists.md)
* [Sticky Notes](sticky_notes.md)

### Introduced in [Windows 8](windows_8.md)

* [File History](windows_file_history.md)
* [Storage Spaces](windows_storage_spaces.md)
* Search Charm History
* [Resilient File System (refs)](resilient_file_system_(refs).md); Was initially
  available in the Windows 8 server edition.

### Introduced in Windows Server 2012

* [Resilient File System (refs)](resilient_file_system_(refs).md)

### Introduced in [Windows 10](windows_10.md)

* [Cortana](cortana.md)
* Microsoft Edge Web Browser
* Notification Center
* WofCompressedData, WofCompressed streams

## Forensics

### Partition layout

Default partition layout, first partition starts:

* at sector 63 in Windows 2000, XP, 2003
* at sector 2048 in Windows Vista, 2008, 7

### Filesystems

* [FAT](fat.md), [exFAT](fat.md)
* [NTFS](ntfs.md)
* [ReFS](resilient_file_system_(refs).md)

### Common paths

| Windows XP (and earlier)                                                    | Windows Vista (and later)                                                   |
|-----------------------------------------------------------------------------|-----------------------------------------------------------------------------|
| \Documents and Settings                                                     | \Users                                                                      |
| \Documents and Settings\\%USERNAME%\My Documents                            | \Users\\%USERNAME%\Documents                                                |
| \Documents and Settings\\%USERNAME%\My Documents\My Music                   | \Users\\%USERNAME%\Music                                                    |
| \Documents and Settings\\%USERNAME%\My Documents\My Pictures                | \Users\\%USERNAME%\Pictures                                                 |
| \Documents and Settings\\%USERNAME%\My Documents\My Videos                  | \Users\\%USERNAME%\Videos                                                   |
| \Documents and Settings\\%USERNAME%\Application Data                        | \Users\\%USERNAME%\AppData\Roaming                                          |
| \Documents and Settings\\%USERNAME%\Cookies                                 | \Users\\%USERNAME%\AppData\Roaming\Microsoft\Windows\Cookies                |
| \Documents and Settings\\%USERNAME%\Local Settings                          | \Users\\%USERNAME%\AppData\Local                                            |
| \Documents and Settings\\%USERNAME%\NetHood                                 | \Users\\%USERNAME%\AppData\Roaming\Microsoft\Windows\Network Shortcuts      |
| \Documents and Settings\\%USERNAME%\PrintHood                               | \Users\\%USERNAME%\AppData\Roaming\Microsoft\Windows\Printer Shortcuts      |
| \Documents and Settings\\%USERNAME%\Recent                                  | \Users\\%USERNAME%\AppData\Roaming\Microsoft\Windows\Recent                 |
| \Documents and Settings\\%USERNAME%\SendTo                                  | \Users\\%USERNAME%\AppData\Roaming\Microsoft\Windows\SendTo                 |
| \Documents and Settings\\%USERNAME%\Start Menu                              | \Users\\%USERNAME%\AppData\Roaming\Microsoft\Windows\Start Menu             |
| \Documents and Settings\\%USERNAME%\Templates                               | \Users\\%USERNAME%\AppData\Roaming\Microsoft\Windows\Templates              |
| \Documents and Settings\\%USERNAME%\Local Settings\Application Data         | \Users\\%USERNAME%\AppData\Local                                            |
| \Documents and Settings\\%USERNAME%\Local Settings\History                  | \Users\\%USERNAME%\AppData\Local\Microsoft\Windows\History                  |
| \Documents and Settings\\%USERNAME%\Local Settings\Temporary Internet Files | \Users\\%USERNAME%\AppData\Local\Microsoft\Windows\Temporary Internet Files |
| \Documents and Settings\All Users                                           | \ProgramData                                                                |
| \Documents and Settings\All Users\Application Data                          | \ProgramData                                                                |
| \Documents and Settings\All Users\Desktop                                   | \Users\Public\Desktop                                                       |
| \Documents and Settings\All Users\Documents                                 | \Users\Public\Documents                                                     |
| \Documents and Settings\All Users\Favorites                                 | \Users\Public\Favorites                                                     |
| \Documents and Settings\All Users\Start Menu                                | \ProgramData\Microsoft\Windows\Start Menu                                   |
| \Documents and Settings\All Users\Templates                                 | \ProgramData\Microsoft\Windows\Templates                                    |
| \Documents and Settings\Default User                                        | \Users\Default                                                              |

### Hosts information

    C:\Windows\System32\drivers\etc\hosts
    C:\Windows\System32\drivers\etc\lmhosts.sam

### Recycle Bin

The Recycle Bin contains "Recycled" files. Moving files and directories
to the Recycle Bin is also referred to as soft deletion, since the files
are not removed from the file system. Files stored in the Recycle Bin
can be parsed using [Rifiuti2](https://abelcheung.github.io/rifiuti2/)

#### RECYCLER

The Recycler format is used by Windows 2000, XP.

Per user Recycle Bin folder in the form:

    C:\Recycler\%SID%\

Which contains:

* INFO2 file; "Recycled" files metadata

#### \$RECYCLE.BIN

The \$Recycle.Bin is used as of Windows Vista.

Per user Recycle Bin folder in the form:

    C:\$Recycle.Bin\%SID%\

Which contains:

* \$I files; "Recycled" file metadata
* \$R files; the original data

### Registry

The [Windows Registry](windows_registry.md) is a database of
keys and values that provides a wealth of information to forensic
[investigators](investigator.md).

### Thumbs.db Files

[Thumbs.db](thumbs.db.md) files can be found on many Windows
systems. They contain thumbnails of images or documents and can be of
great value for the [investigator](investigator.md).

See also: [Vista thumbcache](vista_thumbcache.md).

### Browser Cache

### Browser History

The [Web Browser History](web_browser_history.md) files can
contain significant information. The default [web
browser](web_browser.md) that comes with Windows is [Microsoft
Internet Explorer](internet_explorer.md) but other common
browsers on Windows are [Apple Safari](apple_safari.md), [Google
Chrome](google_chrome.md), [Mozilla
Firefox](mozilla_firefox.md) and [Opera](opera.md).

### Search

See [Windows Desktop Search](windows_desktop_search.md)

### Setup API Logs

Windows Vista introduced several new [Setup API Log
files](setup_api_logs.md).

Also see [1](https://learn.microsoft.com/en-US/troubleshoot/windows-client/deployment/windows-setup-log-file-locations).

### Scheduled Tasks

In Windows the Scheduled Tasks can be found in:

    C:\Windows\Tasks

This directory contains .job files which are in the [Windows Job File
Format](windows_job_file_format.md).

In later versions of Windows (at least Windows 7) XML-based equivalents
can be found in the following locations:

    C:\Windows\System32\Tasks
    C:\Windows\SysWow64\Tasks

### Sleep/Hibernation

After (at least) Windows 7 recovers from sleep/hibernation there often
is a system time change event (event id 1) in the event logs.

### Users

Windows stores a users Security identifiers (SIDs) under the following
registry key:

    HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows NT\CurrentVersion\ProfileList

The %SID%\ProfileImagePath value should also contain the username.

### Crash and minidumps

    C:\Windows\Minidump

### Windows Error Reporting (WER)

As of Vista, for User Access Control (UAC) elevated applications WER
reports can be found in:

    C:\ProgramData\Microsoft\Windows\WER\

As of Vista, for non-UAC elevated applications (LUA) WER reports can be
found in:

    C:\Users\%UserName%\AppData\Local\Microsoft\Windows\WER\

Corresponding registry key:

    HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows\Windows Error Reporting

### Microsoft Office Autosave

Recovery files automatically created by Microsoft Office applications.

References:

* <https://www.vestigeltd.com/in-the-news/virtual-case-notes-piecing-together-truth-word-document/>

### User Access Logging (UAL)

UAL is a local data aggregation feature (enabled by default) on Windows
Servers 2012 and above, recording client usage by role and product on
each system providing the resource. It's typically between 2 and 4
extensible storage engine (ESE) databases ("Current.mdb",
"SystemIdentity.mdb, and "<GUID>.mdb"). The files location:
'%%environ_systemroot%%\System32\LogFiles\SUM\\\*.mdb'

References:

* <https://learn.microsoft.com/en-us/windows-server/administration/user-access-logging/manage-user-access-logging>
* <https://advisory.kpmg.us/blog/2021/digital-forensics-incident-response.html>
* <https://github.com/brimorlabs/KStrike>
* <https://www.crowdstrike.com/blog/user-access-logging-ual-overview/>

### CCM_RecentlyUsedApps

"SCCM has the ability to collect inventory data from many sources, and
tracking executables launching is one. This feature isn’t turned on by
default to have the SCCM server collect this data; however, the logging
occurs on the endpoints regardless of the settings that are configured
on the server." \[1\]

"Software metering history can record the path, name, size, associated
user name, last used time, launch count, and PE metadata of executed
files. For forensic investigators, this execution history can be a
goldmine for identifying both the presence of deleted files and
confirming that a file executed on a system. This artifact will likely
only exist on enterprise systems." \[2\]

Windows stores software metering execution logs as CCM_RecentlyUsedApps
records in the CIM repository, and the definition is provided in the
snippet below \[3\].

    #pragma namespace("\\\\.\\root\\ccm")
    instance of __Namespace
    {
     Name = "SoftwareMeteringAgent" ;
    };
    #pragma namespace("\\\\.\\root\\ccm\\SoftwareMeteringAgent")
    class CCM_RecentlyUsedApps
    {
       [Key]
       string FolderPath;

       [Key]
       string ExplorerFileName;

       [Key]
       string LastUserName;

       string OriginalFileName;
       string FileVersion;
       uint32 FileSize;
       string ProductName;
       string ProductVersion;
       string CompanyName;
       uint32 ProductLanguage;
       string FileDescription;
       uint32 LaunchCount;
       datetime LastUsedTime;

       string ProductCode;
       string AdditionalProductCodes;
       string msiDisplayName;
       string msiPublisher;
       string msiVersion;
       string SoftwarePropertiesHash;
       string FilePropertiesHash;
    };

The entries can be extracted on a live system using the following
details \[4\]:

* **Query:** Select \* from CCM_RecentlyUsedApps
* **Namespace:** root\CCM\SoftwareMeteringAgent

References:

1.  <https://www.4n6ir.com/posts/2017/secret-archives-of-execution-evidence-ccm_recentlyusedapps/>
2.  <https://www.trellix.com/en-us/about/newsroom/stories/research.html>
3.  <https://social.technet.microsoft.com/Forums/en-US/fa8fd68e-588b-4cdf-8d6d-8b8c8fe72719/ccmrecentlyusedapps-wmi-class-empty-on-several-thousand-pcs>
4.  <https://github.com/davehull/Kansa/blob/261bd40ac2ae547855313f777273184a759f01d2/Modules/Process/Get-WMIRecentApps.ps1#L54>

### Cryptnet URL Cache

A set of 2 folders (**MetaData** and **Content**) that contain a Windows
cache of files downloaded from the internet.

Helpful when investigating the use of "Living of the Land" tools that
allow attackers to download arbitrary files from the internet, such as
"certutil.exe".

The locations on disk:

    %SYSTEMROOT%\SysWOW64\config\systemprofile\AppData\LocalLow\Microsoft\CryptnetUrlCache\Content\
    %SYSTEMROOT%\SysWOW64\config\systemprofile\AppData\LocalLow\Microsoft\CryptnetUrlCache\MetaData\
    %SYSTEMROOT%\System32\config\systemprofile\AppData\LocalLow\Microsoft\CryptnetUrlCache\Content\
    %SYSTEMROOT%\System32\config\systemprofile\AppData\LocalLow\Microsoft\CryptnetUrlCache\MetaData\
    C:\Users\%USERNAME%\AppData\LocalLow\Microsoft\CryptnetUrlCache\Content\
    C:\Users\%USERNAME%\AppData\LocalLow\Microsoft\CryptnetUrlCache\MetaData\

References:

* <https://u0041.co/blog/post/3>
* <https://thinkdfir.com/2020/07/30/certutil-download-artefacts/>
* <https://blog.menasec.net/2019/03/initial-access-execution-evidences-for.html>
* <https://github.com/Velocidex/velociraptor/blob/32ff014a4504e95c2650fe4770bfda550d998884/artifacts/definitions/Windows/Forensics/CertUtil.yaml>

### Startup info

StartupInfo XML files include the user account's Security Identifier
(SID) in the name and there could be up to 5 per user account. They
contain a list of processes that were executed within the first 90
seconds from the time the user logged in. The info includes start time,
the full command line and the parent process info, among other things.

The location on disk:

    %SYSTEMROOT%\System32\WDI\LogFiles\StartupInfo\*.xml

References:

* <https://medium.com/dfir-dudes/startupinfo-autoruns-served-up-on-a-plate-ba2da0c753c5>
* <https://gist.github.com/mkorman90/272dbc126409135018de3210dd3d2eca>
* <https://www.trustedsec.com/blog/who-left-the-backdoor-open-using-startupinfo-for-the-win/>

## Advanced Format (4KB Sector) Hard Drives

Windows XP does not natively handle drives that use the new standard of
4KB sectors. For information on this, see [Advanced
Format](advanced_format.md).

## %SystemRoot%

The actual value of %SystemRoot% is stored in the following registry
value:

    Key: HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows NT\CurrentVersion\
    Value: SystemRoot

## See Also

* [Event Tracing for Windows (etw)](event_tracing_for_windows_(etw).md)
* [Prefetch](prefetch.md)
* [PowerShell](powershell.md)
* [Setup API Logs](setup_api_logs.md)
* [SuperFetch](superfetch.md)
* [Windows Application Compatibility](windows_application_compatibility.md)
* [Windows Desktop Search](windows_desktop_search.md)
* [Windows Event Log (evt)](windows_event_log_(evt).md)
* [Windows Job File Format](windows_job_file_format.md)
* [Windows XML Event Log (evtx)](windows_xml_event_log_(evtx).md)
* [Windows Update](windows_update.md)
* [Windows Vista](windows_vista.md)
* [Windows 7](windows_7.md)
* [Windows 8](windows_8.md)
* [Windows 10](windows_10.md)
* [WMI](wmi.md)

## External Links

* [Wikipedia: Microsoft Windows](https://en.wikipedia.org/wiki/Microsoft_Windows)
* [Windows 8 File History Forensics](https://www.dataforensics.org/windows-8-file-history-forensics/)
* [Windows 7, Windows Server 2008 R2, and Windows Vista setup log file locations](https://learn.microsoft.com/en-US/troubleshoot/windows-client/deployment/windows-setup-log-file-locations)
* [Windows Hardware Dev Center Archive](https://learn.microsoft.com/en-us/previous-versions/windows/hardware/download/dn550976(v=vs.85))
* [Windows Data Type](https://learn.microsoft.com/en-us/windows/win32/winprog/windows-data-types)
* [The Forensic Analysis of the Microsoft Windows Vista Recycle Bin](https://forensicfocus.com/downloads/forensic-analysis-vista-recycle-bin.pdf),
  by Mitchell Machor, 2008
* [Microsoft Windows File System Tunneling](http://www.ericjhuber.com/2013/02/microsoft-file-system-tunneling.html?m=1),
  by Eric Huber, February 24, 2013
* [Spotting the Adversary with Windows Event Log Monitoring](http://www.nsa.gov/ia/_files/app/Spotting_the_Adversary_with_Windows_Event_Log_Monitoring.pdf),
  by National Security Agency/Central Security Service, February 28, 2013
* [Search history on Windows 8 and 8.1](https://www.swiftforensics.com/2014/04/search-history-on-windows-8-and-81.html),
  by Yogesh Khatri, April 1, 2014
* [Search history on windows 8.1 - Part 2](https://www.swiftforensics.com/2014/04/search-history-on-windows-81-part-2.html),
  by Yogesh Khatri, April 21, 2014
* [Estoteric Hooks](https://www.alex-ionescu.com/Estoteric%20Hooks.pdf)
  by Alex Ionescu, February 16, 2016
  ([presentation](https://www.youtube.com/watch?v=pHyWyH804xE))
* [A brief look at Windows telemetry: CIT aka Customer Interaction Tracker](https://research.nccgroup.com/2022/04/12/a-brief-look-at-windows-telemetry-cit-aka-customer-interaction-tracker/),
  by Erik Schamper, April 12, 2022

### Client/Server Runtime Subsystem (CSRSS)

* [Windows CSRSS Write Up: the basics (part 1/1)](https://j00ru.vexillium.org/2010/07/windows-csrss-write-up-the-basics/),
  by j00ru, July 8, 2010

### Recycle Bin

* [Lesson 3 – The Recycle Bin](https://www.cybersecurityinstitute.biz),
  by Steve Hailey
* [The Forensic Analysis of the Microsoft Windows Vista Recycle Bin](https://forensicfocus.com/downloads/forensic-analysis-vista-recycle-bin.pdf),
  by Mitchell Machor, January 22, 2008

### Malware/Rootkits

* [Inside Windows Rootkits](https://www.forensicmethods.com/),
  by Chad Tilbury, September 4, 2013

### Tracking removable media

* [Tracking USB First insertion in Event logs](https://www.swiftforensics.com/2012/08/tracking-usb-first-insertion-in-event.html),
  by Yogesh Khatri, August 18, 2012

### Under the hood

* [MSDN: Comparing Memory Allocation Methods](https://learn.microsoft.com/en-us/windows/win32/memory/comparing-memory-allocation-methods),
  by [Microsoft](microsoft.md)
* [DLL/COM Redirection](https://learn.microsoft.com/en-us/windows/win32/sbscs/dll-com-redirection-on-windows)
* [Dynamic-Link Library Search Order](https://learn.microsoft.com/en-us/windows/win32/dlls/dynamic-link-library-search-order)
* [Load Library Safely](https://learn.microsoft.com/en-us/archive/blogs/),
  by Swamy Shivaganga Nagaraju, 13 May 2014
* [Happy DPAPI!](https://blog.digital-forensics.it/2015/01/happy-dpapi.html?m=1),
  by Francesco Picasso, January 13, 2015

#### Windows File Protection (WFP)

* [Description of the Windows File Protection feature](https://support.microsoft.com/en-us/topic/description-of-the-windows-file-protection-feature-db28f515-6512-63d1-6178-982ed2022ffb)
* [Description of Windows XP and Windows Server 2003 System File Checker (Sfc.exe)](https://support.microsoft.com/en-US)

#### MSI

* [MSI: The Case Of The Invalid Signature](https://blog.didierstevens.com/2013/07/26/msi-the-case-of-the-invalid-signature/),
  by Didier Stevens, July 26, 2013

#### Side-by-side (WinSxS)

* [Wikipedia: Side-by-side assembly](https://en.wikipedia.org/wiki/Side-by-side_assembly)
* [Assembly Searching Sequence](https://learn.microsoft.com/en-us/windows/win32/sbscs/assembly-searching-sequence)
* [Isolated Applications and Side-by-side Assemblies](https://learn.microsoft.com/en-us/windows/win32/sbscs/isolated-applications-and-side-by-side-assemblies-portal)
* [EVERYTHING YOU NEVER WANTED TO KNOW ABOUT WINSXS](https://omnicognate.wordpress.com/2009/10/05/winsxs/)
* [DLL Side-loading: A Thorn in the Side of the Anti-Virus Industry](http://www.fireeye.com/resources/pdfs/fireeye-dll-sideloading.pdf),
  by Amanda Stewart, April 2014

#### Crash dumps

* [Technet: Drwtsn32 on Windows Vista/Windows Server 2008/Windows 7/Windows Server 2008 R2](https://learn.microsoft.com/en-us/archive/blogs/),
  by Yong Rhee, December 29, 2010
* [MSDN: How to read the small memory dump file that is created by Windows if a crash occurs](https://learn.microsoft.com/en-US/troubleshoot/windows-client/performance/read-small-memory-dump-file),
   by [Microsoft](microsoft.md)
* <https://medium.com/dfir-dudes/amcache-is-not-alone-using-wer-files-to-hunt-evil-86bdfdb216d7>
* <https://learn.microsoft.com/en-us/windows/win32/wer/collecting-user-mode-dumps>
* <https://www.ired.team/offensive-security/credential-access-and-credential-dumping/dump-credentials-from-lsass-process-without-mimikatz>

#### Kerberos

* [Abusing Microsoft Kerberos - Sorry you guys don't get it](https://www.slideshare.net/gentilkiwi/abusing-microsoft-kerberos-sorry-you-guys-dont-get-it),
  by Benjamin Delpy, August 13, 2014

#### Reliability Monitoring

* [Stability Index and Reliability](https://secureartisan.wordpress.com/2011/01/17/stability-index-and-reliability/),
  by Paul Bobby, January 17, 2011
* [Windows 7 Reliability Monitor Forensic Artifacts](https://phx4n6.wordpress.com/2014/01/03/windows-7-reliability-monitor-forensic-artifacts/),
  by phx4n6, January 3, 2014

#### RPC

* [RPC to Go v.1](https://learn.microsoft.com/en-us/archive/blogs/),
  by Michael Platts, October 24, 2008
* [RPC to Go v.2](https://learn.microsoft.com/en-us/archive/blogs/),
  by Michael Platts, December 4, 2008

#### User Account Control (UAC)

* [User Account Control – What Penetration Testers Should Know](https://www.cobaltstrike.com/),
  by Raphael Mudge, March 20, 2014

#### Windows Event Logs

* [Exploring the Program Inventory Event Log](http://journeyintoir.blogspot.com/2014/03/exploring-program-inventory-event-log.html),
  by Corey Harrell, March 24, 2014
* [Mute Sysmon - Silence Sysmon via event manifest tampering](https://securityjosh.github.io/2020/04/23/Mute-Sysmon.html),
  by SecurityJosh, April 23, 2020
* [Common misconceptions about Windows EventLogs](https://osdfir.blogspot.com/2021/10/common-misconceptions-about-windows.html),
  by Joachim Metz, October 30, 2021

#### Windows Scripting Host

* [Going To Ground with The Windows Scripting Host (WSH)](https://www.mandiant.com/resources/blog),
  by Devon Kerr, February 19, 2014

#### USB

* [USB Key Analysis vs. USB Drive Enclosure Analysis](https://www.sans.org/blog/usb-key-analysis-vs-usb-drive-enclosure-analysis/)
  by Rob Lee, September 9, 2000
* [Computer Forensic Guide To Profiling USB Device Thumbdrives on Win7, Vista, and XP](https://www.sans.org/blog/computer-forensic-guide-to-profiling-usb-device-thumbdrives-on-win7-vista-and-xp/)
  by Rob Lee, September 9, 2009

#### Windows Error Reporting (WER)

* [Drwtsn32 on Windows Vista/Windows Server 2008/Windows 7/Windows Server 2008 R2](https://learn.microsoft.com/en-us/archive/blogs/),
  by Yong Rhee, December 29, 2010
* [Exploring Windows Error Reporting](http://journeyintoir.blogspot.com/2014/02/exploring-windows-error-reporting.html),
  by Corey Harrell, February 24, 2014

#### Windows Event Viewer

* [Windows Event Viewer created Scheduled Task of VBScript](https://www.intramortem.com/2015/12/windows-event-viewer-created-scheduled.html),
  by Eric John, December 23, 2015

#### Windows Firewall

* [Wikipedia: Windows Firewall](https://en.wikipedia.org/wiki/Windows_Firewall)
* [Windows Firewall Tools and Settings](https://learn.microsoft.com/en-us/previous-versions/windows/it-pro/windows-server-2003/cc737845(v=ws.10))

#### Windows 32-bit on Windows 64-bit (WoW64)

* [Wikipedia: WoW64](https://en.wikipedia.org/wiki/WoW64)

### Windows XP

* [Description of Windows XP System Information (Msinfo32.exe) Tool](https://support.microsoft.com/en-us/windows)

### Windows Vault

* [Windows ReVaulting](https://blog.digital-forensics.it/2016/01/windows-revaulting.html?m=1),
  by Francesco Picasso, January 27, 2016

### IPC

* [Offensive Windows IPC Internals 1: Named Pipes](https://csandker.io/2021/01/10/Offensive-Windows-IPC-1-NamedPipes.html),
  by Carsten Sandker, January 10, 2021

### AMCache.hve

### SysCache.hve

* [Daily Blog \#579: The meaning of Syscache.hve](https://www.hecfblog.com/2018/12/daily-blog-579-meaning-of-syscachehve.html),
  by David Cowen, December 26, 2018

### RDP Bitmap Cache

* [BMC-Tools by ANSSI-FR](https://github.com/ANSSI-FR/bmc-tools)
* [RDP Cached Bitmap Extractor by OpenText Security](https://security.opentext.com/appDetails/RDP-Cached-Bitmap-Extractor)
* [RDP Cache Stitcher by Bundesamt fuer Sicherheit in der Informationstechnik (BSI)](https://github.com/BSI-Bund/RdpCacheStitcher)
