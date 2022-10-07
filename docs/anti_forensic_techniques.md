---
tags:
  -  Anti-Forensics

---
**Anti-forensic techniques** try to frustrate [forensic investigators](forensic_investigator.md) and their
[techniques](techniques.md).

From [1](http://en.wikipedia.org/wiki/Anti-computer_forensics): Attempts
to negatively affect the existence, amount and/or quality of evidence
from a crime scene, or make the analysis and examination of evidence
difficult or impossible to conduct

This can include refusing to run when [debugging](debugging.md)
mode is enabled, refusing to run when running inside of a [virtual
machine](virtual_machine.md), or deliberately overwriting data.
Although some anti-forensic tools have legitimate purposes, such as
overwriting sensitive data that shouldn't fall into the wrong hands,
like any [tool](tools.md) they can be abused.

# Traditional anti-forensics

## Overwriting Data and Metadata

### Secure Data Deletion

[Secure Deletion](secure_data_deletion.md) data, so that it
cannot be restored with forensic methods.

Overwriting programs typically operate in one of three modes:

1.  The program can overwrite the entire media.
2.  The program can attempt to overwrite individual files. This task is
    complicated by journaling file systems: the file itself may be
    overwritten, but portions may be left in the journal.
3.  The program can attempt to overwrite files that were previously
    “deleted” but left on the drive. Programs typically do this by
    creating one or more files on the media and then writing to these
    files until no free space remains, taking special measures to erase
    small files — for example, files that exist entirely within the
    Windows Master File Table of an NTFS partition (Garfinkel and Malan,
    2005).

Programs employ a variety of techniques to overwrite data. Apple’s Disk
Utility allows data to be overwritten with a single pass of NULL bytes,
with 7 passes of random data, or with 35 passes of data. Microsoft’s
cipher.exe, writes a pass of zeros, a pass of FFs, and a pass of random
data, in compliance with DoD standard 5220.22-M. (US DoD, 1995). In 1996
Gutmann asserted that it might be possible to recover overwritten data
and proposed a 35-pass approach for assured sanitization (Gutmann 1996).
However, a single overwriting pass is now viewed as sufficient for
[sanitizing](sanitizing_tools.md) data from ATA drives with
capacities over 15 GB that were manufactured after 2001 (NIST 2006).

Be aware that software 'data destroyers' may not necessarily do what
they state on the burb site. In particular a common mistake is the
oversight of how the underlying file system actually stores files, for
instance a 'wipe drive' application that will write a series of random
values across unallocated space on the hard disk may not take into
account the slack space at the end of allocated data blocks. Thus
allowing a large portion of old data to still be recoverable. This is a
very handy for a forensic analyst, but not so handy for IT Managers.

### Overwriting Metadata

If the examiner knows when an attacker had access to a Windows, Mac or
Unix system, it is frequently possible to determine which files the
attacker accessed, by examining file “access” times for every file on
the system. Some CFTs can prepare a “timeline” of the attacker’s actions
by sorting all of the computer’s timestamps in chronological order.
Although an attacker could wipe the contents of the media, this action
itself might attract attention. Instead, the attacker might hide their
tracks by overwriting the access times themselves so that the timeline
could not be reliably constructed.

For example, [Timestomp](timestomp.md) will overwrite
[NTFS](ntfs.md) “create,” “modify,” “access,” and “change”
timestamps ([metasploit](metasploi.md). [The Defiler’s
Toolkit](the_defiler’s_toolkit.md) can overwrite inode
timestamps and deleted directory entries on many Unix systems;
timestamps on allocated files can also be modified using the Unix touch
command ([The Grugq](the_grugq.md).

### Preventing Data Creation

Prevent the creation of certain data in the first place. Data which was
never there, obviously cannot be restored with forensic methods.

For example, a partition can be mounted read-only or accessed through
the raw device to prevent the file access times from being updated. The
Windows registry key
HKLM\SYSTEM\CurrentControlSet\Control\FileSystem\NtfsDisableLastAccessUpdate
can be set to “1” to disable updating of the last-accessed timestamp;
this setting is default under Windows Vista (Microsoft 2006).

## Cryptography, Steganography, and other Data Hiding Approaches

### Encrypted Data

Cryptographic file systems transparently encrypt data when it is written
to the disk and decrypt data when it is read back, making the data
opaque to any attacker (or CFT) that does not have the key. These file
systems are now readily available for Windows, Mac OS, and Linux. The
key can be protected with a passphrase or stored on an auxiliary device
such as a USB token. If there is no copy of the key, intentionally
destroying the key makes the data stored on the media inaccessible
(Boneh and Lipton, 1996). Even if the cryptographic system lacks an
intentional sanitization command or “self-destruct,” cryptography can
still be a potent barrier to forensic analysis if the cryptographic key
is unknown to the examiner.

Cryptography can also be used at the application level. For example,
Microsoft Word can be configured to encrypt the contents of a document
by specifying that the document has a “password to open.” Although older
versions of Microsoft Word encrypted documents with a 40-bit key that
can be cracked with commercial tools, modern versions can optionally use
a 128-bit encryption that is uncrackable if a secure passphrase is used.

### Encrypted Network Protocols

Network traffic can likewise be encrypted to protect its content from
forensic analysis. Cryptographic encapsulation protocols such as
[SSL](ssl_forensics.md) and SSH only protect the content of the
traffic. Protecting against traffic analysis requires the use of
intermediaries. Onion Routing (Goldschlag, Reed and Syverson, 1999)
combines both approaches with multiple layers of encryption, so that no
intermediary knows both ends of the communication and the plaintext
content.

*More information: [Tor](tor.md) and [VPN](vpn.md).*

### Program Packers

Packers are commonly used by attackers so that attack tools will not be
subject to reverse engineering or detection by scanning. Packers such as
PECompact (Bitsum 2006) and Burneye (Vrba 2004) will take a second
program, compress and/or encrypt it, and wrap it with a suitable
extractor. Packers can also incorporate active protection against
debugging or reverse engineering techniques. For example, Shiva will
exit if its process is being traced; if the process is not being traced,
it will create a second process, and the two processes will then trace
each other, since each process on a Unix system may only be traced by
one other process. (Mehta and Clowes, 2003)

Packed programs that require a password in order to be run can be as
strong as their encryption and password. However, the programs are
vulnerable at runtime. Burndump is a loadable kernel module (LKM) that
automatically detects when a Burneye-protected file is run, waits for
the program to be decrypted, and then writes the raw, unprotected binary
to another location (ByteRage 2002). Packed programs are also vulnerable
to static analysis if no password is required (Eagle 2003).

### Steganography

Steganography can be used to embed encrypted data in a cover text to
avoid detection. Steghide embeds text in JPEG, MBP, MP3, WAV and AU
files (Hetzl 2002). Hydan exploits redundancy in the x86 instruction
set; it can encode roughly 1 byte per 110 (El-Khalil 2004). Stegdetect
(Provos 2004) can detect some forms of steganography.

StegFS hides encrypted data in the unused blocks of a Linux ext2 file
system, making the data “look like a partition in which unused blocks
have recently been overwritten with random bytes using some disk wiping
tool” (McDonald and Kuhn, 2003).

[FreeOTFE](freeotfe.md) and [TrueCrypt](truecrypt.md)
allow a second encrypted file system to be hidden within another
encrypted file system. The goal of this filesystem-within-a-filesystem
is to allow the users to have a “decoy” file system with data that is
interesting but not overtly sensitive. A person who is arrested or
captured with a laptop encrypted using this software could then give up
the first file system’s password, with the hope that the decoy would be
sufficient to satisfy the person’s interrogators.

### Generic Data Hiding

Data can also be hidden in unallocated or otherwise unreachable
locations that are ignored by the current generation of forensic tools.

Metasploit’s Slacker will hide data within the slack space of FAT or
NTFS file system. FragFS hides data within the NTFS Master File Table.
RuneFS (Grugq 2003) stores data in bad blocks. (Thompson and Monroe,
2006). Waffen FS stores data in the ext3 journal file (Eckstein and
Jahnke 2005). KY FS stores data in directories (Grugq 2003). Data Mule
FS stores data in inode reserved space (Grugq 2003). It is also possible
to store information in the unallocated pages of Microsoft Office files.

Information can be stored in the [Host Protected
Area](dco_and_hpa.md) and the [Device Configuration
Overlay](dco_and_hpa.md) areas of modern ATA hard drives.
Data in the HPA and DCO is not visible to the BIOS or operating system,
although it can be extracted with special tools.

## Detecting Forensic Analysis

There are methods to detect whether an
[investigator](investigator.md)
forensic analysis on the system. A malicious user or program could react
to that by destroying evidence, for example.

# Other Anti Forensics

## Targeting forensic tool blind spots

## Targeting forensic tool vulnerabilities

### Casper

![](Grml.png "Grml.png") mounted root file system on the [hard drive](hard_drive.md)
[Casper](http://bromavilleherald.com/index.php/Casper_boot_process) is a
set of scripts used to enable Linux-based distributions to boot from
removable media. Casper scripts will search for the root file system
(typically [SquashFS](squashfs.md) on the local data storage
media during the boot, mount it, and execute */sbin/init* program on
mounted root. Most forensic Linux distributions based on
[Ubuntu](ubuntu.md) and [Debian](Debian "wikilink") lack of
integrity checks of selected SquashFS images and will boot specially
crafted images found on the hard drive (not on the CD).

### STARFisH - Structured Testing Approach for Resilience of Forensic Soft- and Hardware

[STARFisH](http://www.digitrace.de/de/forschung/starfish) was a B.Sc.
project by Phil Knüfer, which dealt with using a structured testing
approach to improve the resilience of IT forensic software (and
hardware). To this end, a test schema was designed and test cases were
developed.

## Targeting generic tool/lib vulnerabilities

# References

Garfinkel, S., Anti-Forensics: Techniques, Detection and
Countermeasures, The 2nd International Conference on i-Warfare and
Security (ICIW), Naval Postgraduate School, Monterey, CA, March 8-9,
2007.
[2](http://www.simson.net/clips/academic/2007.ICIW.AntiForensics.pdf)

Henrique, G. Wendel, Anti Forensics: Making computer forensics hard,
Code Breakers III, São Paulo, Brazil, Setember 2006.
[3](http://ws.hackaholic.org/slides/AntiForensics-CodeBreakers2006-Translation-To-English.pdf)

## See also

- [Anti-forensics tools](antiforensics_tools.md)

## Externals Links

- [Anti-Forensics: The Next Step in Digital Forensics Tool
  Testing](http://www.digitrace.de/de/veroeffentlichung-2/fachliteratur/84-anti-forensics-the-next-step-in-digital-forensics-tool-testing),
  in: IT Security Incident Management and IT Forensics (IMF): 2013
  Seventh International Conference on, Date 12-14 March 2013, IEEE, S.
  83 – 97
- [Talk on Anti-Forensics, on
  28C3](https://www.youtube.com/watch?v=OP9k-G2yq9I) (in German)
- [Breaking Encase with FILE0 and
  Winhex](http://www.safehack.com/Textware/forensic/Anti_Forensic_Break_Encase.pdf)
- [Anti Forensics: making computer forensics
  hard](http://ws.hackaholic.org/slides/AntiForensics-CodeBreakers2006-Translation-To-English.pdf)
- [PTK Forensic Local Command Execution Vulnerability (fixed in 1.0.1,
  see CHANGELOG)](http://seclists.org/bugtraq/2008/Nov/0038.html)
- [Anti-Forensics
  Class](http://www.irongeek.com/i.php?page=videos/anti-forensics-occult-computing)
  Little over 3hr of video on the subject of anti-forensic techniques
- [Linux for computer forensic investigators: problems of booting
  trusted operating
  system](http://www.computer-forensics-lab.org/pdf/Linux_for_computer_forensic_investigators_2.pdf)
- [Low Down and Dirty: Anti-forensic
  Rootkits](http://www.blackhat.com/presentations/bh-jp-06/BH-JP-06-Bilby-up.pdf),
  by [Darren Bilby](darren_bilby.md), Blackhat Japan 2006
- [One-byte Modification for Breaking Memory Forensic
  Analysis](https://media.blackhat.com/bh-eu-12/Haruyama/bh-eu-12-Haruyama-Memory_Forensic-Slides.pdf),
  by Takahiro Haruyama, Hiroshi Suzuki, March 14-16, 2012

### Mitigation

- [Mitigating Anti-Forensics: A Schema-based
  Approach](http://starfish.digitrace.de/media/thesis.pdf), by Phil
  Knüfer, January 5, 2014

### Windows

- \[<http://msdn.microsoft.com/en-us/library/windows/hardware/ff557671(v=vs.85>).aspx
  NtSetInformationFile function\]
- \[<http://msdn.microsoft.com/en-us/library/windows/desktop/aa365539(v=vs.85>).aspx
  SetFileInformationByHandle function\]
- \[<http://msdn.microsoft.com/en-us/library/windows/desktop/ms724933(v=vs.85>).aspx
  SetFileTime function\]
- \[<http://msdn.microsoft.com/en-us/library/windows/hardware/ff567096(v=vs.85>).aspx
  ZwSetInformationFile function\]

