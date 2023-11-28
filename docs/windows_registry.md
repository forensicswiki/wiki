---
tags:
  - Database
  - File Formats
  - Registry Analysis
  - Windows
---
## Terminology

### Hive

According to
[1](https://learn.microsoft.com/en-us/windows/win32/sysinfo/registry-hives)

    A hive is a logical group of keys, subkeys, and values in the Windows Registry that has a set of supporting files containing backups of its data.

However in common usage the term hive often does not imply the
supporting files.

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

Both key and values names are case insensitive. The \\ character is used
as the key separator. Note that the \\ character can be used in value
names. The / character is used in both key and value names. Some
examples of which are:

    Key: HKEY_LOCAL_MACHINE\SYSTEM\ControlSet002\Services\NetBT\Parameters\
    Value: Size/Small/Medium/Large

    Key: HKEY_LOCAL_MACHINE\SYSTEM\ControlSet001\Control\Terminal Server\VIDEO\disc\
    Value: \Device\Video0

    Key:
    HKEY_LOCAL_MACHINE\SYSTEM\ControlSet002\services\xmlprov\Parameters\SchemaGroups\User\http://www.microsoft.com/provisioning/eaptlsuserpropertiesv1\
    Value: SchemaFile

Also, null bytes may be present in key values in order to hide data
[3](https://binaryforay.blogspot.com/2016/01/registry-values-starting-with-null.html).

### Codepaged ASCII strings

Value with name "ëigenaardig" created on Windows XP codepage 1252.

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

<b>Note that in the lists below HKEY_CURRENT_USER is a subset of
HKEY_USERS</b>

### Command Processor (cmd.exe)

<table>
<tbody>
<tr class="odd">
<td><p><b>Description</b></p></td>
<td><p>Command Processor Auto Run</p></td>
</tr>
<tr class="even">
<td><p><b><a href="Artifacts" title="wikilink">Artifact
name</a></b></p></td>
<td><p>WindowsCommandProcessorAutoRun</p></td>
</tr>
<tr class="odd">
<td><p><b>Key path(s)</b></p></td>
<td><ul>
<li>HKEY_LOCAL_MACHINE\Software\Microsoft\Command Processor</li>
<li>HKEY_LOCAL_MACHINE\Software\Wow6432Node\Microsoft\Command
Processor</li>
<li>HKEY_USERS\%SID%\Software\Microsoft\Command Processor</li>
<li>HKEY_USERS\%SID%\Software\Wow6432Node\Microsoft\Command
Processor</li>
</ul></td>
</tr>
<tr class="even">
<td><p><b>Value name(s)</b></p></td>
<td><p>AutoRun</p></td>
</tr>
<tr class="odd">
<td><p><b>Additional information</b></p></td>
<td><p>[<a
href="https://technet.microsoft.com/en-us/library/cc779439(v=ws.10">https://technet.microsoft.com/en-us/library/cc779439(v=ws.10</a>).aspx
Command Processor\AutoRun]</p></td>
</tr>
</tbody>
</table>

### Debugging

<table>
<tbody>
<tr class="odd">
<td><p><b>Description</b></p></td>
<td><p>Automatic debugging</p></td>
</tr>
<tr class="even">
<td><p><b><a href="Artifacts" title="wikilink">Artifact
name</a></b></p></td>
<td><p>WindowsAutomaticDebugging</p></td>
</tr>
<tr class="odd">
<td><p><b>Key path(s)</b></p></td>
<td><ul>
<li>HKEY_LOCAL_MACHINE\Software\Microsoft\Windows
NT\CurrentVersion\AeDebug</li>
</ul></td>
</tr>
<tr class="even">
<td><p><b>Value name(s)</b></p></td>
<td><p>Debugger</p></td>
</tr>
<tr class="odd">
<td><p><b>Additional information</b></p></td>
<td><p><a href="https://learn.microsoft.com/en-us/windows/win32/debug/configuring-automatic-debugging">https://learn.microsoft.com/en-us/windows/win32/debug/configuring-automatic-debugging</a>Configuring Automatic Debugging]</p></td>
</tr>
</tbody>
</table>

### Internet Explorer

<table>
<tbody>
<tr class="odd">
<td><p><b>Description</b></p></td>
<td><p>Browser Helper Objects</p></td>
</tr>
<tr class="even">
<td><p><b><a href="Artifacts" title="wikilink">Artifact
name</a></b></p></td>
<td><p>InternetExplorerBrowserHelperObjects</p></td>
</tr>
<tr class="odd">
<td><p><b>Key path(s)</b></p></td>
<td><ul>
<li>HKEY_LOCAL_MACHINE\Software\Microsoft\Windows\CurrentVersion\Explorer\Browser
Helper Objects\*</li>
<li>HKEY_LOCAL_MACHINE\Software\Wow6432Node\Microsoft\Windows\CurrentVersion\Explorer\Browser
Helper Objects\*</li>
</ul></td>
</tr>
<tr class="even">
<td><p><b>Value name(s)</b></p></td>
<td><p>*</p></td>
</tr>
<tr class="odd">
<td><p><b>Additional information</b></p></td>
<td></td>
</tr>
</tbody>
</table>

### Local Security Authority (LSA)

<table>
<tbody>
<tr class="odd">
<td><p><b>Description</b></p></td>
<td><p>Local Security Authority (LSA) Authentication Packages</p></td>
</tr>
<tr class="even">
<td><p><b><a href="Artifacts" title="wikilink">Artifact
name</a></b></p></td>
<td><p>WindowsLSAAuthenticationPackages</p></td>
</tr>
<tr class="odd">
<td><p><b>Key path(s)</b></p></td>
<td><ul>
<li>HKEY_LOCAL_MACHINE\System\CurrentControlSet\Control\Lsa</li>
<li>HKEY_LOCAL_MACHINE\System\CurrentControlSet\Control\Lsa\OSConfig</li>
</ul></td>
</tr>
<tr class="even">
<td><p><b>Value name(s)</b></p></td>
<td><p>Authentication Packages</p></td>
</tr>
<tr class="odd">
<td><p><b>Additional information</b></p></td>
<td></td>
</tr>
</tbody>
</table>

<table>
<tbody>
<tr class="odd">
<td><p><b>Description</b></p></td>
<td><p>Local Security Authority (LSA) Notification Packages</p></td>
</tr>
<tr class="even">
<td><p><b><a href="Artifacts" title="wikilink">Artifact
name</a></b></p></td>
<td><p>WindowsLSANotificationPackages</p></td>
</tr>
<tr class="odd">
<td><p><b>Key path(s)</b></p></td>
<td><ul>
<li>HKEY_LOCAL_MACHINE\System\CurrentControlSet\Control\Lsa</li>
<li>HKEY_LOCAL_MACHINE\System\CurrentControlSet\Control\Lsa\OSConfig</li>
</ul></td>
</tr>
<tr class="even">
<td><p><b>Value name(s)</b></p></td>
<td><p>Notification Packages</p></td>
</tr>
<tr class="odd">
<td><p><b>Additional information</b></p></td>
<td></td>
</tr>
</tbody>
</table>

<table>
<tbody>
<tr class="odd">
<td><p><b>Description</b></p></td>
<td><p>Local Security Authority (LSA) Security Packages</p></td>
</tr>
<tr class="even">
<td><p><b><a href="Artifacts" title="wikilink">Artifact
name</a></b></p></td>
<td><p>WindowsLSASecurityPackages</p></td>
</tr>
<tr class="odd">
<td><p><b>Key path(s)</b></p></td>
<td><ul>
<li>HKEY_LOCAL_MACHINE\System\CurrentControlSet\Control\Lsa</li>
<li>HKEY_LOCAL_MACHINE\System\CurrentControlSet\Control\Lsa\OSConfig</li>
</ul></td>
</tr>
<tr class="even">
<td><p><b>Value name(s)</b></p></td>
<td><p>Security Packages</p></td>
</tr>
<tr class="odd">
<td><p><b>Additional information</b></p></td>
<td></td>
</tr>
</tbody>
</table>

### Run keys

<table>
<tbody>
<tr class="odd">
<td><p><b>Description</b></p></td>
<td><p>Run keys</p></td>
</tr>
<tr class="even">
<td><p><b><a href="Artifacts" title="wikilink">Artifact
name</a></b></p></td>
<td><p>WindowsRunKeys</p></td>
</tr>
<tr class="odd">
<td><p><b>Key path(s)</b></p></td>
<td><ul>
<li>HKEY_LOCAL_MACHINE\Software\Microsoft\Windows\CurrentVersion\Policies\Explorer\Run\*</li>
<li>HKEY_LOCAL_MACHINE\Software\Microsoft\Windows\CurrentVersion\Run\*</li>
<li>HKEY_LOCAL_MACHINE\Software\Microsoft\Windows\CurrentVersion\RunOnce\*</li>
<li>HKEY_LOCAL_MACHINE\Software\Microsoft\Windows\CurrentVersion\RunOnce\Setup\*</li>
<li>HKEY_LOCAL_MACHINE\Software\Microsoft\Windows\CurrentVersion\RunOnceEx\*</li>
<li>HKEY_LOCAL_MACHINE\Software\Wow6432Node\Microsoft\Windows\CurrentVersion\Run\*</li>
<li>HKEY_LOCAL_MACHINE\Software\Wow6432Node\Microsoft\Windows\CurrentVersion\RunOnce\*</li>
<li>HKEY_LOCAL_MACHINE\Software\Wow6432Node\Microsoft\Windows\CurrentVersion\RunOnce\Setup\*</li>
<li>HKEY_LOCAL_MACHINE\Software\Wow6432Node\Microsoft\Windows\CurrentVersion\RunOnceEx\*</li>
<li>HKEY_LOCAL_MACHINE\Software\Wow6432Node\Microsoft\Windows\CurrentVersion\Policies\Explorer\Run\*</li>
<li>HKEY_USERS\%SID%\Software\Microsoft\Windows\CurrentVersion\Policies\Explorer\Run\*</li>
<li>HKEY_USERS\%SID%\Software\Microsoft\Windows\CurrentVersion\Run\*</li>
<li>HKEY_USERS\%SID%\Software\Microsoft\Windows\CurrentVersion\RunOnce\*</li>
<li>HKEY_USERS\%SID%\Software\Microsoft\Windows\CurrentVersion\RunOnce\Setup\*</li>
<li>HKEY_USERS\%SID%\Software\Microsoft\Windows\CurrentVersion\RunOnceEx\*</li>
<li>HKEY_USERS\%SID%\Software\Wow6432Node\Microsoft\Windows\CurrentVersion\Policies\Explorer\Run\*</li>
<li>HKEY_USERS\%SID%\Software\Wow6432Node\Microsoft\Windows\CurrentVersion\Run\*</li>
<li>HKEY_USERS\%SID%\Software\Wow6432Node\Microsoft\Windows\CurrentVersion\RunOnce\*</li>
<li>HKEY_USERS\%SID%\Software\Wow6432Node\Microsoft\Windows\CurrentVersion\RunOnce\Setup\*</li>
<li>HKEY_USERS\%SID%\Software\Wow6432Node\Microsoft\Windows\CurrentVersion\RunOnceEx\*</li>
</ul></td>
</tr>
<tr class="even">
<td><p><b>Value name(s)</b></p></td>
<td><p>*</p></td>
</tr>
<tr class="odd">
<td><p><b>Additional information</b></p></td>
<td></td>
</tr>
</tbody>
</table>

<table>
<tbody>
<tr class="odd">
<td><p><b>Description</b></p></td>
<td><p>Run services keys</p></td>
</tr>
<tr class="even">
<td><p><b><a href="Artifacts" title="wikilink">Artifact
name</a></b></p></td>
<td><p>WindowsRunServices</p></td>
</tr>
<tr class="odd">
<td><p><b>Key path(s)</b></p></td>
<td><ul>
<li>HKEY_LOCAL_MACHINE\Software\Microsoft\Windows\CurrentVersion\RunServicesOnce\*</li>
<li>HKEY_LOCAL_MACHINE\Software\Microsoft\Windows\CurrentVersion\RunServices\*</li>
<li>HKEY_LOCAL_MACHINE\Software\Wow6432Node\Microsoft\Windows\CurrentVersion\RunServicesOnce\*</li>
<li>HKEY_LOCAL_MACHINE\Software\Wow6432Node\Microsoft\Windows\CurrentVersion\RunServices\*</li>
</ul></td>
</tr>
<tr class="even">
<td><p><b>Value name(s)</b></p></td>
<td><p>*</p></td>
</tr>
<tr class="odd">
<td><p><b>Additional information</b></p></td>
<td></td>
</tr>
</tbody>
</table>

### Session Manager

<table>
<tbody>
<tr class="odd">
<td><p><b>Description</b></p></td>
<td><p>Session Manager Execute</p></td>
</tr>
<tr class="even">
<td><p><b><a href="Artifacts" title="wikilink">Artifact
name</a></b></p></td>
<td><ul>
<li>WindowsSessionManagerBootExecute</li>
<li>WindowsSessionManagerExecute</li>
<li>WindowsSessionManagerSetupExecute</li>
</ul></td>
</tr>
<tr class="odd">
<td><p><b>Key path(s)</b></p></td>
<td><p>HKEY_LOCAL_MACHINE\System\CurrentControlSet\Control\Session
Manager</p></td>
</tr>
<tr class="even">
<td><p><b>Value name(s)</b></p></td>
<td><ul>
<li>BootExecute</li>
<li>Execute</li>
<li>SetupExecute</li>
</ul></td>
</tr>
<tr class="odd">
<td><p><b>Additional information</b></p></td>
<td></td>
</tr>
</tbody>
</table>

<table>
<tbody>
<tr class="odd">
<td><p><b>Description</b></p></td>
<td><p>Windows Session Manager Windows-on-Windows (WOW) command
line</p></td>
</tr>
<tr class="even">
<td><p><b><a href="Artifacts" title="wikilink">Artifact
name</a></b></p></td>
<td><p>WindowsSessionManagerWOWCommandLine</p></td>
</tr>
<tr class="odd">
<td><p><b>Key path(s)</b></p></td>
<td><p>HKEY_LOCAL_MACHINE\System\CurrentControlSet\Control\Session
Manager\WOW</p></td>
</tr>
<tr class="even">
<td><p><b>Value name(s)</b></p></td>
<td><ul>
<li>cmdline</li>
<li>wowcmdline</li>
</ul></td>
</tr>
<tr class="odd">
<td><p><b>Additional information</b></p></td>
<td></td>
</tr>
</tbody>
</table>

### Service Control Manager

|                                      |                                                     |
|--------------------------------------|-----------------------------------------------------|
| <b>Description</b>                   | Service Control Manager extension                   |
| <b>[Artifact name](artifacts.md)</b> | WindowsServiceControlManagerExtension               |
| <b>Key path(s)</b>                   | HKEY_LOCAL_MACHINE\System\CurrentControlSet\Control |
| <b>Value name(s)</b>                 | ServiceControlManagerExtension                      |
| <b>Additional information</b>        |                                                     |

### Windows shell (explorer.exe)

<table>
<tbody>
<tr class="odd">
<td><p><b>Description</b></p></td>
<td><p>Shell Icon Overlay Identifiers</p></td>
</tr>
<tr class="even">
<td><p><b><a href="Artifacts" title="wikilink">Artifact
name</a></b></p></td>
<td><p>WindowsShellIconOverlayIdentifiers</p></td>
</tr>
<tr class="odd">
<td><p><b>Key path(s)</b></p></td>
<td><ul>
<li>HKEY_LOCAL_MACHINE\Software\Microsoft\Windows\CurrentVersion\Explorer\ShellIconOverlayIdentifiers\*</li>
<li>HKEY_LOCAL_MACHINE\Software\Wow6432Node\Microsoft\Windows\CurrentVersion\Explorer\ShellIconOverlayIdentifiers\*</li>
<li>HKEY_USERS\%SID%\Software\Microsoft\Windows\CurrentVersion\Explorer\ShellIconOverlayIdentifiers\*</li>
<li>HKEY_USERS\%SID%\Software\Wow6432Node\Microsoft\Windows\CurrentVersion\Explorer\ShellIconOverlayIdentifiers\*</li>
</ul></td>
</tr>
<tr class="even">
<td><p><b>Value name(s)</b></p></td>
<td><p>*</p></td>
</tr>
<tr class="odd">
<td><p><b>Additional information</b></p></td>
<td></td>
</tr>
</tbody>
</table>

<table>
<tbody>
<tr class="odd">
<td><p><b>Description</b></p></td>
<td><p>Shell Extensions</p></td>
</tr>
<tr class="even">
<td><p><b><a href="Artifacts" title="wikilink">Artifact
name</a></b></p></td>
<td><p>WindowsShellExtensions</p></td>
</tr>
<tr class="odd">
<td><p><b>Key path(s)</b></p></td>
<td><ul>
<li>HKEY_LOCAL_MACHINE\Software\Microsoft\Windows\CurrentVersion\Shell
Extensions\Approved</li>
<li>HKEY_LOCAL_MACHINE\Software\Wow6432Node\Microsoft\Windows\CurrentVersion\Shell
Extensions\Approved</li>
<li>HKEY_USERS\%SID%\Software\Microsoft\Windows\CurrentVersion\Shell
Extensions\Approved</li>
<li>HKEY_USERS\%SID%\Software\Wow6432Node\Microsoft\Windows\CurrentVersion\Shell
Extensions\Approved</li>
</ul></td>
</tr>
<tr class="even">
<td><p><b>Value name(s)</b></p></td>
<td><p>*</p></td>
</tr>
<tr class="odd">
<td><p><b>Additional information</b></p></td>
<td></td>
</tr>
</tbody>
</table>

<table>
<tbody>
<tr class="odd">
<td><p><b>Description</b></p></td>
<td><p>Shell Execute Hooks</p></td>
</tr>
<tr class="even">
<td><p><b><a href="Artifacts" title="wikilink">Artifact
name</a></b></p></td>
<td><p>WindowsShellExecuteHooks</p></td>
</tr>
<tr class="odd">
<td><p><b>Key path(s)</b></p></td>
<td><ul>
<li>HKEY_LOCAL_MACHINE\Software\Microsoft\Windows\CurrentVersion\Explorer\ShellExecuteHooks\*</li>
<li>HKEY_LOCAL_MACHINE\Software\Wow6432Node\Microsoft\Windows\CurrentVersion\Explorer\ShellExecuteHooks\*</li>
</ul></td>
</tr>
<tr class="even">
<td><p><b>Value name(s)</b></p></td>
<td><p>*</p></td>
</tr>
<tr class="odd">
<td><p><b>Additional information</b></p></td>
<td></td>
</tr>
</tbody>
</table>

<table>
<tbody>
<tr class="odd">
<td><p><b>Description</b></p></td>
<td><p>Shell Load and Run</p></td>
</tr>
<tr class="even">
<td><p><b><a href="Artifacts" title="wikilink">Artifact
name</a></b></p></td>
<td><p>WindowsShellLoadAndRun</p></td>
</tr>
<tr class="odd">
<td><p><b>Key path(s)</b></p></td>
<td><ul>
<li>HKEY_CURRENT_USER\Software\Microsoft\Windows
NT\CurrentVersion\Windows</li>
<li>HKEY_CURRENT_USER\Software\Wow6432Node\Microsoft\Windows
NT\CurrentVersion\Windows</li>
</ul></td>
</tr>
<tr class="even">
<td><p><b>Value name(s)</b></p></td>
<td><ul>
<li>Load</li>
<li>Run</li>
</ul></td>
</tr>
<tr class="odd">
<td><p><b>Additional information</b></p></td>
<td></td>
</tr>
</tbody>
</table>

<table>
<tbody>
<tr class="odd">
<td><p><b>Description</b></p></td>
<td><p>Shell Service Object Delay Load</p></td>
</tr>
<tr class="even">
<td><p><b><a href="Artifacts" title="wikilink">Artifact
name</a></b></p></td>
<td><p>WindowsShellServiceObjects</p></td>
</tr>
<tr class="odd">
<td><p><b>Key path(s)</b></p></td>
<td><ul>
<li>HKEY_LOCAL_MACHINE\Software\Microsoft\Windows\CurrentVersion\ShellServiceObjectDelayLoad</li>
<li>HKEY_LOCAL_MACHINE\Software\Wow6432Node\Microsoft\Windows\CurrentVersion\ShellServiceObjectDelayLoad</li>
</ul></td>
</tr>
<tr class="even">
<td><p><b>Value name(s)</b></p></td>
<td><p>*</p></td>
</tr>
<tr class="odd">
<td><p><b>Additional information</b></p></td>
<td><p><a
href="http://www.microsoft.com/security/portal/threat/encyclopedia/Entry.aspx?Name=TrojanClicker:Win32/Zirit.X#tab=2">TrojanClicker:Win32/Zirit.X</a></p></td>
</tr>
</tbody>
</table>

### Winlogon and Credential Providers

<table>
<tbody>
<tr class="odd">
<td><p><b>Description</b></p></td>
<td><p>Credential Provider Filters</p></td>
</tr>
<tr class="even">
<td><p><b><a href="Artifacts" title="wikilink">Artifact
name</a></b></p></td>
<td><p>WindowsCredentialProviderFilters</p></td>
</tr>
<tr class="odd">
<td><p><b>Key path(s)</b></p></td>
<td><ul>
<li>HKEY_LOCAL_MACHINE\Software\Microsoft\Windows\CurrentVersion\Authentication\Credential
Provider Filters\*</li>
<li>HKEY_LOCAL_MACHINE\Software\Wow6432Node\Microsoft\Windows\CurrentVersion\Authentication\Credential
Provider Filters\*</li>
</ul></td>
</tr>
<tr class="even">
<td><p><b>Value name(s)</b></p></td>
<td><p>*</p></td>
</tr>
<tr class="odd">
<td><p><b>Additional information</b></p></td>
<td><p><a
href="http://blog.leetsys.com/2012/01/02/capturing-windows-7-credentials-at-logon-using-custom-credential-provider/">Capturing
Windows 7 Credential at logon using custom credential
provider</a></p></td>
</tr>
</tbody>
</table>

<table>
<tbody>
<tr class="odd">
<td><p><b>Description</b></p></td>
<td><p>Credential Providers</p></td>
</tr>
<tr class="even">
<td><p><b><a href="Artifacts" title="wikilink">Artifact
name</a></b></p></td>
<td><p>WindowsCredentialProviders</p></td>
</tr>
<tr class="odd">
<td><p><b>Key path(s)</b></p></td>
<td><ul>
<li>HKEY_LOCAL_MACHINE\Software\Microsoft\Windows\CurrentVersion\Authentication\Credential
Providers\*</li>
<li>HKEY_LOCAL_MACHINE\Software\Wow6432Node\Microsoft\Windows\CurrentVersion\Authentication\Credential
Providers\*</li>
</ul></td>
</tr>
<tr class="even">
<td><p><b>Value name(s)</b></p></td>
<td><p>*</p></td>
</tr>
<tr class="odd">
<td><p><b>Additional information</b></p></td>
<td><p><a
href="http://blog.leetsys.com/2012/01/02/capturing-windows-7-credentials-at-logon-using-custom-credential-provider/">Capturing
Windows 7 Credential at logon using custom credential
provider</a></p></td>
</tr>
</tbody>
</table>

<table>
<tbody>
<tr class="odd">
<td><p><b>Description</b></p></td>
<td><p>Pre-Logon Access Provider (PLAP) Providers</p></td>
</tr>
<tr class="even">
<td><p><b><a href="Artifacts" title="wikilink">Artifact
name</a></b></p></td>
<td><p>WindowsPLAPProviders</p></td>
</tr>
<tr class="odd">
<td><p><b>Key path(s)</b></p></td>
<td><ul>
<li>HKEY_LOCAL_MACHINE\Software\Microsoft\Windows\CurrentVersion\Authentication\PLAP
Providers\*</li>
<li>HKEY_LOCAL_MACHINE\Software\Wow6432Node\Microsoft\Windows\CurrentVersion\Authentication\PLAP
Providers\*</li>
</ul></td>
</tr>
<tr class="even">
<td><p><b>Value name(s)</b></p></td>
<td><p>*</p></td>
</tr>
<tr class="odd">
<td><p><b>Additional information</b></p></td>
<td></td>
</tr>
</tbody>
</table>

<table>
<tbody>
<tr class="odd">
<td><p><b>Description</b></p></td>
<td><p>Winlogon Gina DLL</p></td>
</tr>
<tr class="even">
<td><p><b><a href="Artifacts" title="wikilink">Artifact
name</a></b></p></td>
<td><p>WindowsWinlogonShell</p></td>
</tr>
<tr class="odd">
<td><p><b>Key path(s)</b></p></td>
<td><ul>
<li>HKEY_LOCAL_MACHINE\Software\Microsoft\Windows
NT\CurrentVersion\Winlogon</li>
<li>HKEY_USERS\%SID%\Software\Microsoft\Windows
NT\CurrentVersion\Winlogon</li>
</ul></td>
</tr>
<tr class="even">
<td><p><b>Value name(s)</b></p></td>
<td><p>GinaDLL</p></td>
</tr>
<tr class="odd">
<td><p><b>Additional information</b></p></td>
<td></td>
</tr>
</tbody>
</table>

<table>
<tbody>
<tr class="odd">
<td><p><b>Description</b></p></td>
<td><p>Winlogon Notify</p></td>
</tr>
<tr class="even">
<td><p><b><a href="Artifacts" title="wikilink">Artifact
name</a></b></p></td>
<td><p>WindowsWinlogonNotify</p></td>
</tr>
<tr class="odd">
<td><p><b>Key path(s)</b></p></td>
<td><ul>
<li>HKEY_LOCAL_MACHINE\Software\Microsoft\Windows
NT\CurrentVersion\Winlogon\Notify\*</li>
<li>HKEY_USERS\%SID%\Software\Microsoft\Windows
NT\CurrentVersion\Winlogon\Notify\*</li>
</ul></td>
</tr>
<tr class="even">
<td><p><b>Value name(s)</b></p></td>
<td><p>DLLName</p></td>
</tr>
<tr class="odd">
<td><p><b>Additional information</b></p></td>
<td></td>
</tr>
</tbody>
</table>

<table>
<tbody>
<tr class="odd">
<td><p><b>Description</b></p></td>
<td><p>Winlogon Shell</p></td>
</tr>
<tr class="even">
<td><p><b><a href="Artifacts" title="wikilink">Artifact
name</a></b></p></td>
<td><p>WindowsWinlogonShell</p></td>
</tr>
<tr class="odd">
<td><p><b>Key path(s)</b></p></td>
<td><ul>
<li>HKEY_LOCAL_MACHINE\Software\Microsoft\Windows
NT\CurrentVersion\Winlogon</li>
<li>HKEY_USERS\%SID%\Software\Microsoft\Windows
NT\CurrentVersion\Winlogon</li>
</ul></td>
</tr>
<tr class="even">
<td><p><b>Value name(s)</b></p></td>
<td><p>Shell</p></td>
</tr>
<tr class="odd">
<td><p><b>Additional information</b></p></td>
<td></td>
</tr>
</tbody>
</table>

<table>
<tbody>
<tr class="odd">
<td><p><b>Description</b></p></td>
<td><p>Winlogon System</p></td>
</tr>
<tr class="even">
<td><p><b><a href="Artifacts" title="wikilink">Artifact
name</a></b></p></td>
<td><p>WindowsWinlogonSystem</p></td>
</tr>
<tr class="odd">
<td><p><b>Key path(s)</b></p></td>
<td><ul>
<li>HKEY_LOCAL_MACHINE\Software\Microsoft\Windows
NT\CurrentVersion\Winlogon</li>
<li>HKEY_USERS\%SID%\Software\Microsoft\Windows
NT\CurrentVersion\Winlogon</li>
</ul></td>
</tr>
<tr class="even">
<td><p><b>Value name(s)</b></p></td>
<td><p>System</p></td>
</tr>
<tr class="odd">
<td><p><b>Additional information</b></p></td>
<td></td>
</tr>
</tbody>
</table>

<table>
<tbody>
<tr class="odd">
<td><p><b>Description</b></p></td>
<td><p>Winlogon Taksman</p></td>
</tr>
<tr class="even">
<td><p><b><a href="Artifacts" title="wikilink">Artifact
name</a></b></p></td>
<td><p>WindowsWinlogonTaksman</p></td>
</tr>
<tr class="odd">
<td><p><b>Key path(s)</b></p></td>
<td><ul>
<li>HKEY_LOCAL_MACHINE\Software\Microsoft\Windows
NT\CurrentVersion\Winlogon</li>
<li>HKEY_USERS\%SID%\Software\Microsoft\Windows
NT\CurrentVersion\Winlogon</li>
</ul></td>
</tr>
<tr class="even">
<td><p><b>Value name(s)</b></p></td>
<td><p>Taksman</p></td>
</tr>
<tr class="odd">
<td><p><b>Additional information</b></p></td>
<td></td>
</tr>
</tbody>
</table>

<table>
<tbody>
<tr class="odd">
<td><p><b>Description</b></p></td>
<td><p>Winlogon Userinit</p></td>
</tr>
<tr class="even">
<td><p><b><a href="Artifacts" title="wikilink">Artifact
name</a></b></p></td>
<td><p>WindowsWinlogonUserinit</p></td>
</tr>
<tr class="odd">
<td><p><b>Key path(s)</b></p></td>
<td><ul>
<li>HKEY_LOCAL_MACHINE\Software\Microsoft\Windows
NT\CurrentVersion\Winlogon</li>
<li>HKEY_USERS\%SID%\Software\Microsoft\Windows
NT\CurrentVersion\Winlogon</li>
</ul></td>
</tr>
<tr class="even">
<td><p><b>Value name(s)</b></p></td>
<td><p>Userinit</p></td>
</tr>
<tr class="odd">
<td><p><b>Additional information</b></p></td>
<td></td>
</tr>
</tbody>
</table>

<table>
<tbody>
<tr class="odd">
<td><p><b>Description</b></p></td>
<td><p>Winlogon VMApplet</p></td>
</tr>
<tr class="even">
<td><p><b><a href="Artifacts" title="wikilink">Artifact
name</a></b></p></td>
<td><p>WindowsWinlogonVMApplet</p></td>
</tr>
<tr class="odd">
<td><p><b>Key path(s)</b></p></td>
<td><ul>
<li>HKEY_LOCAL_MACHINE\Software\Microsoft\Windows
NT\CurrentVersion\Winlogon</li>
<li>HKEY_USERS\%SID%\Software\Microsoft\Windows
NT\CurrentVersion\Winlogon</li>
</ul></td>
</tr>
<tr class="even">
<td><p><b>Value name(s)</b></p></td>
<td><p>VMApplet</p></td>
</tr>
<tr class="odd">
<td><p><b>Additional information</b></p></td>
<td></td>
</tr>
</tbody>
</table>

### Policy

<table>
<tbody>
<tr class="odd">
<td><p><b>Description</b></p></td>
<td><p>Windows System Policy replacement shell</p></td>
</tr>
<tr class="even">
<td><p><b><a href="Artifacts" title="wikilink">Artifact
name</a></b></p></td>
<td><p>WindowsSystemPolicyShell</p></td>
</tr>
<tr class="odd">
<td><p><b>Key path(s)</b></p></td>
<td><ul>
<li>HKEY_LOCAL_MACHINE\Software\Microsoft\Windows\CurrentVersion\Policies\System</li>
<li>HKEY_LOCAL_MACHINE\Software\Wow6432Node\Microsoft\Windows\CurrentVersion\Policies\System</li>
</ul></td>
</tr>
<tr class="even">
<td><p><b>Value name(s)</b></p></td>
<td><p>Shell</p></td>
</tr>
<tr class="odd">
<td><p><b>Additional information</b></p></td>
<td></td>
</tr>
</tbody>
</table>

### Unsorted

<table>
<tbody>
<tr class="odd">
<td><p><b>Description</b></p></td>
<td><p>Active Setup - Installed Components</p></td>
</tr>
<tr class="even">
<td><p><b><a href="Artifacts" title="wikilink">Artifact
name</a></b></p></td>
<td><p>WindowsStubPaths</p></td>
</tr>
<tr class="odd">
<td><p><b>Key path(s)</b></p></td>
<td><ul>
<li>HKEY_LOCAL_MACHINE\Software\Microsoft\Active Setup\Installed
Components</li>
<li>HKEY_LOCAL_MACHINE\Software\Wow6432Node\Microsoft\Active
Setup\Installed Components</li>
<li>HKEY_USERS\%SID%\Software\Microsoft\Active Setup\Installed
Components</li>
<li>HKEY_USERS\%SID%\Software\Wow6432Node\Microsoft\Active
Setup\Installed Components</li>
</ul></td>
</tr>
<tr class="even">
<td><p><b>Value name(s)</b></p></td>
<td><p>StubPath</p></td>
</tr>
<tr class="odd">
<td><p><b>Additional information</b></p></td>
<td></td>
</tr>
</tbody>
</table>

<table>
<tbody>
<tr class="odd">
<td><p><b>Description</b></p></td>
<td><p>Application Initial (AppInit) DLLs persistence</p></td>
</tr>
<tr class="even">
<td><p><b><a href="Artifacts" title="wikilink">Artifact
name</a></b></p></td>
<td><p>WindowsAppInitDLLs</p></td>
</tr>
<tr class="odd">
<td><p><b>Key path(s)</b></p></td>
<td><ul>
<li>HKEY_LOCAL_MACHINE\Software\Microsoft\Windows
NT\CurrentVersion\Windows</li>
<li>HKEY_LOCAL_MACHINE\Software\Wow6432Node\Microsoft\Windows
NT\CurrentVersion\Windows</li>
<li>HKEY_USERS\%%users.sid%%\Software\Microsoft\Windows
NT\CurrentVersion\Windows</li>
<li>HKEY_USERS\%%users.sid%%\Software\Wow6432Node\Microsoft\Windows
NT\CurrentVersion\Windows</li>
</ul></td>
</tr>
<tr class="even">
<td><p><b>Value name(s)</b></p></td>
<td><p>AppInit_DLLs</p></td>
</tr>
<tr class="odd">
<td><p><b>Additional information</b></p></td>
<td></td>
</tr>
</tbody>
</table>

<table>
<tbody>
<tr class="odd">
<td><p><b>Description</b></p></td>
<td><p>Security Providers</p></td>
</tr>
<tr class="even">
<td><p><b><a href="Artifacts" title="wikilink">Artifact
name</a></b></p></td>
<td><p>WindowsSecurityProviders</p></td>
</tr>
<tr class="odd">
<td><p><b>Key path(s)</b></p></td>
<td><ul>
<li>HKEY_LOCAL_MACHINE\System\CurrentControlSet\Control\SecurityProviders\*</li>
</ul></td>
</tr>
<tr class="even">
<td><p><b>Value name(s)</b></p></td>
<td><p>*</p></td>
</tr>
<tr class="odd">
<td><p><b>Additional information</b></p></td>
<td></td>
</tr>
</tbody>
</table>

<table>
<tbody>
<tr class="odd">
<td><p><b>Description</b></p></td>
<td><p>Alternate shell</p></td>
</tr>
<tr class="even">
<td><p><b><a href="Artifacts" title="wikilink">Artifact
name</a></b></p></td>
<td><p>WindowsAlternateShell</p></td>
</tr>
<tr class="odd">
<td><p><b>Key path(s)</b></p></td>
<td><ul>
<li>HKEY_LOCAL_MACHINE\System\CurrentControlSet\Control\SafeBoot</li>
</ul></td>
</tr>
<tr class="even">
<td><p><b>Value name(s)</b></p></td>
<td><p>AlternateShell</p></td>
</tr>
<tr class="odd">
<td><p><b>Additional information</b></p></td>
<td></td>
</tr>
</tbody>
</table>

<table>
<tbody>
<tr class="odd">
<td><p><b>Description</b></p></td>
<td><p>Boot verification program</p></td>
</tr>
<tr class="even">
<td><p><b><a href="Artifacts" title="wikilink">Artifact
name</a></b></p></td>
<td><p>WindowsBootVerificationProgram</p></td>
</tr>
<tr class="odd">
<td><p><b>Key path(s)</b></p></td>
<td><ul>
<li>HKEY_LOCAL_MACHINE\System\CurrentControlSet\Control\BootVerificationProgram</li>
</ul></td>
</tr>
<tr class="even">
<td><p><b>Value name(s)</b></p></td>
<td><p>ImagePath</p></td>
</tr>
<tr class="odd">
<td><p><b>Additional information</b></p></td>
<td></td>
</tr>
</tbody>
</table>

## Bibliography

* [Using ShellBag Information to Reconstruct User Activities](http://www.dfrws.org/2009/proceedings/p69-zhu.pdf), by
  Yuandong Zhu\*, Pavel Gladyshev, Joshua James, DFRWS 2009
* [The Windows NT Registry File Format](http://www.sentinelchicken.com/research/registry_format/), by
  Timothy Morgan, June 9, 2009
* [Recovering Deleted Data From the Windows Registry](http://www.dfrws.org/2008/proceedings/p33-morgan.pdf) and
  [slides](http://www.dfrws.org/2008/proceedings/p33-morgan_pres.pdf),
  by Timothy Morgan, DFRWS 2008
* [Forensic Analysis of the Windows Registry in Memory](https://dfrws.org/sites/default/files/session-files/2008_USA_paper-forensic_analysis_of_the_windows_registry_in_memory.pdf) and
  [slides](https://dfrws.org/sites/default/files/session-files/2008_USA_pres-forensic_analysis_of_the_windows_registry_in_memory.pdf),
  by Brendan Dolan-Gavitt, DFRWS 2008
* [Forensic analysis of unallocated space in Windows Registry Hive files](http://www.sentinelchicken.com/data/JolantaThomassenDISSERTATION.pdf),
  by Jolanta Thomassen, March 11, 2008
* [The Windows Registry as a forensic resource](http://www.sciencedirect.com/science?_ob=ArticleURL&_udi=B7CW4-4GX1J3B-1&_user=3326500&_rdoc=1&_fmt=&_orig=search&_sort=d&view=c&_acct=C000060280&_version=1&_urlVersion=0&_userid=3326500&md5=ab887593e7be6d5257696707886978f1),
  Digital Investigation, Volume 2, Issue 3, September 2005, Pages
  201--205.
* [Windows registry file format specification](https://github.com/msuhanov/regf/blob/master/Windows%20registry%20file%20format%20specification.md),
  by Maxim Suhanov, 2015-2016

### Undated

* [A Windows Registry Quick Reference: For the Everyday Examiner](https://www.iapsonline.com/sites/default/files/A%20Windows%20Registry%20Quick%20Reference-%20For%20the%20Everyday%20Examiner%20-%20By%20Derrick%20J.%20Farmer.pdf),
  by Derrick Farmer, Burlington, VT.
* [Forensic Analysis of the Windows Registry](https://forensicfocus.com/articles/forensic-analysis-of-the-windows-registry/),
  by Lih Wern Wong , School of Computer and Information Science, Edith
  Cowan University

## Also see

* [Boot Configuration Data](windows_boot_configuration_data.md)

## External Links

* [Wikipedia: Windows Registry](https://en.wikipedia.org/wiki/Windows_Registry)
* [Windows Incident Response Articles on Registry](https://windowsir.blogspot.com/search/label/Registry)
* [Windows Registry Information](https://www.answers.com/redirectSearch?query=win-registry)
* [Push the Red Button](https://moyix.blogspot.com/search/label/registry)
* [Security Accounts Manager](http://survey-smiles.com)
* [Registry MRU Locations](http://windowsxp.mvps.org/RegistryMRU.htm)
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

* [Cached Credentials](http://juggernaut.wikidot.com/cached-credentials),
  by Juggernaut

### Mounted Devices

* [Registry Analysis (Windows Forensic Analysis) Part 6](http://what-when-how.com/windows-forensic-analysis/registry-analysis-windows-forensic-analysis-part-6/),
  September 2011

### Persistence keys

* [Understand and Control Startup Apps with the System Configuration Utility](https://learn.microsoft.com/en-us/previous-versions/technet-magazine/ee851671(v=msdn.10)),
  by [Microsoft Technet](microsoft.md)
* [Silent Runners](https://www.silentrunners.org/), by Andrew Aronoff
* [Beyond good ol’ Run key](http://www.hexacorn.com/blog/2012/07/23/beyond-good-ol-run-key/),
  Hexacorn blog, July 23, 2012
* [Plugins: soft_run user_run](http://journeyintoir.blogspot.com/2013_04_01_archive.html),
  by Corey Harrell, April 17, 2013
* [Auto-Start Extensibility Points (ASEPs)](https://code.google.com/archive/p/regripper/wikis/ASEPs.wiki),
  by the [RegRipper project](regripper.md), April 29, 2013
* [Volatility autoruns plugin](https://github.com/tomchop/volatility-autoruns/blob/master/README.md),
  by the [Volatility project](volatility_framework.md), April 14, 2015

### User Assist

* [UserAssist](https://blog.didierstevens.com/programs/userassist/), by
  Didier Stevens
* [UserAssist V2.3.0](https://blog.didierstevens.com/2007/07/17/userassist-v230/), by
  Didier Stevens, Tuesday 17 July 2007
* [More on (the) UserAssist keys](https://windowsir.blogspot.com/2007/09/more-on-userassist-keys.html),
  by [Harlan Carvey](harlan_carvey.md), Monday, September 03,
  2007
* [Windows 7 Beta: ROT13 Replaced With Vigenère? Great Joke!](https://blog.didierstevens.com/2009/01/18/quickpost-windows-7-beta-rot13-replaced-with-vigenere-great-joke/),
  by Didier Stevens, January 18, 2009
* [Prefetch and User Assist](http://forensicsfromthesausagefactory.blogspot.com/2010/05/prefetch-and-user-assist.html),
  by DC174, Thursday, 27 May 2010
* [UserAssist Forensics (timelines, interpretation, testing, & more)](https://www.4n6k.com/2013/05/userassist-forensics-timelines.html),
  by Dan (@4n6k), Tuesday, May 14, 2013
* [Daily Blog \#45: Understanding the artifacts: User Assist](https://www.hecfblog.com/2013/08/daily-blog-45-understanding-artifacts.html),
  by David Cowen, Wednesday, August 7, 2013

## Tools

### Open Source

* [Forensic Registry EDitor (fred)](https://www.pinguin.lu/index.php) -
  "Forensic Registry EDitor (fred) is a cross-platform M\$ registry hive
  editor" by Daniel Gillen
* [libregfi](http://projects.sentinelchicken.org/data/doc/reglookup/regfi/) -
  The regfi library is a read-only NT registry library which serves as
  the main engine behind the reglookup tool
* [reglookup](http://projects.sentinelchicken.org/reglookup/) — "small
  command line utility for reading and querying Windows NT-based
  registries."
* [regviewer](https://sourceforge.net/projects/regviewer/) — a tool for
  looking at the registry.
* [RegRipper](regripper.md) — "the fastest, easiest, and best
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

* [cafae](http://tzworks.net/prototype_page.php?proto_id=19) -
  Computer Account Forensic Artifact Extractor. Free tool that can be
  run on Windows, Linux or Mac OS-X to parse ntuser.dat hives.
* [Regisry Manager](http://www.stellarinfo.com/windows-tools/registry-cleaner.php)
* [Abexo Free Regisry Cleaner](http://www.abexo.com/free-registry-cleaner.htm)
* [Auslogics Registry Defrag](https://www.auslogics.com/en/software/registry-defrag/)
* [Alien Registry Viewer](http://lastbit.com/arv/default.asp)
* [NT Registry Optimizer](http://www.larshederer.homepage.t-online.de/erunt/index.htm)
* [iExpert Software-Free Registry Defrag](https://cumdiner.com/categories/)
* [Registry Undelete (russian)](http://paullee.ru/regundel)
* [Windows Registry Recovery](http://mitec.cz/wrr.html)
* [Registry Tool](http://registrytool.com/)
