**Hashing** is a method for reducing large inputs to a smaller fixed
size output. When doing forensics, typically cryptographic hashing
algorithms like [MD5](MD5 "wikilink") and [SHA-1](SHA-1 "wikilink") are
used. These functions have a few properties useful to forensics. Other
types of hashing, such as [Context Triggered Piecewise
Hashing](Context_Triggered_Piecewise_Hashing "wikilink") can also be
used.

## Tools

There are literally hundreds of hashing programs out there, but a few
related to forensics are:

- [md5sum](md5sum "wikilink") - Part of the [GNU](GNU "wikilink")
  coreutils suite, this program is standard on many computers.
- [md5deep](md5deep "wikilink") - Computes hashes, recursively if
  desired, and can compare the results to known values.
- [ssdeep](ssdeep "wikilink") - Computes and matches [Context Triggered
  Piecewise Hashes](Context_Triggered_Piecewise_Hashes "wikilink").

## Hash Databases

[National Software Reference Library](National_Software_Reference_Library "wikilink")
The largest hash database.

[Hashkeeper](Hashkeeper "wikilink")
National Drug Intelligence Center

<http://sunsolve.sun.com/fileFingerprints.do>
Solaris Fingerprint Database lookup for files distributed by Sun
Microsystems

## Online NSRL Lookup

<http://ionrift.ath.cx/nsrl/>
Allows searching of NSRL 2.17 by MD5 or SHA1. Reportedly the dataset
contains 43,103,492 files.

(Infrequently available, and likely only when the site owner (Jason
Spashett) needs to use it himself.)

## MD5 Reverse Hash Services

There are several online services that allow you to enter a hash code
and find out what the preimage might have been. One way to find these
services is to google for 'd41d8cd98f00b204e9800998ecf8427e' (the MD5 of
the null string).

Here are some services that we have been able to find:

<http://md5.benramsey.com>
A nice forward and reverse demonstration system, with an XML and AJAX
interface.

<!-- -->

<http://www.hashcrack.com/>
Reverse hash lookup of MD5, SHA1, MySQL, NTLM, and Lanman hashes. Claims
75 million hashes of 13.2 million unique words.

<!-- -->

<http://gdataonline.com/seekhash.php>
MD5 reverse lookup with approximately 1 million entries.

<!-- -->

<http://hash.insidepro.com/>
Hash database from InsidePro (MD5, NTLM).

<!-- -->

<http://www.xmd5.cn/index_en.htm>
<http://www.xmd5.org/index_en.htm>
This site is another simple MD5 reverse lookup. It claims a database
with "billions" of entries. Mostly for password cracking. (Who uses
straight MD5s for passwords?)

Others:

<http://www.md5this.com/>
<http://www.csthis.com/md5/>
<http://md5.rednoize.com/>

## Online Malware Hash Lookups

<http://www.team-cymru.org/Services/MHR/>
Malware Hash Registry by Team Cymru.

Utilizes a DNS query interface to lookup MD5 or SHA-1 Hashes for malware

<http://www.virustotal.com/buscaHash.html>
VirusTotal.com Online hash lookup no api/automation yet like Team Cymru
but does frequently have hashes for current new malware

## Segmented Hashing

Segmented hashing produces not a single hash value for the entire image,
but a list of hashes of corresponding LBA ranges of the image. By
validating all hashes in a set it is still verify image integrity.
Segmented Hashes are saved in a CSV file with the following format:
hash, start LBA, end LBA

When Segmented hashing is useful

- Segmented hashes support multi-pass imaging and handling of bad
  sectors: Hashes are calculated only for the imaged regions, while all
  bad sectors are excluded from calculation. This allows to validate a
  hash even when the source drive is damaged.
- Better resiliency against data corruption: If an acquired image gets
  damaged later, regular hash is invalid upon verification making the
  entire image useless. With segmented hashing, only a single hash value
  becomes invalid, while the rest of the image can still be validated.

[Seghash on GitHub](https://github.com/atola-technology/seghash) is a
free open-source tool for both calculating and validating segmented
hashes.