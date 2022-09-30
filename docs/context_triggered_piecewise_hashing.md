---
tags:
  -  Hashing
---
Context Triggered Piecewise Hashing, also called **Fuzzy Hashing**, can
match inputs that have homologies. Such inputs have sequences of
identical bytes in the same order, although bytes in between these
sequences may be different in both content and length.

CTPH was originally based on the work of Dr. Andrew Tridgell and a spam
email detector called SpamSum. This method was adapted by [Jesse
Kornblum](jesse_kornblum.md) and published at the
[DFRWS](dfrws.md) conference in 2006 in a paper [Identifying
Almost Identical Files Using Context Triggered Piecewise
Hashing](http://dfrws.org/2006/proceedings/12-Kornblum.pdf).

## Implementations

- [ssdeep](ssdeep.md) is a cross-platform CTPH client.

## See Also

- [Piecewise hashing](piecewise_hashing.md)

## External Links

- [SpamSum](http://samba.org/ftp/unpacked/junkcode/spamsum/)

