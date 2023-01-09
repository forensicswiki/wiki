---
tags:
  -  File Formats
  -  Windows
  -  Text
---
## Overview

On [Windows](windows.md) a .JOB file specifies task
configuration. A .JOB file consists of two main sections, fixed-length
and variable-length.

### Fixed-length section

The fixed-length section is 68 bytes in size and consists of:

<table>
<thead>
<tr class="header">
<th><p>offset</p></th>
<th><p>size</p></th>
<th><p>value</p></th>
<th><p>description</p></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><p>0</p></td>
<td><p>2</p></td>
<td></td>
<td><p>Product version</p></td>
</tr>
<tr class="even">
<td><p>2</p></td>
<td><p>2</p></td>
<td><p>1</p></td>
<td><p>File (format) version</p></td>
</tr>
<tr class="odd">
<td><p>4</p></td>
<td><p>16</p></td>
<td></td>
<td><p>Job UUID (or GUID)</p></td>
</tr>
<tr class="even">
<td><p>20</p></td>
<td><p>2</p></td>
<td></td>
<td><p>Application name size offset<br />
The offset is relative from the start of the file.</p></td>
</tr>
<tr class="odd">
<td><p>22</p></td>
<td><p>2</p></td>
<td></td>
<td><p>Trigger offset<br />
The offset is relative from the start of the file.</p></td>
</tr>
<tr class="even">
<td><p>24</p></td>
<td><p>2</p></td>
<td></td>
<td><p>Error Retry Count</p></td>
</tr>
<tr class="odd">
<td><p>26</p></td>
<td><p>2</p></td>
<td></td>
<td><p>Error Retry Interval</p></td>
</tr>
<tr class="even">
<td><p>28</p></td>
<td><p>2</p></td>
<td></td>
<td><p>Idle Deadline</p></td>
</tr>
<tr class="odd">
<td><p>30</p></td>
<td><p>2</p></td>
<td></td>
<td><p>Idle Wait</p></td>
</tr>
<tr class="even">
<td><p>32</p></td>
<td><p>4</p></td>
<td></td>
<td><p>Priority</p></td>
</tr>
<tr class="odd">
<td><p>36</p></td>
<td><p>4</p></td>
<td></td>
<td><p>Maximum Run Time</p></td>
</tr>
<tr class="even">
<td><p>40</p></td>
<td><p>4</p></td>
<td></td>
<td><p>Exit Code</p></td>
</tr>
<tr class="odd">
<td><p>44</p></td>
<td><p>4</p></td>
<td></td>
<td><p>Status</p></td>
</tr>
<tr class="even">
<td><p>48</p></td>
<td><p>4</p></td>
<td></td>
<td><p>Flags</p></td>
</tr>
<tr class="odd">
<td><p>52</p></td>
<td><p>16</p></td>
<td></td>
<td><p>Last run time<br />
Consists of a SYSTEMTIME</p></td>
</tr>
</tbody>
</table>

#### Product version

| Value  | Identifier | Description    |
|--------|------------|----------------|
| 0x0400 |            | Windows NT 4.0 |
| 0x0500 |            | Windows 2000   |
| 0x0501 |            | Windows XP     |
| 0x0600 |            | Windows Vista  |
| 0x0601 |            | Windows 7      |
| 0x0602 |            | Windows 8      |
| 0x0603 |            | Windows 8.1    |
| 0x0a00 |            | Windows 10     |

#### Priority

| Value      | Identifier              | Description                                                                                                                                                                                                       |
|------------|-------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 0x00800000 | REALTIME_PRIORITY_CLASS | The task can run at the highest possible priority. The threads of a real-time priority class process preempt the threads of all other processes, including operating system processes performing important tasks. |
| 0x01000000 | HIGH_PRIORITY_CLASS     | The task performs time-critical tasks that can be executed immediately for it to run correctly. The threads of a high-priority class process preempt the threads of normal or idle priority class processes.      |
| 0x02000000 | IDLE_PRIORITY_CLASS     | The task can run in a process whose threads run only when the machine is idle, and are preempted by the threads of any process running in a higher priority class.                                                |
| 0x04000000 | NORMAL_PRIORITY_CLASS   | The task has no special scheduling requirements.                                                                                                                                                                  |

#### Status

| Value      | Identifier                  | Description                                                             |
|------------|-----------------------------|-------------------------------------------------------------------------|
| 0x00041300 | SCHED_S_TASK_READY         | Task is not running but is scheduled to run at some time in the future. |
| 0x00041301 | SCHED_S_TASK_RUNNING       | Task is currently running.                                              |
| 0x00041305 | SCHED_S_TASK_NOT_SCHEDULED | The task is not running and has no valid triggers.                      |

#### Flags

See: [Flags](https://learn.microsoft.com/en-us/openspecs/windows_protocols/ms-tsch/3b4cd410-105a-48be-8379-81c84bfcafbe)

#### SYSTEMTIME

| offset | size | value | description  |
|--------|------|-------|--------------|
| 0      | 2    |       | Year         |
| 2      | 2    |       | Month        |
| 4      | 2    |       | Weekday      |
| 6      | 2    |       | Day          |
| 8      | 2    |       | Hour         |
| 10     | 2    |       | Minute       |
| 12     | 2    |       | Second       |
| 14     | 2    |       | Milli second |

### Variable-length section

The variable-length section is variable in size and consists of:

<table>
<thead>
<tr class="header">
<th><p>offset</p></th>
<th><p>size</p></th>
<th><p>value</p></th>
<th><p>description</p></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><p>0</p></td>
<td><p>2</p></td>
<td></td>
<td><p>Running Instance Count</p></td>
</tr>
<tr class="even">
<td><p>2</p></td>
<td><p>...</p></td>
<td></td>
<td><p>Application Name<br />
Consists of a Unicode string.</p></td>
</tr>
<tr class="odd">
<td><p>...</p></td>
<td><p>...</p></td>
<td></td>
<td><p>Parameters<br />
Consists of a Unicode string.</p></td>
</tr>
<tr class="even">
<td><p>...</p></td>
<td><p>...</p></td>
<td></td>
<td><p>Working Directory<br />
Consists of a Unicode string.</p></td>
</tr>
<tr class="odd">
<td><p>...</p></td>
<td><p>...</p></td>
<td></td>
<td><p>Author<br />
Consists of a Unicode string.</p></td>
</tr>
<tr class="even">
<td><p>...</p></td>
<td><p>...</p></td>
<td></td>
<td><p>Comment<br />
Consists of a Unicode string.</p></td>
</tr>
<tr class="odd">
<td><p>...</p></td>
<td><p>...</p></td>
<td></td>
<td><p>User Data</p></td>
</tr>
<tr class="even">
<td><p>...</p></td>
<td><p>...</p></td>
<td></td>
<td><p>Reserved Data</p></td>
</tr>
<tr class="odd">
<td><p>...</p></td>
<td><p>...</p></td>
<td></td>
<td><p>Triggers</p></td>
</tr>
<tr class="even">
<td><p>...</p></td>
<td><p>...</p></td>
<td></td>
<td><p>Job Signature</p></td>
</tr>
</tbody>
</table>

These values are stored as Unicode strings.

#### Unicode string

<table>
<thead>
<tr class="header">
<th><p>offset</p></th>
<th><p>size</p></th>
<th><p>value</p></th>
<th><p>description</p></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><p>0</p></td>
<td><p>2</p></td>
<td></td>
<td><p>Number of characters<br />
The value will be 0 if the string is empty.</p></td>
</tr>
<tr class="even">
<td><p>2</p></td>
<td><p>...</p></td>
<td></td>
<td><p>String<br />
UTF-16 little-endian with end-of-string character</p></td>
</tr>
</tbody>
</table>

#### User Data

| offset | size | value | description |
|--------|------|-------|-------------|
| 0      | 2    |       | data size   |
| 2      | ...  |       | data        |

#### Reserved Data

The Reserved Data is similar in structure as the User Data though if a
size is set, is should be 8 and the Reserved Data consists of:

| offset | size | value | description |
|--------|------|-------|-------------|
| 0      | 2    | 8     | data size   |
| 2      | 4    |       | Start Error |
| 6      | 4    |       | Task Flags  |

#### Triggers

| offset | size | value | description        |
|--------|------|-------|--------------------|
| 0      | 2    |       | Number of triggers |
| 2      | ...  |       | Array of triggers  |

##### Trigger

| offset | size | value | description      |
|--------|------|-------|------------------|
| 0      | 2    |       | Trigger Size     |
| 2      | 2    |       | Reserved1        |
| 4      | 2    |       | Begin Year       |
| 6      | 2    |       | Begin Month      |
| 8      | 2    |       | Begin Day        |
| 10     | 2    |       | End Year         |
| 12     | 2    |       | End Month        |
| 14     | 2    |       | End Day          |
| 16     | 2    |       | Start Hour       |
| 18     | 2    |       | Start Minute     |
| 20     | 4    |       | Minutes Duration |
| 24     | 4    |       | Minutes Interval |
| 28     | 4    |       | Flags            |
| 32     | 4    |       | Trigger Type     |
| 36     | 2    |       | TriggerSpecific0 |
| 38     | 2    |       | TriggerSpecific1 |
| 40     | 2    |       | TriggerSpecific2 |
| 42     | 2    |       | Padding          |
| 44     | 2    |       | Reserved2        |
| 46     | 2    |       | Reserved3        |

##### Trigger type

| Value      | Identifier           | Description |
|------------|----------------------|-------------|
| 0x00000000 | ONCE                 | Not used    |
| 0x00000001 | DAILY                |             |
| 0x00000002 | WEEKLY               |             |
| 0x00000003 | MONTHLYDATE          |             |
| 0x00000004 | MONTHLYDOW           |             |
| 0x00000005 | EVENT_ON_IDLE        | Not used    |
| 0x00000006 | EVENT_AT_SYSTEMSTART | Not used    |
| 0x00000007 | EVENT_AT_LOGON       | Not used    |

#### Job Signature

| offset | size | value | description            |
|--------|------|-------|------------------------|
| 0      | 2    | 1     | Signature version      |
| 2      | 2    | 1     | Minimum client version |
| 4      | 64   |       | Signature              |

## See Also

- [Windows](windows.md)

## External Links

- [.JOB File
  Format](https://learn.microsoft.com/en-us/openspecs/windows_protocols/ms-tsch/96446df7-7683-40e0-a713-b01933b93b18), by
  [Microsoft](microsoft.md)

