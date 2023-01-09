---
tags:
  - No Category
---
*Approximate matching* is a term used in computer forensics to mean that
two objects have similar contents but are not identically the same. It
replaced the previously used terms *similarity* and *fuzzy hashing.*

The following two paragraphs are clearly similar but not identical:


**We the People** of the United States, in Order to form a more perfect
Union, establish Justice, insure domestic Tranquility, provide for the
common defence, promote the general Welfare, and secure the Blessings of
Liberty to ourselves and our Posterity, do ordain and establish this
Constitution for the United States of America.

<!-- -->


**We the People** of the United States, in Order to form a more perfect
Union, establish Justice, insure domestic Tranquility, provide for the
common defense, promote the general Welfare, and secure the Blessings of
Liberty to ourselves and our Posterity, do ordain and establish this
Constitution for the United States of America.

## Kinds of Similarity

In forensics there are several kinds of similarity that are of interest:

1.  Binary Similarity
2.  Textual Similarity
3.  Visual Similarity
4.  Audible Similarity
5.  Algorithmic (code) Similarity

### Binary Similarity

Binary Similarity between a *master object* and a *target object*can be
rigorously defined as the fraction of substrings that the two documents
have in common divided by the total number of substrings in the master
document. Notice that this implies that the similarity function does not
have the commutative property. That is, BS(a,b) may not equal BS(b,a).

There are several applications for a binary similarity function:

1.  Determining that a master object is embedded in the target object.
2.  Determining if the target object is derived from the target object.

The leading similarity systems in use are are:

- sdhash, developed by Vassil Roussev.
- ssdeep, the first widely used binary similarity
  algorithm. Developed by Jesse Kornblum, this system uses a piecewise
  hash comparison algorithm originally developed for anti-spam systems.

### Text Similarity

The leading text similarity system is:

- sdtext, developed by Clay Sheilds.

## Similarity Bibliography

SSDEEP:

Jesse Kornblum, “Identifying almost identical files using context
triggered piecewise hashing,” Jesse Kornblum, DFRWS 2006, Digital
Investigation 3S, S91-S97

Jiang, Z.L., Hui, L.C.K., Chow, K.P., Yiu, S.M., Lai, P.K.Y. Improving
disk sector integrity using 3-dimension hashing scheme, Proceedings of
Future Generation Communication and Networking, FGCN 2007 2, art. no.
4426219, pp. 141-145, 2007

Rönnau, S., Pauli, C., Borghoff, U.M. Merging changes in XML documents
using reliable context fingerprints (2008) DocEng'08 - Proceedings of
the 8th ACM Symposium on Document Engineering, pp. 52-61.

Chen, L., Wang, G. Attacks to context triggered piecewise hashing and
their countermeasures (2008) Journal of Information and Computational
Science, 5 (2), pp. 589-597.

Hejazi, S.M., Debbabi, M., Talhi, C. Automated windows memory file
extraction for cyber forensics investigation (2008) Journal of Digital
Forensic Practice, 2 (3), pp. 117-131.

Long Chen; Wang, Guoyin, "An Efficient Piecewise Hashing Method for
Computer Forensics," Knowledge Discovery and Data Mining, 2008. WKDD
2008. First International Workshop on, vol., no., pp.635,638, 23-24
Jan. 2008

Kimin Seo; KyungSoo Lim; Choi, Jaemin; Kisik Chang; Sangjin Lee,
"Detecting Similar Files Based on Hash and Statistical Analysis for
Digital Forensic Investigation," Computer Science and its Applications,
2009. CSA '09. 2nd International Conference on, vol., no., pp.1,6,
10-12 Dec. 2009

Apel, M., Bockermann, C., Meier, M. Measuring similarity of malware
behavior (2009) Proceedings - Conference on Local Computer Networks,
LCN, art. no. 5355037, pp. 891-898.

Chawathe, S.S. Effective whitelisting for filesystem forensics (2009)
2009 IEEE International Conference on Intelligence and Security
Informatics, ISI 2009, art. no. 5137284, pp. 131-136.

Simon, M., Slay, J. Enhancement of forensic computing investigations
through memory forensic techniques (2009) Proceedings - International
Conference on Availability, Reliability and Security, ARES 2009, art.
no. 5066600, pp. 995-1000.

Chen, L., Wang, G.-Y. Integrity check method for fine-grained data
(2009) Ruan Jian Xue Bao/Journal of Software, 20 (4), pp. 902-909. Cited
10 times.

Maartmann-Moe, C., Thorkildsen, S.E., André Årnes The persistence of
memory: Forensic identification and extraction of cryptographic keys
(2009) Digital Investigation, 6 (SUPPL.), pp. S132-S140.

Seo, K., Lim, K., Choi, J., Chang, K., Lee, S. Detecting similar files
based on hash and statistical analysis for digital forensic
investigation (2009) Proceedings of the 2009 2nd International
Conference on Computer Science and Its Applications, CSA 2009, art. no.
5404198.

Garcia, J., Holleboom, T. Retention of micro-fragments in cluster
slack - A first model (2009) Proceedings of the 2009 1st IEEE
International Workshop on Information Forensics and Security, WIFS 2009,
art. no. 5386487, pp. 31-35.

Vassil Roussev, Hashing and data fingerprinting in digital forensics,
IEEE Security and Privacy 7(2), 2009, pp. 49-55

C. Nickel, C. Busch, X. Zhou, Template protection via piecewise hashing,
IIH-MSP 2009 - 2009 5th International Conference on Intelligent
Information Hiding and Multimedia Signal Processing, art. no. 5337554,
pp. 1056-1060

Roussev, V. Data fingerprinting with similarity digests (2010) IFIP
Advances in Information and Communication Technology, 337 AICT, pp.
207-226.

Holleboom, T., Garcia, J. Fragment retention characteristics in slack
space - Analysis and measurements (2010) 2010 2nd International Workshop
on Security and Communication Networks, IWSCN 2010, art. no. 5497996, .

Wu, Y., Yang, K., Zhang, J. Using DBSCAN clustering algorithm in spam
identifying (2010) ICETC 2010 - 2010 2nd International Conference on
Education Technology and Computer, 1, art. no. 5529221, pp. V1398-V1402.

Fang, J., Jiang, Z.L., Yiu, S.M., Hui, L.C.K. An efficient scheme for
hard disk integrity check in digital forensics by hashing with
combinatorial group testing (2011) International Journal of Digital
Content Technology and its Applications, 5 (2), pp. 300-308.

Jiang, Z.L., Fang, J.-B., Hui, L.C.K., Yiu, S., Chow, K.P., Sheng, M.-M.
K-Dimensional hashing scheme for hard disk integrity verification in
computer forensics (2011) Journal of Zhejiang University: Science C, 12
(10), pp. 809-818.

Harald Baier, Frank Breitinger: Security Aspects of Piecewise Hashing in
Computer Forensics, 6th International Conference on IT Security Incident
Management & IT Forensics (IMF), Stuttgart (Germany). May 2011.

Frank Breitinger, Harald Baier: Performance Issues about Context
Triggered Piecewise Hashing, 3rd International ICST Conference on
Digital Forensics & Cyber Crime (ICDF2C), Dublin (Ireland). October
2011.

Wardman, B., Stallings, T., Warner, G., Skjellum, A. High-performance
content-based phishing attack detection (2011) eCrime Researchers
Summit, eCrime, art. no. 6151977, .

Gennari, J., French, D. Defining malware families based on analyst
insights (2011) 2011 IEEE International Conference on Technologies for
Homeland Security, HST 2011, art. no. 6107902, pp. 396-401.

Grispos, G., Storer, T., Glisson, W.B. A comparison of forensic evidence
recovery techniques for a windows mobile smart phone (2011) Digital
Investigation, 8 (1), pp. 23-36.

Carlos G. Figuerola, Raquel Gómez Díaz, José L. Alonso Berrocal, Angel
F. Zazo Rodríguez, Web Document Duplicate Detection Using Fuzzy Hashing,
in Trends in Practical Applications of Agents and Multiagent Systems,
Advances in Intelligent and Soft Computing, Volume 90, 2011, pp.
117-125, Springer

Jozwiak, I., Kedziora, M. Efficient N-Byte slack space hashing in
retrieving and identifying partially recovered data (2011) ICSOFT 2011 -
Proceedings of the 6th International Conference on Software and Database
Technologies, 1, pp. 309-312.

Song, X., Deng, H., Xiong, Z. Using piecewise hashing and Lagrange
interpolation polynomial to preserve electronic evidence (2011)
Communications in Computer and Information Science, 201 CCIS (PART 1),
pp. 472-480.

Frank Breitinger, Harald Baier: A Fuzzy Hashing Approach based on Random
Sequences and Hamming Distance, 7th annual Conference on Digital
Forensics, Security and Law (ADFSL), Richmond (Virginia, US). May 2012.

Frank Breitinger and Harald Baier, “Performance Issues About
Context-Triggered Piecewise Hashing,” in P. Gladyshev and M. K. Rogers
(Eds): ICDF2C 2011, LNICST 88, 2012, pp. 141-155, 2012.

Thonnard, O., Bilge, L., O'Gorman, G., Kiernan, S., Lee, M. Industrial
espionage and targeted attacks: Understanding the characteristics of an
escalating threat (2012) Lecture Notes in Computer Science (including
subseries Lecture Notes in Artificial Intelligence and Lecture Notes in
Bioinformatics), 7462 LNCS, pp. 64-85.

Garcia, J. Quantifying the benefits of file size information for
forensic hash matching (2012) SECRYPT 2012 - Proceedings of the
International Conference on Security and Cryptography, pp. 333-338.

Frank Breitinger, Knut Petter Åstebøl, Harald Baier, Christoph Busch:
mvHash-B – A new Approach for Similarity Preserving Hash Function. 7th
International Conference on IT Security Incident Management & IT
Forensics (IMF), Nürnberg (Germany). March 2013.

Christian Rathgeb, Frank Breitinger, Christoph Busch: Alignment-Free
Cancelable Iris Biometric Templates based on Adaptive Bloom Filters, In
Proceedings of the 6th IAPR International Conference on Biometrics
(ICB’13), Madrid (Spain). June 2013. To appear.

Frank Breitinger, Georgios Stivaktakis, Harald Baier: FRASH: A framework
to test algorithms of similarity hashing, In Proceedings of the 13th
Digital Forensics Research Conference (DFRWS’13), Monterey (Californien,
US). August 2013. To appear.

Books that mention SSDEEP: Harlan Carvey, Windows Forensic Analysis,
Syngress, June 2009,

Cameron H. Malin, Eoghan Casey, James M. Aquilina, Malware Forensics:
Investigating and Analyzing Malicious Code, Syngress, Aug 2008

Cameron H. Malin, Eoghan Casey, James M. Aquilina, Malware Forensics
Field Guide for Windows Systems, Elsevier, May 2012,

Frank Breitinger, Kaloyan Petrov: Reducing time cost in hashing
operations. Ninth Annual IFIP WG 11.9 International Conference on
Digital Forensics (IFIP WG11.9), Orlando (Florida, US). January 2013.

SDHASH:

Roussev, V. Building open and scalable digital forensic tools (2011)
2011 6th IEEE International Workshop on Systematic Approaches to Digital
Forensic Engineering, SADFE 2011, art. no. 6159116, .

Vassil Roussev, “An evaluation of forensic similarity hashes,” Digital
Investigation 8 (2011), S34-S41

Breitinger, F.; Baier, H., "Properties of a similarity preserving hash
function and their realization in sdhash," Information Security for
South Africa (ISSA), 2012, vol., no., pp.1,8, 15-17 Aug. 2012

Frank Breitinger, Harald Baier, Jesse Beckingham: Security and
Implementation Analysis of the Similarity Digest sdhash, 1st
International Baltic Conference on Network Security & Forensics
(NeSeFo), Tartu (Estland). August 2012.

Frank Breitinger, Harald Baier: Properties of a Similarity Preserving
Hash Function and their Realization in sdhash. 2012 Information Security
South Africa (ISSA 2012), Johannesburg (South Africa). August 2012.

Vassil Roussev, “Managing terabyte-scale investigations with similarity
digests,” IFIP Advances in Informaiton and Communication Technology 383,
AICT, pp. 19-34

Clay Shields, O. Frieder, M. Maloof, “A system for the proactive,
continuous, and efficient collection of digital forensic evidence,”
DFRWS 2011 Annual Conference, pp. S3-S13

MRSH-v2

Frank Breitinger, Harald Baier: Similarity Preserving Hashing: Eligible
Properties and a new Algorithm MRSH-v2. 4th International ICST
Conference on Digital Forensics & Cyber Crime (ICDF2C), Lafayette
(Indiana, US). October 2012.
