---
tags:
  - Applications
  - Anti Virus
---
## Quarantine directory

The Quarantine directory can be found in the following locations:

On Windows XP:

```text
C:\documents and settings\All Users\Application Data\Sophos\Sophos Anti-Virus\INFECTED
```

On Windows 7:

```text
C:\ProgramData\Sophos\Sophos Anti-Virus\INFECTED
```

On Mac OS X:

```text
/Users/Shared/Infected
```

## Log files

The log files can be found in the following locations:

On XP:

```text
C:\documents and settings\All Users\Application Data\Sophos\Sophos Anti-Virus
```

On Windows 7:

```text
C:\ProgramData\Sophos\Sophos Anti-Virus
```

On MacOS-X:

```text
/Library/Logs/Sophos Anti-Virus.log
```

### Log entries

The Sophos logs sometimes contain the following notation:

```text
...\file.exe\FILE:0000
```

These are not an NTFS ADS, but seems to be related to "running" files

These entries also surface when scanning a packed executable. So they
might refer to unpacked versions of the executable.

## External Links

* [Sophos](https://www.sophos.com/en-us)
