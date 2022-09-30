---
tags:
  -  Hashing
---
Run by the National Drug Intelligence Center, part of the U.S.
Department of Justice.

**HashKeeper** is a database application of value primarily to those
conducting forensic examinations of computers on a somewhat regular
basis.

## Overview

The application uses the [MD5](md5.md) file signature algorithm
to establish unique numeric identifiers (hash values) for known files
and compares those known hash values against the hash values of Computer
file\|files on a seized computer system. Where those values match, the
examiner can say, with statistical certainty, that the corresponding
files on the seized system have been authenticated and therefore do not
need to be examined.

## Origins

Created by the National Drug Intelligence Center (NDIC)—an agency of the
United States Department of Justice—in 1996, it was the first source for
hash values of "known to be good" files.

## Availability

HashKeeper is available, free-of-charge, to law enforcement, military
and other government agencies throughout the world. It is available to
the public by sending a [Freedom of Information
Act](http://www.usdoj.gov/ndic/foia.htm) request to NDIC.

## Tools

- Example script
  ([media:hashkeeper.txt](media:hashkeeper.txt.md) to produce a
  pair of **Hashkeeper** format files for a given set of target files
  (can be imported into [EnCase](encase.md).

## External Links

- [Official NDIC website](http://www.usdoj.gov/ndic/about.htm)
- [Hashkeeper mailing
  list](http://tech.groups.yahoo.com/group/hashkeeper/)

