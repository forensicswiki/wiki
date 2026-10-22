---
tags:
  - Database
  - File Formats
  - Registry Analysis
  - Windows
---
## Terminology

### Hive

According to [Registry Hives](https://learn.microsoft.com/en-us/windows/win32/sysinfo/registry-hives)

> A hive is a logical group of keys, subkeys, and values in the Windows
> Registry that has a set of supporting files containing backups of its data.

However in common usage the term hive often does not imply the supporting files.

According to MSDN the origin of the term is bee hives.

## File Locations

The Windows Registry is stored in multiple files.

### Windows NT 4

In Windows NT 4 (and later) the Registry is stored in the [Windows NT Registry File (regf)](windows_nt_registry_file_(regf).md)
format.

Basically the following Registry hives are stored in the corresponding
files:

* HKEY_USERS: \Documents and Setting\User Profile\NTUSER.DAT
* HKEY_USERS\DEFAULT: C:\Windows\system32\config\default
* HKEY_LOCAL_MACHINE\SAM: C:\Windows\system32\config\SAM
* HKEY_LOCAL_MACHINE\SECURITY: C:\Windows\system32\config\SECURITY
* HKEY_LOCAL_MACHINE\SOFTWARE: C:\Windows\system32\config\software
* HKEY_LOCAL_MACHINE\SYSTEM: C:\Windows\system32\config\system

### Windows 9x/ME

In Windows 95, 98, Me the Registry is stored in the [Windows 9x Registry File (creg)](windows_9x_registry_file_(creg).md)
format.

* \Windows\user.dat
* \Windows\system.dat
* \Windows\profiles\user profile\user.dat

## Special cases

The Windows Registry has several special case scenarios, mainly
concerning key and value name, that are easy to fail to account for:

* special characters in key and value names
* duplicate key and value names
* the names when stored in extended ASCII (ANSI string) use a codepage
  that is dependent on the system settings
* unreconciled data

### Special characters in key and value names

Both key and values names are case insensitive. The \ character is used
as the key separator. Note that the \ character can be used in value
names. The / character is used in both key and value names. Some
examples of which are:

```text
Key: HKEY_LOCAL_MACHINE\SYSTEM\ControlSet002\Services\NetBT\Parameters\
Value: Size/Small/Medium/Large
```

```text
Key: HKEY_LOCAL_MACHINE\SYSTEM\ControlSet001\Control\Terminal Server\VIDEO\disc\
Value: \Device\Video0
```

```text
Key:
HKEY_LOCAL_MACHINE\SYSTEM\ControlSet002\services\xmlprov\Parameters\SchemaGroups\User\http://www.microsoft.com/provisioning/eaptlsuserpropertiesv1\
Value: SchemaFile
```

Also, null bytes may be present in key values in order to hide data
[3](https://binaryforay.blogspot.com/2016/01/registry-values-starting-with-null.html).

### Codepaged ASCII strings

Value with name "ëigenaardig" created on Windows XP codepage 1252.

```text
value key data:
00000000: 76 6b 0b 00 46 00 00 00  20 98 1a 00 01 00 00 00   vk..F...  .......
00000010: 01 00 69 6e eb 69 67 65  6e 61 61 72 64 69 67 00   ..in.ige naardig.
00000020: 55 4e 49 43                                        UNIC

value key signature                     : vk
value key value name size               : 11
value key data size                     : 0x00000046 (70)
value key data offset                   : 0x001a9820
value key data type                     : 1 (REG_SZ) String
value key flags                         : 0x0001
        Value name is an ASCII string

value key unknown1                      : 0x6e69 (28265)
value key value name                    : ëigenaardig
value key value name hash               : 0xb78835ee
value key padding:
00000000: 00 55 4e 49 43                                     .UNIC
```

As you can see the name is stored in extended ASCII (ANSI) using
codepage 1252.

### Unreconciled data

Starting from Windows 8.1 and Windows Server 2012 R2, a new
implementation of the hive flusher was introduced in kernel. This
implementation attempts to radically reduce the number of disk writes on
a mounted hive: in particular, a flush operation on a hive will store
modified (dirty) data in a transaction log file, but hive bins in a
primary file (also known as a normal or data file) will be intact. A
kernel will sync a primary file after one of the following conditions
has occurred:

* an hour has elapsed since the latest write to a primary file;
* a power management subsystem reports that all users (local and remote)
  are inactive;
* the operating system is shutting down (hive is unloading).

In order to correctly handle unreconciled data (e.g. when dealing with
an image taken from a live system), one needs to parse transaction log
files along with primary files.

## Persistence keys

The following lists are loosely based of:

* [Silent Runners.vbs](https://www.silentrunners.org/Silent%20Runners.vbs)
* [Forensic Artifacts](artifacts.md)

**Note that in the lists below HKEY_CURRENT_USER is a subset of
HKEY_USERS**

### Command Processor (cmd.exe)

| **Description** | Command Processor Auto Run |
| --- | --- |
| **[Artifact name](artifacts.md)** | WindowsCommandProcessorAutoRun |
| **Key path(s)** | HKEY_LOCAL_MACHINE\Software\Microsoft\Command Processor<br>HKEY_LOCAL_MACHINE\Software\Wow6432Node\Microsoft\Command Processor<br>HKEY_USERS\%SID%\Software\Microsoft\Command Processor<br>HKEY_USERS\%SID%\Software\Wow6432Node\Microsoft\Command Processor |
| **Value name(s)** | AutoRun |
| **Additional information** | <https://technet.microsoft.com/en-us/library/cc779439(v=ws.10).aspx> Command Processor\AutoRun |

### Debugging

| **Description** | Automatic debugging |
| --- | --- |
| **[Artifact name](artifacts.md)** | WindowsAutomaticDebugging |
| **Key path(s)** | HKEY_LOCAL_MACHINE\Software\Microsoft\Windows NT\CurrentVersion\AeDebug |
| **Value name(s)** | Debugger |
| **Additional information** | [Configuring Automatic Debugging](https://learn.microsoft.com/en-us/windows/win32/debug/configuring-automatic-debugging) |

### Internet Explorer

| **Description** | Browser Helper Objects |
| --- | --- |
| **[Artifact name](artifacts.md)** | InternetExplorerBrowserHelperObjects |
| **Key path(s)** | HKEY_LOCAL_MACHINE\Software\Microsoft\Windows\CurrentVersion\Explorer\Browser Helper Objects\*<br>HKEY_LOCAL_MACHINE\Software\Wow6432Node\Microsoft\Windows\CurrentVersion\Explorer\Browser Helper Objects\* |
| **Value name(s)** | * |
| **Additional information** | |

### Local Security Authority (LSA)

| **Description** | Local Security Authority (LSA) Authentication Packages |
| --- | --- |
| **[Artifact name](artifacts.md)** | WindowsLSAAuthenticationPackages |
| **Key path(s)** | HKEY_LOCAL_MACHINE\System\CurrentControlSet\Control\Lsa<br>HKEY_LOCAL_MACHINE\System\CurrentControlSet\Control\Lsa\OSConfig |
| **Value name(s)** | Authentication Packages |
| **Additional information** | |

| **Description** | Local Security Authority (LSA) Notification Packages |
| --- | --- |
| **[Artifact name](artifacts.md)** | WindowsLSANotificationPackages |
| **Key path(s)** | HKEY_LOCAL_MACHINE\System\CurrentControlSet\Control\Lsa<br>HKEY_LOCAL_MACHINE\System\CurrentControlSet\Control\Lsa\OSConfig |
| **Value name(s)** | Notification Packages |
| **Additional information** | |

| **Description** | Local Security Authority (LSA) Security Packages |
| --- | --- |
| **[Artifact name](artifacts.md)** | WindowsLSASecurityPackages |
| **Key path(s)** | HKEY_LOCAL_MACHINE\System\CurrentControlSet\Control\Lsa<br>HKEY_LOCAL_MACHINE\System\CurrentControlSet\Control\Lsa\OSConfig |
| **Value name(s)** | Security Packages |
| **Additional information** | |

### Run keys

| **Description** | Run keys |
| --- | --- |
| **[Artifact name](artifacts.md)** | WindowsRunKeys |
| **Key path(s)** | HKEY_LOCAL_MACHINE\Software\Microsoft\Windows\CurrentVersion\Policies\Explorer\Run\*<br>HKEY_LOCAL_MACHINE\Software\Microsoft\Windows\CurrentVersion\Run\*<br>HKEY_LOCAL_MACHINE\Software\Microsoft\Windows\CurrentVersion\RunOnce\*<br>HKEY_LOCAL_MACHINE\Software\Microsoft\Windows\CurrentVersion\RunOnce\Setup\*<br>HKEY_LOCAL_MACHINE\Software\Microsoft\Windows\CurrentVersion\RunOnceEx\*<br>HKEY_LOCAL_MACHINE\Software\Wow6432Node\Microsoft\Windows\CurrentVersion\Run\*<br>HKEY_LOCAL_MACHINE\Software\Wow6432Node\Microsoft\Windows\CurrentVersion\RunOnce\*<br>HKEY_LOCAL_MACHINE\Software\Wow6432Node\Microsoft\Windows\CurrentVersion\RunOnce\Setup\*<br>HKEY_LOCAL_MACHINE\Software\Wow6432Node\Microsoft\Windows\CurrentVersion\RunOnceEx\*<br>HKEY_LOCAL_MACHINE\Software\Wow6432Node\Microsoft\Windows\CurrentVersion\Policies\Explorer\Run\*<br>HKEY_USERS\%SID%\Software\Microsoft\Windows\CurrentVersion\Policies\Explorer\Run\*<br>HKEY_USERS\%SID%\Software\Microsoft\Windows\CurrentVersion\Run\*<br>HKEY_USERS\%SID%\Software\Microsoft\Windows\CurrentVersion\RunOnce\*<br>HKEY_USERS\%SID%\Software\Microsoft\Windows\CurrentVersion\RunOnce\Setup\*<br>HKEY_USERS\%SID%\Software\Microsoft\Windows\CurrentVersion\RunOnceEx\*<br>HKEY_USERS\%SID%\Software\Wow6432Node\Microsoft\Windows\CurrentVersion\Policies\Explorer\Run\*<br>HKEY_USERS\%SID%\Software\Wow6432Node\Microsoft\Windows\CurrentVersion\Run\*<br>HKEY_USERS\%SID%\Software\Wow6432Node\Microsoft\Windows\CurrentVersion\RunOnce\*<br>HKEY_USERS\%SID%\Software\Wow6432Node\Microsoft\Windows\CurrentVersion\RunOnce\Setup\*<br>HKEY_USERS\%SID%\Software\Wow6432Node\Microsoft\Windows\CurrentVersion\RunOnceEx\* |
| **Value name(s)** | * |
| **Additional information** | |

| **Description** | Run services keys |
| --- | --- |
| **[Artifact name](artifacts.md)** | WindowsRunServices |
| **Key path(s)** | HKEY_LOCAL_MACHINE\Software\Microsoft\Windows\CurrentVersion\RunServicesOnce\*<br>HKEY_LOCAL_MACHINE\Software\Microsoft\Windows\CurrentVersion\RunServices\*<br>HKEY_LOCAL_MACHINE\Software\Wow6432Node\Microsoft\Windows\CurrentVersion\RunServicesOnce\*<br>HKEY_LOCAL_MACHINE\Software\Wow6432Node\Microsoft\Windows\CurrentVersion\RunServices\* |
| **Value name(s)** | * |
| **Additional information** | |

### Session Manager

| **Description** | Session Manager Execute |
| --- | --- |
| **[Artifact name](artifacts.md)** | WindowsSessionManagerBootExecute<br>WindowsSessionManagerExecute<br>WindowsSessionManagerSetupExecute |
| **Key path(s)** | HKEY_LOCAL_MACHINE\System\CurrentControlSet\Control\Session Manager |
| **Value name(s)** | BootExecute<br>Execute<br>SetupExecute |
| **Additional information** | |

| **Description** | Windows Session Manager Windows-on-Windows (WOW) command line |
| --- | --- |
| **[Artifact name](artifacts.md)** | WindowsSessionManagerWOWCommandLine |
| **Key path(s)** | HKEY_LOCAL_MACHINE\System\CurrentControlSet\Control\Session Manager\WOW |
| **Value name(s)** | cmdline<br>wowcmdline |
| **Additional information** | |

### Service Control Manager

| **Description** | Service Control Manager extension |
| --- | --- |
| **[Artifact name](artifacts.md)** | WindowsServiceControlManagerExtension |
| **Key path(s)** | HKEY_LOCAL_MACHINE\System\CurrentControlSet\Control |
| **Value name(s)** | ServiceControlManagerExtension |
| **Additional information** | |

### Windows shell (explorer.exe)

| **Description** | Shell Icon Overlay Identifiers |
| --- | --- |
| **[Artifact name](artifacts.md)** | WindowsShellIconOverlayIdentifiers |
| **Key path(s)** | HKEY_LOCAL_MACHINE\Software\Microsoft\Windows\CurrentVersion\Explorer\ShellIconOverlayIdentifiers\*<br>HKEY_LOCAL_MACHINE\Software\Wow6432Node\Microsoft\Windows\CurrentVersion\Explorer\ShellIconOverlayIdentifiers\*<br>HKEY_USERS\%SID%\Software\Microsoft\Windows\CurrentVersion\Explorer\ShellIconOverlayIdentifiers\*<br>HKEY_USERS\%SID%\Software\Wow6432Node\Microsoft\Windows\CurrentVersion\Explorer\ShellIconOverlayIdentifiers\* |
| **Value name(s)** | * |
| **Additional information** | |

| **Description** | Shell Extensions |
| --- | --- |
| **[Artifact name](artifacts.md)** | WindowsShellExtensions |
| **Key path(s)** | HKEY_LOCAL_MACHINE\Software\Microsoft\Windows\CurrentVersion\Shell Extensions\Approved<br>HKEY_LOCAL_MACHINE\Software\Wow6432Node\Microsoft\Windows\CurrentVersion\Shell Extensions\Approved<br>HKEY_USERS\%SID%\Software\Microsoft\Windows\CurrentVersion\Shell Extensions\Approved<br>HKEY_USERS\%SID%\Software\Wow6432Node\Microsoft\Windows\CurrentVersion\Shell Extensions\Approved |
| **Value name(s)** | * |
| **Additional information** | |

| **Description** | Shell Execute Hooks |
| --- | --- |
| **[Artifact name](artifacts.md)** | WindowsShellExecuteHooks |
| **Key path(s)** | HKEY_LOCAL_MACHINE\Software\Microsoft\Windows\CurrentVersion\Explorer\ShellExecuteHooks\*<br>HKEY_LOCAL_MACHINE\Software\Wow6432Node\Microsoft\Windows\CurrentVersion\Explorer\ShellExecuteHooks\* |
| **Value name(s)** | * |
| **Additional information** | |

| **Description** | Shell Load and Run |
| --- | --- |
| **[Artifact name](artifacts.md)** | WindowsShellLoadAndRun |
| **Key path(s)** | HKEY_CURRENT_USER\Software\Microsoft\Windows NT\CurrentVersion\Windows<br>HKEY_CURRENT_USER\Software\Wow6432Node\Microsoft\Windows NT\CurrentVersion\Windows |
| **Value name(s)** | Load<br>Run |
| **Additional information** | |

| **Description** | Shell Service Object Delay Load |
| --- | --- |
| **[Artifact name](artifacts.md)** | WindowsShellServiceObjects |
| **Key path(s)** | HKEY_LOCAL_MACHINE\Software\Microsoft\Windows\CurrentVersion\ShellServiceObjectDelayLoad<br>HKEY_LOCAL_MACHINE\Software\Wow6432Node\Microsoft\Windows\CurrentVersion\ShellServiceObjectDelayLoad |
| **Value name(s)** | * |
| **Additional information** | [TrojanClicker:Win32/Zirit.X](http://www.microsoft.com/security/portal/threat/encyclopedia/Entry.aspx?Name=TrojanClicker:Win32/Zirit.X#tab=2) |

### Winlogon and Credential Providers

| **Description** | Credential Provider Filters |
| --- | --- |
| **[Artifact name](artifacts.md)** | WindowsCredentialProviderFilters |
| **Key path(s)** | HKEY_LOCAL_MACHINE\Software\Microsoft\Windows\CurrentVersion\Authentication\Credential Provider Filters\*<br>HKEY_LOCAL_MACHINE\Software\Wow6432Node\Microsoft\Windows\CurrentVersion\Authentication\Credential Provider Filters\* |
| **Value name(s)** | * |
| **Additional information** | [Capturing Windows 7 Credential at logon using custom credential provider](http://blog.leetsys.com/2012/01/02/capturing-windows-7-credentials-at-logon-using-custom-credential-provider/) |

| **Description** | Credential Providers |
| --- | --- |
| **[Artifact name](artifacts.md)** | WindowsCredentialProviders |
| **Key path(s)** | HKEY_LOCAL_MACHINE\Software\Microsoft\Windows\CurrentVersion\Authentication\Credential Providers\*<br>HKEY_LOCAL_MACHINE\Software\Wow6432Node\Microsoft\Windows\CurrentVersion\Authentication\Credential Providers\* |
| **Value name(s)** | * |
| **Additional information** | [Capturing Windows 7 Credential at logon using custom credential provider](http://blog.leetsys.com/2012/01/02/capturing-windows-7-credentials-at-logon-using-custom-credential-provider/) |

| **Description** | Pre-Logon Access Provider (PLAP) Providers |
| --- | --- |
| **[Artifact name](artifacts.md)** | WindowsPLAPProviders |
| **Key path(s)** | HKEY_LOCAL_MACHINE\Software\Microsoft\Windows\CurrentVersion\Authentication\PLAP Providers\*<br>HKEY_LOCAL_MACHINE\Software\Wow6432Node\Microsoft\Windows\CurrentVersion\Authentication\PLAP Providers\* |
| **Value name(s)** | * |
| **Additional information** | |

| **Description** | Winlogon Gina DLL |
| --- | --- |
| **[Artifact name](artifacts.md)** | WindowsWinlogonShell |
| **Key path(s)** | HKEY_LOCAL_MACHINE\Software\Microsoft\Windows NT\CurrentVersion\Winlogon<br>HKEY_USERS\%SID%\Software\Microsoft\Windows NT\CurrentVersion\Winlogon |
| **Value name(s)** | GinaDLL |
| **Additional information** | |

| **Description** | Winlogon Notify |
| --- | --- |
| **[Artifact name](artifacts.md)** | WindowsWinlogonNotify |
| **Key path(s)** | HKEY_LOCAL_MACHINE\Software\Microsoft\Windows NT\CurrentVersion\Winlogon\Notify\*<br>HKEY_USERS\%SID%\Software\Microsoft\Windows NT\CurrentVersion\Winlogon\Notify\* |
| **Value name(s)** | DLLName |
| **Additional information** | |

| **Description** | Winlogon Shell |
| --- | --- |
| **[Artifact name](artifacts.md)** | WindowsWinlogonShell |
| **Key path(s)** | HKEY_LOCAL_MACHINE\Software\Microsoft\Windows NT\CurrentVersion\Winlogon<br>HKEY_USERS\%SID%\Software\Microsoft\Windows NT\CurrentVersion\Winlogon |
| **Value name(s)** | Shell |
| **Additional information** | |

| **Description** | Winlogon System |
| --- | --- |
| **[Artifact name](artifacts.md)** | WindowsWinlogonSystem |
| **Key path(s)** | HKEY_LOCAL_MACHINE\Software\Microsoft\Windows NT\CurrentVersion\Winlogon<br>HKEY_USERS\%SID%\Software\Microsoft\Windows NT\CurrentVersion\Winlogon |
| **Value name(s)** | System |
| **Additional information** | |

| **Description** | Winlogon Taksman |
| --- | --- |
| **[Artifact name](artifacts.md)** | WindowsWinlogonTaksman |
| **Key path(s)** | HKEY_LOCAL_MACHINE\Software\Microsoft\Windows NT\CurrentVersion\Winlogon<br>HKEY_USERS\%SID%\Software\Microsoft\Windows NT\CurrentVersion\Winlogon |
| **Value name(s)** | Taksman |
| **Additional information** | |

| **Description** | Winlogon Userinit |
| --- | --- |
| **[Artifact name](artifacts.md)** | WindowsWinlogonUserinit |
| **Key path(s)** | HKEY_LOCAL_MACHINE\Software\Microsoft\Windows NT\CurrentVersion\Winlogon<br>HKEY_USERS\%SID%\Software\Microsoft\Windows NT\CurrentVersion\Winlogon |
| **Value name(s)** | Userinit |
| **Additional information** | |

| **Description** | Winlogon VMApplet |
| --- | --- |
| **[Artifact name](artifacts.md)** | WindowsWinlogonVMApplet |
| **Key path(s)** | HKEY_LOCAL_MACHINE\Software\Microsoft\Windows NT\CurrentVersion\Winlogon<br>HKEY_USERS\%SID%\Software\Microsoft\Windows NT\CurrentVersion\Winlogon |
| **Value name(s)** | VMApplet |
| **Additional information** | |

### Policy

| **Description** | Windows System Policy replacement shell |
| --- | --- |
| **[Artifact name](artifacts.md)** | WindowsSystemPolicyShell |
| **Key path(s)** | HKEY_LOCAL_MACHINE\Software\Microsoft\Windows\CurrentVersion\Policies\System<br>HKEY_LOCAL_MACHINE\Software\Wow6432Node\Microsoft\Windows\CurrentVersion\Policies\System |
| **Value name(s)** | Shell |
| **Additional information** | |

### Unsorted

| **Description** | Active Setup - Installed Components |
| --- | --- |
| **[Artifact name](artifacts.md)** | WindowsStubPaths |
| **Key path(s)** | HKEY_LOCAL_MACHINE\Software\Microsoft\Active Setup\Installed Components<br>HKEY_LOCAL_MACHINE\Software\Wow6432Node\Microsoft\Active Setup\Installed Components<br>HKEY_USERS\%SID%\Software\Microsoft\Active Setup\Installed Components<br>HKEY_USERS\%SID%\Software\Wow6432Node\Microsoft\Active Setup\Installed Components |
| **Value name(s)** | StubPath |
| **Additional information** | |

| **Description** | Application Initial (AppInit) DLLs persistence |
| --- | --- |
| **[Artifact name](artifacts.md)** | WindowsAppInitDLLs |
| **Key path(s)** | HKEY_LOCAL_MACHINE\Software\Microsoft\Windows NT\CurrentVersion\Windows<br>HKEY_LOCAL_MACHINE\Software\Wow6432Node\Microsoft\Windows NT\CurrentVersion\Windows<br>HKEY_USERS\%%users.sid%%\Software\Microsoft\Windows NT\CurrentVersion\Windows<br>HKEY_USERS\%%users.sid%%\Software\Wow6432Node\Microsoft\Windows NT\CurrentVersion\Windows |
| **Value name(s)** | AppInit_DLLs |
| **Additional information** | |

| **Description** | Security Providers |
| --- | --- |
| **[Artifact name](artifacts.md)** | WindowsSecurityProviders |
| **Key path(s)** | HKEY_LOCAL_MACHINE\System\CurrentControlSet\Control\SecurityProviders\* |
| **Value name(s)** | * |
| **Additional information** | |

| **Description** | Alternate shell |
| --- | --- |
| **[Artifact name](artifacts.md)** | WindowsAlternateShell |
| **Key path(s)** | HKEY_LOCAL_MACHINE\System\CurrentControlSet\Control\SafeBoot |
| **Value name(s)** | AlternateShell |
| **Additional information** | |

| **Description** | Boot verification program |
| --- | --- |
| **[Artifact name](artifacts.md)** | WindowsBootVerificationProgram |
| **Key path(s)** | HKEY_LOCAL_MACHINE\System\CurrentControlSet\Control\BootVerificationProgram |
| **Value name(s)** | ImagePath |
| **Additional information** | |

## Bibliography

* [Using ShellBag Information to Reconstruct User Activities](https://dfrws.org/presentation/using-shellbag-information-to-reconstruct-user-activities/),
  by Yuandong Zhu\*, Pavel Gladyshev, Joshua James, DFRWS 2009
* [Recovering Deleted Data From the Windows Registry](https://dfrws.org/presentation/recovering-deleted-data-from-the-windows-registry/),
  by Timothy Morgan, DFRWS 2008
* [Forensic Analysis of the Windows Registry in
  Memory](https://dfrws.org/sites/default/files/session-files/2008_USA_paper-forensic_analysis_of_the_windows_registry_in_memory.pdf)
  and
  [slides](https://dfrws.org/sites/default/files/session-files/2008_USA_pres-forensic_analysis_of_the_windows_registry_in_memory.pdf),
  by Brendan Dolan-Gavitt, DFRWS 2008
* [The Windows Registry as a forensic resource](https://www.sciencedirect.com/science/article/abs/pii/S1742287605000587),
  Digital Investigation, Volume 2, Issue 3, September 2005, Pages
  201--205.
* [Windows registry file format specification](https://github.com/msuhanov/regf/blob/master/Windows%20registry%20file%20format%20specification.md),
  by Maxim Suhanov, 2015-2016

### Undated

* [A Windows Registry Quick Reference: For the Everyday Examiner](https://www.iapsonline.com/sites/default/files/A%20Windows%20Registry%20Quick%20Reference-%20For%20the%20Everyday%20Examiner%20-%20By%20Derrick%20J.%20Farmer.pdf),
  by Derrick Farmer, Burlington, VT.
* [Forensic Analysis of the Windows Registry](https://www.forensicfocus.com/articles/forensic-analysis-of-the-windows-registry/),
  by Lih Wern Wong , School of Computer and Information Science, Edith
  Cowan University

## Also see

* [Boot Configuration Data](windows_boot_configuration_data.md)

## External Links

* [Wikipedia: Windows Registry](https://en.wikipedia.org/wiki/Windows_Registry)
* [Windows Incident Response Articles on Registry](https://windowsir.blogspot.com/search/label/Registry)
* [Windows Registry Information](https://www.answers.com/redirectSearch?query=win-registry)
* [Push the Red Button](https://moyix.blogspot.com/search/label/registry)
* [Exporting registry hives from a live system](https://dfir.ru/2020/10/03/exporting-registry-hives-from-a-live-system/),
  by Maxim Suhanov, October 3, 2020

### Windows 32-bit on Windows 64-bit (WoW64)

* [Registry Keys Affected by WOW64](https://learn.microsoft.com/en-us/windows/win32/winprog64/shared-registry-keys),
  by [Microsoft](microsoft.md)
* [Registry Redirector](https://learn.microsoft.com/en-us/windows/win32/winprog64/registry-redirector),
  by [Microsoft](microsoft.md)
* [Registry Keys Affected by WOW64](https://learn.microsoft.com/en-us/windows/win32/winprog64/shared-registry-keys),
  by [Microsoft](microsoft.md)
* [32-bit and 64-bit Application Data in the Registry](https://learn.microsoft.com/en-us/windows/win32/sysinfo/32-bit-and-64-bit-application-data-in-the-registry),
  by [Microsoft](microsoft.md)

### Cached Credentials

* [Cached Credentials](https://juggernaut.wikidot.com/cached-credentials),
  by Juggernaut

### Persistence keys

* [Understand and Control Startup Apps with the System Configuration Utility](https://learn.microsoft.com/en-us/previous-versions/technet-magazine/ee851671(v=msdn.10)),
  by [Microsoft Technet](microsoft.md)
* [Silent Runners](https://www.silentrunners.org/), by Andrew Aronoff
* [Beyond good ol' Run key](http://www.hexacorn.com/blog/2012/07/23/beyond-good-ol-run-key/),
  Hexacorn blog, July 23, 2012
* [Plugins: soft_run user_run](http://journeyintoir.blogspot.com/2013_04_01_archive.html),
  by Corey Harrell, April 17, 2013
* [Auto-Start Extensibility Points (ASEPs)](https://code.google.com/archive/p/regripper/wikis/ASEPs.wiki),
  by the [RegRipper project](regripper.md), April 29, 2013
* [Volatility autoruns plugin](https://github.com/tomchop/volatility-autoruns/blob/master/README.md),
  by the [Volatility project](volatility_framework.md), April 14, 2015

### User Assist

* [UserAssist](https://blog.didierstevens.com/programs/userassist/),
  by Didier Stevens
* [UserAssist V2.3.0](https://blog.didierstevens.com/2007/07/17/userassist-v230/),
  by Didier Stevens, July 17, 2007
* [More on (the) UserAssist keys](https://windowsir.blogspot.com/2007/09/more-on-userassist-keys.html),
  by [Harlan Carvey](harlan_carvey.md), Monday, September 03, 2007
* [Windows 7 Beta: ROT13 Replaced With Vigenère? Great Joke!](https://blog.didierstevens.com/2009/01/18/quickpost-windows-7-beta-rot13-replaced-with-vigenere-great-joke/),
  by Didier Stevens, January 18, 2009
* [Prefetch and User Assist](http://forensicsfromthesausagefactory.blogspot.com/2010/05/prefetch-and-user-assist.html),
  by DC174, May 27, 2010
* [UserAssist Forensics (timelines, interpretation, testing, &amp; more)](https://www.4n6k.com/2013/05/userassist-forensics-timelines.html),
  by Dan (@4n6k), May 14, 2013
* [Daily Blog \#45: Understanding the artifacts: User Assist](https://www.hecfblog.com/2013/08/daily-blog-45-understanding-artifacts.html),
  by David Cowen, August 7, 2013

## Tools

### Open Source

* [Forensic Registry EDitor (fred)](https://www.pinguin.lu/index.php) -
  "Forensic Registry EDitor (fred) is a cross-platform M\$ registry hive
  editor" by Daniel Gillen
* [regviewer](https://sourceforge.net/projects/regviewer/) - a tool for
  looking at the registry.
* [RegRipper](regripper.md) - "the fastest, easiest, and best
  tool for registry analysis in forensics examinations."
* [Parse::Win32Registry](https://metacpan.org/release/JMACFARLA/Parse-Win32Registry-0.51/view/lib/Parse/Win32Registry.pm)
  Perl module.
* [python-registry](https://github.com/williballenthin/python-registry)
  Python module.
* [libregf](libregf.md) - Library and tools to access the
  Windows NT Registry File (REGF) format
* [Registryasxml](registryasxml.md) - Tool to import/export
  registry sections as XML
* [kregedit](https://www.samba.org/~jelmer/kregedit/) - a KDE utility for
  viewing and editing registry files.
* [Registry](https://github.com/EricZimmerman/Registry) Full featured,
  offline Registry hive parser written in C#. Supports deleted item
  recovery, full searching, and more by @EricZimmerman

#### Discontinued

* [ntreg](https://packetstormsecurity.com/files/10450/ntreg.tar.gz.html)
  a file system driver for linux, which understands the NT registry file format.
* [Registry Decoder](https://github.com/504ensicslabs/registrydecoder) live hive
  acquisition and offline analysis component, by Andrew Case

### Freeware

* [Registry Explorer](https://binaryforay.blogspot.com/p/software.html)
  Registry Explorer and RECmd allow unrivaled access to Registry hives
  and contain bookmarks for common registry keys by @EricZimmerman

### Commercial

* [Windows Registry Recovery](https://www.mitec.cz/wrr.html)
* [Registry Tool](http://registrytool.com/)
