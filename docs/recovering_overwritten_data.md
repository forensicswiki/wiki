---
tags:
  - Articles that need to be expanded
  - Data Recovery
---
Can data be recovered from a hard drive after that data has been written
by 35 passes of random information? How about a single pass of zeros?

Whether or not such data can be recovered has been a question of debate
for decades. Unfortunately, there have been few hard facts published.

# Prior Work

## The Gutmann Paper 1996

The most widely known paper in this area is [Peter
Gutmann](peter_gutmann.md)'s 1996 classic, *Secure Deletion of
Data from Magnetic and Solid-State Memory*, Proceedings of the Sixth
Usenix Security Symposium
[1](http://www.usenix.org/publications/library/proceedings/sec96/gutmann.html).
An extended version of the paper appears on Peter Gutmann's website
[2](http://www.cs.auckland.ac.nz/~pgut001/pubs/secure_del.html).

In this paper, Gutmann discusses techniques using an electron microscope
that might work for recovering overwritten data. He then proposes a
series of erasure patterns that can be used to overwrite data from [hard
drives](hard_drive.md) that use different kinds of encoding
schemes. A total of 35 patterns are proposed, although, as Gutmann
notes, there is no reason to ever use all 35 patterns (because the
patterns are designed for use on different kinds of magnetic recording
technology).

It's important to realize that this paper, written in 1996, discusses a
magnetic recording technology that is no longer widely available. In
1998 Gutmann added the [Epilogue to Gutmann's 1996
paper](epilogue_to_gutmann's_1996_paper.md). The gist of that
epilogue is that two passes of random data should be enough for today's
disk drives.

## ActionFront's Drive Independent Data Recovery 2005

In August 2005 ActionFront Data Recovery Labs presented a detailed
paper at the [IEEE 16th Annual Magnetic Recording
Conference](https://nanoandthepoor.org/) in which they discussed
the current state-of-the-art of recovering information from hard drives
without using the drive's own read/write heads
[3](https://www.seagate.com/de/de/contacts/).

One of the key points that the paper makes is that there is a high
degree of variability between individual modern hard drives.
Manufacturers exploit this variability to increase drive densities.
Unfortunately, this variability makes it dramatically harder to perform
drive independent data recovery — that is, a single recovery approach
that will work on multiple drives.

# Current Work

## Paper: *Overwriting Hard Drive Data: The Great Wiping Controversy*

In December 2008 Craig Wright, Dave Kleiman, and Shyaam Sundhar R.S.
presented a
[paper](http://tracedigital.be/pdf/overwriting_hard_drive_data.pdf) at
ICISS2008, which purpose was "*a categorical settlement to the
controversy surrounding the misconceptions involving the belief that
data can be recovered following a wipe procedure*"
[4](https://www.sans.org/blog/overwriting-hard-drive-data/).

# See also

* [Remnant Data](remnant_data.md)
* [Recovering deleted data](recovering_deleted_data.md)
* [Recovering bad data](recovering_bad_data.md)
