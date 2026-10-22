---
tags:
  - File Formats
  - Text
  - Windows
---
## Overview

On [Windows](windows.md) a .JOB file specifies task configuration. A .JOB file
consists of two main sections, fixed-length and variable-length.

### Fixed-length section

The fixed-length section is 68 bytes in size and consists of:

| Offset | Size | Value | Description |
| --- | --- | --- | --- |
| 0 | 2 | | Product version |
| 2 | 2 | 1 | File (format) version |
| 4 | 16 | | Job UUID (or GUID) |
| 20 | 2 | | Application name size offset. The offset is relative from the start of the file. |
| 22 | 2 | | Trigger offset. The offset is relative from the start of the file. |
| 24 | 2 | | Error Retry Count |
| 26 | 2 | | Error Retry Interval |
| 28 | 2 | | Idle Deadline |
| 30 | 2 | | Idle Wait |
| 32 | 4 | | Priority |
| 36 | 4 | | Maximum Run Time |
| 40 | 4 | | Exit Code |
| 44 | 4 | | Status |
| 48 | 4 | | Flags |
| 52 | 16 | | Last run time. Consists of a SYSTEMTIME |

#### Product version

| Value | Identifier | Description |
| --- | --- | --- |
| 0x0400 | | Windows NT 4.0 |
| 0x0500 | | Windows 2000 |
| 0x0501 | | Windows XP |
| 0x0600 | | Windows Vista |
| 0x0601 | | Windows 7 |
| 0x0602 | | Windows 8 |
| 0x0603 | | Windows 8.1 |
| 0x0a00 | | Windows 10 |

#### Priority

| Value | Identifier | Description |
| --- | --- | --- |
| 0x00800000 | REALTIME_PRIORITY_CLASS | The task can run at the highest possible priority. The threads of a real-time priority class process preempt the threads of all other processes, including operating system processes performing important tasks. |
| 0x01000000 | HIGH_PRIORITY_CLASS | The task performs time-critical tasks that can be executed immediately for it to run correctly. The threads of a high-priority class process preempt the threads of normal or idle priority class processes. |
| 0x02000000 | IDLE_PRIORITY_CLASS | The task can run in a process whose threads run only when the machine is idle, and are preempted by the threads of any process running in a higher priority class. |
| 0x04000000 | NORMAL_PRIORITY_CLASS | The task has no special scheduling requirements. |

#### Status

| Value | Identifier | Description |
| --- | --- | --- |
| 0x00041300 | SCHED_S_TASK_READY | Task is not running but is scheduled to run at some time in the future. |
| 0x00041301 | SCHED_S_TASK_RUNNING | Task is currently running. |
| 0x00041305 | SCHED_S_TASK_NOT_SCHEDULED | The task is not running and has no valid triggers. |

#### Flags

See: [Flags](https://learn.microsoft.com/en-us/openspecs/windows_protocols/ms-tsch/3b4cd410-105a-48be-8379-81c84bfcafbe)

#### SYSTEMTIME

| Offset | Size | Value | Description |
| --- | --- | --- | --- |
| 0 | 2 | | Year |
| 2 | 2 | | Month |
| 4 | 2 | | Weekday |
| 6 | 2 | | Day |
| 8 | 2 | | Hour |
| 10 | 2 | | Minute |
| 12 | 2 | | Second |
| 14 | 2 | | Milli second |

### Variable-length section

The variable-length section is variable in size and consists of:

| Offset | Size | Value | Description |
| --- | --- | --- | --- |
| 0 | 2 | | Running Instance Count |
| 2 | ... | | Application Name. Consists of a Unicode string. |
| ... | ... | | Parameters. Consists of a Unicode string. |
| ... | ... | | Working Directory. Consists of a Unicode string. |
| ... | ... | | Author. Consists of a Unicode string. |
| ... | ... | | Comment. Consists of a Unicode string. |
| ... | ... | | User Data |
| ... | ... | | Reserved Data |
| ... | ... | | Triggers |
| ... | ... | | Job Signature |

These values are stored as Unicode strings.

#### Unicode string

| Offset | Size | Value | Description |
| --- | --- | --- | --- |
| 0 | 2 | | Number of characters. The value will be 0 if the string is empty. |
| 2 | ... | | String. UTF-16 little-endian with end-of-string character |

#### User Data

| Offset | Size | Value | Description |
| --- | --- | --- | --- |
| 0 | 2 | | data size |
| 2 | ... | | data |

#### Reserved Data

The Reserved Data is similar in structure as the User Data though if a
size is set, is should be 8 and the Reserved Data consists of:

| Offset | Size | Value | Description |
| --- | --- | --- | --- |
| 0 | 2 | 8 | data size |
| 2 | 4 | | Start Error |
| 6 | 4 | | Task Flags |

#### Triggers

| Offset | Size | Value | Description |
| --- | --- | --- | --- |
| 0 | 2 | | Number of triggers |
| 2 | ... | | Array of triggers |

##### Trigger

| Offset | Size | Value | Description |
| --- | --- | --- | --- |
| 0 | 2 | | Trigger Size |
| 2 | 2 | | Reserved1 |
| 4 | 2 | | Begin Year |
| 6 | 2 | | Begin Month |
| 8 | 2 | | Begin Day |
| 10 | 2 | | End Year |
| 12 | 2 | | End Month |
| 14 | 2 | | End Day |
| 16 | 2 | | Start Hour |
| 18 | 2 | | Start Minute |
| 20 | 4 | | Minutes Duration |
| 24 | 4 | | Minutes Interval |
| 28 | 4 | | Flags |
| 32 | 4 | | Trigger Type |
| 36 | 2 | | TriggerSpecific0 |
| 38 | 2 | | TriggerSpecific1 |
| 40 | 2 | | TriggerSpecific2 |
| 42 | 2 | | Padding |
| 44 | 2 | | Reserved2 |
| 46 | 2 | | Reserved3 |

##### Trigger type

| Value | Identifier | Description |
| --- | --- | --- |
| 0x00000000 | ONCE | Not used |
| 0x00000001 | DAILY | |
| 0x00000002 | WEEKLY | |
| 0x00000003 | MONTHLYDATE | |
| 0x00000004 | MONTHLYDOW | |
| 0x00000005 | EVENT_ON_IDLE | Not used |
| 0x00000006 | EVENT_AT_SYSTEMSTART | Not used |
| 0x00000007 | EVENT_AT_LOGON | Not used |

#### Job Signature

| Offset | Size | Value | Description |
| --- | --- | --- | --- |
| 0 | 2 | 1 | Signature version |
| 2 | 2 | 1 | Minimum client version |
| 4 | 64 | | Signature |

## See Also

* [Windows](windows.md)

## External Links

* [.JOB File Format](https://learn.microsoft.com/en-us/openspecs/windows_protocols/ms-tsch/96446df7-7683-40e0-a713-b01933b93b18),
  by [Microsoft](microsoft.md)
