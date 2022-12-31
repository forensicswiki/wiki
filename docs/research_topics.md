---
tags:
  -  Research
---
Interested in doing research in computer forensics? Looking for a
master's topic, or just some ideas for a research paper? Here is our
list. Please feel free to add your own ideas.

Many of these would make a nice master's project.

# Programming/Engineering Projects

tcpflow:

- Modify [tcpflow](tcpflow.md)'s iptree.h implementation so that
  it only stores discriminating bit prefixes in the tree, similar
  to D. J. Bernstein's [Crit-bit](http://cr.yp.to/critbit.html) trees.
- Determine why [tcpflow](tcpflow.md)'s iptree.h
  implementation's *prune* works differently when caching is enabled
  then when it is disabled

SleuthKit

- Write a FUSE-based mounter for SleuthKit, so that disk images can be
  forensically mounted using TSK.
- Modify SleuthKit's API so that the physical location on disk of
  compressed files can be learned.

# Digital Forensics Education

- Survey existing DFE programs and DF practitioners regarding which
  tools they use. Report if the tools being taught are the same as the
  tools that are being used.

# Data Sniffing

- Create a method to detect NTFS-compressed cluster blocks on a disk
  (RAW data stream). A method could be to write a generic signature to
  detect the beginning of NTFS-compressed file segments on a disk. This
  method is useful in carving and scanning for textual strings.

# Anti-Frensics Detection

- A pluggable rule-based system that can detect the residual data or
  other remnants of running a variety of anti-forensics software

## Carvers

File carving on disks is largely dead, but carving within files for
information not made visible by existing tools should still be a
research area.

- Adapt current disk-based file carving tools to files. (bulk_extractor
  already does this.)
- Figure out what information is most useful to forensic investigators,
  and how to present that information?
- Concentrate on multimedia applications, such as [Multimedia File
  Carver](https://github.com/rpoisel/mmc), which allows for the
  reassembly of multimedia fragmented files.

### Correlation Engine

- Logfile correlation
- Document identity identification
- Correlation between stored data and intercept data
- Online Social Network Analysis

### Data Snarfing/Web Scraping

- Find and download in a forensically secure manner all of the
  information in a social network (e.g. Facebook, LinkedIn, etc.)
  associated with a targeted individual.
- Determine who is searching for a targeted individual. This might be
  done with a honeypot, or documents with a tracking device in them, or
  some kind of covert Facebook App.
- Automated grouping/annotation of low-level events, e.g. access-time,
  log-file entry, to higher-level events, e.g. program start, login

### Enhancements for Guidance Software's Encase

- Develop an EnScript that allows you to script EnCase from Python. (You
  can do this because EnScripts can run arbitrary DLLs. The EnScript
  calls the DLL. Each "return" from the DLL is a specific EnCase command
  to execute. The EnScript then re-enters the DLL.)

### Volume/File System analysis

- Analysis of inter snapshot changes in [Windows Shadow
  Volumes](windows_shadow_volumes.md)
- Modify SleuthKit's NTFS implementation to support NTFS encrypted files
  (EFS)
- Extend SleuthKit's implementation of NTFS to cover Transaction NTFS
  (TxF) (see [NTFS](ntfs.md)
- Physical layer access to flash storage (requires reverse-engineering
  proprietary APIs for flash USB and SSD storage.)
- Add support to SleuthKit for
  [ReFS](resilient_file_system_(refs).md).

## Error Rates

- Develop improved techniques for identifying encrypted data. (It's
  especially important to distinguish encrypted data from compressed
  data).
- Quantify the error rate of different forensic tools and processes. Are
  these rates theoretical or implementation dependent? What is the
  interaction of the error rates and the [Daubert](daubert.md)
  standard?

## Research Areas

These are research areas that could easily grow into a PhD thesis.

- General-purpose detection of:
  - Steganography
  - Sanitization attempts
  - Evidence Falsification (perhaps through inconsistency in file system
    allocations, application data allocation, and log file analysis)
- Visualization of data/information in digital forensic context
- SWOT of current visualization techniques in forensic tools;
  improvements; feasibility of 3D representation;

## See Also

- [Digital Forensics: Research Challenges and Open Problems, Dr. Yong
  Guan, Iowa State University, Dec. 4,
  2007](http://itsecurity.uiowa.edu/securityday/documents/guan.pdf)
- [Forensic Focus: Project Ideas for Digital Forensics
  Students](https://www.forensicfocus.com/project-ideas)

__NOTOC__

