## Java WebStart Cache

As of Java version 6 the Java WebStart Cache can be found in the
following locations.

On Linux for user accounts:

    /home/$USER/.java/deployment/cache/

On MacOS-X for user accounts:

    /Users/$USER/Library/Caches/Java/cache/

On Windows XP for user accounts:

    C:\Documents and Settings\%USERNAME%\Application Data\Sun\Java\Deployment\cache\

On Windows Vista and later for user accounts:

    C:\Users\%USERNAME%\AppData\LocalLow\Sun\Java\Deployment\cache\

On Windows Vista and later for system accounts:

    C:\Windows\System32\config\systemprofile\AppData\LocalLow\Sun\Java\Deployment\cache\

On Windows Vista and later for system accounts using SysWOW64:

    C:\Windows\SysWOW64\config\systemprofile\AppData\LocalLow\Sun\Java\Deployment\cache\

Note: there also can be an additional SystemCache directory e.g. on
Windows Vista and later for user accounts:

    C:\Users\%USERNAME%\AppData\LocalLow\Sun\Java\Deployment\SystemCache\

Note that if JAR files are cached it does not imply that they have been
executed. The behavior seen with Microsoft Internet Explorer in
combination with JRE 1.7 in high security mode is that it will download
the JAR file and then prompt the user if he/she want to execute the Java
applet.

## IDX file format

Caveat: The following information is based on analysis of several dozen
\*.idx files from different Windows 7 systems. As such, the following
information should not be considered to have been exhaustively
researched.

Values are in big-endian.

    00000000  01 00 00 00 02 5b 00 00  00 00 1d c7 b4 00 00 01  |.....[..........|
    00000010  1f 81 29 fe b8 00 00 00  00 00 00 00 00 00 00 01  |..).............|
    00000020  2b 24 4a cb dd 01 00 00  00 00 00 00 00 00 00 00  |+$J.............|
    00000030  00 00 00 00 00 00 00 00  01 2b 24 4a a4 cd 00 00  |.........+$J....|
    00000040  01 2e 45 83 f4 18 00 00  00 00 00 00 00 00 00 01  |..E.............|
    00000050  01 00 00 00 00 00 00 00  00 00 00 00 01 2b 24 4a  |.............+$J|
    00000060  a4 cd 00 00 00 00 00 00  00 00 00 00 00 00 00 00  |................|
    00000070  00 00 00 00 00 00 00 00  00 00 00 00 00 00 00 00  |................|

The header (or section 1) is 128 bytes in size and contains:

| Offset | Size | Value                   | Description                                                                            |
|:-------|------|-------------------------|----------------------------------------------------------------------------------------|
| 0      | 1    |                         | Busy (flag byte)                                                                       |
| 1      | 1    |                         | Incomplete (flag byte)                                                                 |
| 2      | 4    | 00 00 02 5b (603)       | Format version                                                                         |
| 6      | 1    |                         | Force update (flag byte)                                                               |
| 7      | 1    |                         | No-href (flag byte)                                                                    |
| 8      | 1    |                         | Is shortcut image (flag byte)                                                          |
| 9      | 4    |                         | Content-Length                                                                         |
| 13     | 8    | 00 00 01 1f 81 29 fe b8 | Last modification date (Number of milli seconds since Jan 1, 1970 00:00:00)            |
| 21     | 8    |                         | expiration date (Number of milli seconds since Jan 1, 1970 00:00:00) 0 if not expires? |
| 29     | 8    | 00 00 01 2b 24 4a cb dd | Validation timestamp (Number of milli seconds since Jan 1, 1970 00:00:00)              |
| 37     | 1    |                         | Known to be signed (flag byte)                                                         |
| 38     | 4    |                         | Size of section 2                                                                      |
| 42     | 4    |                         | Size of section 3                                                                      |
| 46     | 4    |                         | Size of section 4                                                                      |
| 50     | 4    |                         | Size of section 5                                                                      |
| 54     | 8    | 00 00 01 2b 24 4a a4 cd | Blacklist validation time (Number of milli seconds since Jan 1, 1970 00:00:00)         |
| 62     | 8    | 00 00 01 2e 45 83 f4 18 | Certificate expiration date (Number of milli seconds since Jan 1, 1970 00:00:00)       |
| 70     | 1    |                         | Class verification status                                                              |
| 71     | 4    |                         | Reduced manifest size                                                                  |
| 75     | 4    |                         | section4Pre15Length?                                                                   |
| 79     | 1    |                         | Has only signed entries (flag byte)                                                    |
| 80     | 1    |                         | Has single code source (flag byte)                                                     |
| 81     | 4    |                         | section4CertsLength?                                                                   |
| 85     | 4    |                         | section4SignersLength?                                                                 |
| 89     | 1    |                         | Has missing signed entries (flag byte)                                                 |
| 90     | 8    | 00 00 01 2b 24 4a a4 cd | Trusted libraries validation time (Number of milli seconds since Jan 1, 1970 00:00:00) |
| 98     | 4    |                         | reducedManifest2Length?                                                                |
| 102    | 26   |                         | Unknown, empty values (likely reserved for future expansion of the header)             |

The values present in the header are dependent on the version. The
definition above is based on version 603 and intended as an example
check the [Java IDX Format
Specification](https://github.com/woanware/javaidx/blob/master/Documents/Java.IDX.Format.pdf)
for more current information.

To convert a timestamp in e.g. Python

    print datetime.datetime(1970, 1, 1) + datetime.timedelta(milliseconds=0x011f8129feb8)
    2009-02-16 22:17:07

    00000080  00 00 00 39 68 74 74 70  3a 2f 2f 77 77 77 2e 74  |...9http://www.t|
    00000090  6f 70 63 6f 64 65 72 2e  63 6f 6d 2f 63 6f 6e 74  |opcoder.com/cont|
    000000a0  65 73 74 2f 63 6c 61 73  73 65 73 2f 43 6f 6e 74  |est/classes/Cont|
    000000b0  65 73 74 41 70 70 6c 65  74 2e 6a 61 72           |estApplet.jar   |

| Offset | Size | Value | Description                                                     |
|:-------|------|-------|-----------------------------------------------------------------|
| 128    | 2    | 00 00 | Version string size                                             |
| 130    | 2    | 00 39 | Original URL string size                                        |
| 132    | size |       | Original URL string (UTF-8 without an end-of-string character?) |

    000000b0                                          00 00 00  |             ...|
    000000c0  0c 36 36 2e 33 37 2e 32  31 30 2e 38 36 00 00 00  |.66.37.210.86   |

| Offset | Size | Value | Description                                           |
|:-------|------|-------|-------------------------------------------------------|
| ...    | 2    | 00 00 | Namespace string size                                 |
| ...    | 2    | 00 0c | IP string size                                        |
| ...    | size |       | IP string (UTF-8 without an end-of-string character?) |

    000000c0                                          00 00 00  |             ...|
    000000d0  07 00 06 3c 6e 75 6c 6c  3e 00 0f 48 54 54 50 2f  |...<null>..HTTP/|
    000000e0  31 2e 31 20 32 30 30 20  4f 4b 00 0e 63 6f 6e 74  |1.1 200 OK..cont|
    000000f0  65 6e 74 2d 6c 65 6e 67  74 68 00 07 31 39 35 31  |ent-length..1951|
    00000100  36 36 38 00 0d 6c 61 73  74 2d 6d 6f 64 69 66 69  |668..last-modifi|
    00000110  65 64 00 1d 4d 6f 6e 2c  20 31 36 20 46 65 62 20  |ed..Mon, 16 Feb |
    00000120  32 30 30 39 20 32 32 3a  31 37 3a 30 37 20 47 4d  |2009 22:17:07 GM|
    00000130  54 00 0c 63 6f 6e 74 65  6e 74 2d 74 79 70 65 00  |T..content-type.|
    00000140  18 61 70 70 6c 69 63 61  74 69 6f 6e 2f 6a 61 76  |.application/jav|
    00000150  61 2d 61 72 63 68 69 76  65 00 04 64 61 74 65 00  |a-archive..date.|
    00000160  1d 53 61 74 2c 20 31 38  20 53 65 70 20 32 30 31  |.Sat, 18 Sep 201|
    00000170  30 20 31 30 3a 30 31 3a  30 36 20 47 4d 54 00 06  |0 10:01:06 GMT..|
    00000180  73 65 72 76 65 72 00 06  41 70 61 63 68 65 00 1b  |server..Apache..|
    00000190  64 65 70 6c 6f 79 2d 72  65 71 75 65 73 74 2d 63  |deploy-request-c|
    000001a0  6f 6e 74 65 6e 74 2d 74  79 70 65 00 1a 61 70 70  |ontent-type..app|
    000001b0  6c 69 63 61 74 69 6f 6e  2f 78 2d 6a 61 76 61 2d  |lication/x-java-|
    000001c0  61 72 63 68 69 76 65 1f  8b 08 00 00 00 00 00 00  |archive.........|
    ...

| Offset | Size | Value | Description                  |
|:-------|------|-------|------------------------------|
| ...    | 4    |       | Number of header value pairs |
| ...    | ...  |       | Array of header value pairs  |

A value pair is variable of size and consists of:

| Offset | Size | Value | Description                         |
|:-------|------|-------|-------------------------------------|
| 0      | 2    |       | Header value identifier string size |
| 2      | size |       | Header value identifier string      |
| ...    | 2    |       | Header value string size            |
| ...    | size |       | Header value string                 |

For the example above the size of the URL string can be found at offset
130 (0x82). The first 4 string values to extract from this data are
prefaced with their lengths (or sizes) as 16-bit big-endian values. E.g.
to retrieve the original URL string, read the WORD at offset 0x82, and
translate it as a big-endian value (e.g. using Perl,
<i>unpack("n",\$data)</i>). Beginning at offset 0x84, the string is 57
(0x39) bytes long. At the end of that string, the next WORD is the
length of the third string, also in big-endian format.

Once you've completed reading the initial 4 strings, there is a DWORD
value which can be interpreted as the number of header values, followed
by the individual header value definitions. Each header value definition
consists of an identifier and a value string. Both strings are prefaced
by a 16-bit big-endian (2-byte) value, containing the length of the
string.

In many cases, the first header value contains the HTTP Response code of
302. Other header values (that have been observed so far) include a
response of 200, as well as additional data (including time stamps), and
the \*.idx files themselves appear to contain certificate (and perhaps
other) information.

## External Links

- [Tracing and
  Logging](http://docs.oracle.com/javase/6/docs/technotes/guides/deployment/deployment-guide/tracing_logging.html),
  by [Oracle](Oracle "wikilink")
- [Java Forensics using TLN
  Timelines](http://sploited.blogspot.ch/2012/08/java-forensics-using-tln-timelines.html)
- [Almost Cooked UP Some
  Java](http://journeyintoir.blogspot.com/2011/02/almost-cooked-up-some-java.html)
- [Finding Initial Infection
  Vector](http://journeyintoir.blogspot.com/2011/11/finding-initial-infection-vector.html)
- [Java IDX Format
  Specification](https://github.com/woanware/javaidx/blob/master/Documents/Java.IDX.Format.pdf),
  by [Mark Woan](Mark_Woan "wikilink"), January 2013
- [Java Malware - Identification and
  Analysis](http://www.ghettoforensics.com/2013/04/java-malware-identification-and-analysis.html),
  by [Brian Baskin](Brian_Baskin "wikilink"), January 12, 2013
- [Java Web Vulnerability Mitigation on
  Windows](http://tojoswalls.blogspot.ch/2013/05/java-web-vulnerability-mitigation-on.html),
  by Tim Johnson, May 23, 2013
- [The State of Java Reversing
  Tools](http://www.ghettoforensics.com/2013/09/malware-analysis-state-of-java-analysis.html),
  by [Brian Baskin](Brian_Baskin "wikilink"), September 3, 2013

### Java source code

- [Cache.java](http://jdk-source-code.googlecode.com/svn/trunk/jdk6u21_src/deploy/src/common/share/classes/com/sun/deploy/cache/Cache.java)
- [CacheEntry.java](http://jdk-source-code.googlecode.com/svn/trunk/jdk6u21_src/deploy/src/common/share/classes/com/sun/deploy/cache/CacheEntry.java)

[Category:Analysis](Category:Analysis "wikilink")