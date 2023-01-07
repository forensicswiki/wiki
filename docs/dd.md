---
tags:
  -  Linux
  -  Windows
  -  MacOS
  -  FreeBSD
  -  Disk Imaging
  -  Tools
  -  Anti-Forensics
---
**dd**, sometimes called **GNU dd**, is the oldest [disk imaging
tool](disk_imaging.md) still used. Although it is functional and requires only
minimal resources to run, it lacks some of the useful features found in more
modern imagers such as [metadata](metadata.md) gathering, error correction,
piecewise hashing, and a user-friendly interface. dd is a command line program
that uses several obscure command line arguments to control the imaging
process. Because some of these flags are similar and, if confused, can destroy
the source media the examiner is trying to duplicate, users should be careful
when running this program. The program generates [raw image
files](raw_image_format.md) which can be read by many other programs.

dd is part of the GNU Coreutils package which in turn has been ported to many
[operating systems](operating_system.md).

There are a few forks of dd for forensic purposes including:

* [dcfldd](dcfldd.md)
* sdd
* [dd_rescue](dd_rescue.md)
* [ddrescue](ddrescue.md)
* [dccidd](dccidd.md), including a [Microsoft Windows](windows.md) version
   that supports reading [physical memory](physical_memory.md)

## Example

Here are two common dd command lines:

**UNIX/Linux**

`dd if=/dev/hda of=mybigfile.img bs=65536 conv=noerror,sync`

**Windows**

`dd.exe if=\\.\PhysicalDrive0 of=d:\images\PhysicalDrive0.img --md5sum --verifymd5`
`--md5out=d:\images\PhysicalDrive0.img.md5`

## Tips

With linux in addition to

`dd if=/dev/hda of=mybigfile.img bs=65536 conv=noerror,sync`

You can wipe a drive with:

`dd if=/dev/zero of=/dev/hda bs=4K conv=noerror,sync`

For imaging a useful alternate invocation in Linux or UNIX is:

`dd if=/dev/hda bs=4K conv=sync,noerror | tee mybigfile.img | md5sum > mybigfile.md5`

The above alternate imaging command uses dd to read the harddrive being
imaged and outputs the data to tee. tee saves a copy of the data as your
image file and also outputs a copy of the data to md5sum. md5sum
calculates the hash which gets saved in mybgifile.md5

For all of the above

`if             => input file`
`/dev/hda       => the linux name of a physical disk.  Mac has their own names.`
`/dev/zero      => in linux, this is an infinite source of nulls`
`of             => output file`
`mybigfile.img  => The name of the image file you are creating`
`bs             => blocksize`
`65536          => 64K  (I normally use 4K in linux.  That is what the linux kernel uses as a page size.)`
`noerror        => don't die if you have a read error from the source drive`
`sync           => if there is an error, null fill the rest of the block.`

In linux, the blocksize value can have a multiplicative suffix:

`c =1`
`w =2`
`b =512`
`kB =1000,           K =1024`
`MB =1000*1000,      M =1024*1024`
`GB =1000*1000*1000, G =1024*1024*1024`
`and so on for T, P, E, Z, Y. `

Things to know:

Having a bigger blocksize is more efficient, but if you use a 1MB block
as an example and have a read error in the first sector, then dd will
null fill the entire MB. Thus you should use as small a blocksize as
feasible.

But with linux if you go below 4KB blocksize, you can hit really bad
performance issues. It can be as much as 10x slower to use the default
512 byte block as it is to use a 4KB block.

Without noerror and sync, you basically don't have a forensic image. For
forensic images they are mandatory.

dd by itself does not hash, that is why the alternate command is
provided.

## Cautions

### Reversing Args can cause evidence erasure

Use extreme care when typing the command line for this program.
Reversing the `if` and `of` flags will cause the computer to erase your
evidence!

### Use extreme caution if reading from a tape drive

At least with Linux/UNIX, tape drives have functional differences from
disk that make them more complex to "image". Specifically they have EOF
and EOT markings on the tape media that do not have a corresponding
functionality with disks.

Most commercial backup software use EOF separators to allow a single
tape to hold multiple backup sessions.

`backup1-- EOF -- backup2 -- EOF -- backup3 -- EOT`

A simple dd if=/dev/st0 of=image.dd will only preserve the first backup
session.

For testing, from Linux you can create a multi-session backup tape via:

`mt rewind -f /dev/st0`
`tar -cf /dev/nst0 /home`
`tar -cf /dev/nst0 /srv`

The nst device driver considers the closing of /dev/nst0 to signal the
end of a tape file, so it appends a EOF mark after each invocation of
tar.

So the tape would have:

`home_tar_archive -- EOF -- srv_tar_archive -- EOF -- EOT`

If you start reading from the start of the tape with either dd or tar,
they will stop when the first EOF is hit and thus will only extract the
home archive and will miss the srv archive.

## See also

- [aimage](aimage.md)
- [Blackbag](blackbag.md)
- [dc3dd](dc3dd.md)
- [dcfldd](dcfldd.md)
- [dd_rescue](dd_rescue.md)
- [ddrescue](ddrescue.md)
- [mdd](mdd.md)
- [Raw Image Format](raw_image_format.md)

## External Links

- [LinuxJournal article about dd](https://www.linuxjournal.com/article/1320)
- [Windows Version of dd and other forensics tools](http://users.erols.com/gmgarner/forensics/)
