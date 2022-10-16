---
tags:
  -  Articles that need to be expanded 
---
Processes on MacOS can be easily monitored using the DTrace facility.

Rather than using the DTrace facility directly, it is easier to use one
of the precompiled DTrace applications that Apple ships with MacOS.

You can find the list of applications with the "man -k trace" command:

    $ man -k dtrace
    bitesize.d(1m)           - analyse disk I/O size by process. Uses DTrace
    cpuwalk.d(1m)            - Measure which CPUs a process runs on. Uses DTrace
    creatbyproc.d(1m)        - snoop creat()s by process name. Uses DTrace
    dappprof(1m)             - profile user and lib function usage. Uses DTrace
    dapptrace(1m)            - trace user and library function usage. Uses DTrace
    diskhits(1m)             - disk access by file offset. Uses DTrace
    dispqlen.d(1m)           - dispatcher queue length by CPU. Uses DTrace
    dtrace(1)                - generic front-end to the DTrace facility
    dtruss(1m)               - process syscall details. Uses DTrace
    errinfo(1m)              - print errno for syscall fails. Uses DTrace
    execsnoop(1m)            - snoop new process execution. Uses DTrace
    fddist(1m)               - file descriptor usage distributions. Uses DTrace
    filebyproc.d(1m)         - snoop opens by process name. Uses DTrace
    hotspot.d(1m)            - print disk event by location. Uses DTrace
    httpdstat.d(1m)          - realtime httpd statistics. Uses DTrace
    iofile.d(1m)             - I/O wait time by file and process. Uses DTrace
    iofileb.d(1m)            - I/O bytes by file and process. Uses DTrace
    iopattern(1m)            - print disk I/O pattern. Uses DTrace
    iopending(1m)            - plot number of pending disk events. Uses DTrace
    iosnoop(1m)              - snoop I/O events as they occur. Uses DTrace
    iotop(1m)                - display top disk I/O events by process. Uses DTrace
    kill.d(1m)               - snoop process signals as they occur. Uses DTrace
    lastwords(1m)            - print syscalls before exit. Uses DTrace
    loads.d(1m)              - print load averages. Uses DTrace
    newproc.d(1m)            - snoop new processes. Uses DTrace
    opensnoop(1m)            - snoop file opens as they occur. Uses DTrace
    pathopens.d(1m)          - full pathnames opened ok count. Uses DTrace
    pidpersec.d(1m)          - print new PIDs per sec. Uses DTrace
    plockstat(1)             - front-end to DTrace to print statistics about POSIX mutexes and read/write locks
    priclass.d(1m)           - priority distribution by scheduling class. Uses DTrace
    pridist.d(1m)            - process priority distribution. Uses DTrace
    procsystime(1m)          - analyse system call times. Uses DTrace
    runocc.d(1m)             - run queue occupancy by CPU. Uses DTrace
    rwbypid.d(1m)            - read/write calls by PID. Uses DTrace
    rwbytype.d(1m)           - read/write bytes by vnode type. Uses DTrace
    rwsnoop(1m)              - snoop read/write events. Uses DTrace
    sampleproc(1m)           - sample processes on the CPUs. Uses DTrace
    seeksize.d(1m)           - print disk event seek report. Uses DTrace
    setuids.d(1m)            - snoop setuid calls as they occur. Uses DTrace
    sigdist.d(1m)            - signal distribution by process. Uses DTrace
    syscallbypid.d(1m)       - syscalls by process ID. Uses DTrace
    syscallbyproc.d(1m)      - syscalls by process name. Uses DTrace
    syscallbysysc.d(1m)      - syscalls by syscall. Uses DTrace
    topsyscall(1m)           - top syscalls by syscall name. Uses DTrace
    topsysproc(1m)           - top syscalls by process name. Uses DTrace
    weblatency.d(1m)         - website latency statistics. Uses DTrace
    <pre>

    For example, to monitor all file opens, use:

    <pre>
    $ sudo filebyproc.d
    dtrace: script '/usr/bin/filebyproc.d' matched 3 probes
    CPU     ID                    FUNCTION:NAME
      1  18510                       open:entry mds /private/var/db/sudo/simsong
      1  18510                       open:entry mds /private/var/db/sudo/simsong
      0  18510                       open:entry mds .
    dtrace: error on enabled probe ID 1 (ID 19296: syscall::open_nocancel:entry): invalid address (0x7fff5fc2dc7f) in action #2 at DIF offset 24
      0  18510                       open:entry backupd-helper /dev/dtracehelper
      0  18510                       open:entry launchd /var/run
      1  19296              open_nocancel:entry backupd-helper /dev/urandom
      1  19296              open_nocancel:entry backupd-helper /dev/urandom
      1  19296              open_nocancel:entry backupd-helper /System/Library/CoreServices/backupd.bundle/Contents/Resources
      1  18510                       open:entry backupd-helper /System/Library/CoreServices/backupd.bundle/Contents/Resources/Resources/Info-macos.plist
      1  18510                       open:entry backupd-helper /System/Library/CoreServices/backupd.bundle/Contents/Resources/Resources/Info.plist
      1  18510                       open:entry backupd-helper /System/Library/CoreServices/backupd.bundle/Contents/Resources/backupd-helper
      1  19296              open_nocancel:entry backupd-helper /etc/sysinfo.conf
      1  18510                       open:entry backupd-helper /var/root/Library/Preferences/ByHost/.GlobalPreferences.A59F3B73-8D3E-5DC8-B7F7-DBD934505101.plist
      1  18510                       open:entry backupd-helper /var/root/Library/Preferences/.GlobalPreferences.plist
      1  18510                       open:entry backupd-helper /Library/Preferences/com.apple.TimeMachine.plist
      1  18510                       open:entry backupd-helper /Library/Preferences/.GlobalPreferences.plist
      1  19296              open_nocancel:entry backupd-helper /var/run/.autoBackup
      1  18510                       open:entry backupd-helper /private/var/db/.TimeMachine.Results.plist