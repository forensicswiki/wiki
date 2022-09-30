---
tags:
  -  Bibliographies
---
Analysis of [physical memory](physical_memory.md) from
[Windows](windows.md) systems can yield significant information
about the target operating system. This field is still very new, but
holds great promise.

## Data types

Data types typical to the WINAPI are documented by Microsoft in MS-DTYP
[1](http://msdn.microsoft.com/en-us/library/cc230273.aspx).

## Sample Memory Images

Getting started with memory analysis can be difficult without some known
images to practice with.

- The 2005 [Digital Forensic Research
  Workshop](digital_forensic_research_workshop.md) [Memory
  Analysis Challenge](http://www.dfrws.org/2005/challenge/) published
  two Windows 2000 Service Pack 1 memory images with some
  [malware](malware.md) installed.

<!-- -->

- The [Digital Forensics Tool Testing](http://dftt.sourceforge.net/)
  project has published a few [Windows memory
  images](http://dftt.sourceforge.net/test13/index.html).

<!-- -->

- The [CFReDS Project](cfreds_project.md) has created some
  [downloadable memory
  images](http://www.cfreds.nist.gov/mem/memory-images.rar).

<!-- -->

- A number of RAM images can be downloaded from
  <http://forensic.belkasoft.com/bfs/en/download.asp>. Images include
  ones with Gmail emails, Skype activity, Paltalk chats, browser URLs
  etc.

## See Also

- [Memory analysis](memory_analysis.md)
- [Tools:Memory Imaging](tools:memory_imaging.md)
- [Pagefile.sys](pagefile.sys.md)
- [Memory Limits for Windows
  Releases](http://msdn.microsoft.com/en-us/library/aa366778%28VS.85%29.aspx),
  Microsoft MSDN.

## History

During the 1990s, it became a [best practice](best_practice.md)
to capture a [memory image](tools:memory_imaging.md) during
[incident response](incident_response.md). At the time, the only
way to analyze such memory images was using
[strings](strings.md). Although this method could reveal
interesting details about the memory image, there was no way to
associate what data came from what program, let alone what user.

In the summer 2005 the [Digital Forensic Research
Workshop](digital_forensic_research_workshop.md) published a
*Memory Analysis Challenge*. They distributed two memory images and
asked researchers to answer a number of questions about a security
incident. The challenge produced two seminal works. The first, by [Chris
Betz](chris_betz.md), introduced a tool called
[memparser](memparser.md). The second, by [George
Garner](george_garner.md) and [Robert-Jan
Mora](robert-jan_mora.md) produced
[KnTList](kntlist.md).

At the [Blackhat Federal](blackhat_(conference).md) conference
in March 2007, [AAron Walters](aaron_walters.md) and [Nick
Petroni](nick_petroni.md) released a suite called
[volatools](volatools.md). Although it only worked on [Windows
XP](windows_xp.md) Service Pack 2 images, it was able to produce
a number of useful data. [volatools](volatools.md) was updated
and re-released as [Volatility](volatility.md) in August 2007,
and is now maintained and distributed by [Volatile
Systems](https://www.volatilesystems.com/).

## Bibliography

2012

- [Defeating Windows memory
  forensics](http://events.ccc.de/congress/2012/Fahrplan/events/5301.en.html),
  by Luka Milkovic, 29C3: 29th Chaos Communication Congress

2011

- [Tracking Stuxnet's Footprint Through
  Memory](http://prezi.com/goocmfeuiqdf/tracking-stuxnets-footprint-through-memory/),
  Michael Ligh, Open Memory Forensics Workshop

2010

- [Extracting Windows Command Line Details from Physical
  Memory](http://dfrws.org/2010/proceedings/2010-307.pdf), Richard
  Stevens and Eoghan Casey, DFRWS

2009

- [Robust Signatures for Kernel Data
  Structures](http://www.cc.gatech.edu/~brendan/ccs09_siggen.pdf) B.
  Dolan-Gavitt, et al., ACM Conference on Computer and Communications
  Security
- [Win32dd : Challenges of Windows physical memory acquisition and
  exploitation](http://www.shakacon.org/talks/NFI-Shakacon-win32dd0.3.pdf),
  Matthieu Suiche, Netherlands Forensics Institute, Shakacon - June 2009

2008

- [Lest We Remember: Cold Boot Attacks on Encryption
  Keys](http://citp.princeton.edu/memory/)
  ([PDF](http://citp.princeton.edu.nyud.net/pub/coldboot.pdf)), Usenix
  Security 2008 (Best student paper)
- [Pushing the Limits of Windows: Physical
  Memory](http://blogs.technet.com/markrussinovich/archive/2008/07/21/3092070.aspx),
  Mark Russinovich, Technet Blogs, July 21, 2008
- [The impact of Microsoft Windows pool allocation strategies on memory
  forensics](http://www.dfrws.org/2008/proceedings/p58-schuster.pdf),
  Andreas Schuster, DFRWS 2008
  [\[slides](http://www.dfrws.org/2008/proceedings/p58-schuster_pres.pdf)\]
- [Finding Digital Evidence In Physical
  Memory](http://www.blackhat.com/presentations/bh-federal-06/BH-Fed-06-Burdach/bh-fed-06-burdach-up.pdf),
  Mariusz Burdach, Black Hat Federal, 2008
- [Forensic Memory Analysis: Files mapped in
  memory](http://www.dfrws.org/2008/proceedings/p52-vanBaar.pdf), Ruud
  van Baar, DFRWS 2008,
  [\[slides](http://www.dfrws.org/2008/proceedings/p52-vanBaar_pres.pdf)\]
- [Forensic Analysis of the Windows Registry in
  Memory](http://www.dfrws.org/2008/proceedings/p26-dolan-gavitt.pdf),
  Brendan Dolan-Gavitt, DFRWS 2008
  [\[slides](http://www.dfrws.org/2008/proceedings/p26-dolan-gavitt_pres.pdf)\]

2007

- [Beyond The CPU: Defeating Hardware Based RAM Acquisition (part I: AMD
  case)](http://www.first.org/conference/2007/papers/rutkowska-joanna-slides.pdf),
  Joanna Rutkowska COSEINC Advanced Malware Labs
- [Forensic Memory Analysis: From Stack and Code to Execution
  History](http://www.dfrws.org/2007/proceedings/p114-arasteh.pdf), Ali
  Reza Arasteh and Mourad Debbabi, DFRWS 2007
- [BodySnatcher: Towards Reliable Volatile Memory Acquisition by
  Software](http://www.dfrws.org/2007/proceedings/p126-schatz.pdf),
  Bradley Schatz, DFRWS 2007
- [The VAD Tree: A Process-Eye View of Physical
  Memory](http://www.dfrws.org/2007/proceedings/p62-dolan-gavitt.pdf),
  Brendan F Dolan-Gavitt, DFRWS 2007
- [FireWire Memory Dump of a Windows XP Computer: A Forensic
  Approach](http://www.friendsglobal.com/papers/FireWire%20Memory%20Dump%20of%20Windows%20XP.pdf),
  Antonio Martin, 2007

2006

- [Searching for Processes and Threads in Microsoft Windows Memory
  Dumps](http://www.dfrws.org/2006/proceedings/2-Schuster.pdf), Andreas
  Schuster, Deutsche Telekom AG, Germany, DFRWS 2006
- Using every part of the buffalo in Windows memory an, Jesse D.
  Kornblum, DFRWS 2006

## External Links

- [NTAPI Undocumented Functions](http://undocumented.ntinternals.net/)
- [MS-DTYP: Windows Data
  Types](http://msdn.microsoft.com/en-us/library/cc230273.aspx)
- [Catalog of key Windows kernel data
  structures](http://www.codemachine.com/article_kernelstruct.html)
- [Jesse Kornblum Memory Analysis discussion on
  Cyberspeak](http://cyberspeak.libsyn.com/index.php?post_id=98104)
- [Fatkit: Links](http://www.4tphi.net/fatkit/#links)
- [Kernel Debugging with
  WinDbg](http://www.cmlab.csie.ntu.edu.tw/~cathyp/eBooks/WindowsNT/Driver/kernel_debugging_tutorial.pdf)
- [Attacking the Windows
  kernel](https://www.blackhat.com/presentations/bh-usa-07/Lindsay/Whitepaper/bh-usa-07-lindsay-WP.pdf),
  by Jonathan Lindsay, BlackHat 2007
- [The VAD tree: A process-eye view of physical
  memory](http://dfrws.org/2007/proceedings/p62-dolan-gavitt.pdf), by
  [Brendan Dolan-Gavitt](brendan_dolan-gavitt.md), DFRWS 2007
- [Malware Analysis Tutorial 7: Exploring Kernel Data
  Structure](http://fumalwareanalysis.blogspot.ch/2011/12/malware-analysis-tutorial-7-exploring.html),
  by Dr. Fu, December 14, 2011
- [Windows Virtual Address Translation and the
  Pagefile](http://rekall-forensic.blogspot.com/2014/10/windows-virtual-address-translation-and.html),
  by [Michael Cohen](michael_cohen.md), October 31, 2014

### Kernel debugging

- [Advanced Windows
  Debugging](http://advancedwindowsdebugging.com/book/contents.htm), by
  Mario Hewardt, Daniel Pravat, November 8, 2007
- [Advanced Windows Debugging: Memory Corruption Part
  II—Heaps](http://www.informit.com/articles/article.aspx?p=1081496), by
  Daniel Pravat and Mario Hewardt, November 9, 2007
- [Finding Kernel Global Variables in
  Windows](http://moyix.blogspot.ch/2008/04/finding-kernel-global-variables-in.html),
  by Brendan Dolan-Gavitt, April 16, 2008
- [Finding the Kernel Debugger
  Block](http://scudette.blogspot.com/2012/11/finding-kernel-debugger-block.html),
  by Michael Cohen, November 18, 2012
- [Do we need the Kernel Debugging
  Block?](http://rekall-forensic.blogspot.ch/2014/02/do-we-need-kernel-debugging-block.html),
  by Michael Cohen, February 21, 2014

### [Volatility Labs](http://volatility-labs.blogspot.com/)

- [MoVP 1.1 Logon Sessions, Processes, and
  Images](http://volatility-labs.blogspot.com/2012/09/movp-11-logon-sessions-processes-and.html)
- [MoVP 1.2 Window Stations and Clipboard
  Malware](http://volatility-labs.blogspot.com/2012/09/movp-12-window-stations-and-clipboard.html)
- [MoVP 1.3 Desktops, Heaps, and
  Ransomware](http://volatility-labs.blogspot.com/2012/09/movp-13-desktops-heaps-and-ransomware.html)
- [MoVP 2.1 Atoms (The New Mutex), Classes and DLL
  Injection](http://volatility-labs.blogspot.com/2012/09/movp-21-atoms-new-mutex-classes-and-dll.html)
- [MoVP 2.2 Malware In Your
  Windows](http://volatility-labs.blogspot.com/2012/09/movp-22-malware-in-your-windows.html)
- [MoVP 2.3 Event Logs and Service
  SIDs](http://volatility-labs.blogspot.com/2012/09/movp-23-event-logs-and-service-sids.html)
- [MoVP 3.1 Detecting Malware Hooks in the Windows GUI
  Subsystem](http://volatility-labs.blogspot.com/2012/09/movp-31-detecting-malware-hooks-in.html)
- [HowTo: Scan for Internet Cache/History and
  URLs](http://volatility-labs.blogspot.com/2012/09/howto-scan-for-internet-cachehistory.html)
- [MoVP 3.2 Shellbags in Memory, SetRegTime, and TrueCrypt
  Volumes](http://volatility-labs.blogspot.com/2012/09/movp-32-shellbags-in-memory-setregtime.html)
- [MoVP 3.3 Analyzing USER Handles and the Win32k.sys
  Gahti](http://volatility-labs.blogspot.com/2012/09/movp-33-analyzing-user-handles-and.html)
- [MoVP 3.4: Recovering tagCLIPDATA: What's In Your
  Clipboard?](http://volatility-labs.blogspot.com/2012/09/movp-34-recovering-tagclipdata-whats-in.html)
- [MoVP 4.1 Detecting Malware with GDI Timers and
  Callbacks](http://volatility-labs.blogspot.com/2012/10/movp-41-detecting-malware-with-gdi.html)
- [MoVP 4.2 Taking Screenshots from Memory
  Dumps](http://volatility-labs.blogspot.com/2012/10/movp-43-taking-screenshots-from-memory.html)
- [MoVP 4.4 Cache Rules Everything Around
  Me(mory)](http://volatility-labs.blogspot.com/2012/10/movp-44-cache-rules-everything-around.html)
- [OMFW 2012: Malware In the Windows GUI
  Subsystem](http://volatility-labs.blogspot.com/2012/10/omfw-2012-malware-in-windows-gui.html)
- [OMFW 2012: Reconstructing the MBR and MFT from
  Memory](http://volatility-labs.blogspot.com/2012/10/omfw-2012-reconstructing-mbr-and-mft.html)
- [OMFW 2012: The Analysis of Process Token
  Privileges](http://volatility-labs.blogspot.com/2012/10/omfw-2012-analysis-of-process-token.html)
- [OMFW 2012: Mining the PFN Database for Malware
  Artifacts](http://volatility-labs.blogspot.com/2012/10/omfw-2012-mining-pfn-database-for.html)

### WinDBG

- [Getting Started with WinDBG - Part
  1](http://blog.opensecurityresearch.com/2013/12/getting-started-with-windbg-part-1.html),
  by [Brad Antoniewicz](brad_antoniewicz.md), December 17, 2013
- [Getting Started with WinDBG - Part
  2](http://blog.opensecurityresearch.com/2013/12/getting-started-with-windbg-part-2.html),
  by [Brad Antoniewicz](brad_antoniewicz.md), December 24, 2013
- [Getting Started with WinDBG - Part
  3](http://blog.opensecurityresearch.com/2013/12/getting-started-with-windbg-part-3.html),
  by [Brad Antoniewicz](brad_antoniewicz.md), December 31, 2013
- [Developing WinDbg ExtEngCpp Extension in C++ – Introduction – Part
  1](http://www.msuiche.net/2014/01/12/extengcpp-part-1/), by [Matt
  Suiche](matt_suiche.md), January 12, 2014
- [Developing WinDbg ExtEngCpp Extension in C++ – COM Interface – Part
  2](http://www.msuiche.net/2014/01/15/developing-windbg-extengcpp-extension-in-c-com-interface/),
  by [Matt Suiche](matt_suiche.md), January 15, 2014
- [Developing WinDbg ExtEngCpp Extension in C++ – Memory & Debugger
  Markup Language (DML) – Part
  3](http://www.msuiche.net/2014/01/20/developing-windbg-extengcpp-extension-in-c-memory-debugger-markup-language-dml-part-3/),
  by [Matt Suiche](matt_suiche.md), January 20, 2014
- [SwishDbgExt - Incident Response & Digital Forensics Debugging
  Extension](https://github.com/msuiche/SwishDbgExt)

[Category:Bibliographies](category:bibliographies.md)
