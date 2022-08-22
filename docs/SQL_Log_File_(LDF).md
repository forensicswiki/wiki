In computing, SQL Log File is a Microsoft SQL Server file type which
stores all the transaction and modification made in the SQL database.
SQL log file is also referred as transaction log file and is created for
each individual database. There is minimum one transactional log file
for each database and it can have more than one as well. File extension
for SQL transaction log file is .ldf (Log Database File).

## Overview

The language, SEQUEL (Structured English Query Language) now known as
SQL was developed by IBM Corporation Inc. in order to use Codd’s model.
Today, SQL is worldwide accepted as a standard RDBMS language. The data
in this SQL server database is saved as primary data files (.mdf) and
secondary data files (.ndf). SQL transaction log files referred as .ldf
files are utilized to store the transaction made to these databases.

SQL Server writes the changes made by user to memory first instead of
writing it directly to the data file. SQL Server records the changes in
memory every now and then and writes it to the transaction log file.
Thus the changes are recorded to transaction log file first and then to
database which is also known as write-ahead log. Hence, this SQL
transaction log file is a critical element of database and as it holds
all the records it can be employed to recover database back to
consistent state in case of system failure. Experts suggest to avoid
deleting or moving this file and also to truncate it at regular basis to
avoid filling it up.

## SQL Log File Architecture

### Logical Architecture

The SQL Server log file logical operation is done considering
transaction log file as a string of log records. Each log record has an
identity of log sequence number (LSN). Log records are written one after
another in serial sequence in such manner that the new log record is
written to logical end of log with LSN which is higher than previous log
record LSN. All the logs comprise of ID of transaction and all log
records are individually linked in chain with backward pointers which
helps in rollback transaction.

### Physical Architecture

SQL Server Database engine separates the transaction log file physically
to multiple virtual log files. These virtual log files don’t have fixed
size or number and its size is chosen dynamically while generating or
extending log files according to the transactions records.
Administrators cannot set the size or number of these virtual log files
and is sum of existing log and new file increment size.

## Support

SQL Server transaction log file can be viewed under some commands of SQL
Server. Some of these commands are undocumented and also fail to show
complete details of transaction log file. DBCC Log () command which is
used commonly, helps to see log information. fn_dblog is another
undocumented SQL Server function which is capable to read the online
transaction log active portion. fn_dump_dblog SQL Server function can be
utilized to read transaction log native or compressed backups (natively)
independent of online database. Users can also explore the structure
using command DBCC LOGINFO which again lacks any official documentation.
After comprehending that the SQL transaction log file can be an
essential element for recovery of SQL databases after server crash, many
commercial utilities also built professional SQL Log File Viewer
utilities which explore the transaction records of log file.

## Tools

- [SQL Log Analyzer](SQL_Log_Analyzer "wikilink")

[Category:File Formats](Category:File_Formats "wikilink")