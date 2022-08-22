Miss Identify is a program to find Win32 applications. In its default
mode it displays the filename of any executable that does not have an
executable extension (i.e. exe, dll, com, sys, cpl, hxs, hxi, olb, rll,
or tlb). The program can also be run to display all executables
encountered, regardless of the extension. This is handy when looking for
all of the executables on a drive. Other options allow the user to
record the strings found in an executable and to work recursively.

## Usage

The program can be used to search for mislabeled executables:

`C:\> missidentify *`
`C:\missidentify-1.0\sample.jpg`

To enumerate all executables:

`C:\> missidentify -a * `
`C:\missidentify-1.0\sample.jpg`
`C:\missidentify-1.0\missidentify.exe`

To search for all executables in an unusual place:

`C:\> missidentify -ar c:\windows\system32`
`...`
`C:\WINDOWS\System32\ntdll.dll`
`C:\WINDOWS\System32\ntoskrnl.exe`
`C:\WINDOWS\System32\NEVER-GONNA-CATCH-ME.EXE`
`C:\WINDOWS\System32\ntver.dll`
`...`

## External Links

- [Official web site](http://missidentify.sourceforge.net/)