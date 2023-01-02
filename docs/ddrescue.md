---
tags:
  - No Category
---
**ddrescue** is a raw disk imaging tool that "copies data from one file
or block device to another, trying hard to rescue data in case of read
errors." The application is developed as part of the GNU project and has
written with UNIX/Linux in mind.

**ddrescue** and **[dd_rescue](dd_rescue.md)** are completely
different programs which share no development between them. The two
projects are not related in any way except that they both attempt to
enhance the standard [dd](dd.md) tool and coincidentally chose
similar names for their new programs.

From the [ddrescue](ddrescue.md) info pages:

> GNU ddrescue is a data recovery tool. It copies data from one file or
> block device (hard disc, cdrom, etc) to another, trying hard to rescue
> data in case of read errors.
>
> Ddrescue does not truncate the output file if not asked to. So, every
> time you run it on the same output file, it tries to fill in the
> gaps.
>
> The basic operation of ddrescue is fully automatic. That is, you don't
> have to wait for an error, stop the program, read the log, run it in
> reverse mode, etc.
>
> If you use the logfile feature of ddrescue, the data is rescued very
> efficiently (only the needed blocks are read). Also you can interrupt
> the rescue at any time and resume it later at the same point.
>
> Automatic merging of backups: If you have two or more damaged copies
> of a file, cdrom, etc, and run ddrescue on all of them, one at a time,
> with the same output file, you will probably obtain a complete and
> error-free file. This is so because the probability of having damaged
> areas at the same places on different input files is very low. Using
> the logfile, only the needed blocks are read from the second and
> successive copies.

## Installation

### Bootable CD

ddrescue is available on bootable rescue cds such as SystemRescueCd
<http://www.sysresccd.org/Main_Page>.

### Debian and Ubuntu

The package 'ddrescue' in Debian and Ubuntu is actually
[dd_rescue](dd_rescue.md), another dd-like program which does
not maintain a recovery log. The correct package is gddrescue.

Debian

> aptitude install gddrescue

Ubuntu

> sudo apt-get install gddrescue

### Gentoo

> emerge ddrescue

## Partition recovery

### Kernel 2.6.3+ & ddrescue 1.4+

'ddrescue --direct' will open the input with the O_DIRECT option for
uncached reads. 'raw devices' are not needed on newer kernels. For older
kernels see below.

First you copy as much data as possible, without retrying or splitting
sectors:

> ddrescue --no-split /dev/hda1 imagefile logfile

Now let it retry previous errors 3 times, using uncached reads:

> ddrescue --direct --max-retries=3 /dev/hda1 imagefile logfile

If that fails you can try again but retrimmed, so it tries to reread
full sectors:

> ddrescue --direct --retrim --max-retries=3 /dev/hda1 imagefile logfile

You can now use ddrescue (or normal dd) to copy the imagefile to a new
partition on a new disk. Use the appropriate filesystem checkers (fsck,
CHKDSK) to try to fix errors caused by the bad blocks. Be sure to keep
the imagefile around. Just in case the filesystem is severely broken,
and datacarving tools like testdisk need to to be used on the original
image.

### Before linux kernel 2.6.3 / 2.4.x

In 2.6.3 the 'raw device' has been marked obsolete. On later kernels
ddrescue will use O_DIRECT on the input to do uncached reads.

First you copy as much data as possible, without retrying or splitting
sectors:

> ddrescue --no-split /dev/hda1 imagefile logfile

Now change over to raw device access. Let it retry previous errors 3
times, don't read past last block in logfile:

> modprobe raw
> raw /dev/raw/raw1 /dev/hda1
> ddrescue --max-retries=3 --complete-only /dev/raw/raw1 imagefile
> logfile

If that fails you can try again (still using raw) but retrimmed, so it
tries to reread full sectors:

> ddrescue --retrim --max-retries=3 --complete-only /dev/raw/raw1
> imagefile logfile

You can now use ddrescue (or normal dd) to copy the imagefile to a new
partition on a new disk. Use the appropriate filesystem checkers (fsck,
CHKDSK) to try to fix errors caused by the bad blocks. Be sure to keep
the imagefile around. Just in case the filesystem is severely broken,
and datacarving tools like testdisk need to to be used on the original
image.

At the end you may want to unbind the raw device:

> raw /dev/raw/raw1 0 0

## Examples

These two examples are taken directly from the
[ddrescue](ddrescue.md) info pages.

Example 1: Rescue an ext2 partition in /dev/hda2 to /dev/hdb2

**Please Note:** This will overwrite ALL data on the partition you are
copying to. If you do not want to do that, rather create an image of the
partition to be rescued.

> ddrescue -r3 /dev/hda2 /dev/hdb2 logfile
> e2fsck -v -f /dev/hdb2
> mount -t ext2 -o ro /dev/hdb2 /mnt

Example 2: Rescue a CD-ROM in /dev/cdrom

> ddrescue -b 2048 /dev/cdrom cdimage logfile

write cdimage to a blank CD-ROM

This example is derived from the ddrescue manual.

Example 3: Rescue an entire hard disk /dev/sda to another disk /dev/sdb

copy the error free areas first

`ddrescue -n /dev/sda /dev/sdb rescue.log`

attempt to recover any bad sectors

`ddrescue -r 1 /dev/sda /dev/sdb rescue.log`

## Options

`-h, --help`
`   display this help and exit `
`-V, --version`
`   output version information and exit `
`-b, --block-size=`<bytes>
`   hardware block size of input device [512] `
`-B, --binary-prefixes`
`   show binary multipliers in numbers [default SI] `
`-c, --cluster-size=`<blocks>
`   hardware blocks to copy at a time [128] `
`-C, --complete-only`
`   do not read new data beyond logfile limits `
`-d, --direct`
`   use direct disc access for input file `
`-D, --synchronous`
`   use synchronous writes for output file `
`-e, --max-errors=`<n>
`   maximum number of error areas allowed `
`-F, --fill=`<types>
`   fill given type areas with infile data (?*/-+) `
`-g, --generate-logfile`
`   generate approximate logfile from partial copy `
`-i, --input-position=`<pos>
`   starting position in input file [0] `
`-n, --no-split`
`   do not try to split or retry error areas `
`-o, --output-position=`<pos>
`   starting position in output file [ipos] `
`-q, --quiet`
`   quiet operation `
`-r, --max-retries=`<n>
`   exit after given retries (-1=infinity) [0] `
`-R, --retrim`
`   mark all error areas as non-trimmed `
`-s, --max-size=`<bytes>
`   maximum size of data to be copied `
`-S, --sparse`
`   use sparse writes for output file `
`-t, --truncate`
`   truncate output file `
`-v, --verbose`
`   verbose operation`

Numbers may be followed by a multiplier: b = blocks, k = kB = 10^3 =
1000, Ki = KiB = 2^10 = 1024, M = 10^6, Mi = 2^20, G = 10^9, Gi = 2^30,
etc...

## Cygwin

As of release 1.4-rc1, it can be compiled directly in
[Cygwin](cygwin.md) [Out of the
Box](http://en.wikipedia.org/wiki/Out_of_the_box). Precompiled packages
are available in the [Cygwin distribution](http://cygwin.com/packages/).
This makes it usable natively on [Windows](windows.md) systems.

## See also

- [aimage](aimage.md)
- [Blackbag](blackbag.md)
- [dcfldd](dcfldd.md)
- [dd](dd.md)
- [dd_rescue](dd_rescue.md)

## Other Resources

\[<http://pfuender.net/?p=80>\| Useful code-snippets for DDrescue\]
