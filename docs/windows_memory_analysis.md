---
tags:
  - Bibliographies
---
Analysis of [physical memory](physical_memory.md) from
[Windows](windows.md) systems can yield significant information
about the target operating system. This field is still very new, but
holds great promise.

## Data types

Data types typical to the WINAPI are documented by Microsoft in MS-DTYP
[1](https://learn.microsoft.com/en-us/openspecs/windows_protocols/ms-dtyp/cca27429-5689-4a16-b2b4-9325d93e4ba2).

## Sample Memory Images

Getting started with memory analysis can be difficult without some known
images to practice with.

* The 2005 [DFRWS: Memory Analysis Challenge](https://github.com/dfrws/dfrws2005-challenge)
  published two Windows 2000 Service Pack 1 memory images with some malware
  installed.
* The [Digital Forensics Tool Testing](https://dftt.sourceforge.net/)
  project has published a few [Windows memory images](https://dftt.sourceforge.net/test13/index.html).
* The CFReDS Project has created some
  [downloadable memory images](https://cfreds.nist.gov/mem/memory-images.rar).
* A number of RAM images can be downloaded from
  <https://belkasoft.com/x>. Images include
  ones with Gmail emails, Skype activity, Paltalk chats, browser URLs
  etc.

## See Also

* [Memory analysis](memory_analysis.md)
* [Tools:Memory Imaging](tools_memory_imaging.md)
* [Pagefile.sys](pagefile.sys.md)
* [Memory Limits for Windows Releases](https://learn.microsoft.com/en-us/windows/win32/memory/memory-limits-for-windows-releases),
  Microsoft MSDN.

## History

During the 1990s, it became a best practice
to capture a [memory image](tools_memory_imaging.md) during
[incident response](incident_response.md). At the time, the only
way to analyze such memory images was using
[strings](strings.md). Although this method could reveal
interesting details about the memory image, there was no way to
associate what data came from what program, let alone what user.

In the summer 2005 the [Digital Forensic Research Workshop](digital_forensic_research_workshop.md)
published a *Memory Analysis Challenge*. They distributed two memory images and
asked researchers to answer a number of questions about a security incident.
The challenge produced two seminal works. The first, by Chris Betz,
introduced a tool called memparser. The second, by [George Garner](george_garner.md)
and Robert-Jan Mora produced KnTList.

At the [Blackhat Federal](blackhat_(conference).md) conference in March 2007,
[AAron Walters](aaron_walters.md) and [Nick Petroni](nick_petroni.md) released
a suite called Volatools. Although it only worked on Windows XP Service Pack 2
images, it was able to produce a number of useful data. Volatools was updated
and re-released as Volatility in August
2007, and is now maintained and distributed by [Volatile Systems](https://www.volatilesystems.com/).

## Bibliography

2012

* [Defeating Windows memory forensics](https://fahrplan.events.ccc.de/congress/2012/Fahrplan/events/5301.en.html),
  by Luka Milkovic, 29C3: 29th Chaos Communication Congress

2011

* [Tracking Stuxnet's Footprint Through Memory](https://prezi.com/goocmfeuiqdf/tracking-stuxnets-footprint-through-memory/),
  by Michael Ligh, Open Memory Forensics Workshop

2010

* [Extracting Windows Command Line Details from Physical Memory](https://www.sciencedirect.com/science/article/pii/S1742287610000356),
  by Richard Stevens and Eoghan Casey, DFRWS

2009

* [Robust Signatures for Kernel Data Structures](https://sites.cc.gatech.edu/~brendan/ccs09_siggen.pdf)
  by B.  Dolan-Gavitt, et al., ACM Conference on Computer and Communications
  Security
* [Win32dd : Challenges of Windows physical memory acquisition and exploitation](http://www.shakacon.org/talks/NFI-Shakacon-win32dd0.3.pdf),
  by Matthieu Suiche, Netherlands Forensics Institute, Shakacon - June 2009

2008

* [Lest We Remember: Cold Boot Attacks on Encryption Keys](https://citp.princeton.edu/our-work/memory/),
  Usenix Security 2008 (Best student paper)
* [Pushing the Limits of Windows: Physical Memory](https://learn.microsoft.com/en-us/archive/blogs/markrussinovich/),
  by Mark Russinovich, Technet Blogs, July 21, 2008
* [The impact of Microsoft Windows pool allocation strategies on memory forensics](https://dfrws.org/presentation/the-impact-of-microsoft-windows-pool-allocation-strategies-on-memory-forensics/),
  by Andreas Schuster, DFRWS 2008
* [Finding Digital Evidence In Physical Memory](https://www.blackhat.com/presentations/bh-federal-06/BH-Fed-06-Burdach/bh-fed-06-burdach-up.pdf),
  by Mariusz Burdach, Black Hat Federal, 2008
* [Forensic Memory Analysis: Files mapped in memory](https://dfrws.org/presentation/forensic-memory-analysis-files-mapped-in-memory/),
  by Ruud van Baar, DFRWS 2008
* [Forensic Analysis of the Windows Registry in Memory](https://dfrws.org/presentation/forensic-analysis-of-the-windows-registry-in-memory/),
  by Brendan Dolan-Gavitt, DFRWS 2008

2007

* [Beyond The CPU: Defeating Hardware Based RAM Acquisition (part I: AMD case)](https://www.first.org/conference/2007/papers/rutkowska-joanna-slides.pdf),
  by Joanna Rutkowska COSEINC Advanced Malware Labs
* [Forensic Memory Analysis: From Stack and Code to Execution History](https://www.sciencedirect.com/science/article/pii/S1742287607000485),
  by Ali Reza Arasteh and Mourad Debbabi, DFRWS 2007
* [BodySnatcher: Towards Reliable Volatile Memory Acquisition by Software](https://www.sciencedirect.com/science/article/pii/S1742287607000497),
  by Bradley Schatz, DFRWS 2007
* [The VAD Tree: A Process-Eye View of Physical Memory](https://dfrws.org/sites/default/files/session-files/2007_USA_paper-the_vad_tree_-_a_process-eye_view_of_physical_memory.pdf),
  by Brendan F Dolan-Gavitt, DFRWS 2007
* [FireWire Memory Dump of a Windows XP Computer: A Forensic Approach](http://www.friendsglobal.com/papers/FireWire%20Memory%20Dump%20of%20Windows%20XP.pdf),
  by Antonio Martin, 2007

2006

* [Searching for Processes and Threads in Microsoft Windows Memory Dumps](https://dfrws.org/sites/default/files/session-files/2006_USA_pres-searching_for_processes_and_threads_in_microsoft_windows_memory_dumps.pdf),
  by Andreas Schuster, Deutsche Telekom AG, Germany, DFRWS 2006
* [Using every part of the buffalo in Windows memory](https://www.sciencedirect.com/science/article/abs/pii/S1742287607000047),
  by Jesse D.  Kornblum, DFRWS 2006

## External Links

* [NTAPI Undocumented Functions](http://undocumented.ntinternals.net/)
* [MS-DTYP: Windows Data Types](https://learn.microsoft.com/en-us/openspecs/windows_protocols/ms-dtyp/cca27429-5689-4a16-b2b4-9325d93e4ba2)
* [Catalog of key Windows kernel data structures](http://www.codemachine.com/article_kernelstruct.html)
* [Jesse Kornblum Memory Analysis discussion on Cyberspeak](https://cyberspeak.libsyn.com/index.php?post_id=98104)
* [Kernel Debugging with WinDbg](http://www.cmlab.csie.ntu.edu.tw/~cathyp/eBooks/WindowsNT/Driver/kernel_debugging_tutorial.pdf)
* [Attacking the Windows kernel](https://www.blackhat.com/presentations/bh-usa-07/Lindsay/Whitepaper/bh-usa-07-lindsay-WP.pdf),
  by Jonathan Lindsay, BlackHat 2007
* [Malware Analysis Tutorial 7: Exploring Kernel Data Structure](http://fumalwareanalysis.blogspot.com/2011/12/malware-analysis-tutorial-7-exploring.html),
  by Dr. Fu, December 14, 2011
* [Windows Virtual Address Translation and the Pagefile](http://blog.rekall-forensic.com/2014/10/windows-virtual-address-translation-and.html),
  by [Michael Cohen](michael_cohen.md), October 31, 2014

### Kernel debugging

* [Advanced Windows Debugging](http://survey-smiles.com), by
  Mario Hewardt, Daniel Pravat, November 8, 2007
* [Advanced Windows Debugging: Memory Corruption Part II—Heaps](https://www.informit.com/articles/article.aspx?p=1081496), by
  Daniel Pravat and Mario Hewardt, November 9, 2007
* [Finding Kernel Global Variables in Windows](https://moyix.blogspot.com/2008/04/finding-kernel-global-variables-in.html),
  by Brendan Dolan-Gavitt, April 16, 2008
* [Finding the Kernel Debugger Block](http://scudette.blogspot.com/2012/11/finding-kernel-debugger-block.html),
  by Michael Cohen, November 18, 2012
* [Do we need the Kernel Debugging Block?](http://blog.rekall-forensic.com/2014/02/do-we-need-kernel-debugging-block.html),
  by Michael Cohen, February 21, 2014

### [Volatility Labs](https://volatility-labs.blogspot.com/)

* [MoVP 1.1 Logon Sessions, Processes, and Images](https://volatility-labs.blogspot.com/2012/09/movp-11-logon-sessions-processes-and.html)
* [MoVP 1.2 Window Stations and Clipboard Malware](https://volatility-labs.blogspot.com/2012/09/movp-12-window-stations-and-clipboard.html)
* [MoVP 1.3 Desktops, Heaps, and Ransomware](https://volatility-labs.blogspot.com/2012/09/movp-13-desktops-heaps-and-ransomware.html)
* [MoVP 2.1 Atoms (The New Mutex), Classes and DLL Injection](https://volatility-labs.blogspot.com/2012/09/movp-21-atoms-new-mutex-classes-and-dll.html)
* [MoVP 2.2 Malware In Your Windows](https://volatility-labs.blogspot.com/2012/09/movp-22-malware-in-your-windows.html)
* [MoVP 2.3 Event Logs and Service SIDs](https://volatility-labs.blogspot.com/2012/09/movp-23-event-logs-and-service-sids.html)
* [MoVP 3.1 Detecting Malware Hooks in the Windows GUI Subsystem](https://volatility-labs.blogspot.com/2012/09/movp-31-detecting-malware-hooks-in.html)
* [HowTo: Scan for Internet Cache/History and URLs](https://volatility-labs.blogspot.com/2012/09/howto-scan-for-internet-cachehistory.html)
* [MoVP 3.2 Shellbags in Memory, SetRegTime, and TrueCrypt Volumes](https://volatility-labs.blogspot.com/2012/09/movp-32-shellbags-in-memory-setregtime.html)
* [MoVP 3.3 Analyzing USER Handles and the Win32k.sys Gahti](https://volatility-labs.blogspot.com/2012/09/movp-33-analyzing-user-handles-and.html)
* [MoVP 3.4: Recovering tagCLIPDATA: What's In Your Clipboard?](https://volatility-labs.blogspot.com/2012/09/movp-34-recovering-tagclipdata-whats-in.html)
* [MoVP 4.1 Detecting Malware with GDI Timers and Callbacks](https://volatility-labs.blogspot.com/2012/10/movp-41-detecting-malware-with-gdi.html)
* [MoVP 4.2 Taking Screenshots from Memory Dumps](https://volatility-labs.blogspot.com/2012/10/movp-43-taking-screenshots-from-memory.html)
* [MoVP 4.4 Cache Rules Everything Around Me(mory)](https://volatility-labs.blogspot.com/2012/10/movp-44-cache-rules-everything-around.html)
* [OMFW 2012: Malware In the Windows GUI Subsystem](https://volatility-labs.blogspot.com/2012/10/omfw-2012-malware-in-windows-gui.html)
* [OMFW 2012: Reconstructing the MBR and MFT from Memory](https://volatility-labs.blogspot.com/2012/10/omfw-2012-reconstructing-mbr-and-mft.html)
* [OMFW 2012: The Analysis of Process Token Privileges](https://volatility-labs.blogspot.com/2012/10/omfw-2012-analysis-of-process-token.html)
* [OMFW 2012: Mining the PFN Database for Malware Artifacts](https://volatility-labs.blogspot.com/2012/10/omfw-2012-mining-pfn-database-for.html)

### WinDBG

* [SwishDbgExt - Incident Response & Digital Forensics Debugging Extension](https://github.com/comaeio/SwishDbgExt)
