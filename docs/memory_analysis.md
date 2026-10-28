---
tags:
  - Analysis Techniques
  - Memory Analysis
---
Memory analysis is the practice of determining information about running programs, the
[operating system](operating_system.md), and the overall state of a computer from a
[memory image](memory_imaging.md).

While volatile memory acquisition provides a critical, real-time snapshot of running processes,
network connections, and decrypted credentials, it remains just one piece of a comprehensive
investigation. Overarching forensic methodologies must actively account for the inherent
shortcomings of memory analysis, such as the risk of data smearing during live acquisition, the
transient nature of volatile data, and anti-forensic techniques designed to evade detection.

Relying solely on RAM analysis creates dangerous blind spots; therefore, sound investigative
frameworks must seamlessly integrate memory artifacts with traditional disk forensics, network
logs, and timeline analysis to ensure findings are defensible, validated, and holistic.

Memory analysis, by its nature, is highly dependent on the operating system, most of its techniques
are described on the per-platform pages:

* [Linux Memory Analysis](linux_memory_analysis.md)
* [Windows Memory Analysis](windows_memory_analysis.md)

This article describes the techniques that apply across platforms:

* reading [data types](#data-types) in memory
* [framework-based](#memory-analysis-frameworks)
* [OS independent](#os-independent-analysis) analysis
* [encryption key](#encryption-keys) extraction
* recovering [browser, e-mail and instant messenger](#browser-and-email-artifacts) artifacts from
  memory.

The tools used to apply these techniques are gathered in
[Memory analysis tools](tools_memory_analysis.md).

## Data types

Per <https://en.wikipedia.org/wiki/Integer_(computer_science)>:

> Different programming languages provide different primitive data types,
> e.g. in C it is common to have "char", "int", "long", "float", "double".
> The size of these primitive data types is dependent on multiple factors
> like the CPU, the programming language, the compiler, etc.

Per <https://en.wikipedia.org/wiki/64-bit_computing>:

> on a 64-bit system the size of an "int" can vary based on the data-model

**Note that some memory analysis resources and tools are known to completely disregard this aspect
of 64-bit computing and claim incorrectly an integer is always 32-bit on 64-bit systems or claim
the size of the integer is operating system dependent.**

Per <https://en.wikipedia.org/wiki/Endianness>:

> When reading primitive data types from a byte stream the endianness specifies how the least and
> most significant parts of the data are stored.

Composite data types (also referred to as data structures) consists of primitive and/or composite
data types.

When reading data structures from memory note that
[data structure alignment](https://en.wikipedia.org/wiki/Data_structure_alignment) can be applied.

### Character and string data types

Note that this subject could fill books by itself and the following information is a very brief
overview of some of the characteristics of character and string data types.

A programming language can distinguish between
[Unicode, non-Unicode and binary (or byte) strings](https://en.wikipedia.org/wiki/Primitive_data_type#Characters_and_strings).

* Unicode strings typically are stored in a [Transform format](https://en.wikipedia.org/wiki/UTF)
  * There are multiple versions of Unicode
  * A predecessor to Unicode is the [Universal Character Set (UCS)](https://en.wikipedia.org/wiki/Universal_Character_Set)
* non-Unicode strings can be stored in various encodings e.g. ASCII
  [8](https://en.wikipedia.org/wiki/Character_encoding)
  * typical the encoding is identified by a codepage e.g. for CP1252 for
    Windows [9](https://en.wikipedia.org/wiki/Windows_code_page)
  * In Windows the supported set of non-Unicode strings is referred to
    as ANSI-strings, which is technically incorrect but a too widely
    used term to be ignored.
  * In other texts or contexts non-Unicode strings can be referred to as
    extended ASCII or ASCII with codepage strings, which, dependent on
    the context, can also be technically incorrect since non-Unicode
    strings can be stored in non-ASCII methods as well, e.g. EBIDIC or
    the codepage in which the string is stored has no historical
    relation to ASCII.
  * There are multiple variants of non-Unicode strings sometimes divided
    in single byte character (SBC) and multi byte character (MBC)
    strings. **Note that character here refers to the primitive data
    type used, not a textual character of the string.**
* Binary strings can contain bit- or byte streams. Since bitstreams are
  often stored in bytes the endianness of the bits within the byte is
  relevant when reading or writing the string.

Another distinction made in some programming languages is to have a default (or narrow) character
type, e.g. in C "char", and a separate wide character type, e.g. in C "wchar_t". The "wchar_t" is
typically associated with Unicode strings. **Note that this should be taken as a very loose
association, since the "char" can be used to store Unicode strings in UTF-8 and wchar_t can be used
to store non-Unicode strings.** The typical size of char is 8-bits where the MSB is the sign bit.
The typical size of wchar_t varies per "platform", e.g. it is common to see wchar_t to be 32-bit of
size on Linux with gcc and 16-bit of size on Windows with MSC.

## Memory analysis frameworks

Most memory analysis is done through a framework -
[Volatility](volatility_framework.md) is the leading example - which
pairs generic analysis plugins with **profiles** that describe the
data structures of a specific operating system and version. Because a
plugin is written against the profile rather than against one
particular system, the same analysis can be applied to images of many
operating systems, and the results - processes, handles, network
connections, encryption keys - are comparable across systems.

See also [Volatility Framework](volatility_framework.md), [Rekall
profiles](rekall_profiles.md), [List of Volatility
plugins](list_of_volatility_plugins.md) and [Memory analysis
tools: memory analysis
frameworks](tools_memory_analysis.md#memory-analysis-frameworks).

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

See also [Platform independent
tools](tools_memory_analysis.md#platform-independent-tools).

## Encryption Keys

Various types of encryption keys can be extracted during memory
analysis, including symmetric keys such as [AES](aes.md) keys,
asymmetric keys such as RSA private and public keys, and passphrases
for [TrueCrypt](truecrypt.md) volumes.

See also [List of Volatility
plugins](list_of_volatility_plugins.md) and [Memory analysis
tools: memory analysis
frameworks](tools_memory_analysis.md#memory-analysis-frameworks).

## Browser and email artifacts

Web-mail and e-mail clients keep session state in memory - message
bodies, attachments and account data - that may never be written to
disk, and that can be recovered from a memory image even when the
on-disk store is unavailable or corrupted.

See also [Memory analysis tools: browser and email
artifacts](tools_memory_analysis.md#browser-and-email-artifacts).

## Instant messenger artifacts

Instant messenger clients cache conversations, contacts and account
information in memory, and those artifacts can be recovered from a
memory image without contacting the messaging service.

See also [Memory analysis tools: instant messenger
artifacts](tools_memory_analysis.md#instant-messenger-artifacts).

## Memory analysis support

Executables extracted from memory are generally left in a state that
cannot be executed, diffed, or hash-validated: their relocations are
not yet applied, so they must be restored to their original state
before comparison or verification is meaningful.

See also [Memory analysis tools: memory
support](tools_memory_analysis.md#memory-analysis-support).

## See Also

* [Memory Imaging](memory_imaging.md)
* [Memory Imaging Tools](tools_memory_imaging.md)
* [Memory Analysis Tools](tools_memory_analysis.md)
* [Linux Memory Analysis](linux_memory_analysis.md)
* [Storage-class memory](storage_class_memory.md)
* [Virtualization Memory Analysis](virtualization_memory_analysis.md)
* [Windows Memory Analysis](windows_memory_analysis.md)

### Rekall Forensics blog

* [Rekall profiles](rekall_profiles.md)
* [The Rekall Profile Repository and Profile Auto-selection](rekall_profile_repository_and_profile_auto_selection.md)
* [Do we need the Kernel Debugging Block?](rekall_do_we_need_the_kernel_debugging_block.md)
* [How to stop memory acquisition by changing one byte](rekall_how_to_stop_memory_acquisition_by_changing_one_byte.md)
* [Mac OS X 10.9 Memory Acquisition](rekall_osx_10_9_memory_acquisition.md)
* [New Rekall Plugin: Mac Compressed Memory](rekall_plugin_mac_compressed_memory.md)
* [VM discovery and introspection with Rekall](rekall_vm_discovery_and_introspection.md)
* [Windows Virtual Address Translation and the Pagefile](rekall_windows_virtual_address_translation_and_the_pagefile.md)
* [The Windows User mode heap and the DNS resolver cache](rekall_windows_user_mode_heap_and_dns_resolver_cache.md)
* [Rekall NTFS Support](rekall_ntfs_support.md)
* [The Pmem Memory acquisition suite](rekall_pmem_memory_acquisition_suite.md)
* [Adding Rekall's Windows 10 Support](rekall_adding_windows_10_support.md)
* [Windows Virtual Address Translation - Part 2](rekall_windows_virtual_address_translation_part_2.md)
* [XEN ParaVirtualization support in Rekall](rekall_xen_paravirtualization_support.md)
* Draft: [Accurately determining the profile of a running operating system](rekall_determining_the_profile_of_the_operating_system.md)
* [The pmem suite of memory acquisition tools](pmem_suite_of_memory_acquisition_tools.md)
* [Rekall and the Windows PFN database](rekall_and_the_windows_pfn_database.md)
* [Searching memory with Rekall](rekall_searching_memory.md)
* [The Rekall Agent Whitepaper](rekall_agent_whitepaper.md)
* [ELF hacking with Rekall](rekall_elf_hacking.md)
* [Virtual Secure Mode and memory acquisition](rekall_virtual_secure_mode_and_memory_acquisition.md)

## External Links

* [YobiWiki: RAM analysis](https://wiki.yobi.be/index.php/Main_Page)
* [RAM is Key - Extracting Disk Encryption Keys From Volatile Memory](https://cryptome.org/0003/RAMisKey.pdf),
  by Brian Kaplan, May 2007
* [Forensics Examination of Volatile System Data Using Virtual Introspection](https://dl.acm.org/doi/10.1145/1368506.1368517),
  by Brian Hay and Kara Nance, 2008
* [An Evaluation Platform for Forensic Memory Acquisition Software](https://dfrws.org/presentation/an-evaluation-platform-for-forensic-memory-acquisition-software/),
  by Stefan Voemel and Johannes Stuettgen, DFRWS 2013

### Anti-forensics

* [Integrating Volatile Memory Forensics into the Digital Investigation Process](https://www.blackhat.com/presentations/bh-dc-07/Walters/Paper/bh-dc-07-Walters-WP.pdf),
  by [AAron Walters](aaron_walters.md), Nick Petroni, Blackhat 2007
* Forensic Analysis of Anti-Forensic Activities,
  by Jack Crook, January 29, 2014
* [ADD: The Next Big Threat To Memory Forensics....Or Not](https://volatility-labs.blogspot.com/2014/02/add-next-big-threat-to-memory.html),
  by Michael Hale Ligh, February 3, 2014
* [Anti-forensics and memory analysis](http://scudette.blogspot.com/2014/02/anti-forensics-and-memory-analysis.html),
  by [Michael Cohen](michael_cohen.md), February 7, 2014
* [Memory Forensics: Still Aborted](http://takahiroharuyama.github.io/blog/2014/04/21/memory-forensics-still-aborted/),
  by Takahiro Haruyama, April 21, 2014

### Computer architecture

* [Wikipedia: 64-bit computing](https://en.wikipedia.org/wiki/64-bit_computing)
* [Intel® 64 and IA-32 Architectures Software Developer's Manual Volume 1: Basic Architecture](https://www.intel.com/content/www/us/en/content-details/782158/intel-64-and-ia-32-architectures-software-developer-s-manual-combined-volumes-1-2a-2b-2c-2d-3a-3b-3c-3d-and-4.html),
  by Intel, May 2011
* [64-Bit Programming Models: Why LP64?](https://unix.org/version2/whatsnew/lp64_wp.html),
  The Open Group, 1997

### Data types

* [Wikipedia: Primitive data type](https://en.wikipedia.org/wiki/Primitive_data_type)
* [Wikipedia: Integer](https://en.wikipedia.org/wiki/Integer_(computer_science))
* [Wikipedia: 64-bit computing](https://en.wikipedia.org/wiki/64-bit_computing)
* [Wikipedia: Endianness](https://en.wikipedia.org/wiki/Endianness)
* [Chapter 4. Programming with Cygwin](https://cygwin.com/cygwin-ug-net/programming.html)
* [Wikipedia: Data structure alignment](https://en.wikipedia.org/wiki/Data_structure_alignment)
* [Type Systems](https://lucacardelli.name/Papers/TypeSystems.pdf),
  by Luca Cardelli

### [Volatility Labs](https://volatility-labs.blogspot.com/)

* [MoVP 1.4 Average Coder Rootkit, Bash History, and Elevated Processes](https://volatility-labs.blogspot.com/2012/09/movp-14-average-coder-rootkit-bash.html)
* [MoVP 1.5 KBeast Rootkit, Detecting Hidden Modules, and sysfs](https://volatility-labs.blogspot.com/2012/09/movp-15-kbeast-rootkit-detecting-hidden.html)
* [MoVP 2.4 Analyzing the Jynx rootkit and LD_PRELOAD](https://volatility-labs.blogspot.com/2012/09/movp-24-analyzing-jynx-rootkit-and.html)
* [MoVP 2.5: Investigating In-Memory Network Data with Volatility](https://volatility-labs.blogspot.com/2012/09/movp-25-investigating-in-memory-network.html)
* [MoVP 3.5: Analyzing the 2008 DFRWS Challenge with Volatility](https://volatility-labs.blogspot.com/2012/09/movp-35-analyzing-2008-dfrws-challenge.html)
* [MoVP 4.2 Taking Screenshots from Memory Dumps](https://volatility-labs.blogspot.com/2012/10/movp-43-taking-screenshots-from-memory.html)
* [MoVP 4.3 Recovering Master Boot Records (MBRs) from Memory](https://volatility-labs.blogspot.com/2012/10/movp-43-recovering-master-boot-records.html)
* [Phalanx 2 Revealed: Using Volatility to Analyze an Advanced Linux Rootkit](https://volatility-labs.blogspot.com/2012/10/phalanx-2-revealed-using-volatility-to.html)
* [Solving the GrrCon Network Forensics Challenge with Volatility](https://volatility-labs.blogspot.com/2012/10/solving-grrcon-network-forensics.html)
* [OMFW 2012: Analyzing Linux Kernel Rootkits with Volatility](https://volatility-labs.blogspot.com/2012/10/omfw-2012-analyzing-linux-kernel.html)
* [OMFW 2012: Datalore: Android Memory Analysis](https://volatility-labs.blogspot.com/2012/10/omfw-2012-datalore-android-memory.html)
* [MoVP for Volatility 2.2 and OMFW 2012 Wrap-Up](https://volatility-labs.blogspot.com/2012/10/movp-for-volatility-22-and-omfw-2012.html)
* [Reverse Engineering Poison Ivy's Injected Code Fragments](https://volatility-labs.blogspot.com/2012/10/reverse-engineering-poison-ivys.html)
* [TrueCrypt Master Key Extraction And Volume Identification](https://volatility-labs.blogspot.com/2014/01/truecrypt-master-key-extraction-and.html),
  by Michael Hale Ligh, January 14, 2014
