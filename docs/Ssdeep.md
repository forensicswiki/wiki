ssdeep is a program for computing and matching [Context Triggered
Piecewise Hashing](Context_Triggered_Piecewise_Hashing "wikilink")
values. It is based on a spam detector called
[spamsum](http://samba.org/ftp/unpacked/junkcode/spamsum/) by [Andrews
Trigdell](http://en.wikipedia.org/wiki/Andrew_Tridgell).

## File Format

The program uses an ASCII text file to record fuzzy hashes. The format
changed slightly in version 2.6 in Sep 2010. Hashes created by the
version 2.6 or later of the program cannot be used in earlier versions
<sup>[ref](http://ssdeep.svn.sourceforge.net/viewvc/ssdeep/tags/release-2.6/FILEFORMAT?revision=107&view=markup)</sup>.
The contains a header followed by one hash per line. The current header
is:

    ssdeep,1.1--blocksize:hash:hash,filename

## Usage Scenarios

### Truncated Files

The program can be used to associate two files where one is a truncated
version of the other. In this example, the examiner has a file
`all-the-kings-men.avi`. She computes a fuzzy hash of his file:

    $ ls -lsh
    -rwxr-xr-x 1 jvalenti users 699M Sep 29 2006 all-the-kings-men.avi

    $ ssdeep -b all-the-kings-men.avi > sig.txt

    $ cat sig.txt
    ssdeep,1.0--blocksize:hash:hash,filename
    12582912:fgQl/nUjQAbaBQvHf8yLr5CHJu3dyh YJ27TuXyphJs3wHC6 rEfAV wDrw6C/AT:fPl8cdAUyLr5CHJu3dyh8uzwHC6 reAS,"all-the-kings-men.avi"

The examiner then creates a second file that contains the first 29% of
the original. This simulates recovering a partial file in some manner.

    $ dd if=all-the-kings-men.avi of=partial.avi bs=1m count=200
    200 0 records in
    200 0 records out
    209715200 bytes transferred in 14.510224 secs (14452926 bytes/sec)

    $ ls -lsh partial.avi
    -rw-r--r-- 1 jvalenti users 200M Oct 6 06:40 partial.avi

The examiner can then use the matching mode of ssdeep, the `-m` option,
to read the known signature generated above and match it against the
partial file.

    $ ssdeep -bm sig.txt partial.avi
    partial.avi matches all-the-kings-men.avi (57)

The files are associated!

### Source Code Reuse

The source code for ssdeep was originally obtained from another open
source project called [md5deep](md5deep "wikilink"). An examiner with
access to both source code directory trees could use ssdeep to find any
similarities between the two. In this example we have two folders,
`ssdeep-1.1` and `md5deep-1.12`. First we record the fuzzy hashes, with
relative filenames (the `-l` switch) to a file:

    C:\> ssdeep -lr md5deep-1.12 > hashes.txt

Then we compare those saved hashes with the other directory:

    C:\> ssdeep -lrm hashes.txt ssdeep-1.1
    ssdeep-1.1\cycles.c matches md5deep-1.12\cycles.c (94)
    ssdeep-1.1\dig.c matches md5deep-1.12\dig.c (35)
    ssdeep-1.1\helpers.c matches md5deep-1.12\helpers.c (57)

Those matches indicate source code reuse! A manual examination of the
files in question is required to tell exactly what kind of copying
occurred, but we've saved the examiner a lot of work.

An advanced examiner can accomplish this matching with just one command
line, but it will also include all of the matches internal to each
directory.

    C:\> ssdeep -lrd md5deep-1.12 ssdeep-1.1
    md5deep-1.12\md5.h matches md5deep-1.12\cycles.c (27)
    md5deep-1.12\sha1.h matches md5deep-1.12\cycles.c (25)
    md5deep-1.12\sha1.h matches md5deep-1.12\md5.h (58)
    md5deep-1.12\sha256.h matches md5deep-1.12\cycles.c (25)
    md5deep-1.12\sha256.h matches md5deep-1.12\md5.h (61)
    md5deep-1.12\sha256.h matches md5deep-1.12\sha1.h (57)
    md5deep-1.12\tiger.h matches md5deep-1.12\cycles.c (29)
    md5deep-1.12\tiger.h matches md5deep-1.12\md5.h (65)
    md5deep-1.12\tiger.h matches md5deep-1.12\sha1.h (63)
    md5deep-1.12\tiger.h matches md5deep-1.12\sha256.h (61)
    ssdeep-1.1\cycles.c matches md5deep-1.12\cycles.c (94)
    ssdeep-1.1\dig.c matches md5deep-1.12\dig.c (35)
    ssdeep-1.1\helpers.c matches md5deep-1.12\helpers.c (57)

If you'd like to see the matches in both directions (i.e. for two files
A and B that match, see that A matches B and B matches A), use the `-p`
flag instead of `-d`.

## External Links

- [Official website](http://ssdeep.sourceforge.net/)

[Category:Cross-platform](Category:Cross-platform "wikilink")