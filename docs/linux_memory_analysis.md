---
tags:
  - Memory Analysis
---
The output of a [memory acquisition tool](tools_memory_imaging.md) is a memory
image which contains the raw physical memory of a system. A wide variety of
tools can be used to search for strings or other patterns in a memory image,
but to extract higher-level information about the state of the system a memory
analysis tool is required.

## Linux Memory Analysis Tools

Active Open Source Projects:

- The [Volatility Framework](https://www.volatilesystems.com/default/volatility) is a
  collection of tools, implemented in Python, for the extraction of
  digital artifacts from volatile memory (RAM) samples. See the
  [LinuxMemoryForensics](https://code.google.com/archive/p/volatility/wikis/LinuxMemoryForensics.wiki)
  page on the Volatility wiki. (Availability/License: GNU GPL)
- [Rekall](http://www.rekall-forensic.com/) includes a Python-based
  analysis framework which forked from Volatility and has since added a
  number of features, as well as its own acquisition tools. It is usable
  as a library and is used as such in the GRR remote live forensics
  project.
- The [Red Hat Crash Utility](http://people.redhat.com/anderson/) is an
  extensible Linux kernel core dump analysis program. Although designed
  as a debugging tool, it also has been utilized for memory forensics.
  See, for example, the [2008 DFRWS challenge write-up by AAron Walters](http://volatilesystems.blogspot.com/2008/07/linux-memory-analysis-one-of-major.html).
  (Availability/License: GNU GPL)

Commercial Products:

- Forcepoint Linux Security ([Second Look](second_look.md)
  provides memory acquisition and analysis tools for Linux incident
  response and enterprise security. Its major differentiators versus
  Volatility are malware detection via integrity verification of the
  kernel, running processes, and cached files; ease of use (automatic
  kernel version detection, a graphical user interface, etc.); and
  enterprise scalability (including live analysis of remote systems via
  a memory access agent). (Availability/License: commercial)

Inactive Open Source and Research Projects:

- The Forensic Analysis Toolkit (FATKit) is
  a cross-platform, modular, and extensible digital investigation
  framework for analyzing volatile system memory. (Publication Date:
  2006; Availability/License: not available)
- [Foriana](http://hysteria.sk/~niekt0/foriana/) is tool for extraction
  of information such as the process and modules lists from a RAM image
  using logical relations between OS structures. (Availability/License:
  GNU GPL)
- [Draugr](https://code.google.com/archive/p/draugr) is a Linux memory forensics
  tool written in Python. (Availability/License: GNU GPL)
- [Volatilitux](https://code.google.com/archive/p/volatilitux) is another Linux
  memory forensics tool written in Python. (Availability/License: GNU
  GPL)
- Idetect (Linux) <http://forensic.seccure.net/> is an older
  implementation of Linux memory analysis.

## Linux Memory Analysis Challenges

- The [Digital Forensic Research Workshop](digital_forensic_research_workshop.md)
  2008 Forensics Challenge focused on the development of Linux memory analysis
  techniques and the fusion of evidence from memory, hard disk, and network.
- [Challenge SSTIC 2010](https://www.sstic.org/2010/challenge/)
  (French) dealt with analysis of physical memory from a mobile device
  running Android.
- [Challenge 7 of the Honeynet Project's Forensic Challenge 2011](https://www.honeynet.org/challenges/forensic-challenge-7-analysis-of-a-compromised-server/)
  included forensic analysis of a memory image from a potentially
  compromised Linux server.

## Linux Memory Images

Aside from those in the challenges referenced above, sample Linux memory
images can also be found on the Second Look website at
<https://secondlookforensics.com/images.html>.

## Linux Memory Analysis Bibliography

- [Digital Forensics of the Physical Memory](http://forensic.seccure.net/pdf/mburdach_digital_forensics_of_physical_memory.pdf) M.
  Burdach, March 2005.
- [Linux Physical Memory Analysis](https://www.usenix.org/legacy/events/usenix05/tech/freenix/full_papers/movall/movall.pdf),
  Paul Movall, Ward Nelson, Shaun Wetzstein; Usenix, 2005.
- [An Analysis Of Linux RAM Forensics](https://apps.dtic.mil/sti/pdfs/ADA445300.pdf),
  J.M. Urrea, Masters Thesis, Naval Postgraduate School, 2006.
- [Linux Memory Forensics for DFRWS Challenge 2008 using Volatility, Crash, and PyFlag](http://volatilesystems.blogspot.com/2008/07/linux-memory-analysis-one-of-major.html),
  by AAron Walters on the Volatile Systems Blog.
- [FACE: Automated digital evidence discovery and correlation](https://www.sciencedirect.com/science/article/pii/S1742287608000340),
  by Andrew Case, Andrew Cristina, Lodovico Marziale, Golden G. Richard,
  Vassil Roussev, DFRWS 2008
- [Linux Live Memory Forensics](http://esiea-recherche.eu/~desnos/papers/slidesdraugr.pdf),
  a presentation by Desnos Anthony describing the implementation of
  draugr, 2009.
- [Forensic RAM Dump Image Analyzer](https://is.cuni.cz/studium/dipl_st/index.php?doo=detailhttp://is.cuni.cz/studium/dipl_st/index.php?doo=detail&did=48540did=48540)
  by Ivor Kollar, describing the implementation of foriana, 2009.
- [Treasure and tragedy in kmem_cache mining for live forensics investigation](https://www.sciencedirect.com/science/article/pii/S1742287610000332),
  by Andrew Case, Lodovico Marziale, Cris Neckar, Golden G. Richard III;
  Digital Investigation, Volume 7, Supplement 1, The Proceedings of the
  Tenth Annual DFRWS Conference, August 2010.
- [Second Look Web Page](https://secondlookforensics.com/)
- [De-Anonymizing Live CDs through Physical Memory Analysis](https://blackhat.com/html/bh-dc-11/bh-dc-11-archives.html#Case)
  ([Whitepaper](https://media.blackhat.com/bh-dc-11/Case/BlackHat_DC_2011_Case_De-Anonymizing_Live_CDs-wp.pdf))
  ([Slides](https://media.blackhat.com/bh-dc-11/Case/BlackHat_DC_2011_Case_De-Anonymizing%20Live%20CDs-Slides.pdf))
  Andrew Case; Blackhat DC 2011.
- [Bringing Linux Support to Volatility](http://dfsforensics.blogspot.com/2011/03/bringing-linux-support-to-volatility.html),
  Andrew Case; Digital Forensics Solutions Blog, 2011.
- [Workshop - Linux Memory Analysis with Volatility](https://blackhat.com/html/bh-us-11/bh-us-11-briefings.html#Case)
  ([Slides](https://gotdfs.com/))
  Andrew Case; Blackhat Vegas 2011.
- [Forcepoint Security Labs Blog: "Horse Pill Rootkit vs. Forcepoint Threat Protection for Linux" (Second Look)](https://www.forcepoint.com/blog/x-labs/horse-pill-rootkit-vs-forcepoint-threat-protection-linux)
- [Forcepoint Security Labs Blog: "Detecting Register-Hooking Linux Rootkits with Forcepoint Second Look"](https://www.forcepoint.com/blog/x-labs/detecting-register-hooking-linux-rootkits-forcepoint-second-look)

Volatility Mailing List Threads on Support for Linux:

- <http://lists.volatilesystems.com/pipermail/vol-users/2010-January/thread.html#143>
- <http://lists.volatilesystems.com/pipermail/vol-dev/2010-September/thread.html#112>
