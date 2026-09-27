---
tags:
  - Windows
---
Windows Update is a core Microsoft service that automates the downloading and
installation of software patches, drivers, and security updates.

From a digital forensics and incident response (DFIR) perspective, analyzing
Windows Update activity can be beneficial for reconstructing system timelines,
determining patch levels, and identifying potential anti-forensics or
exploitation attempts.

## Windows Update Status

The following registry keys and values indicate Windows Update status.

```text
HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows\CurrentVersion\WindowsUpdate\Auto Update\Results\Detect
```

| Entry Name | Data Type | Value |
| --- | --- | --- |
| LastError | REG_DWORD | 0 for success |
| LastSuccessTime | REG_SZ | UTC time string of the last successful contact with Windows Update servers, e.g. 2013-05-14 12:41:26 |

```text
HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows\CurrentVersion\WindowsUpdate\Auto Update\Results\Download
```

| Entry Name | Data Type | Value |
| --- | --- | --- |
| LastError | REG_DWORD | 0 for success |
| LastSuccessTime | REG_SZ | UTC time string of last successful update download e.g. 2013-05-14 12:41:26 |

```text
HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows\CurrentVersion\WindowsUpdate\Auto Update\Results\Install
```

| Entry Name | Data Type | Value |
| --- | --- | --- |
| LastError | REG_DWORD | 0 for success |
| LastSuccessTime | REG_SZ | UTC time string of last successful update install e.g. 2013-05-14 12:41:26 |
