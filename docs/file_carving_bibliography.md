---
tags:
  - Bibliographies
---
**In chronological order, oldest to most recent**

### Basic Techniques

[An analysis of disc carving techniques](https://apps.dtic.mil/sti/citations/ADA432468),
by Mikus, Nicholas A., Master's Thesis, Naval Postgraduate School. March 2005.

[Scalpel: A Frugal, High Performance File Carver](https://dfrws.org/sites/default/files/session-files/2005_USA_paper-scalpel_-_a_frugal_high_performance_file_carver.pdf),
by Golden G. Richard and Vassil Roussev, DFRWS 2005

[Massive threading: Using GPUs to increase the performance of digital forensics tools](https://dfrws.org/sites/default/files/session-files/2007_USA_paper-massive_threading_-_using_gpus_to_increase_the_performance_of_digital_forensics_tools.pdf),
by Lodovico Marziale, Golden G. Richard III\*, Vassil Roussev, DFRWS 2007.

### Fragment Recovery Carving

Automatic Reassembly of Document Fragments via Data Compression, Kulesh
Shanmugasundaram and Nasir Memon, Presented at DFRWS, 2002.

Automatic Reassembly of Document Fragments via Context Based Statistical Models,
by Kulesh Shanmugasundaram and Nasir Memon, Annual Computer Security
Applications Conference, 2003.

[Automated Reassembly of Fragmented Images](https://ieeexplore.ieee.org/document/1202747),
by Anandabrata Pal, Kulesh Shanmugasundaram, Nasir Memon, Proceedings of
the IEEE International Conference on Acoustics, Speech, and Signal
Processing, 2003.

[Carving Contiguous and Fragmented Files with Fast Object Validation](http://www.simson.net/clips/academic/2007.DFRWS.pdf),
by Simson Garfinkel, Digital Forensics Workshop (DFRWS 2007), Pittsburgh, PA,
August 2007.

Automated Reassembly of File Fragmented Images Using Greedy Algorithms,
by Anandabrata Pal and Nasir Memon, IEEE Trans. Image Processing, Feb.  2006.

[In-Place File Carving](https://dl.ifip.org/db/conf/ifip11-9/df2007/RichardRM07.pdf),
by Golden G. Richard III, Vassil Roussev, and Lodovico Marziale, IFIP WG 11.9,
Advances in Digital Forensics, 2007.

Reassembly of Fragmented JPEG Images Containing Restart Markers, Martin
Karresand , Nahid Shahmehri , European Conference on Computer Network
Defense EC2ND in cooperation with ENISA ( 2008 : Dublin, Ireland ) , s.
25 - 32 Los Alamitos, CA, USA : IEEE Computer Society, 2008.

Completing the Picture: Fragments and Back Again, Martin Karresand,
Linköping : Linköpings universitet, 2008, 111 s. Linköping studies in
science and technology. Thesis, ISBN: 978-91-7393-915-7

[Detecting File Fragmentation Point Using Sequential Hypothesis Testing](https://dfrws.org/sites/default/files/session-files/2008_USA_paper-detecting_file_fragmentation_point_using_sequential_hypothesis_testing.pdf),
by Anandabrata Pal, Husrev Sencar, Nasir Memon, DFRWS, 2008.
[slides](https://dfrws.org/sites/default/files/session-files/2008_USA_pres-detecting_file_fragmentation_point_using_sequential_hypothesis_testing.pdf)

https://dfrws.org/sites/default/files/session-files/2009_USA_paper-identification_and_recovery_of_jpeg_files_with_missing_fragments.pdf),
by Husrev Sencar and Nasir Memon. DFRWS, 2009.

The Evolution of File Carving,
by Anandabrata Pal and Nasir Memon. IEEE Signal Processing Magazine,
Volume: 26, Issue 2. March 2009.

### Sector Discrimination

<bibtex> @article{

` journal="Journal of Digital Forensic Practice",  `
` publisher="Taylor & Francis",`
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

` url="`[`https://www.tandfonline.com/doi/abs/10.1080/15567280802050436`](https://www.tandfonline.com/doi/abs/10.1080/15567280802050436)`"`

} </bibtex>

## Evaluations

* [Measuring and Improving the Quality of File Carving Methods](https://github.com/libyal/documentation/blob/main/Thesis%20-%20Measuring%20and%20Improving%20the%20Quality%20of%20File%20Carving%20Methods.pdf)
  by S.J.J. Kloet , Master's thesis, Eindhoven University of Technology, August 2007

## See also

* [File Carving](file_carving.md)
