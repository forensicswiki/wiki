Encrypted File System (EFS) is the [Cryptographic File
System](File_Systems#Cryptographic_File_Systems "wikilink") that is
build into Microsoft [Windows](Windows "wikilink").

[Windows](Windows "wikilink") can encrypt files on an EFS volume by
file, by directory, or by the entire volume.
[Encryption](Encryption "wikilink") is done using a certificate. The
certificate itself is saved on the encrypted volume, but it is encrypted
with a password. Volumes can be configured so that they can be recovered
using one of several certificates — for example, a recovery certificate
belonging to the organization that owns the computer.

# How it works

The first time EFS is used [Windows](Windows "wikilink") creates a
symmetric File Encryption Key (FEK). [Windows](Windows "wikilink") then
creates an [RSA](RSA "wikilink") public/private key pair that is used to
encrypt the FEK. The private key is then encrypted with a hash of the
user's passphrase and username. The FEK can also be encrypted with the
organization's public key. Microsoft calls this second key a "Recovery
Agent".

In [Windows](Windows "wikilink") 2000 the computer's administrator is
the default recovery agent and can decrypt all files encrypted with EFS.

In [Windows](Windows "wikilink") XP and beyond there is no default
recovery agent.

EFS can be used in conjunction with [BitLocker](BitLocker "wikilink") if
desired.

# Recovering an EFS Key

Several tools are available that can recover an EFS key or volume if the
original encryption key (or passphrase) are lost. These include:

- EFS key from Passware;
- Advanced EFS Data Recovery from Elcomsoft
  (http://www.elcomsoft.com/aefsdr.html);
- [EnCase](EnCase "wikilink") Forensic (can perform a brute-force attack
  on the user's passphrase);
- WinHex Forensic (can also perform a brute-force attack on the user's
  passphrase).

# Linux

It is possible to decrypt files using
[ntfsdecrypt](http://www.linux-ntfs.org/doku.php?id=ntfsdecrypt) tool.
In this case, you should get the private key first (by running *cipher
/x filename.pfx* on a [Windows](Windows "wikilink") system).

# Other References

<http://www.beginningtoseethelight.org/efsrecovery>

[Category:Disk encryption](Category:Disk_encryption "wikilink")
[Category:File Systems](Category:File_Systems "wikilink")