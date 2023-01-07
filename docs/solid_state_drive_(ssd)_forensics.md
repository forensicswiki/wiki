---
tags:
  - No Category
---
Solid State Drives pose a variety of interesting challenges for computer
forensics in comparison with traditional rotating magnetic platter hard
drives.

Most SSD devices are based on flash memory; some have battery backed
SRAM or DRAM with a flash backing store.

Flash has a number of key properties that complicate its use in computer
storage systems and subsequent forensic analysis:

1.  Internally, flash memory is not divided into the traditional 512
    byte blocks, but instead is in pages of 2KiB, 4KiB, or larger,
    although it is still presented to the host computer in blocks
2.  Whilst hard drives can be written in a single pass, flash memory
    pages must be erased (in whole) before they can be rewritten.
3.  Rewriting a block at the operating system level does not necessarily
    rewrite the same page in the flash memory due to the controller
    remapping data to spread wear or avoid failing pages
4.  Each page can be erased and rewritten a limited number of times –
    typically 1000 to 10,000. (Hard drive sectors, in contrast, can be
    rewritten millions of times or more.)
5.  Flash data is often encrypted on the drive, and can be "erased" by
    telling the controller to forget the old key and generate a new one,
    as well as marking all blocks as unused

The controller in a flash SSD is significantly more complex in the
number of tasks it has to perform in comparison to a magnetic rotating
drive, with the following features:

1.  *wear leveling* – that is, spreading the writes to flash out among
    different sectors. Wear leveling is typically done with a *flash
    translation layer* that maps *logical sectors* (or LBAs) to
    *physical pages*. Most FTLs are contained within the SSD device and
    are not accessible to end users.
2.  *read/modify/relocate+write* - if the controller allows rewriting of
    a partial flash page, it must read the entire page, modify the
    sector that is being written, and write the new flash page in a
    new/fresh location which has been previously erased. the old
    pre-modification data's page is then queued for erase.

## Bibliography

<bibtex> @inproceedings{wei2011,

` author = {Yuri Gubanov, Oleg Afonin},`
` title = {Why SSD Drives Destroy Court Evidence, and What Can Be Done About It},`
` booktitle={Article},`
` year = 2012,`
` keywords = {ssd forensics},`
` added-at = {2012-09-01T09:00:00.000+0100},`
` url={`[`http://forensic.belkasoft.com/en/why-ssd-destroy-court-evidence`](http://forensic.belkasoft.com/en/why-ssd-destroy-court-evidence)`}`

} </bibtex>

<bibtex> @inproceedings{wei2011,

` author = {Michael Wei and Laura M. Grupp and Frederick M. Spada and Steven Swanson},`
` title = {Reliably Erasing Data from Flash-Based Solid State Drives},`
` booktitle={FAST 2011},`
` year = 2011,`
` keywords = {erasing flash security ssd},`
` added-at = {2011-02-22T09:22:03.000+0100},`
` url={`[`https://cseweb.ucsd.edu//~m3wei/assets/pdf/FMS-2010-Secure-Erase.pdf`](https://cseweb.ucsd.edu//~m3wei/assets/pdf/FMS-2010-Secure-Erase.pdf)`},`
` biburl = {`[`http://www.bibsonomy.org/bibtex/27c408ad559fc19f829717f485707a909/schmidt2`](http://www.bibsonomy.org/bibtex/27c408ad559fc19f829717f485707a909/schmidt2)`}`

} </bibtex> <bibtex> @article{bell2011,

`author="Graeme B. Bell and Richard Boddington",`
`title="Solid State Drives: The Beginning of the End for Current Practice in Digital Forensic Recovery?",`
`journal="Journal of Digital Forensics, Security and Law",`
`volume=5,`
`issue=3,`
`year=2011,`
`url={`[`https://researchrepository.murdoch.edu.au/id/eprint/3714/1/solid_state_drives.pdf`](https://researchrepository.murdoch.edu.au/id/eprint/3714/1/solid_state_drives.pdf)`}`

} </bibtex> <bibtex> @inproceedings{Billard:2010:MSU:1774088.1774426,

`author = {Billard, David and Hauri, Rolf},`
`title = {Making sense of unstructured flash-memory dumps},`
`booktitle = {Proceedings of the 2010 ACM Symposium on Applied Computing},`
`series = {SAC '10},`
`year = {2010},`
`isbn = {978-1-60558-639-7},`
`location = {Sierre, Switzerland},`
`pages = {1579--1583},`
`numpages = {5},`
`url = {`[`https://dl.acm.org/doi/10.1145/1774088.1774426`](http://doi.acm.org/10.1145/1774088.1774426)`},`
`doi = {`[`https://dl.acm.org/doi/10.1145/1774088.1774426`](http://doi.acm.org/10.1145/1774088.1774426)`},`
`acmid = {1774426},`
`publisher = {ACM},`
`address = {New York, NY, USA},`
`keywords = {cell phone, computer forensics, file carving, flash-memory dumps, forensics},`

} </bibtex> <bibtex> @mastersthesis{regan:2009,

` title="The Forensic Potential of Flash Memory",`
` author="James E. Regan",`
` school="Naval Postgraduate School",`
` address="Monterey, CA",`
` date=Sep,`
` year=2009,`
` pages=86,`
` url="`[`https://archive.org/details/theforensicpoten109454629`](https://archive.org/details/theforensicpoten109454629)`"`

} </bibtex> <bibtex> @inproceedings{Phillips:2008:RDU:1363217.1363243,

`author = {Phillips, B. J. and Schmidt, C. D. and Kelly, D. R.},`
`title = {Recovering data from USB flash memory sticks that have been damaged or electronically erased},`
`booktitle = {Proceedings of the 1st international conference on Forensic applications and techniques in telecommunications, information, and multimedia and workshop},`
`series = {e-Forensics '08},`
`year = {2008},`
`isbn = {978-963-9799-19-6},`
`location = {Adelaide, Australia},`
`pages = {19:1--19:6},`
`articleno = {19},`
`numpages = {6},`
`url = {`[`https://dl.acm.org/doi/10.5555/1363217.1363243`](http://portal.acm.org/citation.cfm?id=1363217.1363243)`},`
`acmid = {1363243},`
`publisher = {ICST (Institute for Computer Sciences, Social-Informatics and Telecommunications Engineering)},`
`address = {ICST, Brussels, Belgium, Belgium},`
`keywords = {data recovery, flash memory, semiconductor data remanence},`

} </bibtex>

## External Links

- [Recovering Evidence from SSD Drives in 2014: Understanding TRIM](https://www.forensicfocus.com/articles/recovering-evidence-from-ssd-drives-in-2014-understanding-trim-garbage-collection-and-exclusions/),
  by [Belkasoft](belkasoft.md), September 23, 2014

### Presentations

- [Milan Broz's blog - TRIM & dm-crypt ...  problems?](http://asalor.blogspot.com/2011/08/trim-dm-crypt-problems.html)
- [ATA Trim / Delete Notification Support in Windows 7](https://www.snia.org/sites/default/orig/sdc_archives/2009_presentations/thursday/NealChristiansen_ATA_TrimDeleteNotification_Windows7.pdf),
  Neal Christiansen, Storage Developer 2009
- [Challenges of SSD Forensic Analysis](https://www.slideshare.net/digitalassembly/challenges-of-ssd-forensic-analysis),
  Digital Assembly,
- [Solid State Drives: Ruining Forensics](https://www.youtube.com/watch?v=WcO7xn0wJ2I), by Scott
  Moulton, DEFCON 16 (2008)
- Scott Moulton, Shmoocon 20008, SSD drives vs. Hard Drives.
  - [SSD Flash Hard Drives - Shmoocon 2008 - Part 1](https://www.youtube.com/watch?v=l4hbdZFWGog)
  - [SSD Flash Hard Drives - Shmoocon 2008 - Part 2](https://www.youtube.com/watch?v=mglEnIPnzjo)
  - [SSD Flash Hard Drives - Shmoocon 2008 - Part 3](https://www.youtube.com/watch?v=3psy_d-pyNg)
  - [SSD Flash Hard Drives - Shmoocon 2008 - Part 4](https://www.youtube.com/watch?v=pKeZvhDd5c4)
  - [SSD Flash Hard Drives - Shmoocon 2008 - Part 5](https://www.youtube.com/watch?v=9XMBdDypSO4)
  - [SSD Flash Hard Drives - Shmoocon 2008 - Part 6](https://www.youtube.com/watch?v=LY36SWbfQg0)
- [Risky Business \#185](https://risky.biz/RB185/), Peter Gutmann talks
  SSD forensics, March 4, 2011 (Radio Show)
