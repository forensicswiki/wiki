---
tags:
  - Analysis Techniques
  - Memory Analysis
---

**Memory Analysis** is the science of using a [memory
image](memory_imaging.md) to determine information about running
programs, the [operating system](operating_system.md), and the
overall state of a computer. Because the analysis is highly dependent on
the operating system, it has been divided into the following pages:

- [Linux Memory Analysis](linux_memory_analysis.md)
- [Windows Memory Analysis](windows_memory_analysis.md)

## Data types

Different programming languages provide different primitive data types,
e.g. in C it is common to have "char", "int", "long", "float", "double".
The size of these primitive data types is dependent on multiple factors
like the CPU, the programming language, the compiler, etc.
[1](https://en.wikipedia.org/wiki/Integer_(computer_science)) e.g. on
64-bit system the size of an "int" can vary based on the data-model
[2](https://en.wikipedia.org/wiki/64-bit_computing).

<b>Note that some memory analysis resources and tools are known to
completely disregard this aspect of 64-bit computing and claim
incorrectly an integer is always 32-bit on 64-bit systems or claim the
size of the integer is operating system dependent.</b>

When reading primitive data types from a byte stream the endianness
specifies how the least and most significant parts of the data are
stored [3](https://en.wikipedia.org/wiki/Endianness).

Composite data types (also referred to as data structures) consists of
primitive and/or composite data types.

When reading data structures from memory note that data structure
alignment [4](https://en.wikipedia.org/wiki/Data_structure_alignment) can
be applied.

### Character and string data types

Note that this subject could fill books by itself and the following
information is a very brief overview of some of the characteristics of
character and string data types.

A programming language can distinguish between Unicode, non-Unicode and
binary strings
[5](https://en.wikipedia.org/wiki/Primitive_data_type#Characters_and_strings).

- Unicode strings typically are stored in a Tranform format
  [6](https://en.wikipedia.org/wiki/UTF)
  - There are multiple versions of Unicode
  - A predecessor to Unicode is Universal Character Set (UCS)
    [7](https://en.wikipedia.org/wiki/Universal_Character_Set)
- non-Unicode strings can be stored in various encodings e.g. ASCII
  [8](https://en.wikipedia.org/wiki/Character_encoding)
  - typical the encoding is identified by a codepage e.g. for CP1252 for
    Windows [9](https://en.wikipedia.org/wiki/Windows_code_page)
  - In Windows the supported set of non-Unicode strings is referred to
    as ANSI-strings, which is technically incorrect but a too widely
    used term to be ignored.
  - In other texts or contexts non-Unicode strings can be referred to as
    extended ASCII or ASCII with codepage strings, which, dependent on
    the context, can also be technically incorrect since non-Unicode
    strings can be stored in non-ASCII methods as well, e.g. EBIDIC or
    the codepage in which the string is stored has no historical
    relation to ASCII.
  - There are multiple variants of non-Unicode strings sometimes divided
    in single byte character (SBC) and multi byte character (MBC)
    strings. <b>Note that character here refers to the primitive data
    type used, not a textual character of the string.</b>
- Binary strings can contain bit- or byte streams. Since bitstreams are
  often stored in bytes the endianess of the bits within the byte is
  relevant when reading or writing the string.

Another distinction made in some programming languages is to have a
default (or narrow) character type, e.g. in C "char", and a separate
wide character type, e.g. in C "wchar_t". The "wchar_t" is typically
associated with Unicode strings. <b>Note that this should be taken as a
very loose association, since the "char" can be used to store Unicode
strings in UTF-8 and wchar_t can be used to store non-Unicode
strings.</b> The typical size of char is 8-bits where the MSB is the
sign bit. The typical size of wchar_t varies per "platform", e.g. it is
common to see wchar_t to be 32-bit of size on Linux with gcc and 16-bit
of size on Windows with MSC.

## OS-Independent Analysis

At the IEEE Security and Privacy conference in May 2011, Brendan
Dolan-Gavitt presented a novel system,
[Virtuoso](https://sites.cc.gatech.edu/~brendan/Virtuoso_Oakland.pdf), that
was able to perform operating-system independent memory analysis. Using
virtual machine introspection accompanied by a number of formal program
analysis techniques, his system was able to monitor the machine-level
instructions and behavior of application actions (listing processes,
network connections, etc) and then automatically generate Volatility
plugins that replicated this analysis.

## Encryption Keys

Various types of encryption keys can be extracted during memory
analysis.

- AESKeyFinder extracts 128-bit and 256-bit [AES](aes.md) keys and RSAKeyFinder
  and private and public RSA keys from a memory dump [10](https://citp.princeton.edu/our-work/memory/code/).
- cryptoscan.py which is a [plugin for the Volatility framework](list_of_volatility_plugins.md),
  scans a memory image for [TrueCrypt](truecrypt.md) passphrases

## See Also

- [Memory Imaging](memory_imaging.md)
- [Memory Imaging Tools](tools_memory_imaging.md)
- [Memory Analysis Tools](tools_memory_analysis.md)
- [Linux Memory Analysis](linux_memory_analysis.md)
- [Storage-class memory](storage_class_memory.md)
- [Virtualization Memory Analysis](virtualization_memory_analysis.md)
- [Windows Memory Analysis](windows_memory_analysis.md)

### Assorted tools

- [Legilimency, a Memory Research Platform for iOS](https://github.com/google/Legilimency/)

## External Links

- [YobiWiki: RAM analysis](https://wiki.yobi.be/index.php/Main_Page)
- [RAM is Key - Extracting Disk Encryption Keys From Volatile Memory](https://cryptome.org/0003/RAMisKey.pdf),
  by Brian Kaplan, May 2007
- [Forensics Examination of Volatile System Data Using Virtual Introspection](https://dl.acm.org/doi/10.1145/1368506.1368517),
  by Brian Hay and Kara Nance, 2008
- [An Evaluation Platform for Forensic Memory Acquisition Software](https://dfrws.org/presentation/an-evaluation-platform-for-forensic-memory-acquisition-software/),
  by Stefan Voemel and Johannes Stuettgen, DFRWS 2013

### Anti-forensics

- [Integrating Volatile Memory Forensics into the Digital Investigation Process](https://www.blackhat.com/presentations/bh-dc-07/Walters/Paper/bh-dc-07-Walters-WP.pdf),
  by [AAron Walters](aaron_walters.md), [Nick Petroni](nick_petroni.md), Blackhat 2007
- Forensic Analysis of Anti-Forensic Activities,
  by Jack Crook, January 29, 2014
- [ADD: The Next Big Threat To Memory Forensics....Or Not](https://volatility-labs.blogspot.com/2014/02/add-next-big-threat-to-memory.html),
  by Michael Hale Ligh, February 3, 2014
- [Anti-forensics and memory analysis](http://scudette.blogspot.com/2014/02/anti-forensics-and-memory-analysis.html),
  by [Michael Cohen](michael_cohen.md), February 7, 2014
- [Memory Forensics: Still Aborted](http://takahiroharuyama.github.io/blog/2014/04/21/memory-forensics-still-aborted/),
  by Takahiro Haruyama, April 21, 2014

### Computer architecture

- [Wikipedia: 64-bit computing](https://en.wikipedia.org/wiki/64-bit_computing)
- [Intel® 64 and IA-32 Architectures Software Developer’s Manual Volume 1: Basic Architecture](https://www.intel.com/content/www/us/en/architecture-and-technology/64-ia-32-architectures-software-developer-vol-1-manual.html),
  by Intel, May 2011
- [64-Bit Programming Models: Why LP64?](https://unix.org/version2/whatsnew/lp64_wp.html),
  The Open Group, 1997

### Data types

- [Wikipedia: Primitive data type](https://en.wikipedia.org/wiki/Primitive_data_type)
- [Wikipedia: Integer](https://en.wikipedia.org/wiki/Integer_(computer_science))
- [Wikipedia: 64-bit computing](https://en.wikipedia.org/wiki/64-bit_computing)
- [Wikipedia: Endianness](https://en.wikipedia.org/wiki/Endianness)
- [Chapter 4. Programming with Cygwin](https://cygwin.com/cygwin-ug-net/programming.html)
- [Wikipedia: Data structure alignment](https://en.wikipedia.org/wiki/Data_structure_alignment)
- [Type Systems](http://lucacardelli.name/Papers/TypeSystems.pdf),
  by Luca Cardelli

### [Volatility Labs](https://volatility-labs.blogspot.com/)

- [MoVP 1.4 Average Coder Rootkit, Bash History, and Elevated Processes](https://volatility-labs.blogspot.com/2012/09/movp-14-average-coder-rootkit-bash.html)
- [MoVP 1.5 KBeast Rootkit, Detecting Hidden Modules, and sysfs](https://volatility-labs.blogspot.com/2012/09/movp-15-kbeast-rootkit-detecting-hidden.html)
- [MoVP 2.4 Analyzing the Jynx rootkit and LD_PRELOAD](https://volatility-labs.blogspot.com/2012/09/movp-24-analyzing-jynx-rootkit-and.html)
- [MoVP 2.5: Investigating In-Memory Network Data with Volatility](https://volatility-labs.blogspot.com/2012/09/movp-25-investigating-in-memory-network.html)
- [MoVP 3.5: Analyzing the 2008 DFRWS Challenge with Volatility](https://volatility-labs.blogspot.com/2012/09/movp-35-analyzing-2008-dfrws-challenge.html)
- [MoVP 4.2 Taking Screenshots from Memory Dumps](https://volatility-labs.blogspot.com/2012/10/movp-43-taking-screenshots-from-memory.html)
- [MoVP 4.3 Recovering Master Boot Records (MBRs) from Memory](https://volatility-labs.blogspot.com/2012/10/movp-43-recovering-master-boot-records.html)
- [Phalanx 2 Revealed: Using Volatility to Analyze an Advanced Linux Rootkit](https://volatility-labs.blogspot.com/2012/10/phalanx-2-revealed-using-volatility-to.html)
- [Solving the GrrCon Network Forensics Challenge with Volatility](https://volatility-labs.blogspot.com/2012/10/solving-grrcon-network-forensics.html)
- [OMFW 2012: Analyzing Linux Kernel Rootkits with Volatility](https://volatility-labs.blogspot.com/2012/10/omfw-2012-analyzing-linux-kernel.html)
- [OMFW 2012: Datalore: Android Memory Analysis](https://volatility-labs.blogspot.com/2012/10/omfw-2012-datalore-android-memory.html)
- [MoVP for Volatility 2.2 and OMFW 2012 Wrap-Up](https://volatility-labs.blogspot.com/2012/10/movp-for-volatility-22-and-omfw-2012.html)
- [Reverse Engineering Poison Ivy's Injected Code Fragments](https://volatility-labs.blogspot.com/2012/10/reverse-engineering-poison-ivys.html)
- [TrueCrypt Master Key Extraction And Volume Identification](https://volatility-labs.blogspot.com/2014/01/truecrypt-master-key-extraction-and.html),
  by Michael Hale Ligh, January 14, 2014
