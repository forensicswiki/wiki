---
tags:
  -  Hashing
  -  Linux
---
## General Usage

One of the most important things to remember when performing digital
forensics is how to preserve authenticity. Calculating and retaining
hashes of the files you gather during your investigation (whether they
be script output or actual binaries) is a great way to prove that your
collected evidence hasn't been tampered with. Because of the risk of
[hash
collisions](http://en.wikipedia.org/wiki/Collision_%28computer_science%29),
it is important to use multiple hashing algorithms for each file (e.g.,
MD5 and SHA1).

**GetHashes.sh** is a simple bash script that quickly calculates MD5 and
SHA1 hashes for all files in the same directory as the script. This is
much quicker and simpler than running the hashing commands manually for
each file. The script is used by placing the script in the same folder
as the files to hash, and then running the script. This will produce two
folders of hashes, one of MD5, and one of SHA1 hashes. These can be used
at a later time as evidence that the forensic data has not been tampered
with. The script also ignores itself and any directories located in the
same directory (to avoid errors when trying to hash directories). Only
files in the same directory as the script are hashed.

## Usage Instructions

In order to use the UNIX file hashing script, make sure you download the
*getHashes.sh* file from the repository above onto a UNIX machine with
*md5sum* and *sha1sum* installed (most UNIX-like operating systems have
these installed by default). The guide below used a Kali Linux v1.0.9
machine.

Next, place the *getHashes.sh* script into the same directory as the
files you want to hash. In the screenshot below, the script was placed
in the same directory as a collection of text files containing the
output of commands run on the victim machine, transferred to a forensic
workstation using [Netcat](netcat.md).

![<File:getHashesExample1.png>](getHashesExample1.png "File:getHashesExample1.png")

Next, open up terminal into the directory with the *getHashes.sh* script
and execute the script.

**NOTE:** If you get permission errors when trying to execute the
script, you likely need to run the following command in terminal to make
the script executable:

` chmod a+x getHashes.sh`

![<File:getHashesExample2.png>](getHashesExample2.png "File:getHashesExample2.png")

As you can see in the screenshot above, the script created MD5 and SHA1
directories because they didn't yet exist in that directory. These new
directories each contain .MD5 and .SHA1 files, respectively (each
containing the hash and filename of its corresponding file), for all
files in the same directory as the script. These hashes are also sent as
output to the terminal--with the MD5 hash listed first and the SHA1 hash
listed second--to simplify the process of copying them into your
forensic log.

## Video Demonstration

The following video describes how to use the script:

<https://www.youtube.com/watch?v=j8gaQz9fezQ>

## External Links

- [Download
  location](https://bitbucket.org/stewdebaker/unix-hashing-script)
- [ReadMe
  file](http://technicallysane.blogspot.com/p/unix-file-hashing-script.html)