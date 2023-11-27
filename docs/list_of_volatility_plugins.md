---
  - Articles that need to be expanded
tags:
  - Research
  - Websites
---
The [Volatility Framework](volatility_framework.md) was designed
to be expanded by plugins. Here is a list of the published plugins for
the **Volatility 1.3 framework**. Note that these plugins are not hosted
on the wiki, but all on external sites. **The latest release of the
[Volatility Framework](volatility_framework.md) is 2.2**. These
plugins are **not compatible with the latest version** of the framework
and information about compatible plugins can be found on the
[wiki](https://code.google.com/archive/p/volatility/wiki/VolatilityIntroduction?tm=6)
on the [project Googlecode site](https://code.google.com/archive/p/volatility).

## Command Shell

- [volshell](https://moyix.blogspot.com/2008/08/indroducing-volshell.html)
  (By
  [Moyix](https://moyix.blogspot.com/2008/08/indroducing-volshell.html))-
  Creates a python shell can be used with the framework.

## Malware Detection

- IDT (By [Michael Hale Ligh](http://mnin.blogspot.com/2009/07/new-and-updated-volatility-plug-ins.html)) -
  Prints the Interrupt Descriptor Table (IDT) addresses for one
  processor
- DriverIRP (By [Michael Hale Ligh](http://mnin.blogspot.com/2009/07/new-and-updated-volatility-plug-ins.html)) -
  Prints driver IRP function addresses
- kernel_hooks (By [Michael Hale Ligh](http://mnin.blogspot.com/2009/07/new-and-updated-volatility-plug-ins.html)) -
  Detects IAT, EAT, and in-line hooks in kernel drivers instead of
  usermode modules
- malfind2 (By [Michael Hale Ligh](http://mnin.blogspot.com/2009/07/new-and-updated-volatility-plug-ins.html)) -
  Automates the process of finding and extracting (usually malicious)
  code injected into another process
- orphan_threads (By [Michael Hale Ligh](http://mnin.blogspot.com/2009/07/new-and-updated-volatility-plug-ins.html)) -
  Detects hidden system/kernel threads
- usermode_hooks2 (By [Michael Hale Ligh](http://mnin.blogspot.com/2009/07/new-and-updated-volatility-plug-ins.html)) -
  Detect IAT/EAT/Inline rootkit hooks in usermode processes
- kernel_hooks (By [Michael Hale Ligh](http://mnin.blogspot.com/2009/07/new-and-updated-volatility-plug-ins.html)) -
  Detect IAT/EAT/Inline hooks in kernel drivers
- Volatility Analyst Pack 0.1 (By [Michael Hale Ligh](http://mnin.blogspot.com/2009/12/new-and-updated-volatility-plug-ins.html)) -
  A pack which contains updates to many of the listed modules

## Data Recovery

- cryptoscan, by Jesse Kornblum -
  Finds [TrueCrypt](truecrypt.md) passphrases
- [moddump](https://moyix.blogspot.com/2008/10/plugin-post-moddump.html)
  (By
  [Moyix](https://moyix.blogspot.com/2008/10/plugin-post-moddump.html)) -
  Dump out a kernel module (aka driver)
- [Registry tools](https://sites.cc.gatech.edu/~brendan/volatility/dl/volreg-0.6.tar.gz)
  (By
  [Moyix](https://moyix.blogspot.com/2009/01/memory-registry-tools.html)) -
  A suite of plugins for accessing data from the registry, including
  password hashes, LSA secrets, and arbitrary registry keys.
- [Modified Regripper & Glue Code](https://sites.cc.gatech.edu/~brendan/volatility/dl/volrip-0.1.tar.gz)
  (By
  [Moyix](https://moyix.blogspot.com/2009/03/regripper-and-volatility-prototype.html)) -
  Code to run a modified RegRipper against the registry hives embedded
  in a memory dump. Note that due to a dependency on Inline::Python,
  this only works on Linux.
- [getsids](https://moyix.blogspot.com/2008/08/linking-processes-to-users.html)
  (By
  [Moyix](https://moyix.blogspot.com/2008/08/linking-processes-to-users.html)) -
  Get information about what user (SID) started a process.
- [ssdt](https://moyix.blogspot.com/2008/08/auditing-system-call-table.html)
  (By
  [Moyix](https://moyix.blogspot.com/2008/08/auditing-system-call-table.html)) -
  List entries in the system call table. Can be used to detect certain
  rootkits that hook system calls by replacing entries in this table.
- [threadqueues](http://kurtz.cs.wesleyan.edu/%7Ebdolangavitt/memory/threadqueues.py)
  (By
  [Moyix](https://moyix.blogspot.com/2008/09/window-messages-as-forensic-resource.html)) -
  Enumerates window messages pending for each thread on the system.
  Window messages are the mechanism used to send things like button
  presses, mouse clicks, and other events to GUI programs.
- objtypescan, by Andreas Schuster -
  Enumerates Windows kernel object types. (Note: If running the SVN
  version of Volatility, just install the plugin file from this archive)
- keyboardbuffer, by Andreas Schuster -
  Extracts keyboard buffer used by the BIOS, which may contain BIOS or
  disk encryption passwords.
- mutantscan, by Andreas Schuster -
  Extracts mutexes from the Windows kernel.(Note: If running the SVN
  version of Volatility, just install the plugin file from this
  archive.)
- symlinkobjscan, by Andreas Schuster -
  Extracts symbolic link objects from the Windows kernel.(Note: If
  running the SVN version of Volatility, just install the plugin file
  from this archive.)
- driverscan, by Andreas Schuster -
  Scan for kernel _DRIVER_OBJECTs. (Note: If running the SVN version of
  Volatility, just install the plugin file from this archive.)
- fileobjscan, by Andreas Schuster -
  File object -\> process linkage, including hidden files. (Note: If
  running the SVN version of Volatility, just install the plugin file
  from this archive.)

## Process Enumeration

- suspicious, by Jesse Kornblum -
  Identify "suspicious" processes. This version counts any command line running
  [TrueCrypt](truecrypt.md) or any command line that starts with a lower case
  drive letter as suspicious.

## Output Formatting

- [pstree](http://scudette.blogspot.com/2008/10/pstree-volatility-plugin.html)
  (By
  [Scudette](http://scudette.blogspot.com/2008/10/pstree-volatility-plugin.html)) -
  Produces a tree-style listing of processes
- [vol2html](http://gleeda.blogspot.com/2009/03/briefly-vol2html-update.html)
  (By [Jamie Levy AKA Gleeda](http://gleeda.blogspot.com/2008/11/vol2html-perl-script.html)) -
  Converts volatility output to HTML. Not technically a plugin, but
  useful nonetheless.
- SQLite,
  by [Jamie Levy AKA Gleeda](http://gleeda.blogspot.com/2010/01/volatilitys-output-rendering-functions.html) -
  Allows one to place Volatility output into a SQLite3 Database

## Other Helper Tools

Though these are not actual plugins they are helpful tools for obtaining
output from the [Volatility Framework](volatility_framework.md).

- VolReport(win), by SAL
- [Volatility Batch File Maker](http://forensiczone.blogspot.com/2009/10/volatility-batch-file-maker.html)
  (By [Richard McQuown](http://forensiczone.blogspot.com/2009/10/walk-through-volatility-batch-file.html))
- [Volscript](https://docs.google.com/leaf?id=0Bz2rZ4S-yK8AZDYzNDU3ZjktYTBhMS00NGQ3LTg2MGItYWM2YTFjYWE3YmQ3&sort=name&layout=list&num=50)
  Windows based Volatility batch script that runs a number of Volatility
  commands to produce a report (By [Christopher Bentley](http://active-security.blogspot.com/2011/05/volatility-script-for-windows.html))
