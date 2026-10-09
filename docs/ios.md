---
tags:
  - Mobile
  - Operating Systems
---
iOS (pronounced i-O.S.) is the name of the operating system for Apple's
mobile devices (iPhone/iPad/iPod Touch).

## File System

iOS runs a reduced variant of [OSX](mac_os_x.md) and
[HFSX](hfs+.md) as a file system.

A majority of the useful information is stored in the folder
"/private/var2/mobile/". However there is other useful information stored in
the keychains and db folders.

iOS uses sqlite and plist files to store information.

### /private/var2/mobile folder

This folder contains three sub folders:

* Applications
* Library
* Media

Applications contains a series of folders, which contain the data for
all of the apps stored on the phone. The name of each app is stored in
its iTunesMetadata.plist.

Library contains the most useful information:

* Address Book
* Calendar
* Mail - mail is encrypted and therefore requires the keychain to be decrypted
  before it can be accessed
* Notes - notes.sqlite, which may include deleted notes
* Safari - favorites, open tabs, web history
* SMS - sms.db, which may include deleted SMS messages
* Spotlight - Spotlight database may contain text messages that have since been
  deleted.
* Voicemail

Media contains all Photos loaded onto the device, Books, Purchases,
Podcasts, Recordings and Pictures/Videos taken

## Extraction

There are several tools available to extract information out of iOS
operating systems (listed alphabetically):

* [Aceso by Radio Tactics](https://radio-tactics.com)
* [Nuix Desktop](nuix_desktop.md)
* [Oxygen Forensic Suite](oxygen_forensic_suite.md)
* UFED and Physical Analyzer by Cellebrite
  [5](https://cellebrite.com/en/home/)
* XRY by [Micro Systemation](https://www.msab.com/)

## See Also

* [Cell Phone Forensics](cell_phone_forensics.md)

## External Links

* [Future of Mobile Forensics](https://belkasoft.com/future-of-mobile-forensics),
  by [Belkasoft](belkasoft.md)
* [iPhone Forensics Tools](https://linuxsleuthing.blogspot.com/2011/05/iphone-forensics-tools.html),
  May 4, 2011
* [Getting Started with iOS Forensics](https://www.systoolsgroup.com/forensics/sqlite/ios.html)
