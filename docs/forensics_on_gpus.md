---
tags:
  - Articles that need to be expanded
---
Using a Graphical Processing Unit (GPU) for forensics analysis
attempts to make use of the significant, parallel processing power
available on these high cards for a different purpose than their
original intent. The idea of forensic analysis on a GPU was first
proposed by Marziale, Richard and Roussev in 2007 with a version of
[Scalpel](scalpel.md) that utilized a GPU.

## Password Cracking

Password cracking process accelerated by using GPU is several times
faster than in CPU-only mode.

For example, password recovering speed for [MD5](md5.md) hash
using Core2 Duo is about 4,7 millions passwords per second. By using
8800GTX it is possible to reach 265 millions passwords per second.

* [ElcomSoft](elcomsoft.md) Distributed Password Recovery and Password Recovery Bundle
* [Passware Kit Forensic](https://www.passware.com/)
* [Passcovery Suite](https://passcovery.com/products/passcoverysuite.htm)

## External Links

* [Massive Threading: Using GPUs to Increase the Performance of Digital Forensics Tools](https://www.nvidia.com/docs/IO/47905/dfrws2007-gpu.pdf),
  by Lodovico Marziale, Golden G. Richard III and Vassil Roussev, 2007
* [Offloading IDS Computation to the GPU](https://www.acsac.org/2006/papers/74.pdf),
  by Nigel Jacob and Carla Brodley, 2006
