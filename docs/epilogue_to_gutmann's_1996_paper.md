---
tags:
  -  Articles that need to be expanded 
---
*In the time since this paper was published, some people have treated
the 35-pass overwrite technique described in it more as a kind of voodoo
incantation to banish evil spirits than the result of a technical
analysis of drive encoding techniques. As a result, they advocate
applying the voodoo to PRML and EPRML drives even though it will have no
more effect than a simple scrubbing with random data. In fact performing
the full 35-pass overwrite is pointless for any drive since it targets a
blend of scenarios involving all types of (normally-used) encoding
technology, which covers everything back to 30+-year-old MFM methods (if
you don't understand that statement, re-read the paper). If you're using
a drive which uses encoding technology X, you only need to perform the
passes specific to X, and you never need to perform all 35 passes. For
any modern PRML/EPRML drive, a few passes of random scrubbing is the
best you can do. As the paper says, "A good scrubbing with random data
will do about as well as can be expected". This was true in 1996, and is
still true now.*

*Looking at this from the other point of view, with the ever-increasing
data density on disk platters and a corresponding reduction in feature
size and use of exotic techniques to record data on the medium, it's
unlikely that anything can be recovered from any recent drive except
perhaps one or two levels via basic error-cancelling techniques. In
particular the the drives in use at the time that this paper was
originally written have mostly fallen out of use, so the methods that
applied specifically to the older, lower-density technology don't apply
any more. Conversely, with modern high-density drives, even if you've
got 10KB of sensitive data on a drive and can't erase it with 100%
certainty, the chances of an adversary being able to find the erased
traces of that 10KB in 80GB of other erased traces are close to zero.*''

<http://www.cs.auckland.ac.nz/~pgut001/pubs/secure_del.html>