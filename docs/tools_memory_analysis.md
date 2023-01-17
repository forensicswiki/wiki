---
tags:
  -  Memory Analysis
  -  Tools
  -  Articles that need to be expanded
---
The following tools can be used to conduct memory analysis.

## Memory Analysis Frameworks

- [Volatility Framework](volatility_framework.md) - A complete
  framework for analyzing Windows, Linux and Mac OSX memory images.
- [WindowsSCOPE Pro, Ultimate](https://www.windowsscope.com/) -
  Comprehensive toolkit for the capture and analysis of Windows physical
  and virtual memory targeting cyber analysis, forensics/incident
  response, and education. Software and hardware based acquisition with
  [CaptureGUARD PCIe and ExpressCard](https://www.windowsscope.com/?option=com_virtuemarthttps://www.windowsscope.com//index.php?option=com_virtuemart&Itemid=34Itemid=34).
- [WindowsSCOPE Live](https://www.windowsscope.com/) live fetch and
  analysis of Windows computers on a network from Android smartphones
  and tablets.

## Browser Email Memory Tool

- [pdgmail](https://www.jeffbryner.com/code/pdgmail) is a python script
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

## Analysis support libraries/tools

Additional tools/libraries that are meant to be used in combination with
existing frameworks or tools.

- [1](https://github.com/K2/Reloc) Reloc interfaces with a hosted
  server that has compiled over 200000 fragments of PE relocation data
  that can be used to transform executable's extracted from memory back
  into their original state. This means an exact recovery from any dump
  can be built. This will allow you to validate a secure hash (SHA256,
  etc...) to have total confidence there exists no backdoor or other
  malicious patch to a code in memory.
