Disk imaging is the process of making a bit-by-bit copy of a disk.
Imaging (in more general terms) can apply to anything that can be
considered as a bit-stream, e.g. a physical or logical volumes, network
streams, etc.

The most straight-forward disk imaging method is reading a disk from
start to end and writing the data to a [Forensics image
format](:Category:Forensics_File_Formats "wikilink"). This can be a time
consuming process especially for disks with a large capacity.

The process of disk imaging is also referred to as disk duplication.

## Disk Imaging Solutions

See: [Disk Imaging Solutions](:Category:Disk_Imaging "wikilink")

## Common practice

Its a common practice to use a [Write
Blocker](Write_Blockers "wikilink") when imaging a physical disk. The
write blocker is an additional measure to prevent write access to the
disk.

Also see: [Device Configuration Overlay (DCO) and Host Protected Area
(HPA)](DCO_and_HPA "wikilink")

## Integrity

Often when creating a disk image a [cryptographic
hash](http://en.wikipedia.org/wiki/Cryptographic_hash_function) is
calculated of the entire disk. Commonly used cryptographic hashes are
MD5, SHA1 and/or SHA256.

By recalculating the integrity hash at a later time, one can determine
if the data in the disk image has been changed. This by itself provides
no protection against intentional tampering, but can indicate that the
data was altered, e.g. due to corruption. The integrity hash does not
indicate where in the data the alteration has occurred. Therefore some
image tools and/or formats provide for additional integrity checks like:

- A checksum
- Parity data
- [Piecewise hashing](Piecewise_hashing "wikilink")

## Smart imaging

Smart imaging is a combination of techniques to make the imaging process
more intelligent.

- Compressed storage
- Deduplication
- Selective imaging
- Decryption while imaging

### Compressed storage

A common technique to reduce the size of an image file is to compress
the data. Where the compression method should be
[lossless](http://en.wikipedia.org/wiki/Lossless_data_compression). On
modern computers, with multiple cores, the compression can be done in
parallel reducing the output without prolonging the imaging process.
Since the write speed of the target disk can be a bottleneck in imaging
process, parallel compression can reduce the total time of the imaging
process. [Guymager](Guymager "wikilink") was one of the first imaging
tools to implement the concept of multi-process compression for the
[Encase image file format](Encase_image_file_format "wikilink"). This
technique is now used by various imaging tools including [Tableau Imager
(TIM)](http://www.tableau.com/index.php?pageid=products&model=TSW-TIM)

Other techniques like storing the data sparse, using **empty-block
compression** or **pattern fill**, can reduce the total time of the
imaging process and the resulting size of new non-encrypted (0-byte
filled) disks.

### Deduplication

Deduplication is the process of determining and storing data that occurs
more than once on-disk, only once in the image. It is even possible to
store the data once for a corpus of images using techniques like hash
based imaging.

### Selective imaging

Selective imaging is a technique to only make a copy of certain
information on a disk like the \$MFT on an [NTFS](NTFS "wikilink")
volume with the necessary contextual information.

[EnCase](EnCase "wikilink") Logical Evidence Format (LEF) is an example
of a selective image; although only file related contextual information
is stored in the format by [EnCase](EnCase "wikilink").

### Decryption while imaging

Encrypted data is worst-case scenario for compression. Because the
encryption process should be deterministic, a solution to reduce the
size of an encrypted image is to store it non-encrypted and compressed
and encrypt it again on-the-fly if required. Although this should be
rare since the non-encrypted data is what undergoes analysis.

## Also see

- [Forensics File Formats](:Category:Forensics_File_Formats "wikilink")
- [Write Blockers](Write_Blockers "wikilink")
- [Piecewise hashing](Piecewise_hashing "wikilink")
- [Memory Imaging](Memory_Imaging "wikilink")
- [Imager NG Ideas](Imager_NG_Ideas "wikilink")

## External Links

- [Benchmarking Hard Disk Duplication Performance in Forensic
  Applications](http://www.tableau.com/pdf/en/Tableau_Forensic_Disk_Perf.pdf),
  by [Robert Botchek](Robert_Botchek "wikilink")
- [Feeling odd - Using new OS and CPU features to speed up large file
  copying](http://stealth.openwall.net/papers/odd.pdf), by [Sebastian
  Krahmer](Sebastian_Krahmer "wikilink"), June 2012

### Hash based imaging

- [Hash based disk imaging using
  AFF4](http://www.dfrws.org/2010/proceedings/2010-314.pdf), by [Michael
  Cohen](Michael_Cohen "wikilink"), [Bradley
  Schatz](Bradley_Schatz "wikilink")

[Category:Disk Imaging](Category:Disk_Imaging "wikilink")