---
tags:
  - No Category
---
## User's Configuration

    /etc/passwd: Contain basic users data. UID 0 are reserved for root, 1-99 reserved for predefined accounts ,and 100-999 reserved for system accounts/groups. Format 'username:x:UID:GID:Userinfo:homedir:shell'

    /etc/shadow: Contain the password hashes of the users. Can be cracked using 'John The Ripper' or 'HashCat

    /etc/sudoers: controls who can run what commands as what users on what machines

    /etc/group: Contains groups memberships

## Backups

    Files that end with the '~' character (passwd~) are the previous version of the original file (passed).

## Home

Home folder of each user is located under '/home/<username>/' and for
root home folder is '/root/'.

    Artifacts: .bash_hisotry, App specific configuration files and ssh configurations