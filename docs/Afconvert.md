**afconvert** is part of the [AFF](AFF "wikilink") toolset. This program
can interconvert between all of the different file formats that AFF
supports. It can also be used to restore AFF files on raw disk
partitions. The remainder of this article uses the term "ISO/RAW" to
describe a bit-for-bit disk image with no metadata. This format is also
called a "dd image".

# Converting ISO/RAW to AFF

To convert a file from ISO to AFF, use this command.

`  % afconvert filename.iso`

This will give you output like this:

` convert filename.iso --> filename.aff`
` Converting page 1 of 6`
` Converting page 2 of 6`
` Converting page 3 of 6`
` Converting page 4 of 6`
` Converting page 5 of 6`
` Converting page 6 of 6`

md5: 949442a1cd26d3d26b28a529e08e32df sha1:
198dd3779dce1de0859183a619dd1a9ffbc249f7 bytes converted: 108580864
Total pages: 7 (3 compressed)

# Converting AFF to ISO/RAW

` % afconvert -r filename.aff`
` Convert filename.aff --> filename.raw`
` Converting page 1 of 6`
` Converting page 2 of 6`
` Converting page 3 of 6`
` Converting page 4 of 6`
` Converting page 5 of 6`
` Converting page 6 of 6`
` md5: 949442a1cd26d3d26b28a529e08e32df`
` sha1: 198dd3779dce1de0859183a619dd1a9ffbc249f7`
` bytes converted: 108580864 `
` Conversion finished.`

# Other formats

afconvert can convert to other formats as well. For example, you can
convert an AFF file (which stores all of the data and metadata in a
single file) to AFM (which stores the metadata in an AFM file and the
data in a splitraw file):

`  % afconvert -a afm filename.aff`

` convert filename.aff --> filename.afm`
` Converting page 6 of 6`
` md5: 949442a1cd26d3d26b28a529e08e32df`
` sha1: 198dd3779dce1de0859183a619dd1a9ffbc249f7`
` bytes converted: 108580864 `
` Conversion finished.`

` 02:40 PM s:~$ ls -l filename*`
` -rw-r--r--  1 simsong  simsong  108580864 Mar 30 14:40 filename.000`
` -rwxr-xr-x  1 simsong  simsong  108528960 Mar 30 13:42 filename.aff*`
` -rwxr-xr-x  1 simsong  simsong       1463 Mar 30 14:40 filename.afm*`
` 02:40 PM s:~$ `

In this example, **filename.aff** is the original AFF file,
**filename.afm** is the metadata and **filename.000** is the first
splitraw file. Here there is only one splitraw file, and the file didn't
expand much because the file is a disk image of a file that contains a
ZIP file.

# Restoring AFF onto a RAW partition

You can use afconvert to restore an AFF file onto a raw partition. In
this example, /dev/md1 is a raw partition of a memory file system on a
computer running FreeBSD:

` # mdconfig -a -t malloc -s 10858k`
` md1`
` #`

We can restore filename.aff onto /dev/md1: