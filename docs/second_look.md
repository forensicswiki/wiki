---
tags:
  -  Linux
  -  Memory Analysis
  -  Tools
---
![<File:second_look_logo.png>](second_look_logo.png "File:second_look_logo.png")

Forcepoint Linux Security (Second Look) is a Linux security product that
performs Memory Integrity scans. It uses memory forensics and integrity
verification to report on the state of a system and to alert on unknown
and potentially malicious code in memory. It is designed for two use
cases: 1. intrusion detection (early warning system for Linux
compromise), and 2. incident response (memory acquisition and analysis
for forensic investigation).

## History

Second Look began at Pikewerks Corporation. The original R&D was
sponsored by the US Air Force Reseach Lab (AFRL). During a Phase I STTR
contract in 2007, Pikewerks founder Sandy Ring implemented Linux kernel
integrity checks and cross-view analysis in a framework she called
"Scouts". Under a subsequent Phase II STTR contract that ran from 2008
to 2009, Andrew Tappert and Tom O'Connor developed the software for
Linux kernel integrity verification via memory forensics, codenamed
"pH", that would become Second Look.

Second Look publicly debuted at the DoD Cyber Crime Conference in St.
Louis in January 2009. The first supported distributions were CentOS and
Ubuntu (32-bit only). Subsequent internally-funded R&D at Pikewerks led
to the first hosted reference kernel repository, supporting automated
Linux memory forensics, and 64-bit support. Product releases and backend
infrastructure work in 2010 expanded the set of supported kernel
versions and distros to include CentOS, Fedora, Red Hat Enterprise Linux
(RHEL), and Ubuntu.

In 2011, commercial sales of the product picked up, and it was used to
investigate some high profile compromises involving Linux server
infrastructure. In December 2011, Pikewerks was acquired by Raytheon,
joining its IIS business unit. The year 2012 saw development of the
pagehash-based process integrity verification technique, expanding the
scope of memory forensics-based verification beyond the kernel. In 2012
the Enterprise edition of Second Look was launched, which performed
automated Linux memory forensics scans at scale (the original mode of
operation was ad hoc acquisition and analysis during investigations).
Debian was added as a supported distribution. In 2014, Second Look
gained structured data output (JSON format) and more supported
distributions (Amazon Linux and Oracle Linux). Also in 2014, the product
and its development team joined Raytheon's Cyber Products group. In
2015, Raytheon Cyber Products was spun out into a joint venture with
Websense, and the product was marketed as SureView Memory Integrity. The
product got a web interface in 2015, replacing the legacy Qt-based GUI,
and new capabilities for automatically extracting artifacts from memory.
In 2016, the Raytheon-Websense joint venture was named Forcepoint, and
the product was called Threat Protection for Linux. The scope of memory
integrity verification was further expanded in 2016 with the addition of
cached file verification features, and an advanced alert filtering
framework was added. As of 2017, the product is known as Forcepoint
Linux Security, and is deployed around the world to enhance the security
of large-scale Linux-based IT infrastructure.

## Capabilities

Second Look provides memory acquisition capabilities (local and remote),
which preserve the volatile system state, capturing evidence and
information that does not exist on disk and may otherwise be lost as an
investigation proceeds. A command-line script allows for local
acquisition of memory from running systems without introducing any
additional software. A memory access driver is provided for use on
systems without a native interface to physical memory. Remote memory
acquisition is facilitated by a memory access agent installed on target
systems.

Second Look analyzes live system memory (local or remote), or captured
memory images or virtual machine snapshots. It can help to detect,
investigate, and reverse engineer malware, including stealthy rootkits
and backdoors. A kernel integrity verification approach is utilized to
compare the Linux kernel in memory with a reference kernel. Forcepoint
provides thousands of reference kernels derived from original
distribution kernel packages, and a script for creating reference
kernels for other systems, such as those running custom kernels.
Forcepoint also maintains a database of pagewise hashes (pagehashes) of
the executable files from millions of Linux software packages, to
facilitate the identification of those files in memory (in active
processes or page cache content). Users can add pagehashes for custom
and third-party software to a local reference data repository to
facilitate their verification. This enables Second Look to detect
unknown and unauthorized applications as well as stealthy user-level
malware.

## Supported Systems

Second Look is regularly updated to support analysis of the latest
kernels and the most commonly used Linux distributions. As of March
2017:

- Supported target kernels: 2.6.9 through 4.8
- Supported target architectures: x86 32- and 64-bit
- Supported target distributions: Amazon Linux, CentOS, Debian, Fedora,
  Oracle Linux, SUSE, RHEL, and Ubuntu

## External Links

- [Product Home
  Page](https://www.forcepoint.com/products)
- [Demo Video](https://www.youtube.com/watch?v=m3KbNsd2kvI)
- [Another Demo Video](https://www.youtube.com/watch?v=EIiNgiqr0s0)