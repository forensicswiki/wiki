---
tags:
  - No Category
---
*Archived past selected research articles*

<small>May 2014</small> <bibtex>
@inproceedings{Hurley:2013:MAC:2488388.2488444,

`author = {Sven Ka ̈lber, Andreas Dewald, Steffen Idler},`
`title = {Forensic Zero-Knowledge Event Reconstruction on Filesystem Metadata},`
`booktitle = {Lecture Notes in Informatics},`
`volume="P-228",`
`year=2014,`
`url = {http://subs.emis.de/LNI/Proceedings/Proceedings228/331.pdf},`

} </bibtex>

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

<small>May 2014</small> <bibtex>
@inproceedings{Hurley:2013:MAC:2488388.2488444,

`author = {Hurley, Ryan and Prusty, Swagatika and Soroush, Hamed and Walls, Robert J. and Albrecht, Jeannie and Cecchet, Emmanuel and Levine, Brian Neil and Liberatore, Marc and Lynn, Brian and Wolak, Janis},`
`title = {Measurement and Analysis of Child Pornography Trafficking on P2P Networks},`
`booktitle = {Proceedings of the 22Nd International Conference on World Wide Web},`
`series = {WWW '13},`
`year = {2013},`
`isbn = {978-1-4503-2035-1},`
`location = {Rio de Janeiro, Brazil},`
`pages = {631--642},`
`numpages = {12},`
`url = {http://dl.acm.org/citation.cfm?id=2488388.2488444)},`
`acmid = {2488444},`
`publisher = {International World Wide Web Conferences Steering Committee},`
`address = {Republic and Canton of Geneva, Switzerland},`
`keywords = {digital forensics, forensic triage},`

} </bibtex> Peer-to-peer networks are the most popular mechanism for the
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

<small>June 2013</small> <bibtex> @INPROCEEDINGS{6503202,
author={Gessiou, E. and Volanis, S. and Athanasopoulos, E. and Markatos,
E.P. and Ioannidis, S.}, booktitle={Global Communications Conference
(GLOBECOM), 2012 IEEE}, title={Digging up social structures from
documents on the web}, year={2012}, pages={744-750}, abstract={We
collected more than ten million Microsoft Office documents from public
websites, analyzed the metadata stored in each document and extracted
information related to social activities. Our analysis revealed the
existence of exactly identified cliques of users that edit, revise and
collaborate on industrial and military content. We also examined cliques
in documents downloaded from Fortune-500 company websites. We
constructed their graphs and measured their properties. The graphs
contained many connected components and presented social properties. The
a priori knowledge of a company's social graph may significantly assist
an adversary to launch targeted attacks, such as targeted advertisements
and phishing emails. Our study demonstrates the privacy risks associated
with metadata by cross-correlating all members identified in a clique
with users of Twitter. We show that it is possible to match authors
collaborating in the creation of a document with Twitter accounts. To
the best of our knowledge, this study is the first to identify
individuals and create social cliques solely based on information
derived from document metadata. Our study raises major concerns about
the risks involved in privacy leakage due to document metadata.},
keywords={data privacy;document handling;graph theory;meta data;social
networking (online);Fortune-500 company Websites;Microsoft Office
documents;Twitter accounts;company social graph;document
metadata;information extraction;metadata analysis;phishing
emails;privacy leakage;privacy risks;public Websites;social
activities;social cliques;social properties;social structures;targeted
advertisements}, doi={10.1109/GLOCOM.2012.6503202}, ISSN={1930-529X},}
</bibtex> We collected more than ten million Microsoft Office documents
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

<small>Jan 2013</small> <bibtex> @article{young:distinct,

`title="Distinct Sector hashing for Target Detection",`
`author="Joel Young and Kristina Foster and Simson Garfinkel and Kevin Fairbanks",`
`year=2012,`
`month=Dec,`
`journal="IEEE Computer"`

} </bibtex> Using an alternative approach to traditional file hashing,
digital forensic investigators can hash individually sampled subject
drives on sector boundaries and then check these hashes against a
prebuilt database, making it possible to process raw media without
reference to the underlying file system.

<small>Aug 2012</small> <bibtex> @misc{apple, title="Inﬁltrate the
Vault: Security Analysis and Decryption of Lion Full Disk Encryption",

`abstract="With the launch of Mac OS X 10.7 (Lion), Apple has introduced a volume encryption mechanism known as FileVault 2. Apple only disclosed marketing aspects of the closed-source software, e.g. its use of the AES-XTS tweakable encryption, but a publicly available security evaluation and detailed description was unavailable until now.. We have performed an extensive analysis of FileVault 2 and we have been able to ﬁnd all the algorithms and parameters needed to successfully read an encrypted volume. This allows us to perform forensic investigations on encrypted volumes using our own tools. In this paper we present the architecture of FileVault 2, giving details of the key derivation, encryption process and metadata structures needed to perform the volume  decryption. Besides the analysis of the system, we have also built a library that can mount a volume encrypted with FileVault 2. As a contribution to the research and forensic communities we have made this library open source. Additionally, we present an informal security evaluation of the system and comment on some of the design and implementation features. Among others we analyze the random number generator used to create the recovery password. We have also analyzed the entropy of each 512-byte block in the encrypted volume and discovered that part of the user data was left unencrypted",`

author="Omar Choudary and Felix Grobert and Joachim Metz", year=2012,
month=Aug, url="<http://eprint.iacr.org/2012/374.pdf>" } </bibtex> With
the launch of Mac OS X 10.7 (Lion), Apple has introduced a volume
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

<small>Mar 2012</small>

<bibtex> @inproceedings{Walls:2011a, Audio_Url =
{<http://prisms.cs.umass.edu/brian/pubs/Walls.hotsec.2011.mp3>}, Author
= { Robert J. Walls and Brian Neil Levine and Marc Liberatore and Clay
Shields}, Booktitle = {Proc.\\ USENIX Workshop on Hot Topics in Security
(HotSec)}, Keywords = {forensics; security}, Month = {August},
Slides_Url =
{<http://prisms.cs.umass.edu/brian/pubs/rjwalls.hotsec.2011.slides.pdf>},
Sponsors = {CNS-1018615, CNS-0905349, DUE-0830876, 2008-CE-CXK005},
Title = , Url =
{<http://prisms.cs.umass.edu/brian/pubs/Walls.hotsec.2011.pdf>},
Video_Url =
{<http://prisms.cs.umass.edu/brian/pubs/Walls.hotsec.2011.mp4>}, Year =
{2011}, Bdsk-Url-1 =
{<http://prisms.cs.umass.edu/brian/pubs/Walls.hotsec.2011.pdf>}}
</bibtex> Many technical mechanisms across computer security for
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

- [Usenix
  Presentation](https://www.usenix.org/conference/hotsec11/effective-digital-forensics-research-investigator-centric)
- [Slides](http://prisms.cs.umass.edu/brian/pubs/rjwalls.hotsec.2011.slides.pdf)
- [paper](http://prisms.cs.umass.edu/brian/pubs/Walls.hotsec.2011.pdf)

<small>March 2012</small> <bibtex>
@inproceedings{Balasubramaniyan:2010:PUS:1866307.1866320,

`author = {Balasubramaniyan, Vijay A. and Poonawalla, Aamir and Ahamad, Mustaque and Hunter, Michael T. and Traynor, Patrick},`
`title = {PinDr0p: using single-ended audio features to determine call provenance},`
`booktitle = {Proceedings of the 17th ACM conference on Computer and communications security},`
`series = {CCS '10},`
`year = {2010},`
`isbn = {978-1-4503-0245-6},`
`location = {Chicago, Illinois, USA},`
`pages = {109--120},`
`numpages = {12},`
`url = {`[`https://dl.acm.org/doi/10.1145/1866307.1866320`](https://dl.acm.org/doi/10.1145/1866307.1866320)`},`
`doi = {`[`https://dl.acm.org/doi/10.1145/1866307.1866320`](https://dl.acm.org/doi/10.1145/1866307.1866320)`},`
`acmid = {1866320},`
`publisher = {ACM},`
`address = {New York, NY, USA},`
`keywords = {VoIP, call fingerprinting, provenance, telephony},`

}

</bibtex> The recent diversification of telephony infrastructure allows
users to communicate through landlines, mobile phones and VoIP phones.
However, call metadata such as Caller-ID is either not transferred or
transferred without verification across these networks, allowing
attackers to maliciously alter it. In this paper, we develop PinDr0p, a
mechanism to assist users in determining call provenance — the source
and the path taken by a call. Our techniques detect and mea- sure
single-ended audio features to identify all of the applied voice codecs,
calculate packet loss and noise profiles, while remaining agnostic to
characteristics of the speaker’s voice (as this may le- gitimately
change when interacting with a large organization). In the absence of
verifiable call metadata, these features in combina- tion with machine
learning allow us to determine the traversal of a call through as many
as three different providers (e.g., cellular, then VoIP, then PSTN and
all combinations and subsets thereof) with 91.6% accuracy. Moreover, we
show that once we identify and characterize the networks traversed, we
can create detailed fin- gerprints for a call source. Using these
fingerprints we show that we are able to distinguish between calls made
using specific PSTN, cellular, Vonage, Skype and other hard and soft
phones from loca- tions across the world with over 90% accuracy. In so
doing, we provide a first step in accurately determining the provenance
of a call.

<small>Jan 2012</small>

<bibtex> @article{10.1109/CIS.2011.180, author = {Vrizlynn L.L. Thing
and Tong-Wei Chua and Ming-Lee Cheong}, title = {Design of a Digital
Forensics Evidence Reconstruction System for Complex and Obscure
Fragmented File Carving}, journal ={Computational Intelligence and
Security, International Conference on}, volume = {0}, isbn =
{978-0-7695-4584-4}, year = {2011}, pages = {793-797}, doi =
{<https://www.computer.org/csdl/proceedings-article/cis/2011/4584a793/12OmNyQGS02>}, publisher =
{IEEE Computer Society}, address = {Los Alamitos, CA, USA}, } </bibtex>

<small>Dec 2011</small>

<bibtex> @INPROCEEDINGS{5931110, author={Baier, H. and Breitinger, F.},
booktitle={IT Security Incident Management and IT Forensics (IMF), 2011
Sixth International Conference on}, title={Security Aspects of Piecewise
Hashing in Computer Forensics}, year={2011}, month={may}, volume={},
number={}, pages={21 -36}, keywords={MD5 hash function;SHA-1 hash
function;computer forensics;cryptographic hash function;piecewise
hashing security aspect;pseudorandom number generator;security
analysis;computer forensics;cryptography;random number generation;},
doi={10.1109/IMF.2011.16}, abstract="Although hash functions are a
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
number generator." ISSN={},} </bibtex> Although hash functions are a
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

<small>August 2011</small>

<bibtex> @article{beverly:ipcarving,

`author = "Robert Beverly and Simson Garfinkel and Gregory Cardwell",`
`journal = "Digital Investigation",`
`publisher="Elsevier",`
`booktitle = {Proc. of the Eleventh Annual DFRWS Conference},`
`title = "Forensic Carving of Network Packets and Associated Data Structures",`
`volume=8`
`year = 2011,`
`abstract="Using validated carving techniques, we show that popular operating systems (\eg Windows, Linux, and OSX)  frequently have residual IP packets, Ethernet frames,   and associated data structures present in system memory   from long-terminated network traffic. Such information is useful   for many forensic purposes including establishment of   prior connection activity and services used;   identification of other   systems present on the system's LAN or WLAN; geolocation of the   host computer system; and cross-drive analysis. We show that network structures can also be   recovered from memory that is persisted onto a mass storage medium   during the course of system swapping or hibernation.   We present our network carving techniques, algorithms and tools,   and validate these against both purpose-built memory images and a readily   available forensic corpora.  These techniques are   valuable to both forensics tasks, particularly   in analyzing mobile devices, and to cyber-security objectives such  as malware analysis."`

} </bibtex> <i>Using validated carving techniques, we show that popular
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
objectives such as malware analysis.</i>

<small>July 2011</small> <bibtex> @article{fiorillo-flash,

`title="Theory and practice of flash memory mobile forensics",`
`year=2009,`
`author="Salvatore Florillio",`
` url="`[`https://ro.ecu.edu.au/adf/67/`](https://ro.ecu.edu.au/adf/67/)`",`
`publisher="School of Computer and Information Science, Edith Cowan University, Perth, Western Australia",`
`abstract="This paper is an introduction to flash memory forensics with a special focus on completeness of evidence acquired from mobile phones. Moving through academic papers and industrial documents will be introduced the particular nature of non-volatile memories present in nowadays mobile phones; how they really work and which challenges they pose to forensic investigators. Then will be presented an advanced test in which some brand new flash memories have been used to hide data in man-made bad blocks: the aim is to verify if forensic software tools are able to acquire data from such blocks, and to evaluate the possibility to hide data at analysts’ eyes."`

} </bibtex>

<small>June 2011</small> <bibtex> @PhDThesis{Kessler2010,

`title="Judges’ Awareness, Understanding, and Application of Digital Evidence",`
`author="Gary Craig Kessler",`
`year=2010,`
`institution="Graduate School of Computer and Information Sciences Nova Southeastern University",`

} </bibtex>

<small>Spring 2011</small> [Solid State Drive (SSD)
Forensics](solid_state_drive_(ssd)_forensics.md)
We now have a new page on SSD forensics. The page has some basic
information and a growing bibliography. One of the first entries is:
<bibtex> @inproceedings{wei2011,

` author = {Michael Wei and Laura M. Grupp and Frederick M. Spada and Steven Swanson},`
` title = {Reliably Erasing Data from Flash-Based Solid State Drives},`
` booktitle={FAST 2011},`
` year = 2011,`
` keywords = {erasing flash security ssd},`
` added-at = {2011-02-22T09:22:03.000+0100},`
` url={`[`https://cseweb.ucsd.edu//~m3wei/assets/pdf/FMS-2010-Secure-Erase.pdf`](https://cseweb.ucsd.edu//~m3wei/assets/pdf/FMS-2010-Secure-Erase.pdf)`},`
` biburl = {`[`https://www.bibsonomy.org/bibtex/27c408ad559fc19f829717f485707a909/schmidt2`](https://www.bibsonomy.org/bibtex/27c408ad559fc19f829717f485707a909/schmidt2)`}`

} </bibtex>

(Past selected articles [are archived here](past_selected_articles.md)

</div>

<small>JULY-2010</small>

Sleuth Kit and Open Source Digital Forensics Conference

The slides from the first ever Sleuth Kit and Open Source Digital
Forensics Conference are now available online:

- <https://www.osdfcon.org/>

Highlights include:

- [The Sleuth Kit Overview and Automated Scanning Features](https://www.basistech.com/about/events/)
  (Brian Carrier)
- [Faster Response with Sleuth Kit and Other Open Source Technologies](https://www.basistech.com/about/events/)
  (Jamie Butler and Jason Shiffer)
- [PTK Forensics after Two years: Past, Present and Future](https://www.basistech.com/about/events/)
  (Dario Forte)
- [Mac Forensic Tools Using Sleuth Kit](https://www.basistech.com/about/events/)
  (Rob Joyce)
- [Commando Forensics: What Dongle?](https://www.basistech.com/about/events/)
  (Cory Altheide)
- [AFF and AFF4: Where we are, where we are going, and why it matters to you.](https://www.basistech.com/about/events/)
  (Simson Garfinkel)
- [Timeline Creation using Open-Source Tools](https://www.basistech.com/about/events/)
  (Harlan Carvey)

<small>MARCH-2010</small>

[Internet geolocation: Evasion and counterevasion](https://dl.acm.org/doi/10.1145/1592451.1592455)
ACM Computing Surveys (CSUR), Volume 42 , Issue 1 (December 2009)

> Internet geolocation technology aims to determine the physical
> (geographic) location of Internet users and devices. It is currently
> proposed or in use for a wide variety of purposes, including targeted
> marketing, restricting digital content sales to authorized
> jurisdictions, and security applications such as reducing credit card
> fraud. This raises questions about the veracity of claims of accurate
> and reliable geolocation. We provide a survey of Internet geolocation
> technologies with an emphasis on adversarial contexts; that is, we
> consider how this technology performs against a knowledgeable
> adversary whose goal is to evade geolocation. We do so by examining
> first the limitations of existing techniques, and then, from this
> base, determining how best to evade existing geolocation techniques.
> We also consider two further geolocation techniques which may be of
> use even against adversarial targets: (1) the extraction of client IP
> addresses using functionality introduced in the 1.5 Java API, and (2)
> the collection of round-trip times using HTTP refreshes. These
> techniques illustrate that the seemingly straightforward technique of
> evading geolocation by relaying traffic through a proxy server (or
> network of proxy servers) is not as straightforward as many end-users
> might expect. We give a demonstration of this for users of the popular
> Tor anonymizing network.

<small>FEB-2010</small> [The 'CSI Effect': Does It Really
Exist?](https://nij.ojp.gov/topics/articles/csi-effect-does-it-really-exist), by
The Honorable Donald E. Shelton

Crime and courtroom proceedings have long been fodder for film and
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
1-hour episode that suggested the crime remained a "mystery" . . .
notwithstanding the jury's guilty verdict....

<small>JAN-2010</small> [Using Graphics Processors for Parallelizing
Hash-based Data
Carving](https://hal.science/file/index/docid/350962/filename/ColDanDauDef09.pdf),
by Sylvain Collange, Marc Daumas, Yoginder S. Dandass, and David Defour,
Proceedings of the 42nd Hawaii International Conference on System
Sciences - 2009.

Abstract

The ability to detect fragments of deleted image files and to
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

<small>December-2009</small>

**[What happens when you overwrite data?](https://www.sans.org/blog/what-happens-when-you-overwrite-data/)**.

Data recovery Craig S. Wright explores what happens when you try to
cover overwritten data using high-quality scientific equipment. His
conclusion: "The values do not tell you what existed on the drive prior
to the wipe; they just allow you to make a guess, bit by bit. Each time
you guess, you compound the error. As recovering a single bit value has
little if any forensic value, you soon find that the cumulative errors
render any recovered data worthless."

<small>November-2009</small>

**[Linux for computer forensic investigators: «pitfalls» of mounting file systems](http://www.computer-forensics-lab.org/pdf/Linux_for_computer_forensic_investigators.pdf) [(Russian version)](http://computer-forensics-lab.org/lib/?cid=174), Suhanov Maxim, 2009**

The paper opens discussion about building forensically sound Live CD
distributions based on Linux. Problems described:

- Common misconceptions about "-o ro" mount option (is it forensically
  sound?);
- Bugs in many forensic Live CDs that alter the data on evidentiary
  media.

Denis Frati ([caine](caine_live_cd.md) wrote an
[excellent review
(Italian)](http://www.denisfrati.it/pdf/Suhanov_Maxim_bug.pdf) of the
bug found in Casper scripts.

<small>September-2009</small>

**[Cisco IOS Forensics](https://www.blackhat.com/presentations/bh-dc-08/FX/Whitepaper/bh-dc-08-fx-WP.pdf)**

"Cisco System’s routers running Cisco IOS are still the prevalent
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
requesting feedback from the community on the software’s future
directions."

<small>July-2009</small>

**Android Forensics**
Presentation on Android Forensics by Andrew Hoog, Mobile Forensics World 2009.
Presentation gives an overview of Android, explains how to root phones, and
extract data from a phone once you have superuser access. One of the
complications is that Android phones (like the T-Mobile G1) use YAFFS2, a
flash-specific file system.

<small>2009-June</small>

[Recovery of Damaged Compressed Files for Digital Forensic Purposes](https://ieeexplore.ieee.org/document/4505751/?tp=http://ieeexplore.ieee.org/xpl/freeabs_all.jsp?tp=&arnumber=4505751&isnumber=4505671arnumber=4505751http://ieeexplore.ieee.org/xpl/freeabs_all.jsp?tp=&arnumber=4505751&isnumber=4505671isnumber=4505671), Bora Park Savoldi, A. Gubian, P. Jungheum Park Seok Hee Lee Sangjin Lee

Korea Univ., Seoul, International Conference on Multimedia and
Ubiquitous Engineering, 2008. MUE 2008/

Abstract:


Nowadays compressed files are very widespread and can be considered,
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

<small>2009-May</small>

Overcoming Impediments to Cell Phone Forensics, by Wayne Jansen, Aurelien
Delaitre, and Ludovic Moenner, Proceedings of the 41st Hawaii International
Conference on System Sciences - 2008

Cell phones are an emerging but rapidly growing area of computer
forensics. While cell phones are becoming more like desktop computers
functionally, their organization and operation are quite different in
certain areas. For example, most cell phones do not contain a hard drive
and rely instead on flash memory for persistent storage. Cell phones are
also designed more as special purpose appliances that perform a set of
predefined tasks using proprietary embedded software, rather than
general-purpose extensible systems that run common operating system
software. Such differences make the application of classical computer
forensic techniques difficult. Also complicating the situation is the
state of the art of present day cell phone forensic tools themselves and
the way in which tools are applied. This paper identifies factors that
impede cell phone forensics and describes techniques to address two
resulting problems in particular: the limited coverage of available
phone models by forensic tools, and the inadequate means for validating
the correct functioning of forensic tools

<small>2009-Apr</small>

[A Framework for Automated Digital Forensic Reporting](https://simson.net/clips/students/09_Farrell.pdf), Lt. Paul Farrell, Master's Thesis, Naval Postgraduate School, Monterey, CA, March 2009
Forensic analysis is the science of finding, examining and analyzing
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

<small>2009-Feb-08</small>

[The impact of full disk encryption on digital forensics](https://dl.acm.org/doi/10.1145/1368506.1368519), ACM SIGOPS Operating Systems Review archive, Volume 42 , Issue 3 (April 2008) , Pages 93-98
The integration of strong encryption into operating systems is creating
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

<small>2009-JAN-01</small>

[Forensic Investigation of the Nintendo Wii: A First Glance](http://www.ssddfj.org/papers/SSDDFJ_V2_1_Turnbull.pdf), Dr. Benjamin Turnbull, SMALL SCALE DIGITAL DEVICE FORENSICS JOURNAL, VOL. 2, NO. 1, JUNE 2008 ISSN# 1941-6164
The closed nature of the Wii makes it a challenging game console for
forensic analysis. This article takes a first look at the platform,
discussing the various places where forensically interesting information
may be hidden. There's also a reference to an interesting article about
how the ability of wimotes to move avatars from one system to another
documents a woman's affair while her husband was serving in Iraq.

<small>2008-Nov-18</small>

[Data Acquisition from Cell Phone using Logical Approach](http://www.waset.org/pwaset/v26/v26-6.pdf), Keonwoo Kim, Dowon Hong, Kyoil Chung, and Jae-Cheol Ryou, PROCEEDINGS OF WORLD ACADEMY OF SCIENCE, ENGINEERING AND TECHNOLOGY VOLUME 26 DECEMBER 2007 ISSN 1307-6884
This article discusses three approaches for acquiring data from cell phones:
physically removing the flash RAM chips and reading them directly; reading the
data out using the JTAG interface, and running software on the cell phone to
extract the files at a logical level. The authors have built a logical
extraction system and are working on a system based on JTAG.

<small>2008-Oct-30</small>

Semi-Supervised Named Entity Recognition: Learning to Recognize 100 Entity Types with Little Supervision, David Nadeau, PhD Thesis, University of Ottawa, 2007.
Named Entity Recognition is the process of analyzing text documents and
automatically identifying the Who, What, Where and Whens. David Nadeau's
thesis presents a novel approach which bootstraps a named entity
recognizer using semi-structured documents on the web. Few forensic
tools use NER today, but that may well change in the future. What makes
this thesis so interesting to read is that it also has a history of the
last 20 years or so of the field. Highly recommended.

<small>2008-Oct-24</small>

[Advanced JPEG carving](https://dl.acm.org/doi/10.5555/1363217.1363239), Michael I. Cohen, Proceedings of the 1st international conference on Forensic applications and techniques in telecommunications, information, and multimedia and workshop
Michael I. Cohen presents a fully automated carver which can carve
fragmented JPEGs using typical fragmentation patterns. (Cohen argues the
the DFRWS carving challenges do not represent typical fragmentation
patterns.)

<small>2008-Oct-18</small>

[Threats to Privacy in the Forensic Analysis of Database Systems](http://www.cs.umass.edu/~miklau/pubs/sigmod2007LMS/stahlberg07forensicDB.pdf)
Patrick Stahlberg, Gerome Miklau, and Brian Neil Levine

Proceedings of the 2007 ACM SIGMOD international conference on
Management of data table of contents

Beijing, China.

This paper looks at residual data left behind in databases after DELETE,
UPDATE, and VACUUM operations. The authors show that residual data is a
real issue in databases, and that it's pretty easy to modify a database
so that no residual data is left behind. MySQL with MyISM tables has
clean delete, but InnoDB does not. Very much worth reading.

<small>2008-Aug-13</small>

[Lest We Remember: Cold Boot Attacks on Encryption Keys](https://www.usenix.org/legacy/events/sec08/tech/halderman.html)
J. Alex Halderman, Princeton University; Seth D. Schoen, Electronic
Frontier Foundation; Nadia Heninger and William Clarkson, Princeton
University; William Paul, Wind River Systems; Joseph A. Calandrino and
Ariel J. Feldman, Princeton University; Jacob Appelbaum; Edward W.
Felten, Princeton University

[USENIX Security '08 Refereed
Paper](https://www.usenix.org/legacy/events/sec08/)

Awarded Best Student Paper

<!-- -->


Increasingly memory analysis is of interest in forensic research---both
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

<small>2008-July-27</small>

The [Symposium on Usable Privacy and Security (2008)](http://cups.cs.cmu.edu/soups/2008) concluded this past week in Pittsburgh, PA. One paper that appeared which is interesting to the network forensics crowd is [The Challenges of Using an Intrusion Detection System: Is It Worth the Effort?](http://cups.cs.cmu.edu/soups/2008/proceedings/p107Werlinger.pdf), by Rodrigo Werlinger, Kirstie Hawkey, Kasia Muldner, Pooya Jaferian and Konstantin Beznosov. [slides](http://cups.cs.cmu.edu/soups/2008/slides/hawkey_soups.ppt)

<!-- -->


In this article, the authors conducted interviews with 9 IT security
practitioners who have worked with IDSs performed ethnographic
observations within an organization that was deploying a new IDS. They
found that security practitioners were heavily divided on the value of
the IDS, and learned that the an IDS really only generates value if the
network is well-understood before the IDS is deployed.

<small>2008-July-20</small>

The [International Journal of Digital Evidence](https://ecci.utica.edu/ijde/) is one of two publications by the [Electronic Crime Institute (ECI)](https://ecci.utica.edu/) at Utica College. Current and previous issues are available online.

<!-- -->


The current Fall 2007 issue has an interesting article [Mobile Phone
Forensics Tool Testing: A Database Drive
Approach](https://ecci.utica.edu/publications/articles/1C33DF76-D8D3-EFF5-47AE3681FD948D68.pdf)
by Baggili, Mislan, and Rogers at Purdue University. Given that phones
are increasingly a primary source of forensic information in many cases,
we need to be sure that the tools that are used for forensic analysis
present data that is accurate and repeatable. Unfortunately they
frequently aren't because of there are so many different kinds of phones
on the market and the forensic tools lag far behind the market.

<bibtex> @article{title="Mobile Phone Forensics Tool Testing: A Database
Driven Approach", author="Ibrahim M. Baggili and Richard Mislan and
Marcus Rogers", journal="International Journal of Digital Evidence",
year=2007, volume=6, issue=2,
url="<https://ecci.utica.edu/publications/articles/1C33DF76-D8D3-EFF5-47AE3681FD948D68.pdf>",
abstract="The Daubert process used in the admissibility of evidence
contains major guidelines applied in assessing forensic procedures, two
of which are testing and error rates. The Digital Forensic Science (DFS)
community is growing and the error rates for the forensic tools need to
be continuously re-evaluated as the technology changes. This becomes
more difficult in the case of mobile phone forensics, because they are
proprietary. This paper discusses a database driven approach that could
be used to store data about the mobile phone evidence acquisition
testing process. This data can then be used to calculate tool error
rates, which can be published and used to validate or invalidate the
mobile phone acquisition tools. " } </bibtex>

<small>2008-July-12</small>

<bibtex> @article{

` misc="",`
` publisher="DFRWS 2008",`
` author="Anandabrata Pal and Taha Sencar and Nasir Memon",`
` title="Detecting File Fragmentation Point Using Sequential Hypothesis Testing",`
` year=2008,`
` abstract="Abstract—File carving is a technique whereby data ﬁles are `

extracted from a digital device without the assistance of ﬁle tables or
other disk meta-data. One of the primary challenges in ﬁle carving can
be found in attempting to recover ﬁles that are fragmented. In this
paper, we show how detecting the point of fragmentation of a ﬁle can
beneﬁt fragmented ﬁle recovery. We then present a sequential hypothesis
testing procedure to identify the fragmentation point of a ﬁle by
sequentially comparing adjacent pairs of blocks from the starting block
of a ﬁle until the fragmentation point is reached. By utilizing serial
analysis we are able to to minimize the errors in detecting the
fragmentation points. The performance results obtained from the
fragmented test-sets of DFRWS 2006 and 2007 show that the method can be
effectively used in recovery of fragmented ﬁles. clear that recovery of
fragmented ﬁles is a critical problem in forensics. ",

} </bibtex>

This DFRWS 2008 article presents an improved approach for carving
fragmented JPEGs using sequential hypothesis testing. According to the
authors, "The technique begins with a header block identifying the start
of a ﬁle and then attempts to validate via SHT each subsequent block
following the header block. The fragmentation point is identiﬁed when
SHT identiﬁes a block as not belonging to the ﬁle. By utilizing this
technique, we are able to correctly and efﬁciently recover JPEG images
from the DFRWS 2006 \[1\] and 2007 \[2\] test sets even in the presence
of tens of thousands of blocks and ﬁles fragmented into 3 or more parts.
The bifragment gap carving technique enhanced with SHT allows us to
improve the performance result of DFRWS 2006 challenge test-sets,
although the technique cannot be used for DFRWS 2007. We then show how
Parallel Unique Path enhanced with SHT is able to recover all fragmented
JPEGs from DFRWS 2006 and all recoverable JPEGs from 2007 challenge
test-sets. As far as we are aware, no other automated technique can
recover multi-fragmented JPEGs from the DFRWS 2007 test set."

<small>2008-July-5</small>

<bibtex> @article{

` publisher="Taylor & Francis",`
` journal="Journal of Digital Forensic Practice",  `
` author="Yoginder Singh Dandass and Nathan Joseph Necaise and Sherry Reede Thomas",`
` title="An Empirical Analysis of Disk Sector Hashes for Data Carving",`
` year=2008,`
` volume=2,`
` issue=2,`
` pages="95--106",`
` abstract="Discovering known illicit material on digital storage devices is an important component of a digital forensic investigation. Using existing data carving techniques and tools, it is typically difficult to recover remaining fragments of deleted illicit files whose file system metadata and file headers have been overwritten by newer files. In such cases, a sector-based scan can be used to locate those sectors whose content matches those of sectors from known illicit files. However, brute-force sector-by-sector comparison is prohibitive in terms of time required. Techniques that compute and compare hash-based signatures of sectors in order to filter out those sectors that do not produce the same signatures as sectors from known illicit files are required for accelerating the process.`

This article reports the results of a case study in which the hashes for
over 528 million sectors extracted from over 433,000 files of different
types were analyzed. The hashes were computed using SHA1, MD5, CRC64,
and CRC32 algorithms and hash collisions of sectors from JPEG and WAV
files to other sectors were recorded. The analysis of the results shows
that although MD5 and SHA1 produce no false-positive indications, the
occurrence of false positives is relatively low for CRC32 and especially
CRC64. Furthermore, the CRC-based algorithms produce considerably
smaller hashes than SHA1 and MD5, thereby requiring smaller storage
capacities. CRC64 provides a good compromise between number of
collisions and storage capacity required for practical implementations
of sector-scanning forensic tools.",

` url="`[`https://taylorandfrancis.com`](https://taylorandfrancis.com)`"`

} </bibtex>

Authors Dandass *et. al* analyzed 528 million sectors from 433,630
unique files. They computed the CRC32, CRC64, MD5 and SHA-1 of each
sector. Not surprisingly, they find that the MD5 and SHA-1s of the
sectors are different if the sectors are different. They find 94 CRC64
collisions and 30 million CRC32 collisions. The conclusion is that, if
you are search for a single sector or building a database of single
sector hashes, you are better off building a database of CRC64s because
they are easier to store and dramatically faster to calculate than the
traditional hash functions, and they are nearly as accurate.
