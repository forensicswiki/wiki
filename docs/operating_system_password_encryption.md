---
tags:
  - No Category
---
## Unix/Linux Password File

Unix and its various clones have traditionally used the /etc/passwd file
to store user account information, including passwords. Because the
/etc/password file needs to be world-readable in order for utilities
such as \`ls\` and \`finger\` to work modern Unix operating systems
store the encrypted passwords in 'shadow' file named /etc/shadow.

| Username       | The user's username                                                                                                       |
|----------------|---------------------------------------------------------------------------------------------------------------------------|
| Password       | Older Unixes store the password crypt here, more modern ones use an 'x' character to denote that a shadow file is in use. |
| UID            | The numeric user ID of the user                                                                                           |
| GID            | The primary numeric group ID of the user                                                                                  |
| GECOS Field    | This is a text field which may contain information about the user such as name and contact details                        |
| Home directory | The user's home directory                                                                                                 |
| Shell          | The user's Unix shell                                                                                                     |

    user1:x:600:600:User 1:/home/user1:/bin/bash
    user2:x:601:601:User 2:/home/user2:/bin/bash
    admin:x:602:602:Admin Account:/home/admin:/bin/bash
    apache:x:603:603:Apache HTTP User:/var/www:/bin/bash
    someguy:x:604:604:Someguy:/home/someguy:/bin/bash

The password is stored as an encrypted one-way hash of the original
password. When a user attempts to authenticate the password supplied is
encrypted using the same algorithm and compared to the stored password
crypt.

### Unix Crypt

The most commonly used password encryption in Unix for many year was
crypt(). The Unix crypt command can be used to generate the Unix crypt
value for a given string.

    jim@localhost ~
    $ crypt hello
    S84xRArsM.gtk

In modern computing Unix crypt is severly limited. Passwords are
restricted to 8 character passwords, and any trailing character as
ignored. This puts brute force attacks on Unix crypts well within the
realms of possibility.

    jim@localhost ~
    $ crypt xx hellohel
    xxiHMKqoMTDuc

    jim@localhost ~
    $ crypt xx hellohello
    xxiHMKqoMTDuc

### Salts

Unix passwords usually use what is know as a salt to help make
pre-computation of password hashes more difficult. A salt is a string
which is prepended to the password before it is encrypted and stored
along with the password in /etc/passwd. You cannot simply pre-compute
crypt() values for a list of dictionary words, you would need to
pre-compute the hash for each word along with every possible salt to
produce a rainbow table of Unix password hashes. The result is a number
of different hashes for any given password.

If we use the Unix crypt command to encrypt a password and do not
specify a salt then a random salt value is chosen.

    jim@localhost ~
    $ crypt hello
    YnxINyIeMlKCM

    jim@localhost ~
    $ crypt hello
    v3njh4QHNjoWk

The first two characters of the resulting hash are the salt and must be
used when subsequently comparing a supplied password with the stored
crypt.

    jim@localhost ~
    $ crypt v3 hello
    v3njh4QHNjoWk

Salts can be of any length but is typically 2 characters on Unix
systems, which helps to ensure compatibility across systems.

### MD5/SHA1

More modern Unix systems and just about all Linux systems avoid the
limitations of Unix crypt() by using a message digest algorithm such as
MD5 or SHA1. Like Unix crypts the stored passwords are usually salted.
These message digest algorithms not only allow for longer passwords but
are also compuationally more expensive, making brute force attacks
harder.

### NIS

NIS (Yellow Pages) also uses the Unix password format to store user
credentials. \`ypcat passwd\` will show the password file on a Unix
server configured to user NIS.