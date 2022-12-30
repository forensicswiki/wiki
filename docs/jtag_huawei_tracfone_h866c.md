---
tags:
  - Mobile
---
## Huawei H866C - Ascend Y

This phone is supported by the Tracfone. This uses a Qualcomm 7625A 800
MHz (S1) Processor and comes standard with Android version 2.3. This
phone is unsupported by RIFF Box for the JTAG process for resurrector.

|                                                                 |
|-----------------------------------------------------------------|
| <figure>
 <img src="Huawei-tracfone-m866c-front.JPG"
 title="Huawei-tracfone-m866c-front.JPG" width="200"
 alt="Huawei-tracfone-m866c-front.JPG" />
 <figcaption
 aria-hidden="true">Huawei-tracfone-m866c-front.JPG</figcaption>
 </figure>                                                        |
|                                                                 |

### Getting Started

What you need:

1.  Riff Box
2.  USB to Micro USB cord

### NAND Dump Procedure

1.  Remove the battery and peel the label back to expose the TAPS.
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

|                                                                   |
|-------------------------------------------------------------------|
| <figure>
 <img src="Hauwei_U866C_TAPS.jpg" title="Hauwei_U866C_TAPS.jpg"
 width="600" alt="Hauwei_U866C_TAPS.jpg" />
 <figcaption aria-hidden="true">Hauwei_U866C_TAPS.jpg</figcaption>
 </figure>                                                          |
|                                                                   |

After the wires are connected to the board, the phone is powered by the
USB connection. Plug the Micro USB into the USB connection on the device
and then plug the phone into a wall outlet. The phone should respond
with the vibrator switch activating for less than a second.

Launch the Riff Box JTAG Manager and use the following settings:

- JTAG TCK Speed = RTCK
- Resurrector Settings= Huawei U8655
- Auto FullFlash size

|                                                                    |
|--------------------------------------------------------------------|
| <figure>
 <img src="M866C_setting.jpg" title="M866C_setting.jpg" width="800"
 alt="M866C_setting.jpg" />
 <figcaption aria-hidden="true">M866C_setting.jpg</figcaption>
 </figure>                                                           |
|                                                                    |

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
Then read the memory.

### Notes

The phone has a 512 MB NAND flash memory chip which should take
approximately 30 minutes to download.

### References

- <http://www.phonescoop.com/phones/phone.php?p=3308>
