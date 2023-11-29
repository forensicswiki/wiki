---
tags:
  - Tools
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
- <https://sourceforge.net/projects/libmagic>

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

- [PRONOM](https://www.nationalarchives.gov.uk/PRONOM/Default.aspx)
- [JHOVE](https://jhove.openpreservation.org/)
- [GDFR](https://www.gdfr.info/)
- [UDFR](https://cdlib.org/cdlinfo/2012/07/03/unified-digital-format-registry-udfr-now-available/)
- [DROID download](https://sourceforge.net/projects/droid/)

## TrID - File Identifier

- Recognize over 9.000 file formats
- XML formats definitions, compiled to a single container
- New filetypes can be added in an automated way, simply scanning a
  group of files
- Win32, Linux/x86 & x86-64; closed source; free for non-commercial use
- <https://mark0.net/soft-trid-e.html>

## Forensic Innovations File Investigator TOOLS

- Proprietary, but free trial available.
- Available as consumer applications and OEM API.
- Identifies 3,000+ file types, using multiple methods to maintain high
  accuracy.
- Extracts metadata for many of the supported file types.

## Stellent/Oracle Outside-In

- Proprietary but free demo.
- <https://www.oracle.com/content-management/webcenter-content/technologies/webcenter/outside-in-technology.html>

## Toolsley File Identifier

- Free
- Runs in the browser
- HTML5/JS port of the UNIX "file" tool and libmagic
- <https://www.toolsley.com/file.html>

## Falstaff

- Free
- Online
- Based on machine learning techniques, uses multiple file features
- Uses novel signatures computed from file format samples
- Identifications are linked to the [file formats archive](http://fileformats.archiveteam.org/wiki/Main_Page)
  ontology

## Apache Tika

- Free (Apache v2.0 License)
- The Apache Tika™ toolkit detects and extracts metadata and text from
  over a thousand different file types
- <https://tika.apache.org/>

# Data Sets

If you are working in the field of file format identification, please
consider reporting the results of your algorithm with one of these
publicly available data sets:

- NPS govdocs1m - a corpus of 1 million files that can be redistributed
  without concern of copyright or PII. Download from
  <https://digitalcorpora.org/corpora/files/>
- The NPS Disk Corpus - a corpus of realistic disk images that contain
  no PII. Information is at: <https://digitalcorpora.org/?s=nps>

# Bibliography

Current research papers on the file format identification problem. Most
of these papers concern themselves with identifying file format of a few
file sectors, rather than an entire file. **Please note that this
bibliography is in chronological order!**

2001

- Automatic File Type Detection Algorithm,
  by M. McDaniel, Masters Thesis, James Madison University, 2001

2003

- [Content Based File Type Detection Algorithms](https://ieeexplore.ieee.org/document/1174905),
  by M.  McDaniel and M.H. Heydari, 36th Annual Hawaii International Conference
  on System Sciences (HICSS'03) - Track 9, 2003.

2005

- Fileprints: identifying file types by n-gram analysis, LiWei-Jen, Wang
  Ke, Stolfo SJ, Herzog B.., Proceeding of the 2005 IEEE workshop on
  information assurance, 2005.
  ([PDF](https://academiccommons.columbia.edu/doi/10.7916/D86M3DJC))

<!-- -->

- D.J. Hickok, D.R.Lesniak, M.C. Rowe, File Type Detection Technology,
  2005 Midwest Instruction and Computing
  Symposium.([PDF](https://www.micsymposium.org/mics_2005/papers/paper7.pdf))

2006

- K. Martin, N. Shahmehri, File type identification of data fragments by their
  binary structure, Proceedings of the IEEE workshop on information assurance,
  pp.140–147, 2006. ([link](https://ieeexplore.ieee.org/document/1652088))

<!-- -->

- G.A. Hall, Sliding Window Measurement for File Type Identification,
  Computer Forensics and Intrusion Analysis Group, ManTech Security and
  Mission Assurance, 2006.

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
  Pages](https://link.springer.com/chapter/10.1007/0-387-33406-8_35), Proceedings of
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
  ([PDF](https://www.cerias.purdue.edu/assets/pdf/bibtex_archive/2007-19.pdf))

<!-- -->

- S.J. Moody and R.F. Erbacher, SÁDI – Statistical Analysis for Data type
  Identification, 3rd International Workshop on Systematic Approaches to Digital
  Forensic Engineering, 2008.

2008

- M.C. Amirani, M. Toorani, and A. Beheshti, [A New Approach to
  Content-based File Type
  Detection](https://ieeexplore.ieee.org/document/4625611/;jsessionid=e9ClJYNu5ZPnylpkSj7LoQM5s2LCfErdPPJo0lC0MGmzs9la-7Ld!1844383281),
  Proceedings of the 13th IEEE Symposium on Computers and Communications
  (ISCC'08), pp.1103-1108, July 2008.
  ([PDF](https://arxiv.org/ftp/arxiv/papers/1002/1002.3174.pdf))

2009

- V. Roussev, and S. Garfinkel, "File Classification Fragment-The Case
  for Specialized Approaches," Systematic Approaches to Digital
  Forensics Engineering (IEEE/SADFE 2009), Oakland, California.
  ([PDF](https://simson.net/clips/academic/2009.SADFE.Fragments.pdf))

<!-- -->

- I. Ahmed, K.-S. Lhee, H. Shin and M. Hong, [On Improving the Accuracy
  and Performance of Content-based File Type
  Identification](https://link.springer.com/chapter/10.1007/978-3-642-02620-1_4),
  Proceedings of the 14th Australasian Conference on Information
  Security and Privacy (ACISP 2009), pp.44-59, LNCS (Springer),
  Brisbane, Australia, July 2009.

2010

- I. Ahmed, K.-s. Lhee, H. Shin and M. Hong, [Fast File-type
  Identification](http://www.alphaminers.net/sub05/sub05_03.php?swf_pn=5&swf_sn=3&swf_pn2=3),
  Proceedings of the 25th ACM Symposium on Applied Computing (ACM SAC
  2010), ACM, Sierre, Switzerland, March 2010.

<!-- -->

- I. Ahmed, K.-s. Lhee, H. Shin and M. Hong, Content-based File-type
  Identification Using Cosine Similarity and a Divide-and-Conquer
  Approach, IETE Technical Review, 27(6), 2010.

2011

- I. Ahmed, K.-S. Lhee, H.-J. Shin, M.-P. Hong, [Fast Content-Based File
  Type
  Identification](https://link.springer.com/chapter/10.1007/978-3-642-24212-0_5),
  Proceedings of the 7th Annual IFIP WG 11.9 International Conference on
  Digital Forensics, Orlando, FL, USA, February, 2011

<!-- -->

- C. Mattmann and J. Zitting, [Tika in Action](https://www.manning.com/books/tika-in-action),
  Manning Publications. December, 2011.

2013

- M.C. Amirani, M. Toorani, and S. Mihandoost, Feature‐based Type
  Identification of File Fragments, Journal of Security and Communications
  Networks, Vol.6, No.1, pp. 115–128, 2013.
