---
tags:
  - Mobile
---
### JTAG Huawei Y301-A1 Valiant

This phone is supported by the MetroPCS network. This uses a Qualcomm
MSM8225 1GHz Processor and comes standard with Android version 4.1. This
phone is unsupported by RIFF Box for the JTAG process for resurrector.
The phone has 4GB MoviNAND flash memory.

|                                                                    |                                                                  |
|--------------------------------------------------------------------|------------------------------------------------------------------|
| <figure>
 <img src="Y301-A1_front.JPG" title="Y301-A1_front.JPG" width="200"
 alt="Y301-A1_front.JPG" />
 <figcaption aria-hidden="true">Y301-A1_front.JPG</figcaption>
 </figure>                                                           | <figure>
                                                                      <img src="Y301-A1_back.JPG" title="Y301-A1_back.JPG" width="200"
                                                                      alt="Y301-A1_back.JPG" />
                                                                      <figcaption aria-hidden="true">Y301-A1_back.JPG</figcaption>
                                                                      </figure>                                                         |
|                                                                    |                                                                  |

### Getting Started

What you need:

1.  Riff Box
2.  USB to Micro USB cord

### NAND Dump Procedure

1.  Remove battery and peel the phone label from the board.
2.  Connect the RIFF box to the PC via USB.
3.  Connect the RIFF box to the PCB via the JTAG pins.
4.  Connect the PCB to a Micro USB cord.
5.  Start the "RIFF box" software.
6.  Power the PCB.
7.  Dump the NAND.

The TAPS are located under the battery, behind the Huawei phone label.
The phone will be powered by a Micro USB cord from an AC battery
charger.

The TAPS order is as follows:

1.  1=Not Used
2.  2=TCK
3.  3=GND
4.  4=TMS
5.  5=TDI
6.  6=TDO
7.  7=RTCK
8.  8=TRST
9.  9=NRST

|                                                                  |
|------------------------------------------------------------------|
| <figure>
 <img src="Y301-A1_taps.jpg" title="Y301-A1_taps.jpg" width="600"
 alt="Y301-A1_taps.jpg" />
 <figcaption aria-hidden="true">Y301-A1_taps.jpg</figcaption>
 </figure>                                                         |
|                                                                  |

After the wires are connected to the board, the phone is powered by the
USB connection. Plug the Micro USB into the USB connection on the device
and then plug the phone into a wall outlet or USB port on laptop. The
phone should respond with the vibrator switch activating for less than a
second.

Launch the Riff Box JTAG Manager and use the following settings:

- JTAG TCK Speed = RTCK
- Resurrector Settings= Huawei U8815
- Select the Data Length 4gb or 0x000100000000

|                                                                         |
|-------------------------------------------------------------------------|
| <figure>
 <img src="Huawei-Y301-A1_settings.JPG"
 title="Huawei-Y301-A1_settings.JPG" width="800"
 alt="Huawei-Y301-A1_settings.JPG" />
 <figcaption aria-hidden="true">Huawei-Y301-A1_settings.JPG</figcaption>
 </figure>                                                                |
|                                                                         |

Advanced Settings:

- Ignore Target IDCODE during Resurrection and DCC Loader operations

|                                                                    |
|--------------------------------------------------------------------|
| <figure>
 <img src="RIFF_Settings.JPG" title="RIFF_Settings.JPG" width="600"
 alt="RIFF_Settings.JPG" />
 <figcaption aria-hidden="true">RIFF_Settings.JPG</figcaption>
 </figure>                                                           |
|                                                                    |

Then connect and get the ID, you should receive the dead body signal.
Then read the memory. JTAG complete.

### Notes

The phone has a 4Gb Movi flash memory chip which should take
approximately 2 hours to download.

### References

- <http://www.phonescoop.com/phones/phone.php?p=3308>
