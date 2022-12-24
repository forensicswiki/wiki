---
tags:
  -  Online File Storage
---
## Overview

[Dropbox](http://www.dropbox.com) is a service with dedicated applications
allowing people to share their files between multiple computers (including
smartphones) and each other. It is thus similar in purpose to
[Wuala](wuala.md), [SpiderOak](spideroak.md) and [Box.com](box.com).

## Security

Dropbox has been shown to have major design flaws, making it very
insecure. A key problem is that the files are encrypted by Dropbox's
servers, which allows Dropbox (and legal authorities) to get access to
the files. In June 2011 Dropbox accidentally broke their authentication
control system and allowed access to any account without a password, and
thus potentially every user's files to be exposed to the world.

## Client Application

The Dropbox client running on windows was analyzed and shown to leave a
significant amount of data debris behind when deleted. An overview of
the report is
[here](http://computer-forensics.sans.org/blog/2011/06/17/digital-forensics-rain-drop-keeps-falling-on-my-box).
Even after deletion of the application, this would allow a forensic
analyst to detect that Dropbox has been in use, potentially identify
other computers linked to the same account, and potentially recover
files that were shared using the service.

Server-side file encryption has some benefits to both user and provider,
in that if someone uploads a file already stored by Dropbox, then the
client makes a fingerprint (hash) of the file and Dropbox's servers will
flag that the file doesn't need to be uploaded, so the client "upload"
process completes much faster. However, this also means that it is
possible to detect if a file has already been stored by Dropbox, and
therefore a legal authority can take action against Dropbox to identify
other "owners".

### Configuration

Windows XP

    C:\Documents and Settings\%USERNAME%\Application Data\Dropbox\
    C:\Documents and Settings\%USERNAME%\Local Settings\Application Data\Dropbox\

Windows Vista and later

    C:\Users\%USERNAME%\AppData\Local\Dropbox\
    C:\Users\%USERNAME%\AppData\Roaming\Dropbox\

Mac OS X

    /Users/$USER/.dropbox/

Linux

    /home/$USER/.dropbox/

### config.db and config.dbx

The "config.db" SQLite database contains the configuration for the
account. It contains:

- the email address associated with the account;
- the "host_id";
- local path information.

"config.dbx" is an encrypted variant of "config.db"

### filecache.db and filecache.dbx

### host.db and host.dbx

## Server Side

According to [online help](https://www.dropbox.com/help/7), "All files
stored online by Dropbox are encrypted and kept securely on Amazon's
Simple Storage Service (S3) in multiple data centers located across the
United States."

## External Links

- [Dropbox](http://www.dropbox.com)
- [Digital Forensics:
  Dropbox](https://digital-forensics.sans.org/blog/2011/06/17/digital-forensics-rain-drop-keeps-falling-on-my-box),
  by Frank McClain, June 17, 2011
- [Dropbox Forensics](http://www.forensicfocus.com/dropbox-forensics),
  by Frank McClain
- [Decrypting More Dropbox Files:
  config.dbx](http://www.magnetforensics.com/decrypting-the-config-dbx-file/),
  Magnet Forensics, November 20, 2013
- [Cloud Storage
  Forensics](https://digital-forensics.sans.org/summit-archives/Prague_Summit/Cloud_Storage_Forensics_Mattia_Eppifani.pdf),
  by Mattia Epifani, October 7, 2013

## Tools

- [Dropbox
  Reader](http://www.cybermarshal.com/index.php/cyber-marshal-utilities/dropbox-reader)

