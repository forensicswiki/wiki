---
tags:
  -  Articles that need to be expanded 
  -  File Formats
  -  Text
  -  Linux
---
## Introduction

- Most Linux logs are located under /var/log/ and can be viewed using
  any text editor

## Log files

    /var/log/wtmp: Contains the logs of all logged in and logged out users. Can be analyzed using 'last' command on linux

    /var/log/btmp: Contains only failed login attempts. Can be analyzed using 'last' command on linux

    /var/log/messages or /var/log/syslog: Contains generic system activity logs

    /var/log/auth.log or /var/log/secure: All authentication related events in are logged here.

    /var/log/boot.log: Contains related information and messages logged during system startup process.

    /var/log/dmesg: Contains Information related to hardware devices and their drivers are logged here.

    /var/log/kern.log: Contains information logged by the kernel.

    /var/log/faillog: Contains information on failed login attempts.

    /var/log/cron: Contains information on cron jobs.

    /var/lg/yum: Contains the information that is logged when a new package is installed using the yum command.

    /var/log/mail.log or /var/log/maillog: All mail server related logs are stored here.

    /var/log/httpd/ or /var/log/apache2: Contains the logs recorded by the Apache server. Logging information are stored in two different log files – error_log and access_log.

    /var/log/mysqld.log or /var/log/mysql.log or /var/log/mysql/: All debug, failure and success messages related to the [mysqld] and [mysqld_safe] daemon are logged to this file.

    /var/log/apt/: Contains information related to Advance package tool (apt). Loggin information are stored in history.log and term.log

    /var/log/lastlog: Contains information about the successful logins to the host

## Resources

- [Dr.Ali Hadi Linux
  Forensics](https://www.osdfcon.org/presentations/2019/Ali-Hadi_Performing-Linux-Forensic-Analysis-and-Why-You-Should-Care.pdf)
- [Important Linux Log
  files](https://www.eurovps.com/blog/important-linux-log-files-you-must-be-monitoring/)