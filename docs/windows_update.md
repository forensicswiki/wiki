---
tags:
  -  Articles that need to be expanded
---
TODO: general windows update intro.

## Windows Update Status

The following registry keys and values indicate Windows Update status.

    HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows\CurrentVersion\WindowsUpdate\Auto Update\Results\Detect

| Entry Name      | Data Type | Value                                                                                                |
|-----------------|-----------|------------------------------------------------------------------------------------------------------|
| LastError       | REG_DWORD | 0 for success                                                                                        |
| LastSuccessTime | REG_SZ    | UTC time string of the last successful contact with Windows Update servers, e.g. 2013-05-14 12:41:26 |
|                 |           |                                                                                                      |

    HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows\CurrentVersion\WindowsUpdate\Auto Update\Results\Download

| Entry Name      | Data Type | Value                                                                       |
|-----------------|-----------|-----------------------------------------------------------------------------|
| LastError       | REG_DWORD | 0 for success                                                               |
| LastSuccessTime | REG_SZ    | UTC time string of last successful update download e.g. 2013-05-14 12:41:26 |
|                 |           |                                                                             |

    HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows\CurrentVersion\WindowsUpdate\Auto Update\Results\Install

| Entry Name      | Data Type | Value                                                                      |
|-----------------|-----------|----------------------------------------------------------------------------|
| LastError       | REG_DWORD | 0 for success                                                              |
| LastSuccessTime | REG_SZ    | UTC time string of last successful update install e.g. 2013-05-14 12:41:26 |
|                 |           |                                                                            |