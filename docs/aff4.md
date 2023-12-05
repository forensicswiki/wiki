---
tags:
  - Articles that need to be expanded
  - Disk Image
  - File Formats
---
# Advanced Forensic Framework 4 (AFF4)

AFF4 was developed by [Michael Cohen](michael_cohen.md),
[Simson Garfinkel](simson_garfinkel.md) and [Bradley Schatz](bradley_schatz.md).
This page describes the basic design. See [LibAFF4](libaff4.md) for a
description of how to use the sample implementation, library and tools.

## Why did we want to design yet another forensic file format?

Traditional forensic file formats have a number of limitations which
have been exposed over the years:

* Proprietary formats like EWF are difficult to implement and explain.
  EWF is a fairly complex file format. Most of the details are reverse
  engineered. Recovery from damaged EWF files is difficult as detailed
  knowledge of the file format is required.
* Simple file formats like dd are very large since they are
  uncompressed. They also dont store metadata, signatures or have
  cryptographic support.
* Traditional file formats are designed to store a single stream. Often
  in an investigation, however, multiple source of data need to be
  acquired (sometimes simultaneously) and stored in the same evidence
  volumes.
* Traditional file formats just deal with data - there is no attempt to
  build a universal evidence management system integrated within the
  file specification.

The previous AFF format made huge advancements in the field introducing
excellent support for cryptography, digital signatures, compression and
even the concepts of external referencing. It was time to gather up all
the good things in AFF and redesign a new AFF4 specification.

We wanted to use a well recognized, widely supported and open bit level
format. One of the strengths of AFF was the use of segments within the
file format itself. It because obvious that the only requirement we have
from an underlying storage mechanism is the ability to store blobs of
data by name, and retrieve them by that name. How these are actually
stored is quite irrelevant to us.

The sections below give a quick overview to some of the major ideas.

## Objects

AFF4 is an object oriented architecture. We term the *AFF4 universe* the
total set of objects which are known. Because AFF4 is designed to be
scalable to huge evidence corpuses the AFF4 universe is infinite. All
objects are addressable by their name which is unique in the universe.
For example an AFF4 object might have a name of:

`   urn:aff4:f3eba626-505a-4730-8216-1987853bc4d2`

This is a standard URN notation object. The URN is unique. There will
never be another object created anywhere in the universe with the same
URN. Once objects are created their URN is fixed.

## Relations

The AFF4 universe uses RDF to specify attributes about objects. In its
simplest form (the one we use) RDF is just a set of statements about an
object of the form:

`  Subject   Attribute   Value`

For example:

```
  ******** Object urn:aff4:f3eba626-505a-4730-8216-1987853bc4d2 ***********
    aff4:stored = urn:aff4:4bdbf8bc-d8a5-40cb-9af0-fd7e4d0e2c9e
    aff4:type = image
    aff4:interface = stream
    aff4:timestamp = 0x49E9DEC3
    aff4:chunk_size = 32k
    aff4:compression = 8
    aff4:chunks_in_segment = 2048
    aff4:size = 10485760
```

This shows that the object named (the Subject) has all these attributes
and their values. We call these *relations* or *facts*. The entire AFF4
universe is constructed around these facts. As we will see later facts
can be signed by a person - which essentially has the person asserting
that the facts are true.

AFF4 objects exist because they do something useful. What they do
depends on the interface they present. Currently there are a few
interfaces, the most important ones are the **Volume** interface and the
**Stream** interface. An object's interface is a fact about the object
with an attribute of aff4:interface. This tells us what the object can
do for us.

On the other hand AFF4 objects can actually be different things and do
what they do in a different way. The actual type of an object is
specified by the attribute aff4:type. Whereas an interface tells us what
the object can do for us, a type tells us what it actually is. (Its
possible to change an object's type without changing its interface for
example going from a ZipFile to a Directory volume. This does not affect
any users of the object).

## Volumes

We define a **Volume** as a storage mechanism which can store a segment
(bit of binary data) by name and retrieve it by name. Currently we have
two volume implementations: a **Directory** and a **ZipFile**.

### Directory Volume

The Directory implementation stores the segments as flat files inside a
regular directory on the filesystem. This is really useful if we want to
image to a FAT filesystem since each segment is really small and we will
not exceed the file size limitations. Its also possible to root the
directory on a http url (i.e. the directory starts with
`http://somehost/url/`). This allows us to use the image directly from
the web - no need to download the whole thing.

Directory objects use FileLikeObjects (see below) to actually store the
segments into different files. This means that Directory Volumes can be
stored on HTTP or HTTPS servers, as well as regular directories.

### ZipFile Volume

The ZipFile implementation stores segments inside a zip archive. If the
archive gets too large (over 4Gb) we use the Zip64 extensions to store
offsets in 64 bits. This is nice since small volumes can just be opened
with windows explorer. Its also really easy to extract the data out. A
ZipFile volume uses a FileLikeObject to actually store the zip file.

This means that its possible to write a ZipFile volume directly onto a
HTTP server and use the image directly from the server as well.

Example: `http://www.pyflag.net/images/test.zip` is an example of a
small (about 1 MB) AFF4 image.

Directory and ZipFile volumes can be easily converted from one to the
other (i.e. unzip the ZipFile into a directory to create a Directory
volume).

## Streams

Streams are the basic interface for storing image data. Streams present
a consistent interface which presents the methods of *read*, *seek*,
*tell' and*close*. (Streams also support*write'', but thats a bit
special because its how you actually create them).

As long as an AFF4 object presents a stream interface its possible to
perform random reads within the body of data. Hence its possible to
store any image data within the stream. The following section explain
some of the specific implementations of streams.

### FileBackedObjects

The FileBacked object is a stream which stores data in an actual file on
the filesystem. The location of the file is determined from the file's
URN. Since a URN is a superset of URLs, URLs are also valid URNs. This
means that something like `file:///somedirectory/filename` is a valid
location for a FileBackedObject.

### HTTPObject

HTTP is ubiquitous and easy to deploy. Since URLs are also valid URNs,
its possible to specify that an AFF4 volume be stored or read from a
HTTP server. This implementation uses the Range HTTP header to read
specific byte ranges from the server - so network traffic between the
client and server is minimal. Its possible to examine a remote image
over HTTP without needing to copy the whole thing down.

This is excellent when you just want to have a quick look at a remote
image without needing to download the whole thing.

For security reasons its recommended write support be restricted in some
way (e.g. passwords, SSL certificates etc). Read support can be provided
freely if the volume is encrypted. Securing the web server is outside
the scope of AFF4.

### Segments

Segments are components stored directly within the Volume. Recall that a
volume is simply an object which stores and retrieves segments. Segments
also present the stream interface, but practically they should generally
be used for smaller streams because it may be expensive to seek within
compressed segments.

Segments are particularly useful when you dont have an imaging tool
handy and you want to create a logical image of a subset of a filesystem
(that is you want to image some files from a filesystem rather than a
forensic image of the filesystem itself). This could happen if you can
not take the server down for incident response or if the filesystem is
just so big and you know most of it will not be relevant.

In that case there is nothing simpler than just to open up windows
explorer - right click and send to a compressed folder. A regular zip
file is also an AFF4 volume!!! The files within it are stream objects
and libaff4 will recognize them as such. Larger segments can be
converted to Image streams later (and signed, encrypted etc).

### Image streams

Although segments are great for small files, for very large images we
cant really use those because we could not compress them efficiently.
Therefore we have an image stream.

The Image stream stores the image in chunks. Each chunk (typically 32kb)
is compresses and a group of chunks (called **bevies**) are stored back
to back inside a bevy segment. Segments are named according to the
scheme: URN_OF_IMAGE_STREAM/0000000, URN_OF_IMAGE_STREAM/0000001 etc.

The offset of each chunk within the bevy is stored in an index segment
(with a. idx extension). Here is an example:

`    urn:aff4:f3eba626-505a-4730-8216-1987853bc4d2/00000000`
`    urn:aff4:f3eba626-505a-4730-8216-1987853bc4d2/00000000.idx`
`    urn:aff4:f3eba626-505a-4730-8216-1987853bc4d2/00000001`
`    urn:aff4:f3eba626-505a-4730-8216-1987853bc4d2/00000001.idx`

Here is a short python program to unpack an Image stream:

` volume=zipfile.ZipFile(INPUT_FILE)`
` outfd = open(OUTPUT_FILE,"w")`
` count = 0`
` while True:`
`   idx_segment = volume.read(STREAM+"/%08d.idx" % count)`
`   bevy = volume.read(STREAM+"/%08d" % count)`
`   indexes = struct.unpack("<" + "L" * `
`       (len(idx_segment)/4), idx_segment)`
`   for i in range(len(indexes)-1):`
`       chunk = bevy[indexes[i]:indexes[i+1]]`
`       outfd.write(chunk.decode('zlib'))`
`   count += 1`

### Map Streams

A lot of work in digital forensics involves copying data around. For
example, carving files usually results with the carved files copied out
of the image for testing. If you image a RAID array separately you end
up with 3-5 disk images and typically you will need to copy them into a
logical image (unless your favourite software supports RAID
reconstruction). When you copy a file out of the image using sleuthkit,
you are actually copying bits of data directly from the image.

All these copies are wasteful of disk space. They are also hard to
manage because pretty soon you end up with lots of copies of the same
data in different ways. There must be a better way!!!

Now there is. By having the underlying forensic format doing all the
mapping its possible to use tools which are not capable of doing these
transformations themselves. This is all about tool reuse. For example
suppose you have a carver which is used to work on dd images. But you
want to use it on the virtual memory image of the firefox process. In
the past you had to copy the virtual memory out (it could be 2-4gb) then
run the carver on it, and possibly end up with about 3 or 4 copies of
the same data - for each process address space!!!

Its much easier to have volatility create the initial maps for each
process (with zero storage overheads), and then carvers can just use the
maps without understanding anything about memory forensics. In this way
the AFF4 format is more of an interchange format - allowing tools to be
used on the results from other tools.

The map stream is an AFF4 object which contains a segment called
**map**. Here is an example:

` 1601536,0,urn:aff4:f3eba626-505a-4730-8216-1987853bc4d2`
` 1614848,12288,urn:aff4:f3eba626-505a-4730-8216-1987853bc4d2`
` 1879040,274432,urn:aff4:f3eba626-505a-4730-8216-1987853bc4d2`
` 2142208,536576,urn:aff4:f3eba626-505a-4730-8216-1987853bc4d2`
` 2405376,798720,urn:aff4:f3eba626-505a-4730-8216-1987853bc4d2`
` 2668544,1060864,urn:aff4:f3eba626-505a-4730-8216-1987853bc4d2 `
` 2931712,1323008,urn:aff4:f3eba626-505a-4730-8216-1987853bc4d2`

This map was generated by sleuthkit for an ext2 file. The first number
of the offset in the image. The second number is the offset in the file
and the third number of the URN of the object to read from (the target).
The above map basically says that the byte range from 0-12288 in the
file should be read from aff4:f3eba626-505a-4730-8216-1987853bc4d2
offset 1601536 to 1614848, etc.

Using the fsbuild tool its possible to create map streams for all files
in an image at virtually zero storage requirements. Then its possible to
use other tools which may not know how to read filesystems to examine
the files.

Following is an example of a 3 disk RAID system which was acquired with
into three separate streams:

`  0,0,disk1`
`  1,0,disk0`
`  2,1,disk2`
`  3,1,disk1`
`  4,2,disk0`
`  5,2,disk2`

To make this work we need to tell AFF4 that the map should be repeated.
We do this by setting attributes on the map objects:

` aff4:block_size=64k `
` aff4:stream_period=6 `
` aff4:target_period=3`

## See Also

- [Extending the Advanced Forensic Format to accommodate Multiple Data Sources, Logical Evidence, Arbitrary Information and Forensic Workflow](https://simson.net/clips/academic/2009.DFRWS.AFF4.pdf),
  by M. I. Cohen, Simson Garfinkel and Bradley Schatz, DFRWS 2009,
  Montreal, Canada.
- [Wirespeed: Extending the AFF4 forensic container format for scalable acquisition and live analysis](https://dfrws.org/sites/default/files/session-files/2015_USA_pres-wirespeed_extending_the_aff4_container_format_for_scalable_acquisition_and_live_analysis.pdf),
  by [Bradley L. Schatz](bradley_schatz.md), DFRWS US 2015

### Tools

* [c-aff4](https://github.com/Velocidex/c-aff4)
