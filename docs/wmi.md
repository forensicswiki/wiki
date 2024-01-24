---
tags:
  -  Articles that need to be expanded
  -  Windows
---
Windows Management Instrumentation (WMI) is the infrastructure for
management data and operations on Windows-based operating systems. It is
Microsoft's implementation of Web-Based Enterprise Management (WBEM).

WMI uses the Common Information Model (CIM) to represent classes of
information. CIM is developed and maintained by the DMTF (formerly known
as the Distributed Management Task Force).

The Managed Object Format (MOF) is the language used to describe Common
Information Model (CIM) classes.

The CIM database [consists of multiple
files](https://github.com/libyal/dtformats/blob/main/documentation/WMI%20repository%20file%20format.asciidoc)
(OBJECTS.DATA, MAPPING\*.MAP, INDEX.BTR and prior to Windows Vista
MAPPING.VER) that are located in the following directories:

    "C:\Windows\System32\WBEM\repository\" on Vista+
    "C:\Windows\System32\WBEM\repository\FS\" on WinXP/Win2003

There could also be [copies of the CIM database
files](https://www.4n6ir.com/posts/2017/secret-archives-of-execution-evidence-ccm_recentlyusedapps/),
in the following locations:

    "C:\Windows\System32\WBEM\repository.001\"
    "C:\Windows\System32\WBEM\repository.001\FS\"
    "C:\Windows\System32\WBEM\repository.002\"
    "C:\Windows\System32\WBEM\repository.002\FS\"
    ...

## External Links

* [Windows Management Instrumentation](https://learn.microsoft.com/en-us/windows/win32/wmisdk/wmi-start-page),
  by Microsoft
* [Common Information Model](https://learn.microsoft.com/en-us/windows/win32/wmisdk/common-information-model),
  by Microsoft
* [Managed Object Format (MOF)](https://learn.microsoft.com/en-us/windows/win32/wmisdk/managed-object-format--mof-),
  by Microsoft
* [WMI Command-line Tools](https://learn.microsoft.com/en-us/windows/win32/wmisdk/wmi-command-line-tools),
  by Microsoft
* [CIM Schemas](https://www.dmtf.org/standards/cim/schemas/), by DMTF
  (formerly known as the Distributed Management Task Force)

### Namespaces

* [Understanding WMI Namespaces](https://powershell.one/wmi/root)
* [Configuration Manager WMI namespaces and classes for Configuration Manager reports](https://learn.microsoft.com/en-us/mem/configmgr/develop/core/understand/sqlviews/wmi-namespaces-classes-configuration-manager-reports),
  by Microsoft

### Malware and intrusion analysis

* [Understanding WMI Malware](https://www.trendmicro.com/de_de/business.html),
  by Julius Dizon, Lennard Galang, and Marvin Cruz, July 2010
* [Abusing Windows Management Instrumentation (WMI) to Build a Persistent, Asyncronous, and Fileless Backdoor](https://www.blackhat.com/docs/us-15/materials/us-15-Graeber-Abusing-Windows-Management-Instrumentation-WMI-To-Build-A-Persistent%20Asynchronous-And-Fileless-Backdoor-wp.pdf),
  by Matt Graeber, 2015
* [Subverting Sysmon Application of a Formalized: Security Product Evasion Methodology](https://i.blackhat.com/us-18/Wed-August-8/us-18-Graeber-Subverting-Sysmon-Application-Of-A-Formalized-Security-Product-Evasion-Methodology-wp.pdf),
  by Matt Graeber, Lee Christensen, 2018
* [WmiEventConsumerClassDerivation.ps1](https://gist.github.com/mattifestation/f38a79c7983208aa230030f61dfeb767),
  by Matt Graeber, June 21, 2019

### Evidence of File Execution

* [Do You See What I CCM?](https://www.trellix.com/en-us/about/newsroom/stories/research.html),
  by David Pany, Fred House, December 15, 2016
* [Secret Archives of Execution Evidence: CCM_RecentlyUsedApps](https://www.4n6ir.com/posts/2017/secret-archives-of-execution-evidence-ccm_recentlyusedapps/),
  by James Habben, February 28, 2017
* [WMI_Forensics](https://github.com/davidpany/WMI_Forensics), by David
  Pany, Sept 1, 2017
