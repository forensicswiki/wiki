The **Advanced Forensics Format** (**AFF**) is an extensible open format
for the storage of [disk images](disk_image "wikilink") and related
forensic [metadata](metadata "wikilink"). It was originally developed by
[Simson Garfinkel](Simson_Garfinkel "wikilink") and [Basis
Technology](Basis_Technology "wikilink"). The last version of AFF is
implemented in the [AFFLIBv3](AFFLIBv3 "wikilink") library, which can be
found on [github](https://github.com/simsong/AFFLIBv3).
[AFF4](AFF4 "wikilink") builds upon many of the concepts developed in
AFF. AFF4 was developed by [Michael Cohen](Michael_Cohen "wikilink"),
Simson Garfinkel and Bradley Schatz. That version can be downloaded from
[Google Code](https://code.google.com/p/aff4/).

**AFF3 and AFFLIBv3 have been depreciated and should not be used for new
projects.**

[Sleuthkit](Sleuthkit "wikilink"), [Autopsy](Autopsy "wikilink") ,
[OSFMount](OSFMount "wikilink"), [Xmount](Xmount "wikilink"), [FTK
Imager](FTK_Imager "wikilink") and [FTK](FTK "wikilink") support the
AFFv3 image format.

## AFF Background

AFF was created to be an open and extensible file format to store disk
images and associated metadata. The goal was to create a disk imaging
format that would not lock users into a proprietary format that may
limit how he or she may analyze it. An open standard enables
investigators to quickly and efficiently use their preferred tools to
solve crimes, gather intelligence, and resolve security incidents. The
format was implemented in AFFLIB which was distributed with an open
source license.

After AFFLIB was published, [Joachim Metz](Joachim_Metz "wikilink")
published [libewf](libewf "wikilink"), an open source implementation of
the EnCase Expert Witness format. Later, Guidance Software modified its
format to allow single disk volumes larger than 4GiB. Together these two
changes significantly decreased the need for AFF and AFFLIB.

In 2009 Cohen, Garfinkel and Schatz published an article on AFF4, a new
file format that incorporated and expanded on the underlying AFF ideas.
AFF4 provides for multiple data views within a single data archives and
allows links between archives. As a result, AFF4 natively supports
selective imaging, logical file volumes, hash-based imaging, and a
variety of case-management scenarios.

## AFFv3 Extensions

The original AFF format is a single file that contains segments with
drive data and metadata. Its contents can be compressed, but it can be
quite large as the data on modern hard disks often reach 100GB in size.
AFFv3 supported three file extensions --– AFF, AFD and AFM –-- and
provided a tool to easily convert between the variations.

For ease of transfer, large AFF files can be broken into multiple AFD
format files. The smaller AFD files can be readily moved around a FAT32
file system which limits files to 2GB or stored on DVDs, which have
similar size restrictions. The AFM format stores the metadata in an AFF
file, and the disk data in a separate raw file. This format allows
analysis tools that support the raw format to access the data, but
without losing the metadata.

### Compression and Encryption

AFF supports two compression algorithms: zlib, which is fast and
reasonably efficient, and LZMA, which is slower but dramatically more
efficient. zlib is the same compression algorithm used by EnCase. As a
result, AFF files compressed with zlib are roughly the same size as the
equivalent EnCase file. AFF files can be recompressed using the LZMA
algorithm. These files are anywhere from 1/2 to 1/10th the size of the
original AFF/EnCase file.

AFF2.0 supports encryption of disk images. Unlike the password
implemented by EnCase, encrypted images cannot be accessed without the
necessary encryption key. FTK Imager/FTK added support for this
encryption in version 3.0 and are able to create and access AFF
encrypted images.

### AFFLIBv3 Tools

- [aimage](aimage "wikilink")
- [ident](ident "wikilink")
- [afcat](afcat "wikilink")
- [afcompare](afcompare "wikilink")
- [afconvert](afconvert "wikilink")
- [affix](affix "wikilink")
- [affuse](affuse "wikilink")
- [afinfo](afinfo "wikilink")
- [afstats](afstats "wikilink")
- [afxml](afxml "wikilink")
- [afsegment](afsegment "wikilink")

# See Also

- [AFF Developers Guide](AFF_Developers_Guide "wikilink") --- A guide
  for programmers on how to use the AFF
- [AFF Development Task List](AFF_Development_Task_List "wikilink") ---
  Want to help with AFF? Here is a list of things that need to be done.

## External Links

- [Basis Technology's AFF
  website](http://www.basistech.com/digital-forensics/aff.html)
- [OSFMount - 3rd party tool for mounting AFF disk images with a drive
  letter](http://www.osforensics.com/tools/mount-disk-images.html)

[Category:Forensics File
Formats](Category:Forensics_File_Formats "wikilink") [Category:Open
Source Tools](Category:Open_Source_Tools "wikilink")