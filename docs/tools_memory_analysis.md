---
tags:
  - Analysis Techniques
  - Articles that need to be expanded
  - Memory Analysis
  - Tools
---
Memory analysis tooling for examining running programs, the operating
system, and the overall state of a computer from a memory image -
memory analysis frameworks, artifact extractors, platform independent
detection tools, and support tools for extracted code. The tools below
are grouped according to the [categories of
analysis](memory_analysis.md) described in [Memory
analysis](memory_analysis.md).

> **Warning:** The tools listed below are not necessarily forensic
> tooling in the sense of [Forensic tooling](forensic_tooling.md).

## Memory analysis frameworks

See also [Volatility Framework](volatility_framework.md).

* [Volatility Framework](volatility_framework.md) - A complete
  framework for analyzing Windows, Linux and Mac OS X memory images.
  * AESKeyFinder extracts 128-bit and 256-bit [AES](aes.md) keys, and
    RSAKeyFinder extracts private and public RSA keys, from a memory
    capture.
  * cryptoscan.py - a [Volatility plugin](list_of_volatility_plugins.md)
    that scans a memory image for [TrueCrypt](truecrypt.md)
    passphrases.
* [WindowsSCOPE Pro, Ultimate](https://www.windowsscope.com/) -
  Comprehensive toolkit for the capture and analysis of Windows
  physical and virtual memory targeting cyber analysis,
  forensics/incident response, and education. Software and hardware
  based acquisition with CaptureGUARD PCIe and ExpressCard.
* [WindowsSCOPE Live](https://www.windowsscope.com/) - live fetch and
  analysis of Windows computers on a network from Android smartphones
  and tablets.
* [Legilimency](https://github.com/google/Legilimency/) - a memory
  research platform for iOS.

## Browser and email artifacts

* [pdgmail](https://www.jeffbryner.com/code/pdgmail) is a python
  script to extract gmail artifacts from memory images. Made for images
  extracted with pdd, but works with any memory image.

## Instant messenger artifacts

* [Belkasoft Evidence Center](belkasoft.md#belkasoft-evidence-center)
  is a tool which allows for retrieving various Instant Messenger
  artifacts from an attached memory image.

## Platform independent tools

Tools which should work regardless of future incremental OS / hardware
updates.

* [inVtero.net](https://github.com/ShaneK2/inVtero.net) - Open Source
  Hypervisor/Process/Kernel detection for Windows, FreeBSD, OpenBSD
  and NetBSD. inVtero.net is based on interpreting low-level hardware
  defined constructs which change little over time. See github for
  details.

## Memory analysis support

Tools and libraries that are meant to be used in combination with
existing frameworks or tools.

* [Reloc](https://github.com/K2/Reloc) interfaces with a hosted
  server that has compiled over 200000 fragments of PE relocation
  data that can be used to transform executable's extracted from
  memory back into their original state. This means an exact recovery
  from any dump can be built. This will allow you to validate a secure
  hash (SHA256, etc.) to have total confidence there exists no
  backdoor or other malicious patch to a code in memory.

## See Also

* [Memory analysis](memory_analysis.md)
* [Memory Imaging Tools](tools_memory_imaging.md)
* [Volatility Framework](volatility_framework.md)
* [Belkasoft Evidence Center](belkasoft.md)

## External Links

* [WindowsSCOPE](https://www.windowsscope.com/)
* [pdgmail - gmail artifacts from memory](https://www.jeffbryner.com/code/pdgmail)
* [inVtero.net on GitHub](https://github.com/ShaneK2/inVtero.net)
* [Reloc on GitHub](https://github.com/K2/Reloc)
