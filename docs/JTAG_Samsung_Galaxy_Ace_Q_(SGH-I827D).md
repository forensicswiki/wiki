## JTAG Samsung Galaxy Ace Q (SGH-I827D)

The Samsung Galaxy Ace Q is an Android based smartphone. At the time of
this writing (2014AUG26), I am unaware of any method other than JTAG to
acquire a physical image of the NAND on a Samsung Galaxy Ace Q.

For the purpose of this document, a Samsung Galaxy Ace Q was
disassembled, read via JTAG, and reassembled.

### Getting Started

What you need to dump the NAND:

1.  A Octoplus Box [1](http://www.octoplusbox.com/)
2.  Soldering skills and ultra-fine tip soldering iron (a JTAG jig may
    be available).
3.  A DC Power supply capable of supplying 3.8V/1.83A output. The power
    supply used for this was an [U8002A DC Power
    Supply](http://www.home.agilent.com/agilent/product.jspx?pn=u8002a&cc=CA&lc=eng%7CAgilent).

### NAND Dump Procedure

1.  Disassemble the phone down to the PCB.
2.  Connect the Octoplus JTAG Box to the PC via USB.
3.  Connect the Octoplus JTAG Box to the PCB via the JTAG pins.
4.  Connect the PCB to the DC power supply.
5.  Start the "Octoplus JTAG" software.
6.  Enable the power on the DC power supply.
7.  Power the phone via the power button.
8.  Dump the NAND via the Octoplus software.

Instructions for disassembly can be found on Internet but it can be
summarized as follows:

`* Remove the rear cover and battery.`
`* Remove the 8 x Phillips screws.`
`* Split the phone case using a case opening tool (guitar pick).`

|                                                                  |                                                                         |
|------------------------------------------------------------------|-------------------------------------------------------------------------|
| <figure>
 <img src="1-AceQ-Phone.jpg" title="1-AceQ-Phone.jpg" width="450"
 alt="1-AceQ-Phone.jpg" />
 <figcaption aria-hidden="true">1-AceQ-Phone.jpg</figcaption>
 </figure>                                                         | <figure>
                                                                    <img src="3-AceQ-RemoveScrews.jpg" title="3-AceQ-RemoveScrews.jpg"
                                                                    width="450" alt="3-AceQ-RemoveScrews.jpg" />
                                                                    <figcaption aria-hidden="true">3-AceQ-RemoveScrews.jpg</figcaption>
                                                                    </figure>                                                                |
| <figure>
 <img src="2-AceQ-Phone.jpg" title="2-AceQ-Phone.jpg" width="450"
 alt="2-AceQ-Phone.jpg" />
 <figcaption aria-hidden="true">2-AceQ-Phone.jpg</figcaption>
 </figure>                                                         | <figure>
                                                                    <img src="4-AceQ-RemoveHeatsheild.jpg"
                                                                    title="4-AceQ-RemoveHeatsheild.jpg" width="450"
                                                                    alt="4-AceQ-RemoveHeatsheild.jpg" />
                                                                    <figcaption aria-hidden="true">4-AceQ-RemoveHeatsheild.jpg</figcaption>
                                                                    </figure>                                                                |
|                                                                  |                                                                         |

`* Remove the metal shield.`
`* Disconnect the LCD display connector, and remove the battery mount.`
`* Separate main-board from the device. The JTAG port is located on the opposite side to the left of the keypad.`

|                                                                |
|----------------------------------------------------------------|
| <figure>
 <img src="5-AceQ-JTAG.jpg" title="5-AceQ-JTAG.jpg" width="500"
 alt="5-AceQ-JTAG.jpg" />
 <figcaption aria-hidden="true">5-AceQ-JTAG.jpg</figcaption>
 </figure>                                                       |
|                                                                |

`* Solder the JTAG connector to the JTAG port as follows. I used 0.040 gauge magnet wire to connected an adapter that was inserted into the 20 pin ribbon cable supplied with the RIFF box.`

|                                                                      |
|----------------------------------------------------------------------|
| <figure>
 <img src="6-AceQ-Pinouts.jpg" title="6-AceQ-Pinouts.jpg" width="800"
 alt="6-AceQ-Pinouts.jpg" />
 <figcaption aria-hidden="true">6-AceQ-Pinouts.jpg</figcaption>
 </figure>                                                             |
|                                                                      |

`* Re-connect the LCD display connector to the mainboard.`
`* Connect the PCB battery terminal connections to the DC power supply. The positive (+) connection is the outermost pin (1) and the negative (-) pin is the outermost pin (3). You can configure your power supply to match the battery specifications which in this case is 3.8V and 1.80A but do not apply power at this time.`

`* Now we can start the Octoplus JTAG software and configure it, and connect the phone to the Octoplus box. See the picture for more detail.`

|                                                                        |
|------------------------------------------------------------------------|
| <figure>
 <img src="7-AceQ-Octoplus.jpg" title="7-AceQ-Octoplus.jpg" width="800"
 alt="7-AceQ-Octoplus.jpg" />
 <figcaption aria-hidden="true">7-AceQ-Octoplus.jpg</figcaption>
 </figure>                                                               |
|                                                                        |

Apply power to the DC power supply and turn the phone on using the
button on the side of the PCB. After powering the phone on, select
"Connect". If all goes well the "READ" button and options will be
available. Select "Full Flash", followed by "Read". Once the read is
complete you can save the output to the destination of choice.