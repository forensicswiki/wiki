---
tags:
  - No Category
---
File is a command-line tool that attempts to identify the type of data
and format within the file. It has three tests: filesystem, magic
number, and language, which are performed in that order. The result of
first test that finds a match is returned. These heuristics are fairly
simplistic and can easily be fooled.

The filesystem test examines the filetype and name of the file under
examination, looking for execution flags and common filenames like
*core*. The [magic number](magic_number.md) test examines the
first few bytes of a file in order to identify its type. The language
test checks to see if the file is a text file and attempts to recover
which encoding is being used for the text.

Other things I'd like to see on this page are: command-line usage,
examples, and uses for forensic investigation.

# Identifying Partitions with File

File can identify disk partitions too!

    # file -s /dev/rdisk1s2
    /dev/rdisk1s2: Macintosh HFS Extended version 4 data (mounted) last mounted by: 'HFSJ',
        created: Thu Jan 24 22:05:19 2008,
        last modified: Fri Apr 25 20:58:56 2008,
        last checked: Thu Jan 24 22:05:19 2008, block size: 4096, number of blocks: 183059668, free blocks: 56950487
    #