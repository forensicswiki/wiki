---
tags:
  - Mobile
  - Operating Systems
---
iOS (pronounced i-O.S.) is the name of the operating system for Apple's
mobile devices (iPhone/iPad/iPod Touch).

------------------------------------------------------------------------

## File System

iOS runs a reduced variant of [OSX](mac_os_x.md) and
[HFSX](hfs+.md) as a file system.

A majority of the useful information is stored in /private/var2/mobile/
However there is other useful information stored in the keychains and db
folders.

iOS uses sqlite and plist files to store information.

**/private/var2/mobile**

This contains three folders: Applications, Library and Media

Applications contains a series of folders, which contain the data for
all of the apps stored on the phone. The name of each app is stored in
its iTunesMetadata.plist.

Library contains the most useful information: - Address Book -
Calendar - Safari - favorites, open tabs, web history - Mail - mail is
encrypted and therefore requires the keychain to be decrypted before it
can be accessed - SMS - sms.db, which may include deleted SMS messages -
Notes - notes.sqlite, which may include deleted notes - Voicemail -
Spotlight - Spotlight database may contain text messages that have since
been deleted.

Media contains all Photos loaded onto the device, Books, Purchases,
Podcasts, Recordings and Pictures/Videos taken

## Extraction

There are several tools available to extract information out of iOS
operating systems (listed alphabetically):

* Aceso by Radio Tactics
  [1](https://radio-tactics.com)
* Lantern by Katana Forensics [3](https://katanaforensics.com/)
* [Nuix Desktop](nuix_desktop.md) and [Proof Finder](proof_finder.md) by
  [Nuix](nuix.md).
* Oxygen Forensic Suite by Oxygen Software
  [4](https://www.oxygen-forensic.com/en/)
* UFED and Physical Analyzer by Cellebrite
  [5](https://cellebrite.com/en/home/)
* XRY by [Micro Systemation](https://www.msab.com/)

## See Also

* [Cell Phone Forensics](cell_phone_forensics.md)

## External Links

* [The Future of Mobile Forensics](https://belkasoft.com/future-of-mobile-forensics),
  article by [Belkasoft](belkasoft.md)
* [Database Parsing Tools](https://linuxsleuthing.blogspot.com/2011/05/iphone-forensics-tools.html)
* [iOS (iPhone OS) Forensics](https://www.systoolsgroup.com/forensics/sqlite/ios.html)
