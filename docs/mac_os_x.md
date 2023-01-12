---
tags:
  - Articles that need to be expanded
  - MacOS
  - Operating Systems
---
Apple Inc.'s Macintosh OS X (pronounced "**OS Ten**") is the operating system
distributed with Apple computers. It includes heavily used several programs by
default, including [Apple Mail](apple_mail.md), a web browser called
[Safari](apple_safari.md), and an Apple Address Book,
and iCal.

## EFI boot

The firmware is responsible for initializing the hardware and performing
a POST (Power-On Self Test).

The default boot volume is stored in NVRAM and can be configured through
the "Startup Disk" preference pane or the nvram command line utility
[1](https://developer.apple.com/library/mac/documentation/Darwin/Reference/Manpages/man8/nvram.8.html).
E.g. to print all of the firmware variables.

    nvram -p

Additional boot arguments can be provided via the "boot-args" value
[2](https://www.cnet.com/tech/computing/boot-argument-options-in-os-x/).

Mac OS X extends EFI with a read-only HFS+ driver. According to
[3](https://refit.sourceforge.net/info/boot_process.html) HFS+ volume
header fields are used to point to a "blessed file" to be loaded as an
EFI application. Though it is not clear which header field the source is
referring to but likely related to the "bless" utility
[4](https://developer.apple.com/library/mac/documentation/Darwin/Reference/Manpages/man8/bless.8.html).

The firmware starts the Mac OS X boot loader (boot.efi). The bootloader
displays a dark grey Apple logo on the screen and loads the Darwin
kernel from disk, as well as the essential driver extensions.

The bootloader can be eithe a MZ-PE/COFF or EFI fat binary type
[executables](executable.md) and is commonly stored in:

    /com.apple.recovery.boot/boot.efi
    /System/Library/CoreServices/boot.efi
    /usr/standalone/i386/boot.efi

The behavior of the bootloader can be configured in the
com.apple.Boot.plist
[5](https://developer.apple.com/library/mac/documentation/Darwin/Reference/ManPages/man5/com.apple.Boot.plist.5.html)
which can be found in:

    /Library/Preferences/SystemConfiguration/

## Disk image types

Mac OS X has support for various disk image types built-in, some of
which are:

* read-write disk image (.dmg), which can be stored in [Raw Image Format](raw_image_format.md)
  or [Universal Disk Image Format (udif)](dmg.md)
* Sparse disk image (.spareimage)
* Sparse bundle disk image (.sparsebundle)

## Burn Folder

Mac OS X Burn Folder:

    $NAME.fpbf

This folder normally contains alias files (similar to LNK files under
Windows). Which should have the following signature.

    00000000  62 6f 6f 6b 00 00 00 00  6d 61 72 6b 00 00 00 00  |book....mark....|

These alias files contain additional date and time values.

Also check the following files for references to deleted .fpbf paths:

    /Users/$USERNAME/Library/Preferences/com.apple.finder.plist
    /Users/$USERNAME/Library/Preferences/com.apple.sidebarlists.plist

Actual burning of optical media is logged in:

    /var/log/system.log
    /Users/$USERNAME/Library/Logs/DiscRecording.log
    /private/var/.logs_exporter/cache/Users/$USERNAME/Library/Logs/DiscRecording.log

## Launch Agents

System-wide:

    /Library/LaunchAgents
    /System/Library/LaunchAgents

Per user:

    /Users/$USERNAME/Library/LaunchAgents

These directories contain [Property list
(plist)](property_list_(plist).md) files.

## Launch Daemons

System-wide:

    /Library/LaunchDaemons
    /System/Library/LaunchDaemons

These directories contain [Property list
(plist)](property_list_(plist).md) files.

## Startup Items

    /Library/StartupItems/
    /System/Library/StartupItems/

## Crash Reporter

    /Library/Application Support/CrashReporter

Contains text files named .crash, .diag, .spin

## Diagnostic Reports

    /Library/Logs/DiagnosticReports

## Internet Plug-Ins

System-wide:

    /Library/Internet Plug-Ins

Per user:

    /Users/$USERNAME/Library/Internet Plug-Ins

## Quarantine event database

See
[6](https://menial.co.uk/blog/2011/06/16/mac-quarantine-event-database/)

Snow Leopard and earlier

    /Users/$USER/Library/Preferences/com.apple.LaunchServices.QuarantineEvents

    SELECT datetime(LSQuarantineTimeStamp + 978307200, "unixepoch") as LSQuarantineTimeStamp, LSQuarantineAgentName, LSQuarantineOriginURLString, LSQuarantineDataURLString from LSQuarantineEvent;

Lion and later

    /Users/$USER/Library/Preferences/com.apple.LaunchServices.QuarantineEventsV2

## sleepimage

This file is similar to the hibernation file on Windows.

    /private/var/vm/sleepimage

Also see: [7](https://osxdaily.com/2010/10/11/sleepimage-mac/)

## Last shutdown logs

    /private/var/log/com.apple.launchd/launchd-shutdown.system.log
    /private/var/log/com.apple.launchd/launchd-shutdown.system.log.1

## Package Files (.PKG)

Package Files (.PKG) are [XAR archives](https://en.wikipedia.org/wiki/Xar_(archiver)) that contain a cpio
archive and metadata
[9](http://s.sudre.free.fr/Stuff/Ivanhoe/FLAT.html).

## Encodings / Codepages

Mac OS X typically uses UTF-16 big-endian to store Unicode strings, it
also defines several codepages
[10](https://opensource.apple.com/source/CF/CF-1151.16/CFStringEncodingExt.h.auto.html)
that can be used to store ASCII strings.

Note that some of these codepages can differ for different versions of
Mac OS.

| Codepage | Identifier         | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
|----------|--------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 0        | MacRoman           | Encoding used for English and several other Western languages, also see: [Wikipedia: Mac OS Roman](https://en.wikipedia.org/wiki/Mac_OS_Roman),[Unicode.org: ROMAN.TXT](https://www.unicode.org/Public/MAPPINGS/VENDORS/APPLE/ROMAN.TXT) (sometimes referred to as Microsoft codepage 10000 though it is unclear if this is the pre Mac OS 8.5 MacRoman variant)                                                                                                                                                                                                                                                                                                                                                                                                         |
| 1        | MacJapanese        | also see: [Unicode.org: JAPANESE.TXT](https://www.unicode.org/Public/MAPPINGS/VENDORS/APPLE/JAPANESE.TXT) (sometimes referred to as Mac Shift Jis or Microsoft codepage 10001)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| 2        | MacChineseTrad     | also see: [Unicode.org: CHINTRAD.TXT](https://www.unicode.org/Public/MAPPINGS/VENDORS/APPLE/CHINTRAD.TXT) (sometimes referred to as Mac Big5 or Microsoft codepage 10002)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| 3        | MacKorean          | also see: [Unicode.org: KOREAN.TXT](https://www.unicode.org/Public/MAPPINGS/VENDORS/APPLE/KOREAN.TXT) (sometimes referred to as Mac Hangul or Microsoft codepage 10003)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| 4        | MacArabic          | Encoding used for Arabic texts, also see: [Wikipedia: MacArabic encoding](https://en.wikipedia.org/wiki/MacArabic_encoding), [Unicode.org: ARABIC.TXT](https://www.unicode.org/Public/MAPPINGS/VENDORS/APPLE/ARABIC.TXT) (sometimes referred to as Microsoft codepage 10004). Note that certain Unicode characters can be translated into multiple codepage characters such as U+0020 can be represented as 0x20 or 0xa0.                                                                                                                                                                                                                                                                                                                                                |
| 5        | MacHebrew          | also see: [Unicode.org: HEBREW.TXT](https://www.unicode.org/Public/MAPPINGS/VENDORS/APPLE/HEBREW.TXT) (sometimes referred to as Microsoft codepage 10005)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| 6        | MacGreek           | Encoding used for Greek scripts, [Wikipedia: MacGreek encoding](https://en.wikipedia.org/wiki/MacGreek_encoding), [Unicode.org: GREEK.TXT](https://www.unicode.org/Public/MAPPINGS/VENDORS/APPLE/GREEK.TXT) (sometimes referred to as Microsoft codepage 10006)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| 7        | MacCyrillic        | Encoding used for Cyrillic scripts, also see: [Wikipedia: Mac OS Cyrillic encoding](https://en.wikipedia.org/wiki/Mac_OS_Cyrillic_encoding), [Unicode.org: CYRILIC.TXT](https://www.unicode.org/Public/MAPPINGS/VENDORS/APPLE/CYRILIC.TXT). Note that MacCyrillic supersedes the MacCyrillic encoding prior to Mac OS 9.0 (sometimes referred to as MacCyrillicCurrSignStdVariant, MacRussian or Microsoft codepage 10007) and [MacUkrainian](https://en.wikipedia.org/wiki/Mac_OS_Ukrainian_encoding), [Unicode.org: UKRAINE.TXT](https://www.unicode.org/Public/MAPPINGS/VENDORS/APPLE/UKRAINE.TXT) (sometimes referred to as MacCyrillicCurrSignUkrVariant or Microsoft codepage 10017). |
| 9        | MacDevanagari      | also see: [Unicode.org: DEVANAGA.TXT](https://www.unicode.org/Public/MAPPINGS/VENDORS/APPLE/DEVANAGA.TXT)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| 10       | MacGurmukhi        | also see: [Unicode.org: GURMUKHI.TXT](https://www.unicode.org/Public/MAPPINGS/VENDORS/APPLE/GURMUKHI.TXT)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| 11       | MacGujarati        | also see: [Unicode.org: GUJARATI.TXT](https://www.unicode.org/Public/MAPPINGS/VENDORS/APPLE/GUJARATI.TXT)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| 12       | MacOriya           |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| 13       | MacBengali         |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| 14       | MacTamil           |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| 15       | MacTelugu          |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| 16       | MacKannada         |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| 17       | MacMalayalam       |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| 18       | MacSinhalese       |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| 19       | MacBurmese         |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| 20       | MacKhmer           |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| 21       | MacThai            | also see: [Wikipedia: ISO/IEC 8859-11 - Mac OS Thai](https://en.wikipedia.org/wiki/ISO/IEC_8859-11#Mac_OS_Thai), [Unicode.org: THAI.TXT](https://www.unicode.org/Public/MAPPINGS/VENDORS/APPLE/THAI.TXT) (sometimes referred to as Microsoft codepage 10021)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| 22       | MacLaotian         |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| 23       | MacGeorgian        |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| 24       | MacArmenian        |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| 25       | MacChineseSimp     | also see: [Unicode.org: CHINSIMP.TXT](https://www.unicode.org/Public/MAPPINGS/VENDORS/APPLE/CHINSIMP.TXT) (sometimes referred to as Mac GB2312 or Microsoft codepage 10008)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| 26       | MacTibetan         |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| 27       | MacMongolian       |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| 28       | MacEthiopic        |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| 29       | MacCentralEurRoman | Encoding used for languages that use the Latin script, such as Central European and Southeastern European languages, also see: [Wikipedia: Mac OS Central European encoding](https://en.wikipedia.org/wiki/Mac_OS_Central_European_encoding), [Unicode.org: CENTEURO.TXT](https://www.unicode.org/Public/MAPPINGS/VENDORS/APPLE/CENTEURO.TXT) (sometimes referred to as Mac East Europe or Microsoft codepage 10029)                                                                                                                                                                                                                                                                                                                                                     |
| 30       | MacVietnamese      |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| 31       | MacExtArabic       |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| 33       | MacSymbol          | also see: [Unicode.org: SYMBOL.TXT](https://www.unicode.org/Public/MAPPINGS/VENDORS/APPLE/SYMBOL.TXT)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| 34       | MacDingbats        | also see: [Wikipedia: Zapf Dingbats](https://en.wikipedia.org/wiki/Zapf_Dingbats), [Unicode.org: DINGBATS.TXT](https://www.unicode.org/Public/MAPPINGS/VENDORS/APPLE/DINGBATS.TXT)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| 35       | MacTurkish         | also see: [Wikipedia: Mac OS Turkish encoding](https://en.wikipedia.org/wiki/Mac_OS_Turkish_encoding), [Unicode.org: TURKISH.TXT](https://www.unicode.org/Public/MAPPINGS/VENDORS/APPLE/TURKISH.TXT) (sometimes referred to as Microsoft codepage 10081)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| 36       | MacCroatian        | also see: [Wikipedia: Mac OS Croatian encoding](https://en.wikipedia.org/wiki/Mac_OS_Croatian_encoding),[Unicode.org: CROATIAN.TXT](https://www.unicode.org/Public/MAPPINGS/VENDORS/APPLE/CROATIAN.TXT) (sometimes referred to as Microsoft codepage 10082)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| 37       | MacIcelandic       | also see: [Wikipedia: Mac OS Icelandic encoding](https://en.wikipedia.org/wiki/Mac_OS_Icelandic_encoding), [Unicode.org: ICELAND.TXT](https://www.unicode.org/Public/MAPPINGS/VENDORS/APPLE/ICELAND.TXT) (sometimes referred to as Microsoft codepage 10079)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| 38       | MacRomanian        | also see: [Wikipedia: Mac OS Romanian encoding](https://en.wikipedia.org/wiki/Mac_OS_Romanian_encoding),[Unicode.org: ROMANIAN.TXT](https://www.unicode.org/Public/MAPPINGS/VENDORS/APPLE/ROMANIAN.TXT) (sometimes referred to as Microsoft codepage 10010)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| 39       | MacCeltic          | also see: [Unicode.org: CELTIC.TXT](https://www.unicode.org/Public/MAPPINGS/VENDORS/APPLE/CELTIC.TXT)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| 40       | MacGaelic          | also see: [Unicode.org: GAELIC.TXT](https://www.unicode.org/Public/MAPPINGS/VENDORS/APPLE/GAELIC.TXT)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| 140      | MacFarsi           | also see: [Wikipedia: MacFarsi encoding](https://en.wikipedia.org/wiki/MacFarsi_encoding), [Unicode.org: FARSI.TXT](https://www.unicode.org/Public/MAPPINGS/VENDORS/APPLE/FARSI.TXT)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| 152      | MacUkrainian       | see: MacCyrillic                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| 236      | MacInuit           | also see: [Unicode.org: INUIT.TXT](https://www.unicode.org/Public/MAPPINGS/VENDORS/APPLE/INUIT.TXT)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| 252      | MacVT100           |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| 255      | MacHFS             |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| 2564     | MacRomanLatin1     |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |

## Also see

* [MacOS Process Monitoring](macos_process_monitoring.md)
* [Acquiring a MacOS System with Target Disk Mode](acquiring_a_macos_system_with_target_disk_mode.md)
* [Converting Binary Plists](converting_binary_plists.md)
* [FileVault Disk Encryption](filevault_disk_encryption.md)
* [File Vault](file_vault.md)

### Formats

* [Apple File System (apfs)](apple_file_system_(apfs).md)
* [Apple Partition Map (apm)](apm.md)
* [Basic Security Module (BSM) file format](basic_security_module_(bsm)_file_format.md)
* [DMG](dmg.md)
* [Hierarchical File System Plus (HFS+) format](hfs+.md)
* [Property list (plist)](property_list_(plist).md)

## External Links

* [Official website](https://www.apple.com/macos/ventura/)
* [Wikipedia entry on OS X](https://en.wikipedia.org/wiki/OS_X)
* [Inside Macintosh](https://developer.apple.com/library/archive/documentation/mac/pdf/Text.pdf),
  by Apple Computer, Inc., 1993
* [What is Mac OS X?](http://osxbook.com/book/bonus/ancient/whatismacosx/whatismacosx.pdf),
  by Amit Singh, 1994
* [Mac OS X Directory Services Integration including Active Directory](http://web.me.com/driley/iWeb/Previous_files/Directory_Services_Overview.pdf)
* [NSKeyedArchiver files – what are they, and how can I use them?](https://digitalinvestigation.wordpress.com/2012/04/04/geek-post-nskeyedarchiver-files-what-are-they-and-how-can-i-use-them/)
* [Command Line ALF on Mac OS X](https://krypted.com/mac-os-x/command-line-alf-on-mac-os-x/)
* [mac-security-tips](https://code.google.com/archive/p/mac-security-tips/wikis/ALL_THE_TIPS.wiki)
* [Mac OS X Forensics](https://www.ma.rhul.ac.uk/static/techrep/2015/RHUL-MA-2015-8.pdf),
  by Joaquin Moreno Garijo, March 4, 2015
* [Hidden backdoor API to root privileges in Apple OS X](https://truesecdev.wordpress.com/2015/04/09/hidden-backdoor-api-to-root-privileges-in-apple-os-x/),
  by Emil Kvarnhammar, April 9, 2015
* [Max OS X Internals book (1st ed)](http://newosxbook.com/1stEdIsFree.html) by Jonathan Levin PDF
  download
* [The Boot Loader](https://developer.apple.com/library/archive/documentation/Darwin/Conceptual/KernelProgramming/booting/booting.html),
  by Apple

### Alias

* [Reversing Mac Alias v3 Data
  Objects](http://survey-smiles.com), by
  Patrick Olsen, August 15, 2016

### Apple Examiner

* [The Apple Examiner](http://www.appleexaminer.com/)
* [USB Entries on OS X](http://www.appleexaminer.com)
* [Macintosh Forensics - A Guide for the Forensically Sound Examination of a Macintosh Computer](http://www.appleexaminer.com),
  by Ryan R. Kubasiak

### EFI

* [The Intel Mac boot process](https://refit.sourceforge.net/info/boot_process.html), by the
  [rEFIt project](refit.md) - [Carving up EFI fat binaries](http://ho.ax/posts/2012/02/carving-up-efi-fat-binaries/),
  by snare, February 24, 2012

### iCloud

* [iCloud: iCloud security and privacy overview](https://support.apple.com/en-us/HT202303)

### ColorSync

* [Technical Note TN2035 - ColorSync on Mac OS X](https://developer.apple.com/library/archive/technotes/tn2035/_index.html)
* [Internet Archive: Managing Color With ColorSync](https://web.archive.org/web/20001118053700/http://developer.apple.com/techpubs/macos8/MultimediaGraphics/ColorSyncManager/ManagingColorWithColorSync/ColorSync.7b.html)
* [ICC.1:2004-10 - Image technology colour management - Architecture, profile format, and data structure](https://www.color.org/icc1v42.pdf),
  by International Color Consortium (ICC)
* [ICC Profile Format Specification](https://www.color.org/icc32.pdf), by
  International Color Consortium (ICC), November 20, 1995
* [ICC profiles](https://www.color.org/profiles2.xalter)
* [ICC_Profile Tags](https://exiftool.org/TagNames/ICC_Profile.html)
* [Adobe XMP Developer Center](https://www.adobe.com/devnet/xmp.html)

### Quarantine event database

* [Quarantine event database](https://menial.co.uk/blog/2011/06/16/mac-quarantine-event-database/)

### Unified logging

* [New macOS Sierra (10.12) Forensic Artifacts – Introducing Unified Logging](https://www.mac4n6.com/blog/2016/11/13/new-macos-sierra-1012-forensic-artifacts-introducing-unified-logging),
  by Sarah Edwards, November 13, 2016

### Yet Another Assembler (YAA)

* [YAA: An Obscure MacOS Compressed File Format](https://wwws.nightwatchcybersecurity.com/2020/06/14/yaa-an-obscure-macos-compressed-file-format/),
  by nightwatchcyber, June 14, 2020
