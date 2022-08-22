## Methodology and tools

To make some different off line tests and collect this information you
can boot test system and power off it without software shutdown. On
other hand it is possible to make virtual system and make an offline
test online :)

Tools you need are: qemu, fls, mactime.

Steps to reproduce:

- qemu-img create -f raw windows_xp.img 4G ( it should be exactly raw
  format )
- install Windows or other OS on this image
- qemu windows_xp.img -localtime ( option -localtime will help see exact
  boot/start time, it is important for our investigation )
- fls -o 63 windows_xp.img -r -m / \> body
- mactime -b body 10/18/2007 \> afterboot_report ( 10/18/2007 instead
  here should be the day you make this test )

Not all file marked as changed really changed. It is better to disable
last access time update if you working with NTFS:

To disable Last Access timestamps create the following registry key on
your run-time image:

          Key Name: HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Control\FileSystem
          Name: NtfsDisableLastAccessUpdate
          Type: REG_DWORD
          Value: 1

## Files changed on boot

    Sat Oct 20 2007 17:07:47  2097152 m.c -/-rwxrwxrwx 0        0        2427-128-3 /WINDOWS/system32/config/system
                             201326592 m.c -/-r-xr-xr-x 0        0        27-128-1 /pagefile.sys
    Sat Oct 20 2007 17:07:48 133746688 m.c -/-r-xr-xr-x 0        0        3316-128-1 /hiberfil.sys
    Sat Oct 20 2007 17:07:49      256 ..c d/dr-xr-xr-x 0        0        8166-144-1 /Documents and Settings/NetworkService/Local Settings/History
                                  256 ..c d/dr-xr-xr-x 0        0        8809-144-1 /Documents and Settings/NetworkService/Local Settings/Application Data
                                    0 m.c -/-rwxrwxrwx 0        0        3337-128-11 /WINDOWS/Debug/PASSWD.LOG
                                   62 m.c -/-r-xr-xr-x 0        0        8815-128-1 /Documents and Settings/NetworkService/Local Settings/desktop.ini
                                   20 ..c -/-r-xr-xr-x 0        0        8814-128-1 /Documents and Settings/NetworkService/ntuser.ini
                                   56 ..c d/dr-xr-xr-x 0        0        8112-144-6 /Documents and Settings/NetworkService/Local Settings
                                  256 ..c d/dr-xr-xr-x 0        0        8114-144-1 /Documents and Settings/NetworkService/Local Settings/Temporary Internet Files
                                 2048 m.c -/-rwxrwxrwx 0        0        2261-128-1 /WINDOWS/bootstat.dat
    Sat Oct 20 2007 17:07:51       56 ..c d/dr-xr-xr-x 0        0        8823-144-6 /Documents and Settings/LocalService/Local Settings
                                   20 ..c -/-r-xr-xr-x 0        0        8855-128-1 /Documents and Settings/LocalService/ntuser.ini
                                   62 m.c -/-r-xr-xr-x 0        0        8856-128-1 /Documents and Settings/LocalService/Local Settings/desktop.ini
                                  256 ..c d/dr-xr-xr-x 0        0        8850-144-1 /Documents and Settings/LocalService/Local Settings/Application Data
    Sat Oct 20 2007 17:07:52      472 ..c d/dr-xr-xr-x 0        0        8903-144-1 /Documents and Settings/qwert/Local Settings/Application Data
                                   56 ..c d/dr-xr-xr-x 0        0        8893-144-6 /Documents and Settings/qwert/Local Settings
                                  256 ..c d/dr-xr-xr-x 0        0        8894-144-1 /Documents and Settings/qwert/Local Settings/Temporary Internet Files
                                   62 m.c -/-r-xr-xr-x 0        0        8959-128-3 /Documents and Settings/qwert/Local Settings/desktop.ini
                                  180 ..c -/-r-xr-xr-x 0        0        8968-128-1 /Documents and Settings/qwert/ntuser.ini
                                  256 ..c d/dr-xr-xr-x 0        0        8901-144-1 /Documents and Settings/qwert/Local Settings/History
                                 1024 m.c -/-r-xr-xr-x 0        0        3331-128-3 /WINDOWS/system32/config/SAM.LOG
    Sat Oct 20 2007 17:07:53      280 ..c d/drwxrwxrwx 0        0        8863-144-5 /WINDOWS/Prefetch
                                    6 m.c -/-r-xr-xr-x 0        0        5269-128-11 /WINDOWS/Tasks/SA.DAT
    Sat Oct 20 2007 17:08:00    16384 m.c -/-rwxrwxrwx 0        0        8826-128-3 /Documents and Settings/LocalService/Cookies/index.dat
                                32768 m.c -/-rwxrwxrwx 0        0        8876-128-3 /Documents and Settings/LocalService/Local Settings/Temporary Internet Files/Content.IE5/index.dat
                                    0 ..c -/-rwxrwxrwx 0        0        8828-128-1 /WINDOWS/Debug/oakley.log.sav
                                    0 mac -/-rwxrwxrwx 0        0        8844-128-1 /WINDOWS/Debug/oakley.log
                                  256 ..c d/drwxrwxrwx 0        0        8830-144-1 /Documents and Settings/LocalService/Local Settings/History
                                  152 ..c d/drwxrwxrwx 0        0        8832-144-1 /Documents and Settings/LocalService/Cookies
                                  256 ..c d/drwxrwxrwx 0        0        8831-144-1 /Documents and Settings/LocalService/Local Settings/History/History.IE5
                                   56 ..c d/drwxrwxrwx 0        0        8825-144-5 /Documents and Settings/LocalService/Local Settings/Temporary Internet Files/Content.IE5
                                12104 m.c -/-rwxrwxrwx 0        0        3400-128-3 /WINDOWS/Debug/UserMode/userenv.log
                                  256 ..c d/drwxrwxrwx 0        0        8824-144-1 /Documents and Settings/LocalService/Local Settings/Temporary Internet Files
                                16384 m.c -/-rwxrwxrwx 0        0        8827-128-3 /Documents and Settings/LocalService/Local Settings/History/History.IE5/index.dat
                                  696 mac d/drwxrwxrwx 0        0        88-144-1 /WINDOWS/Debug
    Sat Oct 20 2007 17:08:03      261 ..c -/-rwxrwxrwx 0        0        5196-128-1 /WINDOWS/system32/wbem/Logs/FrameWork.log
                                 2439 ..c -/-rwxrwxrwx 0        0        5138-128-3 /WINDOWS/system32/wbem/Logs/wmiprov.log
                                  108 ..c -/-rwxrwxrwx 0        0        4446-128-1 /WINDOWS/system32/wbem/Logs/WinMgmt.log
                                    0 m.c -/-rwxrwxrwx 0        0        8974-128-10 /WINDOWS/0.log
                                14365 ..c -/-rwxrwxrwx 0        0        7088-128-3 /WINDOWS/system32/wbem/Logs/wbemess.log
                                  120 ..c -/-rwxrwxrwx 0        0        5202-128-1 /WINDOWS/system32/wbem/Logs/wbemcore.log
                                 4943 ..c -/-rwxrwxrwx 0        0        5199-128-3 /WINDOWS/system32/wbem/Logs/setup.log
                                   97 ..c -/-rwxrwxrwx 0        0        9019-128-1 /WINDOWS/system32/wbem/Logs/wmiadap.log
                                   16 ..c -/-rwxrwxrwx 0        0        5209-128-1 /WINDOWS/system32/wbem/Repository/$WinMgmt.CFG
                               950272 ..c -/-rwxrwxrwx 0        0        5206-128-3 /WINDOWS/system32/wbem/Repository/FS/INDEX.BTR
                              5005312 ..c -/-rwxrwxrwx 0        0        5205-128-4 /WINDOWS/system32/wbem/Repository/FS/OBJECTS.DATA
                                10021 ..c -/-rwxrwxrwx 0        0        5201-128-3 /WINDOWS/system32/wbem/Logs/mofcomp.log
    Sat Oct 20 2007 17:08:08     1024 m.c -/-r-xr-xr-x 0        0        8967-128-4 /Documents and Settings/qwert/Local Settings/Application Data/Microsoft/Windows/UsrClass.dat.LOG
    Sat Oct 20 2007 17:08:09     1024 m.c -/-r-xr-xr-x 0        0        3332-128-3 /WINDOWS/system32/config/SECURITY.LOG
                                 1024 m.c -/-r-xr-xr-x 0        0        8813-128-4 /Documents and Settings/NetworkService/Local Settings/Application Data/Microsoft/Windows/UsrClass.dat.LOG
                                 1024 m.c -/-r-xr-xr-x 0        0        8854-128-4 /Documents and Settings/LocalService/Local Settings/Application Data/Microsoft/Windows/UsrClass.dat.LOG
    Sat Oct 20 2007 17:08:18     8192 m.c -/-r-xr-xr-x 0        0        3869-128-4 /Documents and Settings/qwert/NTUSER.DAT.LOG
                                   56 mac d/drwxrwxrwx 0        0        5203-144-5 /WINDOWS/system32/wbem/Repository/FS
                                  488 mac -/-rwxrwxrwx 0        0        9021-128-1 /WINDOWS/system32/wbem/Repository/FS/INDEX.MAP
                                 8192 m.c -/-r-xr-xr-x 0        0        8808-128-4 /Documents and Settings/NetworkService/ntuser.dat.LOG
                                 8192 m.c -/-r-xr-xr-x 0        0        3321-128-3 /WINDOWS/system32/config/default.LOG
                                 8192 m.c -/-r-xr-xr-x 0        0        3320-128-0 /WINDOWS/system32/config/software.LOG
                                 8192 m.c -/-r-xr-xr-x 0        0        8849-128-4 /Documents and Settings/LocalService/ntuser.dat.LOG
                                 2468 mac -/-rwxrwxrwx 0        0        8866-128-4 /WINDOWS/system32/wbem/Repository/FS/OBJECTS.MAP
    Sat Oct 20 2007 17:08:24    20480 m.c -/-r-xr-xr-x 0        0        3319-128-0 /WINDOWS/system32/config/system.LOG

## Files changed on power off

    Sat Oct 20 2007 17:12:00     2634 m.c -/-rwxrwxrwx 0        0        5138-128-3 /WINDOWS/system32/wbem/Logs/wmiprov.log
                                  162 m.c -/-rwxrwxrwx 0        0        4446-128-1 /WINDOWS/system32/wbem/Logs/WinMgmt.log
    Sat Oct 20 2007 17:12:34     1024 m.c -/-r-xr-xr-x 0        0        3869-128-4 /Documents and Settings/qwert/NTUSER.DAT.LOG
                               524288 ma. -/-r-xr-xr-x 0        0        3344-128-4 /Documents and Settings/qwert/NTUSER.DAT
                               262144 ma. -/-r-xr-xr-x 0        0        8966-128-3 /Documents and Settings/qwert/Local Settings/Application Data/Microsoft/Windows/UsrClass.dat
                                  180 m.c -/-r-xr-xr-x 0        0        8968-128-1 /Documents and Settings/qwert/ntuser.ini
    Sat Oct 20 2007 17:12:36       56 mac d/drwxrwxrwx 0        0        5203-144-5 /WINDOWS/system32/wbem/Repository/FS
                                    6 m.c -/-r-xr-xr-x 0        0        5269-128-11 /WINDOWS/Tasks/SA.DAT
                                 2468 mac -/-rwxrwxrwx 0        0        8866-128-4 /WINDOWS/system32/wbem/Repository/FS/OBJECTS.MAP
                                17121 m.c -/-rwxrwxrwx 0        0        7088-128-3 /WINDOWS/system32/wbem/Logs/wbemess.log
                                 2288 m.c -/-rwxrwxrwx 0        0        8862-128-3 /WINDOWS/SchedLgU.Txt
                                  488 mac -/-rwxrwxrwx 0        0        9021-128-1 /WINDOWS/system32/wbem/Repository/FS/INDEX.MAP
                                65536 m.c -/-rwxrwxrwx 0        0        3341-128-1 /WINDOWS/system32/config/SysEvent.Evt
    Sat Oct 20 2007 17:12:37     1024 m.c -/-r-xr-xr-x 0        0        3320-128-0 /WINDOWS/system32/config/software.LOG
                                 2048 m.c -/-rwxrwxrwx 0        0        2261-128-1 /WINDOWS/bootstat.dat
    Sat Oct 20 2007 17:12:38  8650752 ma. -/-rwxrwxrwx 0        0        3298-128-3 /WINDOWS/inf/wkstamig.inf (deleted-realloc)
                              8650752 ma. -/-rwxrwxrwx 0        0        3298-128-3 /WINDOWS/system32/config/software
                               262144 ma. -/-r-xr-xr-x 0        0        8812-128-3 /Documents and Settings/NetworkService/Local Settings/Application Data/Microsoft/Windows/UsrClass.dat
                                 1024 m.c -/-r-xr-xr-x 0        0        3319-128-0 /WINDOWS/system32/config/system.LOG
                               262144 ma. -/-r-xr-xr-x 0        0        8853-128-3 /Documents and Settings/LocalService/Local Settings/Application Data/Microsoft/Windows/UsrClass.dat
                              2097152 ma. -/-rwxrwxrwx 0        0        2427-128-3 /WINDOWS/system32/config/system
                               262144 ma. -/-rwxrwxrwx 0        0        3329-128-3 /WINDOWS/system32/config/SECURITY
                               229376 ma. -/-r-xr-xr-x 0        0        7133-128-4 /Documents and Settings/NetworkService/NTUSER.DAT
                               229376 ma. -/-r-xr-xr-x 0        0        8822-128-4 /Documents and Settings/LocalService/NTUSER.DAT
                               262144 ma. -/-rwxrwxrwx 0        0        3899-128-3 /WINDOWS/system32/config/default
                               262144 ma. -/-rwxrwxrwx 0        0        3330-128-3 /WINDOWS/system32/config/SAM