---
tags:
  -  Howtos
---
# Decrypting Android Full Disk Encryption

This document was written to provide some methods around decrypting
Android Full Disk Encryption. The document assumes that you do not have
adb, nor root access to the phone, rather, that you are trying to
decrypt a file system which was retrieved by getting a physical dump
from the phone (via a physical acquisition, JTAG, chip-off, etc).

## Decrypting LG and other Android Full Disk Encryption (FDE)

oclHashcat includes support for decrypting PBKDF2-HMAC-SHA1 +
CBC-ESSIV-AES encyption using brute force. The current version at the
time of this writing is oclHashcat v1.3.0 which includes GPU accelerated
4-digit PIN brute forcing. See:

- <https://hashcat.net>

## Decrypting Samsung Full Disk Encryption (FDE)

At the time of this writing, Samsung "does things different" than other
Android vendors. This may change with later releases of the Android OS
releases. For specifics on how Samsung does things different, see the
DerbyCon 2013 talk given by LÃ¡szlÃ³ TÃ³th and Ferenc Spala which covers
the technical details. Without their research and effort this document
would not be possible!

- <http://soonerorlater.hu/download/They_thinked_differently_DerbyCon2013.pdf>
- <https://www.youtube.com/watch?v=dUFl2tkyVyo>

The process for decrypting Samsung FDE is as follows:

- Acquire a physical acquisition of the device (not covered within the
  scope of this document).
- Extract the encryption key from the device image.
- Convert the encryption key to John The Ripper format.
- Brute force the John The Ripper format encrpytion key using a
  dictionary.

### Getting Started

You will need the following tools before you get started:

- Linux (Debian GNU/Linux jessie was used in this case)
- Sandy source code (https://github.com/donctl/sandy)
- John the Ripper jumbo community-edition source code
  (http://www.openwall.com/john/)
- Python 2.7 (https://www.python.org/downloads/)

Optional:

- crunch (https://sourceforge.net/projects/crunch-wordlist/)

#### Locating the Encryption Key

Depending on the model of phone and Android version on the device, the
location of the password key (or password footer as it's referred to in
some cases) varies. According to the research by TÃ³th and Spala, in
some versions of Android the key is located in the last 16K of the
encrypted userdata partition. In other Android versions the key is
located in /efs/metadata. For these cases, their 'sandy' framework can
locate your key quite effectively.

In the case of the testing below, the phone was a Samsung SII SGH-T989D
running Android 4.1.2 (with an encryption passphrase of 'test123'). The
key in this case was not located in the userdata partition nor
/efs/metadata so we manually searched for the ASCII string
'aes-cbc-essiv:sha256' using grep (or the tool of your choice) to locate
it. The 'DumpData.bin' is a single 16GB raw image which was acquired
from the device.

`dk@anubis:~/Samsung_SII_SGHT989D$ strings -t d DumpData.bin | grep aes-cbc-essiv:sha256`
`402653220 aes-cbc-essiv:sha256`
`663743397 aes-cbc-essiv:sha256`

Let's check the first hit, is that the key? It is! You can tell as the
key area we need starts with 0xC5B1B5D0, contains some "whitespace",
then the 'aes-cbc-essiv:sha256', followed by more "whitespace", and
finally the encryption key or encrypted footer which starts with
0xF1DA84CF in our case and is 80 bytes in length. Ultimately, these 80
bytes are all that we want to extract and brute force with JtR. If you
want to skip ahead slightly, at this point you could select those 80 hex
bytes, save them to a file in JtF format, and start brute forcing with
JtR. These steps are covered in more detail below.

*Note: The starting 0xC5B1B5D0 bytes were noted to vary slightly between
different Android dumps however the variations were minor. Just note
that a search for '0xC5B1B5D0' will not always work hence why we search
for 'aes-cbc-essiv:sha256'.*

In this example we are using 'dd' to extract 512 bytes around the area
where our ASCII string was located. In order to show the entire match
including the 0xC5B1B5D0 starting point, I am skipping back 36 bytes
before the ASCII string hit. 36 is an arbitrary number which is enough
in this case to show the starting 0xC5B1B5D0 which is indicative of the
start of the area which contains the encryption key.

`dk@anubis:~/Samsung_SII_SGHT989D$ dd bs=1 skip=$((402653220-36)) count=512 if=DumpData.bin | hexdump -C`
`00000000  c5 b1 b5 d0 01 00 00 00  d8 00 00 00 00 00 00 00  |................|`
`00000010  20 00 00 00 00 00 00 00  00 10 40 00 00 00 00 00  | .........@.....|`
`00000020  00 00 00 00 61 65 73 2d  63 62 63 2d 65 73 73 69  |....aes-cbc-essi|`
`00000030  76 3a 73 68 61 32 35 36  00 00 00 00 00 00 00 00  |v:sha256........|`
`00000040  00 00 00 00 00 00 00 00  00 00 00 00 00 00 00 00  |................|`
`*`
`00000060  00 00 00 00 b1 e4 01 10  02 00 00 00 00 00 00 00  |................|`
`00000070  00 00 00 00 00 00 00 00  00 00 00 00 00 00 00 00  |................|`
`00000080  00 00 00 00 f1 da 84 cf  0f 82 30 b9 a7 bc 16 d4  |..........0.....|`
`00000090  bc ed 22 20 43 6d 7c b7  50 aa a3 f2 6f 41 d3 28  |.." Cm|.P...oA.(|`
`000000a0  48 cc 63 0d 10 30 ae 35  b6 e3 73 b2 5c 1c 61 dd  |H.c..0.5..s.\.a.|`
`000000b0  34 80 07 89 67 34 2e 47  23 68 20 ac df cf 41 3a  |4...g4.G#h ...A:|`
`000000c0  10 0c 2d f4 18 9e 50 a0  47 09 ca 5c 90 1d 42 84  |..-...P.G..\..B.|`
`000000d0  8a 48 62 7c 00 00 00 00  00 00 00 00 00 00 00 00  |.Hb|............|`
`000000e0  00 00 00 00 00 00 00 00  00 00 00 00 00 00 00 00  |................|`
`*`
`00000200`
`512+0 records in`
`512+0 records out`
`512 bytes (512 B) copied, 0.00276768 s, 185 kB/s`

For fun, let's check the second hit from our previous strings + grep
search. You can see that this is not the key as expected so we can
ignore this hit.

`dk@anubis:~/Samsung_SII_SGHT989D$ dd bs=1 skip=$((663743397-36)) count=512 if=DumpData.bin | hexdump -C`
`00000000  70 20 2f 64 61 74 61 20  69 6e 20 74 69 6d 65 21  |p /data in time!|`
`00000010  00 61 65 73 2d 63 62 63  2d 70 6c 61 69 6e 3a 73  |.aes-cbc-plain:s|`
`00000020  68 61 31 00 61 65 73 2d  63 62 63 2d 65 73 73 69  |ha1.aes-cbc-essi|`
`00000030  76 3a 73 68 61 32 35 36  00 6e 6f 74 20 72 75 6e  |v:sha256.not run|`
`00000040  6e 69 6e 67 20 77 69 74  68 20 65 6e 63 72 79 70  |ning with encryp|`
`00000050  74 69 6f 6e 2c 20 61 62  6f 72 74 69 6e 67 00 6d  |tion, aborting.m|`
`00000060  61 73 74 65 72 20 6b 65  79 20 66 69 6c 65 20 64  |aster key file d|`
`00000070  6f 65 73 20 6e 6f 74 20  65 78 69 73 74 2c 20 61  |oes not exist, a|`
`00000080  62 6f 72 74 69 6e 67 00  45 72 72 6f 72 20 67 65  |borting.Error ge|`
`00000090  74 74 69 6e 67 20 63 72  79 70 74 20 66 6f 6f 74  |tting crypt foot|`
`000000a0  65 72 20 61 6e 64 20 6b  65 79 0a 00 64 65 63 72  |er and key..decr|`
`000000b0  79 70 74 69 6e 67 00 44  65 63 72 79 70 74 69 6f  |ypting.Decryptio|`
`000000c0  6e 20 70 72 6f 63 65 73  73 20 64 69 64 6e 27 74  |n process didn't|`
`000000d0  20 66 69 6e 69 73 68 20  73 75 63 63 65 73 73 66  | finish successf|`
`000000e0  75 6c 6c 79 0a 00 45 6e  63 72 79 70 74 69 6f 6e  |ully..Encryption|`
`000000f0  20 70 72 6f 63 65 73 73  20 64 69 64 6e 27 74 20  | process didn't |`
`00000100  66 69 6e 69 73 68 20 73  75 63 63 65 73 73 66 75  |finish successfu|`
`00000110  6c 6c 79 0a 00 72 6f 2e  63 72 79 70 74 6f 2e 73  |lly..ro.crypto.s|`
`00000120  75 70 70 6f 72 74 00 72  65 63 6f 76 65 72 79 5f  |upport.recovery_|`
`00000130  6d 6f 75 6e 74 00 43 6c  65 61 72 20 52 65 63 6f  |mount.Clear Reco|`
`00000140  76 65 72 79 20 6d 6f 75  6e 74 21 28 25 64 29 0a  |very mount!(%d).|`
`00000150  00 66 69 6e 64 20 70 72  6f 63 65 73 73 20 25 73  |.find process %s|`
`00000160  20 28 25 64 29 20 68 61  73 20 6f 70 65 6e 20 66  | (%d) has open f|`
`00000170  69 6c 65 20 25 73 00 66  69 6e 64 20 70 72 6f 63  |ile %s.find proc|`
`00000180  65 73 73 20 25 73 20 28  25 64 29 20 68 61 73 20  |ess %s (%d) has |`
`00000190  6f 70 65 6e 20 66 69 6c  65 6d 61 70 20 66 6f 72  |open filemap for|`
`000001a0  20 25 73 00 66 69 6e 64  20 70 72 6f 63 65 73 73  | %s.find process|`
`000001b0  20 25 73 20 28 25 64 29  20 68 61 73 20 63 77 64  | %s (%d) has cwd|`
`000001c0  20 77 69 74 68 69 6e 20  25 73 00 66 69 6e 64 20  | within %s.find |`
`000001d0  70 72 6f 63 65 73 73 20  25 73 20 28 25 64 29 20  |process %s (%d) |`
`000001e0  68 61 73 20 63 68 72 6f  6f 74 20 77 69 74 68 69  |has chroot withi|`
`000001f0  6e 20 25 73 00 66 69 6e  64 20 70 72 6f 63 65 73  |n %s.find proces|`
`00000200`
`512+0 records in`
`512+0 records out`
`512 bytes (512 B) copied, 0.000387062 s, 1.3 MB/s`

Now, using the forensic tool of your choice, extract 16384 bytes
starting from the 0xC5B1B5D0 hex and save that out as a new file. You
don't necessarily need to take all 16384 bytes but for the purpose of
this document, let's take 16384 bytes as that number emulates pulling
out the last 16K of the encrypted userdata partition.

`dk@anubis:~/Samsung_SII_SGHT989D$ dd bs=1 skip=$((402653220-36)) count=16384 if=DumpData.bin of=encryption_footer`
`16384+0 records in`
`16384+0 records out`
`16384 bytes (16 kB) copied, 0.0167546 s, 978 kB/s`

Your extracted chunk containing the encryption key should look as
follows:

`dk@anubis:~/Samsung_SII_SGHT989D$ hexdump -C encryption_footer`
`00000000  c5 b1 b5 d0 01 00 00 00  d8 00 00 00 00 00 00 00  |................|`
`00000010  20 00 00 00 00 00 00 00  00 10 40 00 00 00 00 00  | .........@.....|`
`00000020  00 00 00 00 61 65 73 2d  63 62 63 2d 65 73 73 69  |....aes-cbc-essi|`
`00000030  76 3a 73 68 61 32 35 36  00 00 00 00 00 00 00 00  |v:sha256........|`
`00000040  00 00 00 00 00 00 00 00  00 00 00 00 00 00 00 00  |................|`
`*`
`00000060  00 00 00 00 b1 e4 01 10  02 00 00 00 00 00 00 00  |................|`
`00000070  00 00 00 00 00 00 00 00  00 00 00 00 00 00 00 00  |................|`
`00000080  00 00 00 00 f1 da 84 cf  0f 82 30 b9 a7 bc 16 d4  |..........0.....|`
`00000090  bc ed 22 20 43 6d 7c b7  50 aa a3 f2 6f 41 d3 28  |.." Cm|.P...oA.(|`
`000000a0  48 cc 63 0d 10 30 ae 35  b6 e3 73 b2 5c 1c 61 dd  |H.c..0.5..s.\.a.|`
`000000b0  34 80 07 89 67 34 2e 47  23 68 20 ac df cf 41 3a  |4...g4.G#h ...A:|`
`000000c0  10 0c 2d f4 18 9e 50 a0  47 09 ca 5c 90 1d 42 84  |..-...P.G..\..B.|`
`000000d0  8a 48 62 7c 00 00 00 00  00 00 00 00 00 00 00 00  |.Hb|............|`
`000000e0  00 00 00 00 00 00 00 00  00 00 00 00 00 00 00 00  |................|`
`*`
`00001000  4b 44 4f 00 00 00 00 00  00 00 00 00 00 00 00 00  |KDO.............|`
`00001010  00 00 00 00 00 00 00 00  00 00 00 00 00 00 00 00  |................|`
`*`
`00004000`

Finally, let's further extract just the encryption key and save it out
in JtR format. This can either be done with the Sandy framework, a hex
editor, dd, xxd, etc. Let's do it with xxd in this case. Note: We are
seeking 132 bytes (jumping 132 bytes) into our file for the purpose that
we want to grab the 80 bytes starting at 0xF1DA84CF. You can do this
manually using the forensic tool of your choice as well. Just make sure
you save those 80 bytes to a flat text file like the file we create
below.

`dk@anubis:~/Samsung_SII_SGHT989D$ xxd -seek 132 -len 80 -c 128 -p encryption_footer`
`f1da84cf0f8230b9a7bc16d4bced2220436d7cb750aaa3f26f41d32848cc630d1030ae35b6e373b25c1c61dd3480078967342e47236820acdfcf413a100c2df4189e50a04709ca5c901d42848a48627c`

You can see we have extracted just the key. Let's repeat that and write
it out to a file.

`dk@anubis:~/Samsung_SII_SGHT989D$ xxd -seek 132 -len 80 -c 128 -p encryption_footer > encryption_footer.jtr`
`dk@anubis:~/Samsung_SII_SGHT989D$ cat encryption_footer.jtr`
`f1da84cf0f8230b9a7bc16d4bced2220436d7cb750aaa3f26f41d32848cc630d1030ae35b6e373b25c1c61dd3480078967342e47236820acdfcf413a100c2df4189e50a04709ca5c901d42848a48627c`

That's it! This .jtr file will later be fed into JtR for our brute force
attempt.

#### Installing Sandy

Installing Sandy involves cloning the 'sandy' repository from github.
After cloning the repository you will have a 'sandy' directory which
contains the Python application.

`dk@anubis:/sc/git-ext$ git clone https://github.com/donctl/sandy`
`Cloning into 'sandy'...`
`remote: Counting objects: 95, done.`
`remote: Total 95 (delta 0), reused 0 (delta 0)`
`Unpacking objects: 100% (95/95), done.`
`Checking connectivity... done.`

On supported devices, 'sandy' can be used to extract the encrypted key
and convert it to JtR format however as noted previously this did not
work in our case. If you are interested in playing with 'sandy', you can
start it as follows:

`dk@anubis:/sc/git-ext$ cd sandy`
`dk@anubis:~/sc/git-ext/sandy$ python main.py -p sandy`

#### Compiling John The Ripper (JtR) Jumbo with the sandcrypt plugin

Start by exploding your JtR jumbo source code and copying the sandcrypt
plugin (from the 'sandy' installation) into the 'src' tree of JtR. After
that you can start your compilation:

`dk@anubis:~/src$ tar -zxf john-1.7.9-jumbo-7.tar.gz`
`dk@anubis:~/src$ cd john-1.7.9-jumbo-7/src/`
`dk@anubis:~/src/john-1.7.9-jumbo-7/src$ cp ~/sc/git-ext/sandy/jtr_plugin/sandcrypt_fmt_plug.c .`
`dk@anubis:~/src/john-1.7.9-jumbo-7/src$ make linux-x86-64-native`

Note: If you receive an error about '\<openssl/HMAC.h\>' when JtR is
compiling 'sandcrypt_fmt_plug.c', please ensure you have pulled the
latest version of 'sandy' from github. An issue previously existed which
was corrected in the latest revision.

#### Brute forcing the Samsung Android FDE

The first thing you will need is a wordlist file. For the purpose of
this document, my sample wordlist file is as follows. If you would like
to generate a wordlist you can use the tool of your choice or use
'crunch' which is optionally included at the bottom of this document.
When generating your wordlist please keep in mind that Samsung FDE
specifically requires 6 characters including 1 digit. Note: The wordlist
is likely the most important part of the decryption and should be
crafted with care.

`dk@anubis:~/Samsung_SII_SGHT989D$ cat wordlist.txt`
`this5215`
`is23123`
`a000000`
`test10101`
`test123`
`test321`
`test2test`
`bleck2bleck`
`end2end`

Once the compilation of 'john' has completed you can change into the
'run' directory which is where the 'john' binary is located. Now you can
run 'john', provide it your wordlist, the sandcrypt plugin, and the
Samsung FDE .jtr you created earlier.

`dk@anubis:~/src/john-1.7.9-jumbo-7/run$ ./john --wordlist=/home/dk/Samsung_SII_SGHT989D/wordlist.txt --format=sandcrypt /home/dk/Samsung_SII_SGHT989D/encryption_footer.jtr`
`Loaded 1 password hash (Samsung phone encryption [32/64])`
`test123          (?)`
`guesses: 1  time: 0:00:00:00 DONE (Mon Sep 22 14:23:52 2014)  c/s: 71.42  trying: test123`
`Use the "--show" option to display all of the cracked passwords reliably`

Success! JtR identified 'test123' as the decryption password.

Note: If you run 'john' a second time you will notice that it doesn't
crack any passwords! The reason being is that 'john' is smart enough to
keep track of passwords it has already processed and it stores these in
a 'john.pot' file. If you delete the 'john.pot' file then 'john' will
reattempt cracking the passwords again.

`dk@anubis:~/src/john-1.7.9-jumbo-7/run$ ./john --wordlist=/home/dk/Samsung_SII_SGHT989D/wordlist.txt --format=sandcrypt /home/dk/Samsung_SII_SGHT989D/encryption_footer.jtr`
`Loaded 1 password hash (Samsung phone encryption [32/64])`
`No password hashes left to crack (see FAQ)`
`dk@anubis:~/src/john-1.7.9-jumbo-7/run$ cat john.pot`
`f1da84cf0f8230b9a7bc16d4bced2220436d7cb750aaa3f26f41d32848cc630d1030ae35b6e373b25c1c61dd3480078967342e47236820acdfcf413a100c2df4189e50a04709ca5c901d42848a48627c:test123`
`dk@anubis:~/src/john-1.7.9-jumbo-7/run$ rm john.pot`
`dk@anubis:~/src/john-1.7.9-jumbo-7/run$ ./john --wordlist=/home/dk/Samsung_SII_SGHT989D/wordlist.txt --format=sandcrypt /home/dk/Samsung_SII_SGHT989D/encryption_footer.jtr`
`Loaded 1 password hash (Samsung phone encryption [32/64])`
`test123          (?)`
`guesses: 1  time: 0:00:00:00 DONE (Tue Sep 23 13:39:45 2014)  c/s: 83.33  trying: test123`
`Use the "--show" option to display all of the cracked passwords reliably`

### Optional: Wordlist generation

You can use 'crunch' to generate a '6 character including 1 digit'
wordlist or bigger wordlist. Start by extracting the crunch source code
and compiling it as follows:

`dk@anubis:~/src$ tar -zxf crunch-3.6.tgz`
`dk@anubis:~/src$ cd crunch-3.6/`
`dk@anubis:~/src/crunch-3.6$ make`
`Building binary...`
`/usr/bin/gcc  -pthread -Wall -pedantic -std=c99   crunch.c -lm  -o crunch`

Now, as an example, let's generate a wordlist that is 6 -\> 8 characters
in length which is just comprised of digits.

`dk@anubis:~/src/crunch-3.6$ ./crunch 6 8 -f charset.lst numeric -o wordlist.txt`
`Crunch will now generate the following amount of data: 987000000 bytes`
`941 MB`
`0 GB`
`0 TB`
`0 PB`
`Crunch will now generate the following number of lines: 111000000`
``
`crunch:  22% completed generating output`
``
`crunch:  43% completed generating output`
``
`crunch:  65% completed generating output`
``
`crunch:  86% completed generating output`
``
`crunch: 100% completed generating output`

Here is what our wordlist.txt looks like:

`dk@anubis:~/src/crunch-3.6$ head wordlist.txt`
`000000`
`000001`
`000002`
`000003`
`000004`
`000005`
`000006`
`000007`
`000008`
`000009`

You can now use this wordlist for your JtR attempt to crack the FDE.

