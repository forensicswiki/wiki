Rekall is the stand-alone continuation of the
[Volatility](Volatility "wikilink") Technology Preview (TP) version, aka
the scudette branch.

One of Rekalls goals is to provide better integration with
[GRR](GRR "wikilink") by improved modularity of the framework and having
memory acquisition capability
[1](http://www.rekall-forensic.com/about.html).

## Memory acquisition drivers

The drivers can be found under:

    rekall/tools/linux
    rekall/tools/osx
    rekall/tools/windows

### Linux

#### lmap

In rekall RC11 the advanced Linux acquisition tool (LMAP) was added.
lmap allows to inject the pmem functionality into existing kernel
modules to bypass having to build a pmem kernel module for every
different kernel version. See the corresponding DFRWS EU 2014 paper for
more information about LMAP. LMAP is also known as the "pmem parasite".

#### pmem

To build the kernel module for the current kernel version, make sure you
have a working build environment and the kernel headers installed.
Change into this directory and run make:

    cd rekall/tools/linux/
    make

The acquisition driver is named pmem.ko.

To load the driver:

    sudo insmod pmem.ko

To check if the driver is running:

    sudo lsmod

The driver create a device file named:

    /dev/pmem

To unload the driver:

    sudo rmmod pmem

To read acquire the memory just read from the device file. e.g.

    dd if=/dev/pmem of=image.raw

For more information see:

    rekall/tools/linux/README

### Mac OS X

For more information see:

    rekall/tools/osx/OSXPMem/README

### Windows

Since recent versions of Windows require a signed driver rekall comes
with both pre-built (signed binary) and source versions of the driver.

Both the i386 and amd64 binary version of the driver can be found in the
directory:

    rekall/tools/windows/winpmem/binaries

E.g.

    rekall/tools/winpmem/binaries/amd64/winpmem.sys

A standalone tool for imaging memory that uses an embedded copy of the
pmem driver can be found as winpmem.exe in:

    rekall/tools/winpmem/executables/Release/

To load the driver:

    winpmem.exe -l

The device filename is (This can not be changed without recompiling):

    \\.\pmem

Note that running dd directly on this device file can crash the machine.
Use the winpmem.exe tool instead because it handles protected memory
regions.

To read and acquire the physical memory and write it to image.raw:

    winpmem.exe image.raw

To unload the driver:

    winpmem.exe -u

For more information see:

    rekall/tools/windows/README

## See Also

- [Memory analysis](Memory_analysis "wikilink")
- [Memory Imaging](Memory_Imaging "wikilink")
- [Volatility](Volatility "wikilink")

## External Links

- [Project site](http://www.rekall-forensic.com/)
- [Project documentation](http://www.rekall-forensic.com/docs.html)
- [Rekall Memory Forensics blog](http://rekall-forensic.blogspot.com/)
- [Anti-forensic resilient memory
  acquisition](http://www.rekall-forensic.com/docs/References/Papers/DFRWS2013.html)\]
  by [Johannes Stüttgen](Johannes_Stüttgen "wikilink"), [Michael
  Cohen](Michael_Cohen "wikilink"), August 2013
- [Robust Linux memory acquisition with minimal target
  impact](http://www.rekall-forensic.com/docs/References/Papers/DFRWS2014EU.html),
  [Johannes Stüttgen](Johannes_Stüttgen "wikilink"), [Michael
  Cohen](Michael_Cohen "wikilink"), May 2014