---
tags:
  - Linux
  - Network Forensics
  - Open Source Software
  - Tools
---
## Overview

Tcpdstat is an old, but useful tool for analyzing network based
evidence. Tcpdstat offers very helpful statistical information about
packet captures, including start/finish timestamps (to identify the
total duration of the packet capture), breakdown by protocol/port, and
packet size distribution.

Tcpdstat is useful for analyzing network trace data because it gives a
high-level overview, which can identify where to look next. For example,
if quite a few packets show up for a protocol/port that isn’t normally
used on the victim machine, you've already been clued in on what to look
for next on a lower level.

## External Links

* [Tcpdstat Overview and Build Instructions](http://cyberforensics.et.byu.edu/wiki/Tcpdstat)
