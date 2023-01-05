---
tags:
  - Operating Systems
---
## New Features

- [BitLocker To Go](bitlocker_disk_encryption.md)
- [Jump Lists](jump_lists.md)
- [Sticky Notes](sticky_notes.md)

## File System

The file system used by Windows 7 is primarily [NTFS](ntfs.md).

## SSD

Per MS KB2727880, when Windows 7 is installed on a system with an SSD drive,
automatic defragmentation and SuperFetch/prefetching are disabled.

Further, [this TechNet
post](https://learn.microsoft.com/en-us/previous-versions/technet-magazine/ff356869(v=msdn.10)?redirectedfrom=MSDN) states:

> Since ReadyBoost will not provide a performance gain when the primary
> disk is an SSD, Windows 7 disables ReadyBoost when reading from an SSD
> drive.

## Jump Lists

[Jump Lists](jump_lists.md) are Task Bar artifacts first
introduced on Windows 7 (and also available on Windows 8).

## [Prefetch](prefetch.md)

The prefetch hash function is similar to Windows 2008.

## Registry

The [Windows Registry](windows_registry.md) remains a central
component of the Windows 7 operating system.

### Known Registry keys of forensic interest

<b>TODO: add some description why they are of interest</b>

#### SAM Registry

- SAM\SAM\Domains\Account\Users
- SAM\SAM\Domains\Builtin\Aliases

#### Security Registry

- Security\Policy\PolAcDmSPolicy\PolPrDmS
- Security\Policy\PolAdtEv
- Security\Policy\Secrets

#### NTUSER Registry

- NTUSER\Control Panel\Desktop
- NTUSER\Control Panel\don\\
- NTUSER\Environment
- NTUSER\Network
- NTUSER\Printers\Settings\Wizard\ConnectMRU
- NTUSER\Software\Adobe\Acrobat Reader\Software\Adobe\Acrobat Reader\\
- NTUSER\Software\Ahead
- NTUSER\Software\America Online\AOL Instant Messenger
  (TM)\CurrentVersion\Users
- NTUSER\Software\Ares
- NTUSER\Software\bindshell.net\Odysseus
- NTUSER\Software\Blizzard Entertainment\Warcraft III\String
- NTUSER\Software\Cain\Settings
- NTUSER\Software\DECAFme
- NTUSER\Software\Google\Google Toolbar\4.0\whitelist
- NTUSER\Software\Google\NavClient\1.1\History
- NTUSER\Software\JavaSoft\Java Update\Policy\JavaFX
- NTUSER\Software\JavaSoft\Prefs\haven
- NTUSER\Software\Microsoft
- NTUSER\Software\Microsoft\Command Processor
- NTUSER\Software\Microsoft\Dependency Walker\Recent File List
- NTUSER\Software\Microsoft\IntelliPoint\AppSpecific
- NTUSER\Software\Microsoft\Internet Explorer\Main
- NTUSER\Software\Microsoft\Internet
  Explorer\MainSoftware\Microsoft\Windows\CurrentVersion\Explorer\AutoCompleteSoftware\Microsoft\Internet
  Account Manager\Accounts
- NTUSER\Software\Microsoft\Internet Explorer\Settings
- NTUSER\Software\Microsoft\Internet Explorer\TypedURLs
- NTUSER\Software\Microsoft\Internet Explorer\TypedURLsTime
- NTUSER\Software\Microsoft\MediaPlayer\Player\RecentFileList
- NTUSER\Software\Microsoft\Microsoft Management Console\Recent File
  List
- NTUSER\Software\Microsoft\Multimedia\OtherSoftware\Microsoft\CTF\LangBarAddIn
- NTUSER\Software\Microsoft\Office\14.0Software\Microsoft\Office\14.0
- NTUSER\Software\Microsoft\Office\Software\Microsoft\Office\\
- NTUSER\Software\Microsoft\OfficeSoftware\Microsoft\Office\\
- NTUSER\Software\Microsoft\PIMSRV
- NTUSER\Software\Microsoft\Search Assistant\ACMru
- NTUSER\Software\Microsoft\Snapshot Viewer\Recent File List
- NTUSER\Software\Microsoft\Terminal Server
  Client\DefaultSoftware\Microsoft\Terminal Server Client\Servers
- NTUSER\Software\Microsoft\Terminal Server Client\Servers
- NTUSER\Software\Microsoft\User Location Service\Client
- NTUSER\Software\Microsoft\Windows Live Contacts\Database
- NTUSER\Software\Microsoft\Windows Live Mail
- NTUSER\Software\Microsoft\Windows
  NT\CurrentVersion\AppCompatFlags\Compatibility Assistant\Persisted
- NTUSER\Software\Microsoft\Windows
  NT\CurrentVersion\AppCompatFlags\Layers
- NTUSER\Software\Microsoft\Windows NT\CurrentVersion\PrinterPorts
- NTUSER\Software\Microsoft\Windows NT\CurrentVersion\Windows
- NTUSER\Software\Microsoft\Windows NT\CurrentVersion\Windows Messaging
  Subsystem\Profiles
- NTUSER\Software\Microsoft\Windows NT\CurrentVersion\Windows Messaging
  Subsystem\Profiles\Outlook\0a0d020000000000c000000000000046
- NTUSER\Software\Microsoft\Windows\CurrentVersion
- NTUSER\Software\Microsoft\Windows\CurrentVersion\App
  Management\ARPCache
- NTUSER\Software\Microsoft\Windows\CurrentVersion\Applets
- NTUSER\Software\Microsoft\Windows\CurrentVersion\Explorer
- NTUSER\Software\Microsoft\Windows\CurrentVersion\Explorer\BitBucket
- NTUSER\Software\Microsoft\Windows\CurrentVersion\Explorer\ComDlg32
- NTUSER\Software\Microsoft\Windows\CurrentVersion\Explorer\ComputerDescriptions
- NTUSER\Software\Microsoft\Windows\CurrentVersion\Explorer\ControlPanel
- NTUSER\Software\Microsoft\Windows\CurrentVersion\Explorer\FileExts
- NTUSER\Software\Microsoft\Windows\CurrentVersion\Explorer\Map Network
  Drive MRU
- NTUSER\Software\Microsoft\Windows\CurrentVersion\Explorer\MenuOrder
- NTUSER\Software\Microsoft\Windows\CurrentVersion\Explorer\MountPoints2
- NTUSER\Software\Microsoft\Windows\CurrentVersion\Explorer\PublishingWizard\AddNetworkPlace\AddNetPlace\LocationMRU
- NTUSER\Software\Microsoft\Windows\CurrentVersion\Explorer\RecentDocs
- NTUSER\Software\Microsoft\Windows\CurrentVersion\Explorer\RunMRU
- NTUSER\Software\Microsoft\Windows\CurrentVersion\Explorer\Shell
  Folders
- NTUSER\Software\Microsoft\Windows\CurrentVersion\Explorer\StartPage
- NTUSER\Software\Microsoft\Windows\CurrentVersion\Explorer\StreamMRU
- NTUSER\Software\Microsoft\Windows\CurrentVersion\Explorer\TypedPaths
- NTUSER\Software\Microsoft\Windows\CurrentVersion\Explorer\UserAssist
- NTUSER\Software\Microsoft\Windows\CurrentVersion\Explorer\Wallpaper\MRU
- NTUSER\Software\Microsoft\Windows\CurrentVersion\Explorer\WordWheelQuery
- NTUSER\Software\Microsoft\Windows\CurrentVersion\Ext\Settings\\{8AD9C840-044E-11D1-B3E9-00805F499D93}
- NTUSER\Software\Microsoft\Windows\CurrentVersion\FileHistory
- NTUSER\Software\Microsoft\Windows\CurrentVersion\Internet Settings
- NTUSER\Software\Microsoft\Windows\CurrentVersion\Internet
  Settings\ZoneMap
- NTUSER\Software\Microsoft\Windows\CurrentVersion\Internet
  SettingsSoftware\Microsoft\Internet Explorer\Main\WindowsSearch
- NTUSER\Software\Microsoft\Windows\CurrentVersion\Policies\Explorer
- NTUSER\Software\Microsoft\Windows\CurrentVersion\UFH\SHC
- NTUSER\Software\Microsoft\Windows\CurrentVersion\UnreadMail
- NTUSER\Software\Microsoft\Windows\Shell\Bags\1\Desktop
- NTUSER\Software\Nico Mak Computing\WinZip
- NTUSER\Software\ORL\VNCHooks\Application_Prefs
- NTUSER\Software\ORL\VNCviewer\MRUSoftware\RealVNC\VNCViewer4\MRU
- NTUSER\Software\Piriform\CCleaner
- NTUSER\Software\Privoxy
- NTUSER\Software\RealNetworks\RealPlayer\6.0\Preferences
- NTUSER\Software\RealVNC\VNCViewer4\MRU
- NTUSER\Software\SimonTatham\PuTTY\SshHostKeys
- NTUSER\Software\Skype
- NTUSER\Software\SmartLine Vision\aports
- NTUSER\Software\SysInternals
- NTUSER\Software\Sysinternals\RootkitRevealer
- NTUSER\Software\VMware
- NTUSER\Software\WinRAR\ArcHistory

## See Also

- [Windows](windows.md)
- [Windows Vista](windows_vista.md)
- [Windows 8](windows_8.md)

## External Links

- [The Windows 7 Event Log and USB Device Tracking](https://dfstream.blogspot.com/2014/01/the-windows-7-event-log-and-usb-device.html),
  by Jason Hale, January 2, 2014
- [Windows 7 DLL File Information](http://www.win7dll.info/)
