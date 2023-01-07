---
tags:
  -  Online File Storage
---
## Overview

[Dropbox](https://www.dropbox.com/) is a service with dedicated applications
allowing people to share their files between multiple computers (including
smartphones) and each other. It is thus similar in purpose to
[Wuala](wuala.md), [SpiderOak](spideroak.md) and Box.com.

## Security

Dropbox has been shown to have major design flaws, making it very
insecure. A key problem is that the files are encrypted by Dropbox's
servers, which allows Dropbox (and legal authorities) to get access to
the files. In June 2011 Dropbox accidentally broke their authentication
control system and allowed access to any account without a password, and
thus potentially every user's files to be exposed to the world.

## Client Application

The Dropbox client running on windows was analyzed and shown to leave a
significant amount of data debris behind when deleted.

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

Per [Where is my data stored?](https://help.dropbox.com/security/physical-location-data-storage)

```
All files stored online by Dropbox are encrypted and kept in secure storage
servers. Storage servers are located in data centers across the United States.
Additionally, storage servers are available in Australia, the European Union,
Japan, and the United Kingdom for eligible Dropbox business users
```

## External Links

- [Product site](https://www.dropbox.com/)
- [Dropbox Forensics](https://www.forensicfocus.com/articles/dropbox-forensics/)
  by Frank McClain, July 24, 2011
- [Decrypting More Dropbox Files: config.dbx](https://www.magnetforensics.com/resources/),
  Magnet Forensics, November 20, 2013
