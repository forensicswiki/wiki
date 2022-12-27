---
tags:
  -  Windows
  -  Articles that need to be expanded
---
Windows Prefetch files, introduced in [Windows XP](windows.md),
are designed to speed up the application startup process. Prefetch files
contain the name of the executable, a Unicode list of DLLs used by that
executable, a count of how many times the executable has been run, and a
timestamp indicating the last time the program was run. Although
Prefetch is present in Windows 2003, by default it is only enabled for
boot prefetching. The feature is also found in [Windows
Vista](windows.md), where it has been augmented with
[SuperFetch](superfetch.md), [ReadyBoot](readyboot.md),
and [ReadyBoost](readyboost.md).

From
\[<http://msdn.microsoft.com/en-us/library/windows/hardware/dn653317(v=vs.85>).aspx\]:

- [SuperFetch](superfetch.md); analyzes per-machine usage
  patterns over time and optimizes the data that is kept in memory.
- [ReadyBoot](readyboot.md); decreases boot time (the time from
  turning power on to reaching the log-on screen) by preloading the
  files and startup programs needed per-machine into a cache.
- [ReadyBoost](readyboost.md); supports the use of flash storage
  devices like Universal Serial Bus (USB) flash drives and Secure
  Digital (SD) flash cards to boost PC performance.
- ReadyDrive; supports hybrid hard disk drives.

For SSD drives Prefetch is disabled by default
[1](http://blogs.msdn.com/b/e7/archive/2009/05/05/support-and-q-a-for-solid-state-drives-and.aspx).

## Prefetch files

The Prefetch files are stored in the directory:

    %SystemRoot%\Prefetch

The following files can be found in the Prefetch directory:

- `*.pf`, which are Prefetch files;
- `Ag*.db` and `Ag*.db.trx`, which are
  [SuperFetch](superfetch.md) files;
- `Layout.ini`;
- `PfPre_*.db`;
- `PfSvPerfStats.bin`

A Prefetch file contains the name of the application, a dash, and then
an eight character hash of the location from which that application was
run, and a `.pf` extension. The filenames should be all uppercase except
for the extension. E.g. a filename for [md5deep](md5deep.md)
would look like: `MD5DEEP.EXE-4F89AB0C.pf`. If an application is run
from two different locations on the drive (i.e. the user runs
`C:\md5deep.exe` and then `C:\Apps\Hashing\md5deep.exe`), there will be
two different prefetch files in the Prefetch folder. According to MSDN
up to 128 Prefetch files can be stored in the Prefetch directory
[2](http://blogs.msdn.com/ryanmy/archive/2005/05/25/421882.aspx).

### File format

Each Prefetch file has a 4-byte signature (at offset 4) "SCCA" (or in
hexadecimal notation 0x53 0x43 0x43 0x41). The signature is assumed to
be preceded by a 4-byte format version indicator:

- 17 (0x00000011) for Windows XP and Windows 2003
- 23 (0x00000017) for [Windows Vista](windows_vista.md),
  Windows 2008, [Windows 7](windows_7.md) and Windows 2012
  (note Windows 2012 has not been confirmed)
- 26 (0x0000001a) for [Windows 8.1](windows_8.md) (note this
  could be Windows 8 as well but has not been confirmed)
- 30 (0x0000001e) for [Windows 10](windows_10.md)

For more information about the file format see: [Windows Prefetch File Format](windows_prefetch_file_format.md)

## Metadata

The Prefetch file contains various metadata.

- The executable's name, up to 29 characters.
- The run count, or number of times the application has been run.
- Volume related information, like volume path and volume serial number.
- The size of the Prefetch file (sometimes referred to as end of file
  (EOF)).
- The files and directories that were used doing the application's
  start-up.

### Timestamps

The Prefetch file contains 2 types of timestamps

- The time when the application was last ran (executed). Version 26 of
  the Prefetch format maintains 7 previous last run times.
- The volume creation time (part of the volume information) of the
  volume the Prefetch file was created on.

The file system creation time of the Prefetch file indicates the first
time the application was executed. Both the file system modification
time of the Prefetch file and the embedded last run time indicate the
last time the application was executed.

## Prefetch hash

There are multiple known hashing functions to be used for prefetch file
filename hashing, namely:

- SCCA XP hash function; used on Windows XP and Windows 2003
- SCCA Vista hash function; used on Windows Vista
- SCCA 2008 hash function; used on Windows 2008, Windows 7, (possibly:
  Windows 2012) and Windows 8 (including 8.1)

### SCCA XP hash function

A Python implementation of the SCCA XP hash function:

    def ssca_xp_hash_function(filename):
        hash_value = 0
        for character in filename:
            hash_value = ((hash_value * 37) + ord(character)) % 0x100000000
            hash_value = (hash_value * 314159269) % 0x100000000
            if hash_value > 0x80000000:
                hash_value = 0x100000000 - hash_value

        return (abs(hash_value) % 1000000007) % 0x100000000

### SCCA Vista hash function

A Python implementation of the SCCA Vista hash function:

    def ssca_vista_hash_function(filename):
        hash_value = 314159
        for character in filename:
            hash_value = ((hash_value * 37) + ord(character)) % 0x100000000
        return hash_value

### SCCA 2008 hash function

A Python implementation of the SCCA 2008 hash function:

    def ssca_2008_hash_function(filename):
        hash_value = 314159
        filename_index = 0
        filename_length = len(filename)
        while filename_index + 8 < filename_length:
            character_value = ord(filename[filename_index + 1]) * 37
            character_value += ord(filename[filename_index + 2])
            character_value *= 37
            character_value += ord(filename[filename_index + 3])
            character_value *= 37
            character_value += ord(filename[filename_index + 4])
            character_value *= 37
            character_value += ord(filename[filename_index + 5])
            character_value *= 37
            character_value += ord(filename[filename_index + 6])
            character_value *= 37
            character_value += ord(filename[filename_index]) * 442596621
            character_value += ord(filename[filename_index + 7])
            hash_value = ((character_value - (hash_value * 803794207)) % 0x100000000)
            filename_index += 8

        while filename_index < filename_length:
           hash_value = (((37 * hash_value) + ord(filename[filename_index])) % 0x100000000)
           filename_index += 1

        return hash_value

### /prefetch flag

From: [Misinformation and the The Prefetch
Flag](https://web.archive.org/web/20160714134633/https://blogs.msdn.microsoft.com/ryanmy/2005/05/25/misinformation-and-the-the-prefetch-flag/)

    The /prefetch:# flag is looked at by the OS when we create the process — however, it has one (and only one) purpose.  We add the passed number to the hash.

It appears that the following are equivalent on Windows 10 1903 and
2004:

- Notepad.exe
- Notepad.exe /prefetch:0
- Notepad.exe /prefetch:9

So that /prefetch:\[0-8\] only seem to be the supported values and the
/prefetch:9 and larger are equivalent to /prefetch:0

## Registry Keys

    Key: HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Control\Session Manager\Memory Management\PrefetchParameters

The EnablePrefetcher Registry value can be used to disable prefetch.

## See Also

- [Prefetch XML](prefetch_xml.md)
- [ReadyBoot](readyboot.md)
- [SuperFetch](superfetch.md)
- [Windows](windows.md)
- [Windows Prefetch File Format](windows_prefetch_file_format.md)

## External Links

- [Wikipedia Prefetcher](http://en.wikipedia.org/wiki/Prefetcher)
- \[<http://msdn.microsoft.com/en-us/library/ms940847(v=winembedded.5>).aspx
  MSDN: Disabling Prefetch\]
- [Windows XP: Kernel Improvements Create a More Robust, Powerful, and Scalable OS](http://msdn.microsoft.com/en-us/magazine/cc302206.aspx),
  by [Mark Russinovich](mark_russinovich.md), David Solomon, December 2001
- [Kernel Enhancements for Windows XP](http://www.microsoft.com/whdc/driver/kernel/XP_kernel.mspx), by
  [Microsoft](microsoft.md), January 13, 2003 (Microsoft's
  description of Prefetch when Windows XP was introduced)
- [Misinformation and the The Prefetch
  Flag](http://blogs.msdn.com/b/ryanmy/archive/2005/05/25/421882.aspx),
  MSDN Blogs, May 25, 2005
- [Prefetch file metadata](http://windowsir.blogspot.ch/2005/07/prefetch-file-metadata.html),
  by [Harlan Carvey](harlan_carvey.md), July 13, 2005
- [Prefetch files, revisited](http://windowsir.blogspot.ch/2006/04/prefetch-files-revisited.html),
  by [Harlan Carvey](harlan_carvey.md), April 13, 2006
- [Windows Memory Management](http://www.codeproject.com/Articles/29449/Windows-Memory-Management),
  by logicchild, September 17, 2008
- [Windows Memory Management - Part 2](http://www.codeproject.com/Articles/29692/Windows-Memory-Management-Part),
  by logicchild, September 25, 2008
- [Support and Q&A for Solid-State Drives](http://blogs.msdn.com/b/e7/archive/2009/05/05/support-and-q-a-for-solid-state-drives-and.aspx),
  by Steven Sinofsky, May 5, 2009
- [De-mystifying Defrag: Identifying When Defrag Has Been Used for Anti-Forensics (Part 1 - Windows XP)](http://computer-forensics.sans.org/blog/2009/08/05/de-mystifying-defrag-identifying-when-defrag-has-been-used-for-anti-forensics-part-1-windows-xp/),
  by Chad Tilbury, August 5, 2009
- [Windows Prefetch File (old blog entry from 42 LLC)](http://www.swiftforensics.com/2010/04/the-windows-prefetchfile.html),
  by Yogesh Khatri, April 14, 2010
- \[<http://msdn.microsoft.com/en-us/library/windows/hardware/dn653317(v=vs.85>).aspx
  Windows PC Accelerators\], by Microsoft, October 8, 2010
- [Decoding Prefetch Files for Forensic Purposes: Part 1](http://www.dfinews.com/articles/2010/12/decoding-prefetch-files-forensic-purposes-part-1),
  by Mark Wade, December 8, 2010
- [Prefetch Files at Face Value](http://crucialsecurityblog.harris.com/2011/04/11/prefetch-files-at-face-value/),
  by Mark Wade, April 11, 2011
- [Windows Logical Prefetcher](http://kitrap08.blogspot.hk/2011/07/windows-logical-prefetcher.html),
  TTS blog, July 30, 2011 (article is in Russian)
- [Prefetch i niedokładny licznik](http://labit.in/pliki-prefetch-w-windows/) by Paweł
  Hałdrzyński, August 20, 2011 (article in Polish; uncertain about the
  year of publication)
- [Prefetch Analysis, Revisited](http://windowsir.blogspot.ch/2012/03/prefetch-analysis-revisited.html),
  by [Harlan Carvey](harlan_carvey.md), March 8, 2012
- [Prefetch Analysis, Revisited...Again...](http://windowsir.blogspot.ch/2012/03/prefetch-analysis-revisitedagain.html),
  by [Harlan Carvey](harlan_carvey.md), March 15, 2012
- [Prefetch Hash Calculator + a hash lookup table xp/vista/w7/w2k3/w2k8](http://www.hexacorn.com/blog/2012/06/13/prefetch-hash-calculator-a-hash-lookup-table-xpvistaw7w2k3w2k8/),
  Hexacorn blog, June 13, 2012
- [Prefetch file names and UNC paths](http://www.hexacorn.com/blog/2012/10/29/prefetch-file-names-and-unc-paths/),
  Hexacorn blog, October 29, 2012
- [NTOSBOOT Prefetch File](http://journeyintoir.blogspot.ch/2012/12/ntosboot-prefetch-file.html),
  by Corey Harrell, December 5, 2012
- [What's New in the Prefetch for Windows 8??](http://www.invoke-ir.com/2013/09/whats-new-in-prefetch-for-windows-8.html),
  by Jared Atkinson, September 21, 2013
- [Windows Prefetch (.PF) files](http://www.swiftforensics.com/2013/10/windows-prefetch-pf-files.html?m=1),
  by Yogesh Khatri, October 21, 2013
- [Windows Systems and Artifacts in Digital Forensics: Part III: Prefetch Files](http://resources.infosecinstitute.com/windows-systems-artifacts-digital-forensics-part-iii-prefetch-files/),
  by Ivan Dimov, November 21, 2013
- [Prefetch 101 - a Windows 8 Prefetch file walkthrough](http://i.imgur.com/riuljsK.jpg),
  by Jared Atkinson, 2014
- [Forensic examination and analysis of the Prefetch files on the banking Trojan malware incidents](http://ro.ecu.edu.au/cgi/viewcontent.cgi?article=1132&context=adf),
  by Andri P. Heriyanto, 2014
- [A first look at Windows 10 prefetch files](http://blog.digital-forensics.it/2015/06/a-first-look-at-windows-10-prefetch.html),
  by Francesco Picasso, June 22, 2015

## Tools

### Free - Non Open Source

- [Windows File Analyzer](http://www.mitec.cz/wfa.html) - Parses
  Prefetch files, thumbnail databases, shortcuts, index.dat files, and
  the recycle bin
- [CrowdResponse](https://www.crowdstrike.com/resources/community-tools/crowdresponse/)

### Open Source

- [libscca](libscca.md)
- [prefetch-tool](https://code.google.com/p/prefetch-tool/), Script to
  extract information from windows prefetch folder
- [Plaso](plaso.md)
- [PECmd](https://github.com/EricZimmerman/PECmd), Prefetch command line
  tool using [Prefetch](https://github.com/EricZimmerman/Prefetch),
  Prefetch parser written in C# with support for XP through Windows 10 -
  Needs WINAPI for decompression
