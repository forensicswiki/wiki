**dd_rescue**, is an an advanced evolution of [dd](dd "wikilink"), a
command line program that has been ported only for UNIX/Linux. The
program uses a complex series of flags to allow the user to image or
write data from and to [raw image files](raw_image_file "wikilink").
Like [dcfldd](dcfldd "wikilink"), the program makes an effort to keep
the user apprised of the status of the current operation.

**[ddrescue](ddrescue "wikilink")** and **dd_rescue** are completely
different programs which share no development between them. The two
projects are not related in any way except that they both attempt to
enhance the standard [dd](dd "wikilink") tool and coincidentally chose
similar names for their new programs.

## Sample usage

Here is a common dd_rescue command:

**UNIX/Linux**

    $ dd_rescue /dev/hda myfile.img

**STDOUT**

A large difference between **[ddrescue](ddrescue "wikilink")** and
**dd_rescue** is that **dd_rescue** can pipe output to STDOUT whereas
**[ddrescue](ddrescue "wikilink")** can only transfer block/file to
block/file.

One example of this usage would be transfering a disk image over the
network using ssh.

    dd_rescue /dev/sda1 - | ssh user@remote.host "cat - > /remote/destination/file.img"

Another example would be adding compression to an image file on the fly.

    dd_rescue /dev/sda1 - | bzip2 > /dir/file.img.bz2

## Cautions

Unlike regular [dd](dd "wikilink"), dd_rescue does not use the command
line arguments `if` or `of`.

## See also

- [aimage](aimage "wikilink")
- [Blackbag](Blackbag "wikilink")
- [dcfldd](dcfldd "wikilink")
- [dd](dd "wikilink")
- [ddrescue](ddrescue "wikilink")
- [sdd](sdd "wikilink")