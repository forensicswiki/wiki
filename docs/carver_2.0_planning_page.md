---
tags:
  -  Research
  -  Articles that need to be expanded
---
This page is for planning Carver 2.0.

Please, do not delete text (ideas) here. Use something like this:

    <s>bad idea</s>
    :: good idea

This will look like:

<s>bad idea</s>



good idea

# Progress

There is a proof-of-concept open-source solution available: [Multimedia
File Carver](https://github.com/rpoisel/mmc) which focuses currently on
the recovery of fragmented multimedia files (movies) or fragmented JPEG
files (experimental). The following features have already been
implemented:

- Multi-Platform support (Linux and Windows)
- Graphical User Interface (PySide)
- Backend in C (performance critical); GUI in Python
- Support for Multi-Processing during the classification phase
- Support for Multi-Processing during the reassembly phase (ffmpeg)
- Support for The Sleuth Kit (TSK) to identify unallocated blocks

# License

BSD-3.



[Joachim](user:joachim_metz.md) library based validators could
require other licenses


Make the other libraries plug-able. If you them, you use them.
[Simsong](user:simsong.md)

# OS

Linux/FreeBSD/MacOS


Shouldn't this just match what the underlying afflib & sleuthkit cover?
[RB](user:rb.md)


Yes, but you need to test and validate on each. Question: Do we want toCARBON
2008 (UTC)

[Joachim](user:joachim_metz.md) I think we would do wise to
design with windows support from the start this will improve the
platform independence from the start



Agreed; I would even settle at first for being able to run against
Cygwin. Note that I don't even own or use a copy of Windows, but the
vast majority of forensic investigators do. [RB](user:rb.md)
14:01, 31 October 2008 (UTC)

[Rob J Meijer](user:capibara.md) Leaning heavily on the
autotools might be the way to go. I do however feel that support
requirements for windows would not be essential. Being able to run from
a virtual machine with the main storage mounted over cifs should however
be tested and if possible tuned extensively.



[Joachim](user:joachim_metz.md) You'll need more than autotools
to do native Windows support i.e. file access, UTF-16 support, wrap someCARBON
basic system functions or have them available otherwise



[Rob J Meijer](user:capibara.md) That´s exactly my point,
windows support as in being able to build and run on windows natively is
much more trouble than its worth. Better make for a lean and mean
autotools based build with little dependencies and no or little
recursion, and better spent effort on a lean POLA design on POSIX based
systems than on supporting building and running on non POSIX systems.

# Name tooling

- [Joachim](user:joachim_metz.md) A name for the tooling I
  propose coldcut



How about 'butcher'? ;) [RB](user:rb.md) 14:20, 31 October 2008
(UTC)

[Joachim](user:joachim_metz.md) cleaver ( scalpel on steroids
;-) )

- I would like to propose Gouge or Chisel :-) [Rob J
  Meijer](user:capibara.md)

# Requirements

[Joachim](user:joachim_metz.md) Could we do a MoSCoW evaluation
of these.

- AFF and EWF file images supported from scratch.
  ([Joachim](user:joachim_metz.md) I would like to have
  raw/split raw and device access as well)



If we base our image i/o on afflib, we get all three with one interface.
[RB](user:rb.md) Instead of letting the tools use afflib, better
to write an afflib module for carvfs, and update the libewf module. The
tool could than be oblivious of the file format. [Rob J
Meijer](user:capibara.md)



[Simsong](user:simsong.md) 06:29, 3 November 2008 (UTC) The
problem with using carvfs is that this adds another dependency. Do you
really want to require that people install carvfs in order to run the
carver? What about having the thing ported to Windows?



[Rob J Meijer](user:capibara.md) I would support adding one
build dependency (libcarvpath) and removing two (libewf/libaff) by
moving them to a layer more suited for them (carvfs) that would possibly
allow some form of file handle (as cap) based POLA design. I am a
proponent of making small things that do one and do one thing right, and
to stack those to do what you need. In my view that would lead ideally
to the following (simplified) chain:

- recursive [computer forensics
  framework](computer_forensics_framework.md)
  - <b>The-(pola-based)-carving-tool</b>
    - <b>The-carving-lib</b> working on open fd's.
      - libcarvpath
        - carvfs (Over cifs/nfs-v4 on platforms that don't support
          Fuse).
          - libewf
          - libaff
    - AppArmor (on supporting platforms)
    - suid (on supporting platforms)
    - iptables/ipfw (on supporting platforms)

As fow windows support, I would imagine making carvfs run over smb would
come a long way, that is for as far as windows support is all that
relevant.

There are two advantages to using libcarvpath and carvfs instead of
libaff/libewf t this layer:

- storage requirements for doing carving. Beyond what sleuthkit or
  alternatives provide I have seen many situations where carving was not
  done due to storage limitations.
- File handles are like object capabilities. You can often do pretty
  simple POLA based implementations using file handles and something
  like AppArmor. POLA could IMHO be a strong weapon against the more
  nasty forms of anti forensics.

Next to this, I would consider making different tools for different
stages instead of one semi recursive one, and looking at how to
integrate these tools into existing frameworks (ocfa/pyflag).

Keep things simple but rigid and try to easily integrate things into
existing frameworks as effectively as possible I would suggest.

Please note, I am not ptoposing the lib/tool should be useless without
libcarvpath, only that usage without carvfs should limit the

supported image formats to raw images, and that libewf/libaff should be
abstracted at the Fuse level or below and not at the tool level.


[Joachim](user:joachim_metz.md) do you have an idea what the
performance impact of this approach would be? It might be wise to do a
proof of concept for this approach first.


[Rob J Meijer](user:capibara.md) It would I think depend greatly on behavior of
the carving lib/tool. Small 512 byte reads are relatively very expensive, 128kb
reads have negligible impact. There are some numbers from ntfs-3g that might be
relevant. More relevant than performance might be library footprint. For
example, using OCFA, we often would want to keep e few hundred images that
total to tens of TB of projected storage size fuse mounted. If libewf/libaff
have a big combined memory footprint in such cases, this can be a major issue
for this approach.

[Joachim](user:joachim_metz.md) this layer should support multi
threaded decompression of compressed image types, this speeds up IO

- [Joachim](user:joachim_metz.md) volume/partition aware layer
  (what about carving unpartioned space)
- File system aware layer. This could be or make use of tsk-cp.
  - By default, files are not carved. (clarify: only identified?
    [RB](user:rb.md); I guess that it operates like [Selective
    file dumper](selective_file_dumper.md)
    [.FUF](user:.fuf.md).
    Alternatively, the tool could use libcarvpath and output carvpaths
    or create a directory with symlinks to carvpaths that point into a
    carvfs mountpoint [Rob J Meijer](user:capibara.md).
- Plug-in architecture for identification/validation.
  - [Joachim](user:joachim_metz.md) support for multiple types
    of validators
    - dedicated validator
    - validator based on file library (i.e. we could specify/implement a
      file structure API for these)
    - configuration based validator (Can handle config files,like
      Revit07, to enter different file formats used by the carver.)

[Joachim](user:joachim_metz.md) Moderator: Could we limit the
requirements for prototype version 1 of the tool to get a working
version up and running ASAP? And keep discussing future options?

I think the following set will be large enough to handle: Input
facilities

- IO support (AFF, device, EWF, RAW and split RAW)



Abstraction of input format and multi threaded decompression (spin-off
code out of afflib?)

- Volume/Partitions support



at least for DOS based layout and GPT (spin-off code out of
TSK/Photorec?)

- File system support



VFAT/NTFS (spin-off code out of TSK/Photorec?)

Carving facilities

- File format support using plug-able validator model (use dedicated
  validators Photorec/Scarve and/or wrap revit07 file format as
  validator?)
- Content support using plug-able validator model (to handle text/mbox
  base64)
- File system carving support (to handle file system fragments, could be
  linked to file system support layer?)
- Basic fragment handling

Output facilities

- audit/analysis/debug log
- extraction of result files

## Supported File Formats

Ship with validators for



[Joachim](user:joachim_metz.md) I think we should distinguish
between file format validators and content validators

- Grapical Images
  - JPEG (the 3 different types with JFIF/EXIF support)



[Joachim](user:joachim_metz.md) How different is JPEG 2000?

- - PNG
  - GIF
  - BMP
  - TIFF

- Office documents
  - Microsoft Office 97 - 2003 [OLE Compound
    File](ole_compound_file.md) format based with [Word Document
    (doc)](word_document_(doc).md) and [Excel Spreadsheet
    (xls)](excel_spreadsheet_(xls).md) file format support
  - [PDF](pdf.md)
  - Open Office and Microsoft Office 2007 [ZIP
    archive](zip.md) based file formats



Extension validation? AFAIK, MS Office 2007 [Word Document
(docx)](word_document_(docx).md) format uses plain ZIP (or
not?), and carved files will (or not?) have .zip extension instead of
DOCX. Is there any way to fix this (may be using the file list in zip)?
[.FUF](user:.fuf.md)

[Joachim](user:joachim_metz.md) Addition: Office 2007 also has a
binary file format which is also a ZIP-ed data [Excel Spreadsheet
(xlsb)](excel_spreadsheet_(xlsb).md)

- Archive files
- [ZIP archive](zip.md) file format
  - 7z
  - tar, gzip, bzip2
  - RAR
- E-mail files
  - [Personal Folder File (PAB, PST,
    OST)](personal_folder_file_(pab,_pst,_ost).md)
  - MBOX (text based format, base64 content support)
- Audio/Video files
  - MPEG
  - MP2/MP3
  - AVI
  - ASF/WMV
  - QuickTime
  - MKV
- Printer spool files
  - EMF (if I remember correctly)
- Internet history files
  - index.dat
  - firefox (sqllite 3)
- Other files
  - thumbs.db which also is an [OLE Compound
    File](ole_compound_file.md) based format
  - pagefile?

## Carving Strategies

[Joachim](user:joachim_metz.md) Note to moderator could this
section be merged with the carving algorithm section?

- Simple fragment recovery carving using gap carving.
  - [Joachim](user:joachim_metz.md) have hook in for more
    advanced fragment recovery?
- Recovering of individual ZIP sections and JPEG icons that are not
  sector aligned.
  - [Joachim](user:joachim_metz.md) I would propose a generic
    fragment detection and recovery
- Autonomous operation (some mode of operation should be completely
  non-interactive, requiring no human intervention to complete
  [RB](user:rb.md))
  - [Joachim](user:joachim_metz.md) as much as possible, but
    allow to be overwritten by user
- [Joachim](user:joachim_metz.md) When the tool output files the
  filenames should contain the offset in the input data (in
  hexadecimal?)



Mark Stam: I really like the fact carved files
are named after the physical or logical sector in which the file is
found (photorec)



[Joachim](user:joachim_metz.md) This naming schema might cause
duplicate name problem for extracting embedded files and extracting
files from non sector aligned file systems.

- [Joachim](user:joachim_metz.md) Should the tool allow to
  export embedded files?
- [Joachim](user:joachim_metz.md) Should the tool allow to
  export fragments separately?
- Mark Stam: I personally use photorec often for
  carving files in the whole volume (not only unallocated clusters), so
  I can store information about all potential interesting files in MySQL



[Joachim](user:joachim_metz.md) interesting, Bas Kloet and me
have been discussing to use information about allocated files in the
recovery process, i.e. recovered fragments could be part of allocated
files. Do we want to be able to extract them? Or could we rebuild the
file from the fragments and the allocated files.

- Mark Stam: It would also be nice if the files
  can be hashed immediately (MD5) so looking for them in other tools
  (for example Encase) is a snap

## Performance Requirements

- Tested on 500GB-sized images. Should be able to carve a 500GB image in
  roughly 50% longer than it takes to read the image.
  - Perhaps allocate a percentage budget per-validator (i.e. each
    validator adds N% to the carving time) [RB](user:rb.md)
  - [Joachim](user:joachim_metz.md) have multiple carving phases
    for precision/speed trade off?
- Parallelizable
  - [Joachim](user:joachim_metz.md) tunable for different
    architectures
- Configuration:
  - Capability to parse some existing carvers' configuration files,
    either on-the-fly or as a one-way converter.
  - Disengage internal configuration structure from configuration files,
    create parsers that present the expected structure
  - [Joachim](user:joachim_metz.md) The validator should deal
    with the file structure the carving algorithm should not know
    anything about the file structure (as in revit07 design)
  - Either extend Scalpel/Foremost syntaxes for extended features or use
    a tertiary syntax ([Joachim](user:joachim_metz.md) I would
    prefer a derivative of the revit07 configuration syntax which
    already has encountered some problems of dealing with defining file
    structure in a configuration file)

## Output

- Can output audit.txt file.
- [Joachim](user:joachim_metz.md) Can output database with
  offset analysis values i.e. for visualization tooling
- [Joachim](user:joachim_metz.md) Can output debug log for
  debugging the algorithm/validation
- Easy integration into ascription software.



[Joachim](user:joachim_metz.md) I'm no native speaker what do
you mean with "ascription software"?


I think this was another non-native requesting easy scriptability.
[RB](user:rb.md) 14:20, 31 October 2008 (UTC)


[Joachim](user:joachim_metz.md) that makes sense ;-)


Incorrect. Ascription software is software that determines who the owner
of a file is. [Simsong](user:simsong.md) 06:36, 3 November 2008
(UTC)

# Ideas

- Use as much TSK if possible. Don't carry your own FS implementation
  the way photorec does.



[Joachim](user:joachim_metz.md) using TSK as much as possible
would not allow to add your own file system support (i.e. mobile phones,
memory structures, cap files) I would propose wrapping TSK and using it
as much as possible but allow to integrate own FS implementations.



[Rob J Meijer](user:capibara.md) I'm currently working on
wrapping TSK filesystem as several loadable modules for OCFA. In OCFA a
loadable (tree-graph) module implements the OCFA tree-graph API that
basically states 'everything is a tree-graph node'. Possibly you could
look at the OCFA treegraph API and module loading interface as an
example, or we could work together on changing the API and module
loading interface in such a way that it doesn't break OCFA and is
usefull for the stand alone carver, but allowing both to use exactly the
same tree-graph loadable modules.

- Extracting/carving data from [Thumbs.db](thumbs.db.md)? I've
  used [foremost](foremost.md) for it with some success.
  [Vinetto](vinetto.md) has some critical bugs :(
  [.FUF](user:.fuf.md)
- Extracting/carving executable binaries, dlls etc.
  [Volatility](volatility_framework.md), JE.

## Recursive Carving

[Joachim](joachim_metz.md) do we want to support (let's
call it) 'recursive in file carving' (for now) this is different from
embedded files because there is a file system structure in the file and
not just another file structure

- Is it just me, or do a lot of the above (and below) ideas somewhat
  skirt around the fact that many of us want recursive carving? Can we
  bend back to that instead of discussing object particulars? I think
  this can be distilled down to three requirements:
  - Simple recursion: once an object is identified, have the ability to
    re-carve it for internal structures
  - Directed recursion: the carver should be able to be directed at
    arbitrary blobs and told to carve it as a specified type. This
    allows programmatically more simple methods of dealing with
    unidentifiably compressed or encrypted data. Or filesystem
    fragments.
  - Export: the ability to export an object (recognized or not) for
    later or external "recursion". Should go without saying for a
    carver, but...


--[RB](user:rb.md) 18:45, 2 November 2008 (UTC)


[Simsong](user:simsong.md) 06:30, 3 November 2008 (UTC) pyflag
already does recursive carving. Are we just going to reimplement pyflag
as a single executable?


[Joachim](user:joachim_metz.md) that could be useful ;-)

## Library Dependencies

[Rob J Meijer](user:capibara.md) :

- Use libcarvpath whenever possible and by default to avoid high storage
  requirements.



[Joachim](user:joachim_metz.md) For easy deployment I would not
opt for making an integral part of the tool solely dependant on a single
external library or the library must be integrated in the package

[Rob J Meijer](user:capibara.md) Integrating libraries
(libtsk,libaff.libewf,libcarvpath etc) is bad practice, autotools are
your friend IMO.

[Joachim](user:joachim_metz.md) I'm not talking about
integrating (shared) libraries. I'm talking about that an integral part
of a tool should be part of it's package. Why can't the tool package
contain shared or static libraries for local use? A far worse thing to
do is to have a large set of dependencies and making the tool difficult
to install for most users. The tool package should contain the most
necessary code. afflib/libewf support could be detected by the autotools
a neat separation of functionality.


From a packager's standpoint, [Joachim](user:joachim_metz.md)'s
other libraries do a really good job of this, carrying around what they
need but using a system-global version if available.
[RB](user:rb.md)

- libtsk
- libaff ? : possibly the discussion in the requirements section should
  move to his section.
- libewf ? : possibly the discussion in the requirements section should
  move to his section.
- posix ? : Can we depend especially on the availability of UNIX domain
  sockets and the possibility to use msg_accrights for passing opn file
  handles as ocaps?

## Filesystem Detection

- Dont stop with filesystem detection after the first match. Often if a
  partition is reused with a new FS and is not all that full yet, much
  of the old FS can still be valid. I have seen this with ext2/fat. The
  fact that you have identified a valid FS on a partition doesn't mean
  there isn't an(almost) valid second FS that would yield additional
  files. Identifying doubly allocated space might in some cases also be
  relevant.



[Joachim](user:joachim_metz.md) What your saying is that dealing
with file system fragments should be part of the carving algorithm

- Allow use where filesystem based carving is done by other tool, and
  the tool is used as second stage on (sets of) unallocated block
  (pseudo) files and/or non FS partition (pseudo) files.



[Joachim](user:joachim_metz.md) I would not opt for this. The
tool would be dependent on other tools and their data format, which
makes the tool difficult to maintain. I would opt to integrate the
functionality of having multiple recovery phases (stages) and allow the
tooling to run the phases after one and other or separately.

[Rob J Meijer](user:capibara.md) More generically, I feel a way
should exist to communicate the 'left overs' a previous (non open, for
example LE-only) tool left.

[Joachim](user:joachim_metz.md) I guess if the tool is designed
to handle multiple phases it should store its data somewhere. So it
should be possible to convert results of such non open tooling to the
format required. However I would opt to design the recovery
functionality of these non-open tools into open tools. And not to limit
ourselves making translators due to the design of these non-open tools.

- Ability to be used as a library instead of a tool. Ability to access
  metadata true library, and thus the ability to set metadata from the
  carving modules. This would be extremely usefull for integrating the
  project into a [computer forensics
  framework](computer_forensics_framework.md) .



[Joachim](user:joachim_metz.md) I guess most of the code could
be integrated into libraries, but I would not opt integrating tool
functionality into a library

- Mark Stam: I think it would be very handy to
  have a CSV, TSV, XML or other delimited output (log)file with
  information about carved files. This output file can then be stored in
  a database or Excel sheet (report function)

## Anti forensics and system integrity concerns

- It might be very interesting to look at the possibilities of using a
  multi process style of module support and combine it with a least
  authority design. On platforms that support AppArmor (or similar) and
  uid based firewall rules, this could make for the first true POLA
  (principle of least authority) based forensic tool ever. POLA based
  forensics tools should make for a strong integrity guard against many
  anti forensics. Alternatively we could look at integrating a
  capability secure language (E?) for implementation of at least
  validation modules. I don't expect this idea to make it, but
  mentioning it I hope might spark off less strong alternatives that at
  least partially address the integrity + anti-forensics problem. If we
  can in some way introduce POLA to a wider forensics public, other
  tools might also pick up on it what would be great.



[Joachim](user:joachim_metz.md) Could you give an example of how
you see this in action?



[Rob J Meijer](user:capibara.md) I see two layers where using
POLA could be applied. The best one would require one of the folowing as
prerequisites:

- The libaff/libewf layer is moved to a fuse implementation (for example
  carvfs).
- Libewf/Libaff are updated to accept opened filhandles instead of
  demanding to open their own files.

If one of these is fulfilled, than the tool running as some user can
just have the simple task of opening the image files, starting up the
'real' tool and handing over the appropriate file handles. If the real
tool runs with a restrictive AppArmor profile, and is started suid to a
tool specific user that also has its own iptables uid based filter, than
the real tool will run with least authority.

A second alternative, if neither of the first prerequisite could not be
bet, would be to run the modules as confined processes and have a non
confined process run as proxy for the first.

A third probably far fetched alternative would be to embed an object
capability language in the tool and make the module interface thus that
modules are to be written in this ocap language.

A 4th alternative might include minorfs or plash, but I havn't geven
those sufficient thinking hours yet.

## Format syntax specification

- Carving data structures. For example, extract all TCP headers from
  image by defining TCP header structure and some fields (e.g. source
  port \> 1024, dest port = 80). This will extract all data matching the
  pattern and write a file with other fields. Another example is carving
  INFO2 structures and URL activity records from index.dat
  [.FUF](user:.fuf.md)
  - This has the opportunity to be extended to the concept of "point at
    blob FOO and interpret it as BAR"

.FUF added: The main idea is to allow users to define structures, for
example (in pascal-like form):

    Field1: Byte = 123;
    SomeTextLength: DWORD;
    SomeText: string[SomeTextLength];
    Field4: Char = 'r';
    ...

This will produce something like this:

    Field1 = 123
    SomeTextLength = 5
    SomeText = 'abcd1'
    Field4 = 'r'

(In text or raw forms.)

Opinions?

Opinion: Simple pattern identification like that may not suffice, I
think Simson's original intent was not only to identify but to allow for
validation routines (plugins, as the original wording was). As such, the
format syntax would need to implement a large chunk of some programming
language in order to be sufficiently flexible. [RB](user:rb.md)

[Joachim](user:joachim_metz.md) In my option your example is too
limited. Making the revit configuration I learned you'll need a near
programming language to specify some file formats. A simple descriptive
language is too limiting. I would also go for 2 bytes with endianess
instead of using terminology like WORD and small integer, it's much more
clear. The configuration also needs to deal with aspects like
cardinality, required and optional structures.



This is simply data structures carving, see ideas above. Somebody (I
cannot track so many changes per day) separated the original text. There
is no need to count and join different structures.
[.FUF](user:.fuf.md)



[Joachim](user:joachim_metz.md) This was probably me is the text
back in it's original form?

I started it by moving your Revit07 comment to the validator/plugin section
since I was still at that point thinking operational configuration for that
section, not parser configurations. [RB](user:rb.md)

[Joachim](user:joachim_metz.md) I renamed the title to format
syntax, clarity is important ;-)

Please take a look at the revit07 format syntax specification
(configuration). It's not there yet but goes a far way. Some things
currently missing:

- bitwise alignment
- handling encapsulated streams (MPEG/capture files)
- handling content based formats (MBOX)

# Caving algorithm

[Joachim](user:joachim_metz.md)

- should we allow for multiple carving phases (runs/stages)?



I opt yes (separation of concern)

- should we allow for multiple carving algorithms?



I opt yes, this allows testing of different approaches

- Should the algorithm try to do as much in 1 run over the input data?
  To reduce IO?



I opt that the tool should allow for multiple and single run over the
input data to minimize the IO or the CPU as bottleneck

- Interaction between algorithm and validators
  - does the algorithm passes data blocks to the validators?
  - does a validator need to maintain a state?
  - does a validator need to revert a state?
  - How do we deal with embedded files and content validation? Do the
    validators call another validator?
- do we use the assumption that a data block can be used by a single
  file (with the exception of embedded/encapsulated files)?
- Revit07 allows for multiple concurrent result files states to deal
  with fragmentation. One has the attribute of being active (the
  preferred) and the other passive. Do we want/need something similar?
  The algorithm adds block of input data (offsets) to these result files
  states.
  - if so what info would these result files states require (type, list
    of input data blocks)
- how do we deal with file system remainders?
  - Can we abstract them and compare them against available file system
    information?
- Do we carve file systems in files?



I opt that at least the validator uses this information

## Caving scenarios

[Joachim](user:joachim_metz.md)

- normal file (file structure, loose text based structure (more a
  content structure?))
- fragmented file (the file entirely exist)
- a file fragment (the file does not entirely exist)
- intertwined file
- encapsulated file (MPEG/network capture)
- embedded file (JPEG thumbnail)
- obfuscation ('encrypted' PFF) this also entails encryption and/or
  compression
- file system in file

# File System Awareness

## Background: Why be File System Aware?

Advantages of being FS aware:

- You can pick up sector allocation sizes



[Joachim](user:joachim_metz.md) do you mean file system block
sizes?

- Some file systems may store things off sector boundaries. (ReiserFS
  with tail packing)
- Increasingly file systems have compression (NTFS compression)



[Joachim](user:joachim_metz.md) Carving NTFS-compressed (lznt1)
files: https://github.com/libyal/documentation/blob/main/Carving%20for%20NTFS%20compressed%20files.pdf

- Carve just the sectors that are not in allocated files.



[Joachim](user:joachim_metz.md) sparse (file system) blocks e.g.
NTFS cluster blocks

## Tasks that would be required

## Discussion



As noted above, TSK should be utilized as much as possible, particularly
the filesystem-aware portion. If we want to identify filesystems outside
of its supported set, it would be more worth our time to work on
implementing them there than in the carver itself.
[RB](user:rb.md)

<!-- -->



I guess this tool operates like [Selective file
dumper](selective_file_dumper.md) and can recover files in both
ways (or not?). Recovering files by using carving can recover files in
situations where sleuthkit does nothing (e.g. file on NTFS was deleted
using ntfs-3g, or filesystem was destroyed or just unknown). And we
should build the list of filesystems supported by carver, not by TSK.
[.FUF](user:.fuf.md)

<!-- -->



This tool is still in the early planning stages (requirements
discovery), hence few operational details (like precise modes of
operation) have been fleshed out - those will and should come later. The
justification for strictly using TSK for the filesystem-sensitive
approach is simple: TSK has good filesystem APIs, and it would be
foolish to create yet another standalone, incompatible implementation of
filesystem(foo) when time would be better spent improving those in TSK,
aiding other methods of analysis as well. This is the same reason
individuals that have implemented several other carvers are
participating: de-duplication of effort. [RB](user:rb.md)

<!-- -->



[Joachim](user:joachim_metz.md) A design problem might be that
TSK currently is a single library operating on multiple layers (storage
media IO, volume/partition analysis and file system analysis). I'm not
aware how easily the parts can be used separately. But I estimate that
for the carver we want to use these 3 layers differently than TSK
currently does.

[Joachim](user:joachim_metz.md) I would like to have the carver
(recovery tool) also do recovery using file allocation data or
remainders of file allocation data.

[Joachim](user:joachim_metz.md) I would go as far to ask you all
to look beyond the carver as a tool and look from the perspective of the
carver as part of the forensic investigation process. In my eyes certain
information needed/acquired by the carver could be also very useful
investigative information i.e. what part of a hard disk contains empty
sectors.

# Supportive tooling

[Joachim](user:joachim_metz.md)

- validator (definitions) tester (detest in revit07)
- tool to make configuration based definitions
- post carving validation
- the carver needs to provide support for fuse mount of carved files
  (carvfs)

# Testing

[Joachim](user:joachim_metz.md)

- automated testing
- test data

# Validator Construction

Options:

- Write validators in C/C++
  - [Joachim](user:joachim_metz.md) you mean dedicated
    validators
- Have a scripting language for writing them (python? Perl?) our own?
  - [Joachim](user:joachim_metz.md) use easy to embed
    programming languages i.e. Phyton or Lua
- Use existing programs (libjpeg?) as plug-in validators?
  - [Joachim](user:joachim_metz.md) define a file structure api
    for this

# Existing Code that we have

[Joachim](user:joachim_metz.md) Please add any missing links

Documentation/Articles

- DFRWS2006/2007 carving challenge results
- DFRWS2008 paper on carving

Carvers

- DFRWS2006/2007 carving challenge results
- photorec (http://www.cgsecurity.org/wiki/PhotoRec)
- revit06 and revit07 (https://github.com/libyal/reviveit)
- s3/scarve

Possible file structure validator libraries

- divers existing file support libraries
- libole2 (inhouse experimental code of OLE2 support)
- [libnk2](libnk2.md)
- [libpff](libpff.md)

Input support

- AFF (http://www.afflib.org/)
- [libewf](libewf.md)
- TSK device & raw & split raw (http://www.sleuthkit.org/)

Volume/Partition support

- disktype (http://disktype.sourceforge.net/)
- testdisk (http://www.cgsecurity.org/wiki/TestDisk)
- TSK

File system support

- TSK
- photorec FS code
- implementations of FS in Linux/BSD
- The tree-graph loadable module support, module loader and loadable
  modules of the Open Computer Forensics Architecture.

Content support

Zero storage support

- libcarvpath (
  <https://sourceforge.net/project/showfiles.php?group_id=170249&package_id=210704>
  )
- carvfs (
  <https://sourceforge.net/project/showfiles.php?group_id=170249&package_id=210954>
  )
- tsk-cp (
  <https://sourceforge.net/project/showfiles.php?group_id=170249&package_id=267227>
  )
- carvfsmodewf
  (https://sourceforge.net/project/showfiles.php?group_id=170249&package_id=268256
  )

POLA

- joe-e (java) ( <http://code.google.com/p/joe-e/> )
- Emily (ocaml) ( <http://erights.org/download/emily/> )
- the E language ( <http://www.erights.org/> )
- AppArmor
- iptables/ipfw
- minorfs ( <http://polacanthus.net/minorfs.html> )

# Implementation Timeline

1.  gather the available resources/ideas/wishes/needs etc. (I guess
    we're in this phase)
2.  start discussing a high level design (in terms of algorithm,
    facilities, information needed)
    1.  input formats facility
    2.  partition/volume facility
    3.  file system facility
    4.  file format facility
    5.  content facility
    6.  how to deal with fragment detection (do the validators allow for
        fragment detection?)
    7.  how to deal with recombination of fragments
    8.  do we want multiple carving phases in light of speed/precision
        tradeoffs
3.  start detailing parts of the design
    1.  Discuss options for a grammar driven validator?
    2.  Hard-coded plug-ins?
    3.  Which existing code can we use?
4.  start building/assembling parts of the tooling for a prototype
    1.  Implement simple file carving with validation.
    2.  Implement gap carving
5.  Initial Release
6.  Implement the *threaded carving* that [.FUF](user:.fuf.md)
    is describing above.

[Joachim](user:joachim_metz.md) Shouldn't multi threaded carving
(MTC) not be part of the 1st version? The MT approach makes for
different design decisions


It is virtually impossible to turn a non-MT application into an MT
application .[Simsong](user:simsong.md) 06:37, 3 November 2008
(UTC)

