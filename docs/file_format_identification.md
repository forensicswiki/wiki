---
tags:
  -  Tools
---
File Format Identification is the process of figuring out the format of
a sequence of bytes. Operating systems typically do this by file
extension or by embedded MIME information. Forensic applications need to
identify file types by content.

# Tools

## libmagic

- Written in C.
- Rules in /usr/share/file/magic and compiled at runtime.
- Powers the Unix “file” command, but you can also call the library
  directly from a C program.
- <http://sourceforge.net/projects/libmagic>

## Digital Preservation Efforts

PRONOM is a project of the National Archives of the United Kingdom to
develop a registry of file types. A similar project was started by JSTOR
and Harvard as the JSTOR/Harvard Object Validation Environment. Attempts
are now underway to merge these two efforts in the Global Digital Format
Registry and the Universal Digital Format Registry.

The UK National Archives developed the Digital Record Object
Identification (DROID) tool, an "automatic file format identification
tool." This tool is written in Java and can be downloaded from
SourgeForge.

See:

- [PRONOM](http://www.nationalarchives.gov.uk/PRONOM/Default.aspx)
- [JHOVE](http://hul.harvard.edu/jhove/)
- [JHOVE2](https://wiki.ucop.edu/display/JHOVE2Info/Home)
- [GDFR](http://www.gdfr.info/)
- [UDFR](http://www.udfr.org/)
- [DROID download](http://droid.sourceforge.net)

## TrID - File Identifier

- Recognize over 9.000 file formats
- XML formats definitions, compiled to a single container
- New filetypes can be added in an automated way, simply scanning a
  group of files
- Win32, Linux/x86 & x86-64; closed source; free for non-commercial use
- <http://mark0.net/soft-trid-e.html>

## Forensic Innovations File Investigator TOOLS

- Proprietary, but free trial available.
- Available as consumer applications and OEM API.
- Identifies 3,000+ file types, using multiple methods to maintain high
  accuracy.
- Extracts metadata for many of the supported file types.
- <http://www.forensicinnovations.com/fitools.html>

## Stellent/Oracle Outside-In

- Proprietary but free demo.
- <http://www.oracle.com/technology/products/content-management/oit/oit_all.html>

## [Forensic Assistant](forensic_assistant.md)

- Proprietary.
- Provides detection of password protected archives, some files of
  cryptographic programs, Pinch/Zeus binary reports, etc.
- <http://nhtcu.ru/0xFA_eng.html>

## Toolsley File Identifier

- Free
- Runs in the browser
- HTML5/JS port of the UNIX "file" tool and libmagic
- <http://www.toolsley.com/file.html>

## Falstaff

- Free
- Online
- Based on machine learning techniques, uses multiple file features
- Uses novel signatures computed from file format samples
- Identifications are linked to <http://fileformats.archiveteam.org>
  ontology
- <http://ec2-52-37-126-112.us-west-2.compute.amazonaws.com/falstaff>

## Apache Tika

- Free (Apache v2.0 License)
- The Apache Tika™ toolkit detects and extracts metadata and text from
  over a thousand different file types
- <http://tika.apache.org/>



# Data Sets

If you are working in the field of file format identification, please
consider reporting the results of your algorithm with one of these
publicly available data sets:

- NPS govdocs1m - a corpus of 1 million files that can be redistributed
  without concern of copyright or PII. Download from
  <http://domex.nps.edu/corp/files/govdocs1/>
- The NPS Disk Corpus - a corpus of realistic disk images that contain
  no PII. Information is at: <http://digitalcorpora.org/?s=nps>

# Comparisons/Evaluations

- Comparison of Apache Tika, DROID and 'file' on 1TB, \~3 million files
  from govdocs1 and a sample of Common Crawl, April 2016.
  <http://162.242.228.174/mimes/mime_comparisons.html>

# Bibliography

Current research papers on the file format identification problem. Most
of these papers concern themselves with identifying file format of a few
file sectors, rather than an entire file. **Please note that this
bibliography is in chronological order!**

2001

- M. McDaniel, [Automatic File Type Detection
  Algorithm](media:mcdaniel01.pdf.md), Masters Thesis, James
  Madison University,2001

2003

- [Content Based File Type Detection
  Algorithms](http://www2.computer.org/portal/web/csdl/abs/proceedings/hicss/2003/1874/09/187490332a.pdf), M.
  McDaniel and M.H. Heydari, 36th Annual Hawaii International Conference
  on System Sciences (HICSS'03) - Track 9, 2003.

2005

- Fileprints: identifying file types by n-gram analysis, LiWei-Jen, Wang
  Ke, Stolfo SJ, Herzog B.., Proceeding of the 2005 IEEE workshop on
  information assurance, 2005. ([Presentation
  Slides](http://www.itoc.usma.edu/workshop/2005/Papers/Follow%20ups/FilePrintPresentation-final.pdf))
  ([PDF](http://www1.cs.columbia.edu/ids/publications/FilePrintPaper-revised.pdf))

<!-- -->

- D.J. Hickok, D.R.Lesniak, M.C. Rowe, File Type Detection Technology,
  2005 Midwest Instruction and Computing
  Symposium.([PDF](http://www.micsymposium.org/mics_2005/papers/paper7.pdf))

2006

- K. Martin, N. Shahmehri [File type identification of data fragments by
  their binary
  structure.](http://ieeexplore.ieee.org/iel5/10992/34632/01652088.pdf),
  Proceedings of the IEEE workshop on information assurance, pp.140–147,
  2006.([Presentation
  Slides](http://www.itoc.usma.edu/workshop/2006/Program/Presentations/IAW2006-07-3.pdf))

<!-- -->

- G.A. Hall, Sliding Window Measurement for File Type Identification,
  Computer Forensics and Intrusion Analysis Group, ManTech Security and
  Mission Assurance, 2006.
  ([PDF](http://www.mantechcfia.com/SlidingWindowMeasurementforFileTypeIdentification.pdf))

<!-- -->

- FORSIGS; Forensic Signature Analysis of the Hard Drive for Multimedia
  File Fingerprints, J. Haggerty and M. Taylor, IFIP TC11 International
  Information Security Conference, 2006, Sandton, South Africa.

<!-- -->

- M.Karresand , N. Shahmehri, "Oscar -- Using Byte Pairs to Find File
  Type and Camera Make of Data Fragments," Annual Workshop on Digital
  Forensics and Incident Analysis, Pontypridd, Wales, UK, pp.85-94,
  Springer-Verlag, 2006.

2007

- M. Karresand, N. Shahmehri, [Oscar: File Type Identification of Binary
  Data in Disk Clusters and RAM
  Pages](http://dx.doi.org/10.1007/0-387-33406-8_35), Proceedings of
  IFIP International Information Security Conference: Security and
  Privacy in Dynamic Environments (SEC2006), Springer, ISBN
  0-387-33405-x, pp.413-424, Karlstad, Sweden, May 2006.

<!-- -->

- R.F. Erbacher and J. Mulholland, "Identification and Localization of
  Data Types within Large-Scale File Systems," Proceedings of the 2nd
  International Workshop on Systematic Approaches to Digital Forensic
  Engineering, Seattle, WA, April 2007.

<!-- -->

- R.M. Harris, "Using Artificial Neural Networks for Forensic File Type
  Identification," Master's Thesis, Purdue University, May 2007.
  ([PDF](https://www.cerias.purdue.edu/tools_and_resources/bibtex_archive/archive/2007-19.pdf))

<!-- -->

- S.J. Moody and R.F. Erbacher, [SÁDI – Statistical Analysis for Data
  type
  Identification](http://ieeexplore.ieee.org/stamp/stamp.jsp?arnumber=04545366),
  3rd International Workshop on Systematic Approaches to Digital
  Forensic Engineering, 2008.

2008

- M.C. Amirani, M. Toorani, and A. Beheshti, [A New Approach to
  Content-based File Type
  Detection](http://ieeexplore.ieee.org/xpls/abs_all.jsp?arnumber=4625611),
  Proceedings of the 13th IEEE Symposium on Computers and Communications
  (ISCC'08), pp.1103-1108, July 2008.
  ([PDF](http://arxiv.org/ftp/arxiv/papers/1002/1002.3174.pdf))

2009

- V. Roussev, and S. Garfinkel, "File Classification Fragment-The Case
  for Specialized Approaches," Systematic Approaches to Digital
  Forensics Engineering (IEEE/SADFE 2009), Oakland, California.
  ([PDF](http://simson.net/clips/academic/2009.SADFE.Fragments.pdf))

<!-- -->

- I. Ahmed, K.-S. Lhee, H. Shin and M. Hong, [On Improving the Accuracy
  and Performance of Content-based File Type
  Identification](http://www.springerlink.com/content/g2655k2044615q75/),
  Proceedings of the 14th Australasian Conference on Information
  Security and Privacy (ACISP 2009), pp.44-59, LNCS (Springer),
  Brisbane, Australia, July 2009.

2010

- I. Ahmed, K.-s. Lhee, H. Shin and M. Hong, [Fast File-type
  Identification](http://www.alphaminers.net/sub05/sub05_03.php?swf_pn=5&swf_sn=3&swf_pn2=3),
  Proceedings of the 25th ACM Symposium on Applied Computing (ACM SAC
  2010), ACM, Sierre, Switzerland, March 2010.

<!-- -->

- I. Ahmed, K.-s. Lhee, H. Shin and M. Hong, [Content-based File-type
  Identification Using Cosine Similarity and a Divide-and-Conquer
  Approach](http://cs.uno.edu/~irfan/Publications/IETE-2010.pdf), IETE
  Technical Review, 27(6), 2010.

2011

- I. Ahmed, K.-S. Lhee, H.-J. Shin, M.-P. Hong, [Fast Content-Based File
  Type
  Identification](http://link.springer.com/chapter/10.1007/978-3-642-24212-0_5),
  Proceedings of the 7th Annual IFIP WG 11.9 International Conference on
  Digital Forensics, Orlando, FL, USA, February, 2011

<!-- -->

- C. Mattmann and J. Zitting, [Tika in
  Action](https://www.manning.com/books/tika-in-action), Manning
  Publications. December, 2011.

2013

- M.C. Amirani, M. Toorani, and S. Mihandoost, [Feature‐based Type
  Identification of File Fragments](http://dx.doi.org/10.1002/sec.553),
  Journal of Security and Communications Networks, Vol.6, No.1, pp.
  115–128, 2013.
  ([PDF](http://onlinelibrary.wiley.com/doi/10.1002/sec.553/pdf))

[Category:Tools](category:tools.md)
