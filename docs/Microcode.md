From [Wikipedia](http://en.wikipedia.org/wiki/Microcode):

Microcode is a layer of hardware-level instructions that implement
higher-level machine code instructions or internal state machine
sequencing in many digital processing elements. Microcode is used in
general central processing units, in more specialized processors such as
microcontrollers, digital signal processors, channel controllers, disk
controllers, network interface controllers, network processors, graphics
processing units, and in other hardware.

## Linux

In Linux the CPU microcode can be stored in the initial ramdisk (initrd)
e.g.

    kernel/x86/microcode/GenuineIntel.bin
    kernel/x86/microcode/AuthenticAMD.bin

The initrd is a (compressed) [cpio archive](cpio_archive "wikilink").

## External Links

- [Wikipedia: Microcode](http://en.wikipedia.org/wiki/Microcode)
- [Early load
  microcode](https://www.kernel.org/doc/Documentation/x86/early-microcode.txt),
  by Fenghua Yu
- [Security Analysis of x86 Processor
  microcode](https://www.dcddcc.com/pubs/paper_microcode.pdf), by
  Daming D. Chen, Gail-Joon Ahn, December 11, 2014

### Intel microcode

- [Linux\* Processor Microcode Data
  File](https://downloadcenter.intel.com/download/24661/Linux-Processor-Microcode-Data-File)

[Category:Micro processor](Category:Micro_processor "wikilink")