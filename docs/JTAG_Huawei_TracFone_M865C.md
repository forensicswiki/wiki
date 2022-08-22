## JTAG Huawei TracFone M865C (Ascend II)

This phone is supported by the Cricket Network and Tracfone. This uses a
Qualcomm 7627 600 MHz (S1) Processor and comes standard with Android
version 2.3. This phone is unsupported by RIFF Box for the JTAG process
for resurrector.

|                                                                 |                                                                |
|-----------------------------------------------------------------|----------------------------------------------------------------|
| <figure>
 <img src="huawei-tracfone-m865c-front.jpg"
 title="huawei-tracfone-m865c-front.jpg" width="200"
 alt="huawei-tracfone-m865c-front.jpg" />
 <figcaption
 aria-hidden="true">huawei-tracfone-m865c-front.jpg</figcaption>
 </figure>                                                        | <figure>
                                                                   <img src="huawei-tracfone-m865c-back.jpg"
                                                                   title="huawei-tracfone-m865c-back.jpg" width="200"
                                                                   alt="huawei-tracfone-m865c-back.jpg" />
                                                                   <figcaption
                                                                   aria-hidden="true">huawei-tracfone-m865c-back.jpg</figcaption>
                                                                   </figure>                                                       |
|                                                                 |                                                                |

### Getting Started

What you need:

1.  Riff Box
2.  USB to Micro USB cord

### NAND Dump Procedure

1.  Disassemble the phone down to the PCB.
2.  Connect the RIFF box to the PC via USB.
3.  Connect the RIFF box to the PCB via the JTAG pins.
4.  Connect the PCB to a Micro USB cord and power via a power supply.
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

|                                                                |
|----------------------------------------------------------------|
| <figure>
 <img src="huawei-tracfone-m865c-taps.jpg"
 title="huawei-tracfone-m865c-taps.jpg" width="600"
 alt="huawei-tracfone-m865c-taps.jpg" />
 <figcaption
 aria-hidden="true">huawei-tracfone-m865c-taps.jpg</figcaption>
 </figure>                                                       |
|                                                                |

For the TAPs, the Huawei-8650 was utilized, pictured above. The TAPS on
the M865C are located in the same location as the 8650. See below for
TAPS locations.

|                                                                         |
|-------------------------------------------------------------------------|
| <figure>
 <img src="huawei-tracfone-m865c-soldered-taps.png"
 title="huawei-tracfone-m865c-soldered-taps.png" width="600"
 alt="huawei-tracfone-m865c-soldered-taps.png" />
 <figcaption
 aria-hidden="true">huawei-tracfone-m865c-soldered-taps.png</figcaption>
 </figure>                                                                |
|                                                                         |

After the wires are connected to the board, the phone is powered by the
USB connection. Plug the Micro USB into the USB connection on the device
and then plug the phone into a wall outlet. The phone should respond
with the vibrator switch activating for less than a second.

Launch the Riff Box JTAG Manager and use the following settings:

- JTAG TCK Speed = RTCK
- Resurrector Settings= Huawei U8650
- Auto FullFlash size

|                                                                         |
|-------------------------------------------------------------------------|
| <figure>
 <img src="huawei-tracfone-m865c-riff-settings.jpg"
 title="huawei-tracfone-m865c-riff-settings.jpg" width="600"
 alt="huawei-tracfone-m865c-riff-settings.jpg" />
 <figcaption
 aria-hidden="true">huawei-tracfone-m865c-riff-settings.jpg</figcaption>
 </figure>                                                                |
|                                                                         |

Advanced Settings:

- Ignore Target IDCODE during Resurrection and DCC Loader operations

|                                                                                  |
|----------------------------------------------------------------------------------|
| <figure>
 <img src="huawei-tracfone-m865c-riff-advanced-settings.jpg"
 title="huawei-tracfone-m865c-riff-advanced-settings.jpg" width="600"
 alt="huawei-tracfone-m865c-riff-advanced-settings.jpg" />
 <figcaption
 aria-hidden="true">huawei-tracfone-m865c-riff-advanced-settings.jpg</figcaption>
 </figure>                                                                         |
|                                                                                  |

Then connect and get the ID, you should receive the dead body signal.
Then read the memory. JTAG complete.

### Notes

The phone has a 512 MB NAND flash memory chip which should take
approximately 30 minutes to download.

### References

- <http://www.phonescoop.com/phones/phone.php?p=3308>
- <http://www.riffbox.org/>