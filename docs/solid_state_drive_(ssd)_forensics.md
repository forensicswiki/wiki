---
tags:
  - Hardware
---
Solid State Drives pose a variety of interesting challenges for computer
forensics in comparison with traditional rotating magnetic platter hard
drives.

Most SSD devices are based on flash memory; some have battery backed
SRAM or DRAM with a flash backing store.

Flash has a number of key properties that complicate its use in computer
storage systems and subsequent forensic analysis:

1. Internally, flash memory is not divided into the traditional 512
   byte blocks, but instead is in pages of 2KiB, 4KiB, or larger,
   although it is still presented to the host computer in blocks
2. Whilst hard drives can be written in a single pass, flash memory
   pages must be erased (in whole) before they can be rewritten.
3. Rewriting a block at the operating system level does not necessarily
   rewrite the same page in the flash memory due to the controller
   remapping data to spread wear or avoid failing pages
4. Each page can be erased and rewritten a limited number of times -
   typically 1000 to 10,000. (Hard drive sectors, in contrast, can be
   rewritten millions of times or more.)
5. Flash data is often encrypted on the drive, and can be "erased" by
   telling the controller to forget the old key and generate a new one,
   as well as marking all blocks as unused

The controller in a flash SSD is significantly more complex in the
number of tasks it has to perform in comparison to a magnetic rotating
drive, with the following features:

1. *wear leveling* - that is, spreading the writes to flash out among
   different sectors. Wear leveling is typically done with a *flash
   translation layer* that maps *logical sectors* (or LBAs) to
   *physical pages*. Most FTLs are contained within the SSD device and
   are not accessible to end users.
2. *read/modify/relocate+write* - if the controller allows rewriting of
   a partial flash page, it must read the entire page, modify the
   sector that is being written, and write the new flash page in a
   new/fresh location which has been previously erased. the old
   pre-modification data's page is then queued for erase.

## External Links

* [Recovering data from USB flash memory sticks that have been damaged or electronically erased](https://dl.acm.org/doi/10.5555/1363217.1363243),
  by B. J. Phillips, C. D. Schmidt and D. R. Kelly, 2008
* [The Forensic Potential of Flash Memory](https://archive.org/details/theforensicpoten109454629),
  by James E. Regan, 2009
* [Solid State Drives: The Beginning of the End for Current Practice in Digital Forensic Recovery?](https://researchportal.murdoch.edu.au/esploro/outputs/journalArticle/Solid-State-Drives-The-Beginning-of/991005543502107891),
  by G.B. Bell and R. Boddington, 2010
* [Making sense of unstructured flash-memory dumps](https://dl.acm.org/doi/10.1145/1774088.1774426),
  by David Billard and Rolf Hauri, March 22, 2010
* [Reliably Erasing Data from Flash-Based Solid State Drives](https://cseweb.ucsd.edu/~m3wei/assets/pdf/FMS-2010-Secure-Erase.pdf),
  by Michael Wei, Laura M. Grupp, Frederick M. Spada, Steven Swanson, 2011
* [Why SSD Drives Destroy Court Evidence, and What Can Be Done About It](https://belkasoft.com/why-ssd-destroy-court-evidence),
  by Yuri Gubanov and Oleg Afonin, October 2012
* [Recovering Evidence from SSD Drives in 2014: Understanding TRIM](https://www.forensicfocus.com/articles/recovering-evidence-from-ssd-drives-in-2014-understanding-trim-garbage-collection-and-exclusions/),
  by Yuri Gubanov and Oleg Afonin, September 23, 2014

### Presentations

* [Reliably Erasing Data from Flash-Based Solid State Drives](https://cseweb.ucsd.edu//~m3wei/assets/pdf/FMS-2010-Secure-Erase.pdf),
  by Michael Wei, Laura Grupp, Steven Swanson, February 2011
* [TRIM &amp; dm-crypt ... problems?](http://asalor.blogspot.com/2011/08/trim-dm-crypt-problems.html),
  by Milan Broz, August 14, 2011
* [Challenges of SSD Forensic Analysis](https://www.slideshare.net/digitalassembly/challenges-of-ssd-forensic-analysis),
  by Digital Assembly,
* [Solid State Drives: Ruining Forensics](https://www.youtube.com/watch?v=WcO7xn0wJ2I),
  by Scott Moulton, DEFCON 16 (2008)
* Scott Moulton, Shmoocon 20008, SSD drives vs. Hard Drives.
  * [SSD Flash Hard Drives - Shmoocon 2008 - Part 1](https://www.youtube.com/watch?v=l4hbdZFWGog)
  * [SSD Flash Hard Drives - Shmoocon 2008 - Part 2](https://www.youtube.com/watch?v=mglEnIPnzjo)
  * [SSD Flash Hard Drives - Shmoocon 2008 - Part 3](https://www.youtube.com/watch?v=3psy_d-pyNg)
  * [SSD Flash Hard Drives - Shmoocon 2008 - Part 4](https://www.youtube.com/watch?v=pKeZvhDd5c4)
  * [SSD Flash Hard Drives - Shmoocon 2008 - Part 5](https://www.youtube.com/watch?v=9XMBdDypSO4)
  * [SSD Flash Hard Drives - Shmoocon 2008 - Part 6](https://www.youtube.com/watch?v=LY36SWbfQg0)
* [Risky Business \#185](https://risky.biz/RB185/),
  Peter Gutmann talks SSD forensics, March 4, 2011 (Radio Show)
