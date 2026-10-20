---
tags:
  - Analysis
---
File Format Identification is the process of figuring out the format of
a sequence of bytes. Operating systems typically do this by file
extension or by embedded MIME information. Forensic applications need to
identify file types by content. It is one of the
[categories of file analysis](file_analysis.md).

## Tools

See also [File format identification
tools](tools_file_analysis.md#file-format-identification).

## Data Sets

If you are working in the field of file format identification, please
consider reporting the results of your algorithm with one of these
publicly available data sets:

* NPS govdocs1m - a corpus of 1 million files that can be redistributed
  without concern of copyright or PII. Download from the [Digital Coprora website](https://digitalcorpora.org/corpora/file-corpora/files/)
* The NPS Disk Corpus - a corpus of realistic disk images that contain
  no PII. Information is at: <https://digitalcorpora.org/?s=nps>

## Bibliography

Current research papers on the file format identification problem. Most
of these papers concern themselves with identifying the file format of a few
file sectors, rather than an entire file. **Please note that this
bibliography is in chronological order!**

### 2003

* [Content Based File Type Detection Algorithms](https://ieeexplore.ieee.org/document/1174905),
  by M.  McDaniel and M.H. Heydari, 36th Annual Hawaii International Conference
  on System Sciences (HICSS'03) - Track 9, 2003.

### 2005

* Fileprints: identifying file types by n-gram analysis, LiWei-Jen, Wang
  Ke, Stolfo SJ, Herzog B.., Proceeding of the 2005 IEEE workshop on
  information assurance, 2005.
  ([PDF](https://academiccommons.columbia.edu/doi/10.7916/D86M3DJC))
* D.J. Hickok, D.R.Lesniak, M.C. Rowe, File Type Detection Technology,
  2005 Midwest Instruction and Computing
  Symposium.([PDF](https://www.micsymposium.org/mics_2005/papers/paper7.pdf))

### 2006

* K. Martin, N. Shahmehri, File type identification of data fragments by their
  binary structure, Proceedings of the IEEE workshop on information assurance,
  pp.140-147, 2006. (<https://ieeexplore.ieee.org/document/1652088>)

### 2007

* [Oscar: File Type Identification of Binary Data in Disk Clusters and RAM Pages](https://link.springer.com/chapter/10.1007/0-387-33406-8_35),
  by M. Karresand, N. Shahmehri, May 2006.
* [Using Artificial Neural Networks for Forensic File Type Identification](https://www.cerias.purdue.edu/assets/pdf/bibtex_archive/2007-19.pdf),
  by R.M. Harris, May 2007.

### 2008

* M.C. Amirani, M. Toorani, and A. Beheshti, [A New Approach to
  Content-based File Type
  Detection](https://ieeexplore.ieee.org/document/4625611/;jsessionid=e9ClJYNu5ZPnylpkSj7LoQM5s2LCfErdPPJo0lC0MGmzs9la-7Ld!1844383281),
  Proceedings of the 13th IEEE Symposium on Computers and Communications
  (ISCC'08), pp.1103-1108, July 2008.
  ([PDF](https://arxiv.org/ftp/arxiv/papers/1002/1002.3174.pdf))

### 2009

* V. Roussev, and S. Garfinkel, "File Classification Fragment-The Case
  for Specialized Approaches," Systematic Approaches to Digital
  Forensics Engineering (IEEE/SADFE 2009), Oakland, California.
  ([PDF](https://simson.net/clips/academic/2009.SADFE.Fragments.pdf))
* I. Ahmed, K.-S. Lhee, H. Shin and M. Hong, [On Improving the Accuracy
  and Performance of Content-based File Type
  Identification](https://link.springer.com/chapter/10.1007/978-3-642-02620-1_4),
  Proceedings of the 14th Australasian Conference on Information
  Security and Privacy (ACISP 2009), pp.44-59, LNCS (Springer),
  Brisbane, Australia, July 2009.

### 2010

* [Fast File-type Identification](https://www.researchgate.net/publication/228451843_Fast_file-type_identification),
  by I. Ahmed, K.-s. Lhee, H. Shin and M. Hong, March 2010.

### 2011

* [Fast Content-Based File Type Identification](https://link.springer.com/chapter/10.1007/978-3-642-24212-0_5),
  by I. Ahmed, K.-S. Lhee, H.-J. Shin, M.-P. Hong, February, 2011
* [Tika in Action](https://www.manning.com/books/tika-in-action),
  by C. Mattmann and J. Zitting, December, 2011.

## See also

* [File analysis](file_analysis.md)
* [File formats](file_formats.md)
* [Tools: File analysis](tools_file_analysis.md)
