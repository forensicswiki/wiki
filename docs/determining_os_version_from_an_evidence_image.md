---
tags:
  -  Howtos
---
One of the first steps an examiners will need to carry out once they
have an evidence image is to log system metadata, including OS version
and patch level. This may be of particular importance if the image in
question is from a machine that is suspected of having been compromised.

## Windows

### Windows 95/98/ME

Establish the boot volume, verify that it is a FAT file system, and
locate the hidden text file \MSDOS.SYS. Locate the \[Options\]WinVer
parameter:

| WinVer    | OS                |
|-----------|-------------------|
| 4.00.0950 | Windows 95        |
| 4.00.1111 | Windows 95 OSR2   |
| 4.03.1212 | Windows 95 OSR2.1 |
| 4.03.1214 | Windows 95 OSR2.5 |
| 4.10.1998 | Windows 98        |
| 4.10.2222 | Windows 98 SE     |
| 4.90.3000 | Windows ME        |

Alternatively, establish WinDir (\[Paths\]WinDir in \MSDOS.SYS), locate
the %WINDIR%\SYSTEM.DAT registry file. Next, look up the registry key
Software\Microsoft\Windows\CurrentVersion\\, and values Version and
VersionNumber. (Backup copies of SYSTEM.DAT may be found in .CAB files
in %WINDIR%\SYSBCKUP.)

### Windows NT4

### Windows 2000, XP, 2003, Vista

Information about a running system can be displayed using the command
\`ver\` (and \`systeminfo\` on some systems).

During a forensic examination, information regarding the version of
Windows can be found in a number of places. For example, by default, the
Windows directory on Windows XP is "C:\Windows", where on Windows NT and
2000, it was "C:\Winnt". This is not definitive, however, because this
directory name is easily modified during installation.

Determining the version of Windows from the Software Registry Hive
file - navigate to the *Microsoft\Windows NT\CurrentVersion* key, and
examine the values beneath the key; specifically, values such as
ProductName, CSDVersion, ProductId (if available), BuildLab, and on
Vista, BuildLabEx.

Determining the version of Windows from file version information -
locate the file %WinDir%\system32\ntoskrnl.exe and review the file
version information/strings from the resource section of the PE file.
You can view this information with a hex editor, or extract it using a
variety of means. There is a Perl module (Win32::<File::VersionInfo>)
that will allow you to extract this information, and the Perl script
[kern.pl](https://sourceforge.net/project/showfiles.php?group_id=164158&package_id=203967)
illustrates a platform independent means of examining the PE header and
ultimately locating the file version information.

In order to determine the difference between Windows XP Professional and
Home versions, look for the %WinDir%\system32\prodspec.ini file; it
contains information regarding the Product type (either XP Pro or Home).
Another way to do this is to look at Microsoft Product Code (first 5
digits of *Product ID*). Some of these values:

| Value (MPC) | Version                         |
|-------------|---------------------------------|
| 55034       | Windows XP Professional English |
| 55683       | Windows XP Professional Russian |
| 55681       | Windows XP Home Edition Russian |

### Other

- Windows 2008
- Windows 7
- Windows 8
- Windows CE, Mobile

Different editions per version?

## Unix/Linux

Information about a running system, including the kernel version, can be
displayed using the command \`uname -a\`. However, this is not much good
if you performing dead analysis on a disk image.

### Linux

A number of Linux distributions create a file in */etc* to identify the
release or version installed.

    /etc/issue
    /etc/issue.net

| Distro  | Tag                 |
|---------|---------------------|
| Red Hat | /etc/redhat-release |
| Debian  | /etc/debian-version |

### (Open) Solaris

### Free/Net/OpenBSD

A first indicator of the presence of a BSDs operating system is the
partition table on a MBR-partitioned disk:

| OS      | Partition type |
|---------|----------------|
| FreeBSD | FreeBSD (0xA5) |
| OpenBSD | OpenBSD (0xA6) |
| NetBSD  | NetBSD (0xA9)  |
|         |                |

You can get the release and version of BSDs operating system inside the
kernel images, even with only a disk image.

| OS      | Kernel path         |
|---------|---------------------|
| FreeBSD | /boot/kernel/kernel |
| OpenBSD | /bsd                |
| NetBSD  | /netbsd             |
|         |                     |

You can use `strings` and `grep` tools to find this information with
`strings kernel_path | grep os_name`. (e.g.:
`strings /bsd | grep OpenBSD`)

### AIX

### HP/UX

### Other

- BSDI

## Other

- Plan9
- QNX RTOS
- OS2
- MacOS-X/IOS
- DOS

