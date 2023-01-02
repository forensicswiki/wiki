---
tags:
  - Mobile
---
### LG - L45C -Optimus 2

This phone is supported by the Tracfone. This uses a Qualcomm 7627
Processor and comes standard with Android version 2.3 and has internal
storage of 512 MB. This phone is unsupported by RIFF Box for the JTAG
process for resurrector. RIFF does support the Qualcomm 7627 processor.

|                                                                    |
|--------------------------------------------------------------------|
| <figure>
 <img src="LG-L45C-front.PNG" title="LG-L45C-front.PNG" width="600"
 alt="LG-L45C-front.PNG" />
 <figcaption aria-hidden="true">LG-L45C-front.PNG</figcaption>
 </figure>                                                           |
|                                                                    |

### Getting Started

What you need:

1.  Riff Box
2.  USB to Micro USB cord

### NAND Dump Procedure

1.  Disassemble the rear housing of the phone and metal plate covering
    the PCB board.
2.  Connect the RIFF box to the PC via USB.
3.  Connect the RIFF box to the PCB via the JTAG pins.
4.  Connect the PCB to a Micro USB cord and power via a power supply.
5.  Start the "RIFF box" software.
6.  Power the PCB.
7.  Dump the NAND.

The Taps are located under the white LG sticker. The easiest way to
access the TAPS is to remove the back cover of the phone. first remove
the 7 screws (small Philips) and then the metal cover over the board.

|                                                                  |
|------------------------------------------------------------------|
| <figure>
 <img src="LG-L45C-TAPS.PNG" title="LG-L45C-TAPS.PNG" width="630"
 alt="LG-L45C-TAPS.PNG" />
 <figcaption aria-hidden="true">LG-L45C-TAPS.PNG</figcaption>
 </figure>                                                         |
|                                                                  |

|                                                                    |
|--------------------------------------------------------------------|
| <figure>
 <img src="LG-L45C-TAPS-order.PNG" title="LG-L45C-TAPS-order.PNG"
 width="400" alt="LG-L45C-TAPS-order.PNG" />
 <figcaption aria-hidden="true">LG-L45C-TAPS-order.PNG</figcaption>
 </figure>                                                           |
|                                                                    |

The TAPS order is as follows:

1.  1= TCK
2.  2= RTCK
3.  3= TDO
4.  4= TDI
5.  5= TMS
6.  6= TRST
7.  7= VCC
8.  8= NRST
9.  9= No Used
10. 10=GND

This order applies to the RIFF box. Other boxes refer to the VCC as VREF
and NRST as RESET.

After the wires are connected to the board, the phone is powered by the
USB connection to a wall charger. May need a DC power supply to
supplement the phone power. In that case, connect the DC power supply to
the battery connections and set the DC power supply to 4.0. May also
need to attach the two negative leads. During testing, one LG phone only
responded to an actual battery and not the power supply.

Launch the Riff Box JTAG Manager and use the following settings:

- JTAG TCK Speed = RTCK
- Resurrector Settings= Qualcomm MSM 7XXX L41 D04 NAND
- Auto FullFlash size

|                                                                   |
|-------------------------------------------------------------------|
| <figure>
 <img src="JTAG_Mang_Setting.JPG" title="JTAG_Mang_Setting.JPG"
 width="800" alt="JTAG_Mang_Setting.JPG" />
 <figcaption aria-hidden="true">JTAG_Mang_Setting.JPG</figcaption>
 </figure>                                                          |
|                                                                   |

Then connect and get the ID, you should receive the dead body signal.
Then read the memory.

### Notes

The phone has a 512 MB NAND flash memory chip which should take
approximately 30 minutes to download.

### References

- <http://www.phonescoop.com/phones/phone.php?p=3308>
