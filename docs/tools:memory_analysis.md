---
tags:
  - No Category
---
The following tools can be used to conduct memory analysis.

## Memory Analysis Frameworks

- [Volatility Framework](volatility_framework.md) - A complete
  framework for analyzing Windows, Linux and Mac OSX memory images.
- [WindowsSCOPE Pro, Ultimate](http://www.windowsscope.com) -
  Comprehensive toolkit for the capture and analysis of Windows physical
  and virtual memory targeting cyber analysis, forensics/incident
  response, and education. Software and hardware based acquisition with
  [CaptureGUARD PCIe and
  ExpressCard](http://www.windowsscope.com/index.php?option=com_virtuemart&Itemid=34).
- [WindowsSCOPE Live](http://www.windowsscope.com) live fetch and
  analysis of Windows computers on a network from Android smartphones
  and tablets.
- [Second Look](second_look.md) from [Raytheon Pikewerks
  Corporation](http://www.pikewerks.com) - provides Linux memory
  forensics, including acquisition and analysis.

## Browser Email Memory Tool

- [pdgmail](http://www.jeffbryner.com/code/pdgmail) is a python script
  to extract gmail artifacts from memory images. Made for images
  extracted with pdd, but works with any memory image.

## Instant Messenger Memory Tool

- [Belkasoft Evidence Center](http://belkasoft.com) is a tool by
  [Belkasoft](belkasoft.md) which allows for retrieving various
  Instant Messenger artifacts from an attached memory image.

## Platform Independent Tools

A list of tools which should work regardless of future incremental OS /
hardware updates.

- [inVtero.net](https://github.com/ShaneK2/inVtero.net) Open Source
  Hypervisor/Process/Kernel detection for Windows, FreeBSD, OpenBSD and
  NetBSD. inVtero.net is based on interpreting low-level hardware
  defined constructs which change little over time. See github for
  details.
- [Forensics MemDump
  Extractor](http://www.techipick.com/forensics-memdump-extractor), is a
  tool by Gem George which can extract any kind of files residing in
  memory dump based on file signature. For example, if we put signature
  of a JPG file, it will extract all JPGs residing in memory dump.

## Analysis support libraries/tools

Additional tools/libraries that are meant to be used in combination with
existing frameworks or tools.

- [1](https://github.com/ShaneK2/Reloc) Reloc interfaces with a hosted
  server that has compiled over 200000 fragments of PE relocation data
  that can be used to transform executable's extracted from memory back
  into their original state. This means an exact recovery from any dump
  can be built. This will allow you to validate a secure hash (SHA256,
  etc...) to have total confidence there exists no backdoor or other
  malicious patch to a code in memory.