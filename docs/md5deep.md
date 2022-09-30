---
tags:
  - No Category
---
**md5deep** is a suite of [cross platform](cross_platform.md)
tools to compute and audit [hashes](hashing.md) for any number
of input files. Although similar to other hashing programs like
[md5sum](md5sum.md), it can also recursively traverse directory
structures, use a variety of algorithms, and use files of known hashes
to perform both positive and negative matching. Another program in the
suite [hashdeep](hashdeep.md) can conduct a computer forensics
audit. The programs runs on [Microsoft](microsoft.md)
[Windows](windows.md), [Mac OS X](Mac_OS_X "wikilink"),
[Linux](linux.md), [FreeBSD](FreeBSD "wikilink"),
[Solaris](solaris.md), and most other [\*nix](Unix "wikilink")
[operating systems](operating_system.md). It has been included
in the [Fink](fink.md) and [FreeBSD
Ports](freebsd_ports.md) projects.

## Algorithms Supported

md5deep currently supports [MD5](md5.md),
[SHA-1](sha-1.md), [SHA-256](SHA-256 "wikilink"),
[Tiger](tiger.md), and [Whirlpool](Whirlpool "wikilink").

## File Formats

The md5deep suite can handle a wide variety of input and output file
formats. It can use [md5sum](md5sum.md), [BSD](BSD "wikilink")
md5, [Hashkeeper](hashkeeper.md), [iLook](iLook "wikilink"), and
[NSRL](national_software_reference_library.md) files as sources
for known hashes. The suite does not support [Encase hash
files](encase_hash_files.md).

The output for md5deep can be controlled using command line switches,
but in general is the hash, two spaces, and the filename.

    210ece36fffb77ff660b0280d7655a9c  /home/username/doc.txt

The `-k` switch can be used to add an asterisk like
[md5sum](md5sum.md),

    210ece36fffb77ff660b0280d7655a9c */home/username/doc.txt

The line terminator can be changed to a \0, or NULL character, using the
`-0` command line switch.

## Cross Compiling

The md5deep suite can be cross-compiled for Windows (both 32-bit and
64-bit) using the Fedora Core Linux Distribution. The
[CONFIGURE_FC.sh](https://md5deep.svn.sourceforge.net/svnroot/md5deep/branches/version4/CONFIGURE_FC.sh)
script distributed with the distribution will configure a newly
installed FC release for the mingw32 and mingw64 cross-compilers,
download all necessary libraries, download the md5deep source-code
distribution from the SVN repository, and compile everything. Thus, a
complete cross-compile can be performed on a new install with these
commands:

    wget https://md5deep.svn.sourceforge.net/svnroot/md5deep/branches/version4/CONFIGURE_FC.sh
    sudo sh CONFIGURE_FC.sh

## Digital Forensics XML

As of version 4.0, the md5deep suite tools can produce DFXML output
files. DFXML is specified with the -d option. In the example below two
files are hashed with the md5 algorithm. The output file contains the
file names, file sizes, and MAC times for the two files, as well as
provenance information regarding how the md5deep tool was compiled, the
system on which it was run, and the amount of CPU time required for the
run.

Here is an example:

    $ echo "foo" > foo
    $ echo "bar" > bar
    $ md5deep -d foo bar
    <?xml version='1.0' encoding='UTF-8'?>
    <dfxml xmloutputversion='1.0'>
      <metadata
      ns='http://md5deep.sourceforge.net/md5deep/'
      xmlns:xsi='http://www.w3.org/2001/XMLSchema-instance'
      xmlns:dc='http://purl.org/dc/elements/1.1/'>
        <dc:type>Hash List</dc:type>
      </metadata>
      <creator version='1.0'>
        <program>MD5DEEP</program>
        <version>4.0.0_beta2-002</version>
        <build_environment>
          <compiler>GCC 4.2</compiler>
        </build_environment>
        <execution_environment>
          <os_sysname>Darwin</os_sysname>
          <os_release>11.2.0</os_release>
          <os_version>Darwin Kernel Version 11.2.0: Tue Aug  9 20:54:00 PDT 2011; root:xnu-1699.24.8~1/RELEASE_X86_64</os_version>
          <host>Mucha.local</host>
          <arch>x86_64</arch>
          <command_line>md5deep -d foo bar</command_line>
          <uid>502</uid>
          <start_time>2012-01-19T17:04:59Z</start_time>
        </execution_environment>
      </creator>
      <configuration>
        <algorithms>
          <algorithm name='md5' enabled='1'/>
          <algorithm name='sha1' enabled='0'/>
          <algorithm name='sha256' enabled='0'/>
          <algorithm name='tiger' enabled='0'/>
          <algorithm name='whirlpool' enabled='0'/>
        </algorithms>
      </configuration>
      <fileobject>
        <filename>/Users/simsong/foo</filename>
        <filesize>4</filesize>
        <ctime>2012-01-19T17:04:44Z</ctime>
        <mtime>2012-01-19T17:04:44Z</mtime>
        <atime>2012-01-19T17:04:46Z</atime>
        <hashdigest type='MD5'>d3b07384d113edec49eaa6238ad5ff00</hashdigest>
      </fileobject>
      <fileobject>
        <filename>/Users/simsong/bar</filename>
        <filesize>4</filesize>
        <ctime>2012-01-19T17:04:54Z</ctime>
        <mtime>2012-01-19T17:04:54Z</mtime>
        <atime>2012-01-19T17:04:56Z</atime>
        <hashdigest type='MD5'>c157a79031e1c40f85931829bc5fc552</hashdigest>
      </fileobject>
      <rusage>
        <utime>0.001229</utime>
        <stime>0.002204</stime>
        <maxrss>913408</maxrss>
        <minflt>268</minflt>
        <majflt>62</majflt>
        <nswap>0</nswap>
        <inblock>0</inblock>
        <oublock>0</oublock>
        <clocktime>0.002447</clocktime>
      </rusage>
    </dfxml>

## External Links

- [Official website](http://md5deep.sourceforge.net/)
- [Wikipedia entry on md5deep](http://en.wikipedia.org/wiki/Md5deep)