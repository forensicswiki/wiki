---
tags:
  - Articles that need to be expanded
---
Archived past selected research articles in reverse chronological order.

## May 2014

[Forensic Zero-Knowledge Event Reconstruction on Filesystem Metadata](http://subs.emis.de/LNI/Proceedings/Proceedings228/331.pdf),
by Sven Kälber, Andreas Dewald, Steffen Idler, 2014

Abstract: Criminal investigations today can hardly be imagined without
the forensic analysis of digital devices, regardless of whether it is a
desktop computer, a mobile phone, or a navigation system. This not only
holds true for cases of cybercrime, but also for traditional delicts
such as murder or blackmail, and also private corporate investigations
rely on digital forensics. This leads to an increasing number of cases
with an ever-growing amount of data, that exceeds the capacity of the
forensic experts. To support investigators to work more efficiently, we
introduce a novel approach to automatically reconstruct events that
previously occurred on the examined system and to provide a quick
overview to the investigator as a starting point for further
investigation. In contrast to the few existing approaches, our solution
does not rely on any previously profiled system behavior or knowledge
about specific applications, log files, or file formats. We further
present a prototype implementation of our so-called zero knowledge event
reconstruction approach, that solely tries to make sense of
characteristic structures in file system metadata such as file- and
folder-names and timestamps.

[Measurement and Analysis of Child Pornography Trafficking on P2P Networks](https://dl.acm.org/citation.cfm?id=2488388.2488444),
by Hurley, Ryan, Prusty, Swagatika, Soroush, Hamed, Walls, Robert J., Albrecht, Jeannie, Cecchet,
Emmanuel, Levine, Brian Neil, Liberatore, Marc, Lynn, Brian, Wolak, Janis, 2013.

Abstract: Peer-to-peer networks are the most popular mechanism for the
criminal acquisition and distribution of child pornography (CP). In this
paper, we examine observations of peers sharing known CP on the eMule
and Gnutella networks, which were collected by law enforcement using
forensic tools that we developed. We characterize a year's worth of
network activity and evaluate different strategies for prioritizing
investigators' limited resources. The highest impact research in
criminal forensics works within, and is evaluated under, the constraints
and goals of investigations. We follow that principle, rather than
presenting a set of isolated, exploratory characterizations of users.

First, we focus on strategies for reducing the number of CP files
available on the network by removing a minimal number of peers. We
present a metric for peer removal that is more effective than simply
selecting peers with the largest libraries or the most days online.
Second, we characterize six aggressive peer subgroups, including: peers
using Tor, peers that bridge multiple p2p networks, and the top 10% of
peers contributing to file availability. We find that these subgroups
are more active in their trafficking, having more known CP and more
uptime, than the average peer. Finally, while in theory Tor presents a
challenge to investigators, we observe that in practice offenders use
Tor inconsistently. Over 90% of regular Tor users send traffic from a
non-Tor IP at least once after first using Tor.

## June 2013

[Digging up social structures from documents on the web](https://doi.org/10.1109/GLOCOM.2012.6503202),
by Gessiou, E., Volanis, S., Athanasopoulos, E., Markatos, E.P., Ioannidis, S., 2012.

Abstract: We collected more than ten million Microsoft Office documents
from public websites, analyzed the metadata stored in each document and
extracted information related to social activities. Our analysis
revealed the existence of exactly identified cliques of users that edit,
revise and collaborate on industrial and military content. We also
examined cliques in documents downloaded from Fortune-500 company
websites. We constructed their graphs and measured their properties. The
graphs contained many connected components and presented social
properties. The a priori knowledge of a company's social graph may
significantly assist an adversary to launch targeted attacks, such as
targeted advertisements and phishing emails. Our study demonstrates the
privacy risks associated with metadata by cross-correlating all members
identified in a clique with users of Twitter. We show that it is
possible to match authors collaborating in the creation of a document
with Twitter accounts. To the best of our knowledge, this study is the
first to identify individuals and create social cliques solely based on
information derived from document metadata. Our study raises major
concerns about the risks involved in privacy leakage due to document
metadata.

## Jan 2013

[Distinct Sector hashing for Target Detection](https://doi.org/10.1109/MC.2012.327),
by Joel Young, Kristina Foster, Simson Garfinkel, Kevin Fairbanks, December 2012.

Abstract: Using an alternative approach to traditional file hashing,
digital forensic investigators can hash individually sampled subject
drives on sector boundaries and then check these hashes against a
prebuilt database, making it possible to process raw media without
reference to the underlying file system.

## Aug 2012

[Infiltrate the Vault: Security Analysis and Decryption of Lion Full Disk Encryption](https://eprint.iacr.org/2012/374.pdf),
by Omar Choudary, Felix Grobert, Joachim Metz, August 2012.

Abstract: With the launch of Mac OS X 10.7 (Lion), Apple has introduced a volume
encryption mechanism known as FileVault 2. Apple only disclosed
marketing aspects of the closed-source software, e.g. its use of the
AES-XTS tweakable encryption, but a publicly available security
evaluation and detailed description was unavailable until now.. We have
performed an extensive analysis of FileVault 2 and we have been able to
ﬁnd all the algorithms and parameters needed to successfully read an
encrypted volume. This allows us to perform forensic investigations on
encrypted volumes using our own tools. In this paper we present the
architecture of FileVault 2, giving details of the key derivation,
encryption process and metadata structures needed to perform the volume
decryption. Besides the analysis of the system, we have also built a
library that can mount a volume encrypted with FileVault 2. As a
contribution to the research and forensic communities we have made this
library open source. Additionally, we present an informal security
evaluation of the system and comment on some of the design and
implementation features. Among others we analyze the random number
generator used to create the recovery password. We have also analyzed
the entropy of each 512-byte block in the encrypted volume and
discovered that part of the user data was left unencrypted.

## Mar 2012

[Effective Digital Forensics Research Is Investigator-Centric](https://www.usenix.org/events/hotsec11/tech/final_files/Walls.pdf),
by Robert J. Walls, Brian Neil Levine, Marc Liberatore, Clay Shields, August 2011.

Abstract: Many technical mechanisms across computer security for
attribution, identiﬁcation, and classiﬁcation are neither sufﬁcient nor
necessary for forensically valid digital investigations; yet they are
often claimed as useful or necessary. Similarly, when forensic research
is evaluated using the viewpoints held by computer security venues, the
challenges, constraints, and usefulness of the work is often misjudged.
In this paper, we point out many key aspects of digital forensics with
the goal of ensuring that research seeking to advance the discipline
will have the highest possible adoption rate by practitioners. We
enumerate general legal and practical constraints placed on forensic
investigators that set the ﬁeld apart. We point out the assumptions,
often limited or incorrect, made about forensics in past work, and
discuss how these assumptions limit the impact of contributions.

* [Usenix Presentation](https://www.usenix.org/conference/hotsec11/effective-digital-forensics-research-investigator-centric)
* [Slides](https://www.usenix.org/events/hotsec11/tech/slides/walls.pdf)
* [paper](https://www.usenix.org/events/hotsec11/tech/final_files/Walls.pdf)

[PinDr0p: using single-ended audio features to determine call provenance](https://dl.acm.org/doi/10.1145/1866307.1866320),
by Vijay A. Balasubramaniyan, Aamir Poonawalla, Mustaque Ahamad, Michael T. Hunter, Patrick Traynor,
2010.

Abstract: The recent diversification of telephony infrastructure allows
users to communicate through landlines, mobile phones and VoIP phones.
However, call metadata such as Caller-ID is either not transferred or
transferred without verification across these networks, allowing
attackers to maliciously alter it. In this paper, we develop PinDr0p, a
mechanism to assist users in determining call provenance - the source
and the path taken by a call. Our techniques detect and mea- sure
single-ended audio features to identify all of the applied voice codecs,
calculate packet loss and noise profiles, while remaining agnostic to
characteristics of the speaker's voice (as this may legitimately
change when interacting with a large organization). In the absence of
verifiable call metadata, these features in combina- tion with machine
learning allow us to determine the traversal of a call through as many
as three different providers (e.g., cellular, then VoIP, then PSTN and
all combinations and subsets thereof) with 91.6% accuracy. Moreover, we
show that once we identify and characterize the networks traversed, we
can create detailed fin- gerprints for a call source. Using these
fingerprints we show that we are able to distinguish between calls made
using specific PSTN, cellular, Vonage, Skype and other hard and soft
phones from locations across the world with over 90% accuracy. In so
doing, we provide a first step in accurately determining the provenance
of a call.

## Jan 2012

[Design of a Digital Forensics Evidence Reconstruction System for Complex and Obscure Fragmented
File Carving](https://doi.org/10.1109/CIS.2011.180),
by Vrizlynn L.L. Thing, Tong-Wei Chua, Ming-Lee Cheong, 2011.

## Dec 2011

[Security Aspects of Piecewise Hashing in Computer Forensics](https://doi.org/10.1109/IMF.2011.16),
by Baier, H., Breitinger, F., May 2011.

Abstract: Although hash functions are a
well-known method in computer science to map arbitrary large data to bit
strings of a fixed length, their use in computer forensics is currently
very limited. As of today, in a pre-step process hash values of files
are generated and stored in a database, typically a cryptographic hash
function like MD5 or SHA-1 is used. Later the investigator computes hash
values of files, which he finds on a storage medium, and performs look
ups in his database. This approach has several drawbacks, which have
been sketched in the community, and some alternative approaches have
been proposed. The most popular one is due to Jesse Kornblum, who
transferred ideas from spam detection to computer forensics in order to
identify similar files. However, his proposal lacks a thorough security
analysis. It is therefore one aim of the paper at hand to present some
possible attack vectors of an active adversary to bypass Kornblum's
approach. Furthermore, we present a pseudo random number generator being
both more efficient and more random compared to Kornblum's pseudo random
number generator.

## August 2011

[Forensic Carving of Network Packets and Associated Data Structures](https://doi.org/10.1016/j.diin.2011.05.010),
by Robert Beverly, Simson Garfinkel, Gregory Cardwell, August 2011.

Abstract: Using validated carving techniques, we show that popular
operating systems (\eg Windows, Linux, and OSX) frequently have residual
IP packets, Ethernet frames, and associated data structures present in
system memory from long-terminated network traffic. Such information is
useful for many forensic purposes including establishment of prior
connection activity and services used; identification of other systems
present on the system's LAN or WLAN; geolocation of the host computer
system; and cross-drive analysis. We show that network structures can
also be recovered from memory that is persisted onto a mass storage
medium during the course of system swapping or hibernation. We present
our network carving techniques, algorithms and tools, and validate these
against both purpose-built memory images and a readily available
forensic corpora. These techniques are valuable to both forensics tasks,
particularly in analyzing mobile devices, and to cyber-security
objectives such as malware analysis.

## July 2011

[Theory and practice of flash memory mobile forensics](https://ro.ecu.edu.au/adf/67/),
by Salvatore Fiorillo, 2009

## June 2011

[Judges' Awareness, Understanding, and Application of Digital Evidence](https://nsuworks.nova.edu/gscis_etd/196),
by Gary Craig Kessler, 2010

## July 2010

Sleuth Kit and [Open Source Digital Forensics Conference](https://www.osdfcon.org/)

The slides from the first ever Sleuth Kit and Open Source Digital
Forensics Conference are now available online:

* [The Sleuth Kit Overview and Automated Scanning Features](https://www.basistech.com/about/events/)
  (Brian Carrier)
* [Faster Response with Sleuth Kit and Other Open Source Technologies](https://www.basistech.com/about/events/)
  (Jamie Butler and Jason Shiffer)
* [PTK Forensics after Two years: Past, Present and Future](https://www.basistech.com/about/events/)
  (Dario Forte)
* [Mac Forensic Tools Using Sleuth Kit](https://www.basistech.com/about/events/)
  (Rob Joyce)
* [Commando Forensics: What Dongle?](https://www.basistech.com/about/events/)
  (Cory Altheide)
* [AFF and AFF4: Where we are, where we are going, and why it matters to you.](https://www.basistech.com/about/events/)
  (Simson Garfinkel)
* [Timeline Creation using Open-Source Tools](https://www.basistech.com/about/events/)
  (Harlan Carvey)

## March 2010

[Internet geolocation: Evasion and counterevasion](https://dl.acm.org/doi/10.1145/1592451.1592455)
ACM Computing Surveys (CSUR), Volume 42, Issue 1 (December 2009)

Abstract: Internet geolocation technology aims to determine the physical
(geographic) location of Internet users and devices. It is currently
proposed or in use for a wide variety of purposes, including targeted
marketing, restricting digital content sales to authorized
jurisdictions, and security applications such as reducing credit card
fraud. This raises questions about the veracity of claims of accurate
and reliable geolocation. We provide a survey of Internet geolocation
technologies with an emphasis on adversarial contexts; that is, we
consider how this technology performs against a knowledgeable
adversary whose goal is to evade geolocation. We do so by examining
first the limitations of existing techniques, and then, from this
base, determining how best to evade existing geolocation techniques.
We also consider two further geolocation techniques which may be of
use even against adversarial targets: (1) the extraction of client IP
addresses using functionality introduced in the 1.5 Java API, and (2)
the collection of round-trip times using HTTP refreshes. These
techniques illustrate that the seemingly straightforward technique of
evading geolocation by relaying traffic through a proxy server (or
network of proxy servers) is not as straightforward as many end-users
might expect. We give a demonstration of this for users of the popular
Tor anonymizing network.

## February 2010

[The 'CSI Effect': Does It Really Exist?](https://nij.ojp.gov/topics/articles/csi-effect-does-it-really-exist),
by The Honorable Donald E. Shelton

Abstract: Crime and courtroom proceedings have long been fodder for film and
television scriptwriters. In recent years, however, the media's use of
the courtroom as a vehicle for drama has not only proliferated, it has
changed focus. In apparent fascination with our criminal justice
process, many of today's courtroom dramas are based on actual cases.
Court TV offers live gavel-to-gavel coverage of trials over the Internet
for \$5.95 a month. Now, that's "reality television"!

Reality and fiction have begun to blur with crime magazine television
shows such as 48 Hours Mystery, American Justice, and even, on occasion,
Dateline NBC. These programs portray actual cases, but only after
extensively editing the content and incorporating narration for dramatic
effect. Presenting one 35-year-old cold case, for example, 48 Hours
Mystery filmed for months to capture all pretrial hearings as well as
the 2-week trial; the program, however, was ultimately edited to a
1-hour episode that suggested the crime remained a "mystery" ...
notwithstanding the jury's guilty verdict.

## January 2010

[Using Graphics Processors for Parallelizing Hash-based Data Carving](https://hal.science/file/index/docid/350962/filename/ColDanDauDef09.pdf),
by Sylvain Collange, Marc Daumas, Yoginder S. Dandass, and David Defour

Abstract: The ability to detect fragments of deleted image files and to
reconstruct these image files from all available fragments on disk is a
key activity in the field of digital forensics. Although reconstruction
of image files from the file fragments on disk can be accomplished by
simply comparing the content of sectors on disk with the content of
known files, this brute-force approach can be time consuming.

This paper presents results from research into the use of Graphics
Processing Units (GPUs) in detecting specific image file byte patterns
in disk clusters. Unique identifying pattern for each disk sector is
compared against patterns in known images. A pattern match indicates the
potential presence of an image and flags the disk sector for further
in-depth examination to confirm the match. The GPU-based implementation
outperforms the software implementation by a significant margin.

## September 2009

[Developments in Cisco IOS Forensics](https://www.blackhat.com/presentations/bh-dc-08/FX/Whitepaper/bh-dc-08-fx-WP.pdf)
by Felix Lindner

Abstract: Cisco System's routers running Cisco IOS are still the prevalent
routing platform on the Internet and corporate networks. Their huge
population, architectural deficiencies and hugely diverse version
distribution make them a valuable target that gains importance as common
operating system platforms are closed down and secured. This paper takes
the position that the currently used, well accepted practices for
monitoring, debugging and post mortem crash analysis are insufficient to
deal with the threat of compromised IOS devices. It sets forth a
different method that reduces the requirement for constant logging,
favoring on- demand in-depth analysis in case of suspicion or actual
device crashes. The paper concludes by presenting the current state in
the development of software supporting the proposed method and
requesting feedback from the community on the software's future
directions.

## June 2009

[Recovery of Damaged Compressed Files for Digital Forensic Purposes](https://ieeexplore.ieee.org/document/4505751/?tp=http://ieeexplore.ieee.org/xpl/freeabs_all.jsp?tp=&arnumber=4505751&isnumber=4505671arnumber=4505751http://ieeexplore.ieee.org/xpl/freeabs_all.jsp?tp=&arnumber=4505751&isnumber=4505671isnumber=4505671),
by Bora Park Savoldi, A. Gubian, P. Jungheum Park Seok Hee Lee Sangjin Lee

Abstract: Nowadays compressed files are very widespread and can be considered,
without any doubt, with regard to the Digital Forensic realm, an
important and precious source of probatory data. This is especially true
when in a digital investigation the examiner has to deal with corrupted
compressed files, which have been gathered in the collection phase of
the investigative process. Therefore, in the computer forensic field,
data recovery technologies are very important for acquiring useful
pieces of data which can become, in a court of low, digital evidence.
This kind of technology is used not only by law enforcement, but also by
the multitude of users in their daily activities, which justify the
relevant presence of tools in the software market which are devoted to
rescue data from damaged compressed files. However, state-of-the-art
data recovery tools have many limitations with regard to the capability
of recovering the original data, especially in the case of damaged
compressed files. So far, such recovery tools have been based on a which
controls the signature/header of the file and, thus, provides the offset
to the raw compressed data block. As a result, they cannot recover the
compressed files if the first part of the raw compressed data block,
which pertains to the header, is damaged or the signature/header block
is corrupted. Therefore, in order to deal with this issue, we have
developed a new tool capable of rescuing damaged compressed files,
according to the DEFLATE compression scheme, even though the header
block is missing or corrupted. This represents a new interesting
opportunity for the digital forensic discipline.

## April 2009

[A Framework for Automated Digital Forensic Reporting](https://simson.net/clips/students/09_Farrell.pdf),
by Lt. Paul Farrell, March 2009

Abstract: Forensic analysis is the science of finding, examining and analyzing
evidence in support of law enforcement, regulatory compliance or
information gathering. Today, almost all digital forensic analysis is
done by humans, requiring dedicated training and consuming man-hours at
a considerable rate. As storage sizes increase and digital forensics
gain importance in investigations, the backlog of media requiring human
analysis has increased as well. This thesis tests today's
top-of-the-line commercial and open source forensic tools with the
analysis of a purpose-built Windows XP computer system containing two
users that engaged in email, chat and web browsing. It presents the
results of a pilot user study of the PyFlag forensic tool. Finally, it
presents a technique to use software to do a preliminary analysis on
media and provide a human readable report to the examiner. The goal of
the technique is to perform rapid triaging of media and allow the human
examiner to better prioritize man hours towards media with high return
on investment.

## February 2009

[The impact of full disk encryption on digital forensics](https://dl.acm.org/doi/10.1145/1368506.1368519),
ACM SIGOPS Operating Systems Review archive, Volume 42, Issue 3 (April 2008), Pages 93-98

Abstract: The integration of strong encryption into operating systems is creating
challenges for forensic examiners, potentially preventing us from
recovering any digital evidence from a computer. Because strong
encryption cannot be circumvented without a key or passphrase, forensic
examiners may not be able to access data after a computer is shut down,
and must decide whether to perform a live forensic acquisition. In
addition, with encryption becoming integrated into the operating system,
in some cases, virtualization is the most effective approach to
performing a forensic examination of a system with FDE. This paper
presents the evolution of full disk encryption (FDE) and its impact on
digital forensics. Furthermore, by demonstrating how full disk
encryption has been dealt with in past investigations, this paper
provides forensics examiners with practical techniques for recovering
evidence that would otherwise be inaccessible.

## January 2009

[Forensic Investigation of the Nintendo Wii: A First Glance](https://www.researchgate.net/publication/253436253_Forensic_Investigation_of_the_Nintendo_Wii_A_First_Glance),
by Dr. Benjamin Turnbull

Abstract: The closed nature of the Wii makes it a challenging game console for
forensic analysis. This article takes a first look at the platform,
discussing the various places where forensically interesting information
may be hidden. There's also a reference to an interesting article about
how the ability of wimotes to move avatars from one system to another
documents a woman's affair while her husband was serving in Iraq.

## November 2008

[Data Acquisition from Cell Phone using Logical Approach](https://publications.waset.org/7561/data-acquisition-from-cell-phone-using-logical-approach),
by Keonwoo Kim, Dowon Hong, Kyoil Chung, and Jae-Cheol Ryou

Abstract: The article discusses three approaches for acquiring data from cell phones:
physically removing the flash RAM chips and reading them directly; reading the
data out using the JTAG interface, and running software on the cell phone to
extract the files at a logical level. The authors have built a logical
extraction system and are working on a system based on JTAG.

## October 2008

[Advanced JPEG carving](https://dl.acm.org/doi/10.5555/1363217.1363239),
by Michael I. Cohen

Abstract: Michael I. Cohen presents a fully automated carver which can carve
fragmented JPEGs using typical fragmentation patterns. (Cohen argues the
the DFRWS carving challenges do not represent typical fragmentation
patterns.)

[Threats to Privacy in the Forensic Analysis of Database Systems](https://people.cs.umass.edu/~miklau/assets/pubs/sigmod2007LMS/stahlberg07forensicDB.pdf)
by Patrick Stahlberg, Gerome Miklau, and Brian Neil Levine

Abstract: This paper looks at residual data left behind in databases after DELETE,
UPDATE, and VACUUM operations. The authors show that residual data is a
real issue in databases, and that it's pretty easy to modify a database
so that no residual data is left behind. MySQL with MyISM tables has
clean delete, but InnoDB does not. Very much worth reading.

## August 2008

[Lest We Remember: Cold Boot Attacks on Encryption Keys](https://www.usenix.org/legacy/events/sec08/tech/halderman.html)
by J. Alex Halderman, Seth D. Schoen, Nadia Heninger, William Clarkson, William Paul, Joseph A.
Calandrino, Ariel J. Feldman, Jacob Appelbaum, Edward W. Felten

Abstract: Increasingly memory analysis is of interest in forensic research - both
because new malware only resides in memory, and because memory analysis
is frequently the only way for analysts to get the keys that are used to
protect cryptographic file systems. In this paper the authors show that
cryptographic keys in memory are vulnerable to exploitation *after the
computer is turned off.* The authors show that the contents of dynamic
RAM are retained seconds, and sometimes minutes, after power is turned
off. By chilling the memory the data can be retained as long as
necessary. And while most laptops wipe their memory when they reboot,
the authors show that the chilled memory can be moved from one laptop
that wipes to another laptop that does not wipe. Finally, the authors
show that it is possible to find the cryptographic keys in memory and
correct random bit errors by using the AES key schedule as an
error-correction code. The authors demonstrate an attack USB stick which
reboots a computer protected with BitLocker, finds the cryptographic
keys, and then allows access to the cleartext information on the disk.

## July 2008

[The Challenges of Using an Intrusion Detection System: Is It Worth the Effort?](http://cups.cs.cmu.edu/soups/2008/proceedings/p107Werlinger.pdf),
by Rodrigo Werlinger, Kirstie Hawkey, Kasia Muldner, Pooya Jaferian and Konstantin Beznosov.

Abstract: In this article, the authors conducted interviews with 9 IT security
practitioners who have worked with IDSs performed ethnographic
observations within an organization that was deploying a new IDS. They
found that security practitioners were heavily divided on the value of
the IDS, and learned that the an IDS really only generates value if the
network is well-understood before the IDS is deployed.

* [slides](http://cups.cs.cmu.edu/soups/2008/slides/hawkey_soups.ppt)

[Mobile Phone Forensics Tool Testing: A Database Drive Approach](https://www.utica.edu/academic/institutes/ecii/publications/articles/1C33DF76-D8D3-EFF5-47AE3681FD948D68.pdf),
 by Ibrahim M. Baggili, Richard Mislan, Marcus Rogers, 2007

Abstract: Given that phones
are increasingly a primary source of forensic information in many cases,
we need to be sure that the tools that are used for forensic analysis
present data that is accurate and repeatable. Unfortunately they
frequently aren't because of there are so many different kinds of phones
on the market and the forensic tools lag far behind the market.

[Detecting File Fragmentation Point Using Sequential Hypothesis Testing](https://doi.org/10.1016/j.diin.2008.05.015),
by Anandabrata Pal, Taha Sencar, Nasir Memon, 2008

Abstract: This DFRWS 2008 article presents an improved approach for carving
fragmented JPEGs using sequential hypothesis testing. According to the
authors, "The technique begins with a header block identifying the start
of a ﬁle and then attempts to validate via SHT each subsequent block
following the header block. The fragmentation point is identiﬁed when
SHT identiﬁes a block as not belonging to the ﬁle. By utilizing this
technique, we are able to correctly and efﬁciently recover JPEG images
from the DFRWS 2006 and 2007 test sets even in the presence
of tens of thousands of blocks and ﬁles fragmented into 3 or more parts.
The bifragment gap carving technique enhanced with SHT allows us to
improve the performance result of DFRWS 2006 challenge test-sets,
although the technique cannot be used for DFRWS 2007. We then show how
Parallel Unique Path enhanced with SHT is able to recover all fragmented
JPEGs from DFRWS 2006 and all recoverable JPEGs from 2007 challenge
test-sets. As far as we are aware, no other automated technique can
recover multi-fragmented JPEGs from the DFRWS 2007 test set."

[An Empirical Analysis of Disk Sector Hashes for Data Carving](https://doi.org/10.1080/15567280802050436),
by Yoginder Singh Dandass, Nathan Joseph Necaise, Sherry Reede Thomas, 2008

Abstract: Authors Dandass *et. al* analyzed 528 million sectors from 433,630
unique files. They computed the CRC32, CRC64, MD5 and SHA-1 of each
sector. Not surprisingly, they find that the MD5 and SHA-1s of the
sectors are different if the sectors are different. They find 94 CRC64
collisions and 30 million CRC32 collisions. The conclusion is that, if
you are search for a single sector or building a database of single
sector hashes, you are better off building a database of CRC64s because
they are easier to store and dramatically faster to calculate than the
traditional hash functions, and they are nearly as accurate.
