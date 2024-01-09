---
tags:
  - No Category
---
This page describes large-scale corpora of forensically interesting
information that are available for those involved in forensic research.

# Disk Images

## Real Data Corpus

Between 1998 and 2006, [Garfinkel](simson_garfinkel.md) acquired
1250+ hard drives on the secondary market. These hard drive images have
proven invaluable in performing a range of studies such as the
developing of new forensic techniques and the [sanitization practices](https://simson.net/clips/academic/2003.IEEE.DiskDriveForensics.pdf)
of computer users.

## Computer Forensic Reference Data Sets (CFReDS)

The [Computer Forensic Reference Data Sets (CFReDS)](https://cfreds.nist.gov/)
project from [NIST](national_institute_of_standards_and_technology.md) hosts
sample cases that may be useful for examiners to practice with.

## Digital Forensics Tool Testing Images

Digital Forensics Tool Testing Images can be downloaded from [Sourceforge](https://dftt.sourceforge.net/).

## ForensicsKB blog

Lance Mueller has created some disk images; they can be downloaded from his blog:

* [Practical 1](https://www.forensickb.com/2008/01/forensic-practical.html)
* [Practical 2](https://www.forensickb.com/2008/01/forensic-practical-2.html)
* [Practical 3](https://www.forensickb.com/2010/01/forensic-practical-exercise-3.html)
* [Practical 4](https://www.forensickb.com/2010/06/forensic-practical-exercise-4.html)

## Linux LEO

Barry Grundy created some disk images as parts of a [Linux-based forensics tutorial](https://linuxleo.com/).

## Digital Forensic Research Workshop (DFRWS)

The Digital Forensic Research Workshop's rodeos and Challenges. Several of the
rodeos and Challenges from DFRWS released their data and scenario writeups. The
following had disk images as parts of their scenario:

* 2005 Rodeo, hosted on [CFReDS](https://cfreds.nist.gov/dfrws/Rhino_Hunt.html)
* 2008 Rodeo
* 2009 Rodeo
* 2009 Challenge
* 2011 Challenge

## The Honeynet Project

In 2001 the Honeynet project distributed a set of disk images and asked
participants to conduct a forensic analysis of a compromised computer.

[The Honeynet Project: Challenges](https://www.honeynet.org/challenges/)

## Honeynet Project: Scans of the Month

The Honeynet Project provided network scans in the majority of its Scan of the
Month challenges. Some of the challenges provided disk images instead. The
Sleuth Kit's Wiki lists Brian Carrier's responses to those challenges.

[Case Studies - Honeynet Challenges](https://wiki.sleuthkit.org/index.php?title=Case_Studies)

## BelkaCTF

[BelkaCTF](https://belkasoft.com/ctf)

# Network Packets and Traces

## DARPA Intrusion Detection Evaluation

In 1998, 1999 and 2000 the Information Systems Technology Group at MIT Lincoln
Laboratory created a test network complete with simulated servers, clients,
clerical workers, programmers, and system managers. Baseline traffic was
collected. The systems on the network were then “attacked” by simulated
hackers. Some of the attacks were well-known at the time, while others were
developed for the purpose of the evaluation.

* [1998 DARPA Intrusion Detection Evaluation](https://www.ll.mit.edu/r-d/datasets/1998-darpa-intrusion-detection-evaluation-dataset)
* [1999 DARPA Intrusion Detection Evaluation](https://www.ll.mit.edu/r-d/datasets/1999-darpa-intrusion-detection-evaluation-dataset)
* [2000 DARPA Intrusion Detection Scenario Specific](https://www.ll.mit.edu/r-d/datasets/2000-darpa-intrusion-detection-scenario-specific-datasets)

## Wireshark

The open source Wireshark project (formerly known as Ethereal) has a
website with many network packet captures:

* <https://wiki.wireshark.org/SampleCaptures>

## NFS Packets

The Storage Networking Industry Association has a set of network file
system traces that can be downloaded from:

* <http://iotta.snia.org/traces>

## Other

Github user "markofu" has aggregated several other network captures into
a Git repository.

* <https://github.com/markofu/pcaps>

# Email messages

*The Enron Corpus* of email messages that were seized by the Federal
Energy Regulatory Commission during its investigation of Enron.

* <http://www.cs.cmu.edu/~enron>
* <http://www.enronemail.com/>

The NIST **TextREtrieval Conference 2007** has released a public Spam
corpus:

* <https://plg.uwaterloo.ca/~gvcormac/spam/>

Email Messages Corpus Parsed from W3C Lists (for TRECENT 2005)

* <https://tides.umiacs.umd.edu/webtrec/trecent/parsed_w3c_corpus.html>

# Text Files

## Log files

[CAIDA](https://catalog.caida.org/) collects a wide variety of data.

[DShield](https://www.dshield.org/howto.html) asks users to submit
firewall logs.

## Text for Text Retrieval

The [Text REtrieval Conference (TREC)](https://trec.nist.gov/) has made
available a series of [text collections](https://trec.nist.gov//data.html).

## American National Corpus

The [American National Corpus (ANC) project](https://anc.org/) is creating
a collection of American english from 1990 onward. The goal is to create a
corpus of at least 100 million words that is comparable to the British
National Corpus.

## British National Corpus

The [British National Corpus (100)](http://www.natcorp.ox.ac.uk/) is a
100 million word collection of written and spoken english from a variety
of sources.

## IEEE VAST Challenges

IEEE Visual Analytics Science & Technology (VAST) Challenges

# Images

[Object and Concept Recognition for Content-Based Image Retrieval](http://imagedatabase.cs.washington.edu)
UW Image Database. A set of freely redistributable images from all over
the world, used for content-based image retrieval.

# Voice

## CALLFRIEND

CALLFRIEND is a database of recorded English conversations. A total of
60 recorded conversations are available from the University of
Pennsylvania at a cost of \$600.

## TalkBank

TalkBank in an online database of spoken language. The project was
originally funded between 1999 and 2004 by two National Science
Foundation grants; ongoing support is provided by two NSF grants and one
NIH grant.

## Augmented Multi-Party Interaction Corpus

The [AMI Meeting Corpus](https://groups.inf.ed.ac.uk/ami/corpus/) has 100 hours
of meeting recordings.

## Other Corpora

* Under an NSF grant, Kam Woods and [Simson Garfinkel](simson_garfinkel.md)
  created a website for [digital corpora](https://digitalcorpora.org/). The
  site includes a complete training scenario, including disk images, packet
  captures and exercises.

* The [Canterbury Corpus](https://corpus.canterbury.ac.nz/) is a set of
  files used for testing lossless compression algorithms. The corpus
  consists of 11 natural files, 4 artificial files, 3 large files, and a
  file with the first million digits of pi. You can also find a copyof
  the Calgaruy Corpus at the website, which was the defacto standard for
  testing lossless compression algorithms in the 1990s.

* The [UMass Trace Repository](https://traces.cs.umass.edu/index.php/Main/HomePage)
  provides network, storage, and other traces to the research community
  for analysis. The UMass Trace Repository is supported by grant
  \#CNS-323597 from the National Science Foundation.

* [Sony has made 60TB of Everquest 2 logs available to researchers.](https://arstechnica.com/gaming/2009/02/aaas-60tb-of-behavioral-data-the-everquest-2-server-logs/)
  What's there? "everything."

* UCI's [Network Data Repository](http://networkdata.ics.uci.edu/resources.php)
  provides data sets of a diverse set of networks. Some of the networks are
  related to computers, some aren't.

* [UT San Antonio Digital Corpora](https://downloads.digitalcorpora.org/corpora/files/filetypes1/)

# External Links

* [Forensic Focus - Test Images and Forensic Challenges](https://www.forensicfocus.com/challenges-and-images/)
* [Honeynet Project Challenges](https://www.honeynet.org/challenges/)
* [Second Look - Linux Memory Images](https://secondlookforensics.com/linux-memory-images/)
* [NullconCTF2014](https://sourceforge.net/projects/nullconctf2014/)
* [Daily Blog \#277: Sample Forensic Images](https://www.hecfblog.com/2014/03/daily-blog-277-sample-forensic-images.html)
* [ForGe – Computer Forensic Test Image Generator](https://www.forensicfocus.com/articles/forge-computer-forensic-test-image-generator/),
  by Hunnu Visti, October 18, 2013
