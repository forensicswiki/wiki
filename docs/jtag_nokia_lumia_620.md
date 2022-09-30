---
tags:
  - No Category
---
## JTAG Nokia Lumia 620

The Nokia Lumia 620 is a Windows based smartphone. As of this writing
(2014AUG28), I am unaware of any method other than JTAG to acquire a
physical image of the NAND on a Nokia Lumia 620.

For the purpose of this document, a Lumia 620 was disassembled, read via
JTAG, and reassembled.

### Getting Started

What you need to dump the NAND:

1.  A Riff Box [Box](http://www.riffbox.org/%7CRIFF)
2.  Soldering skills and ultra-fine tip soldering iron (a JTAG jig may
    be available).
3.  A DC Power supply capable of supplying 3.7V/1.30A output. The power
    supply used for this was an [U8002A DC Power
    Supply](http://www.home.agilent.com/agilent/product.jspx?pn=u8002a&cc=CA&lc=eng%7CAgilent).
4.  A hot air re-work station. The hot air re-work station used for this
    was an [LF-852D Hot Air
    Station](http://www.howardelectronics.com/xytronic/LF-852D.html%7CXytronic).

### NAND Dump Procedure

1.  Disassemble the phone down to the PCB.
2.  Connect the RIFF JTAG Box to the PC via USB.
3.  Connect the RIFF JTAG Box to the PCB via the JTAG pins.
4.  Connect the PCB to the DC power supply.
5.  Start the "RIFF JTAG" software.
6.  Enable the power on the DC power supply.
7.  Power the phone via the power button.
8.  Dump the NAND via the RIFF software.

Instructions for dis-assembly can be found on Internet but it can be
summarized as follows:

`* Remove the rear cover using a case opening tool (guitar pick)`
`* Remove the battery.`
`* Remove the 6 x T-4 Torx screws.`
`* Remove the 2 plastic covers  protecting the mainboard.`
`* Disconnect the 2 ribbon cables that are connected to the main-board.`

|                                                                          |                                                                          |
|--------------------------------------------------------------------------|--------------------------------------------------------------------------|
| <figure>
 <img src="1-Lumia620-Phone.jpg" title="1-Lumia620-Phone.jpg" width="450"
 alt="1-Lumia620-Phone.jpg" />
 <figcaption aria-hidden="true">1-Lumia620-Phone.jpg</figcaption>
 </figure>                                                                 | <figure>
                                                                            <img src="2-Lumia620-Phone.jpg" title="2-Lumia620-Phone.jpg" width="450"
                                                                            alt="2-Lumia620-Phone.jpg" />
                                                                            <figcaption aria-hidden="true">2-Lumia620-Phone.jpg</figcaption>
                                                                            </figure>                                                                 |
| <figure>
 <img src="3-Lumia620-Screws.jpg" title="3-Lumia620-Screws.jpg"
 width="450" alt="3-Lumia620-Screws.jpg" />
 <figcaption aria-hidden="true">3-Lumia620-Screws.jpg</figcaption>
 </figure>                                                                 | <figure>
                                                                            <img src="4-Lumia620-RemovePlastic.jpg"
                                                                            title="4-Lumia620-RemovePlastic.jpg" width="450"
                                                                            alt="4-Lumia620-RemovePlastic.jpg" />
                                                                            <figcaption aria-hidden="true">4-Lumia620-RemovePlastic.jpg</figcaption>
                                                                            </figure>                                                                 |
|                                                                          |                                                                          |

`* Separate the main-board from the phone.`
`* The JTAG TAPs on the Lumia 620 are located under an EMI shield above the SD card slot. The shield was removed using a hot air re-work station at a temperature of approximately 350 centigrade.`

|                                                                      |                                                                      |
|----------------------------------------------------------------------|----------------------------------------------------------------------|
| <figure>
 <img src="6-Lumia620-EMI.jpg" title="6-Lumia620-EMI.jpg" width="500"
 alt="6-Lumia620-EMI.jpg" />
 <figcaption aria-hidden="true">6-Lumia620-EMI.jpg</figcaption>
 </figure>                                                             | <figure>
                                                                        <img src="7-Lumia620-EMI.jpg" title="7-Lumia620-EMI.jpg" width="500"
                                                                        alt="7-Lumia620-EMI.jpg" />
                                                                        <figcaption aria-hidden="true">7-Lumia620-EMI.jpg</figcaption>
                                                                        </figure>                                                             |
|                                                                      |                                                                      |

`* Solder connecting wire to the JTAG TAPs as follows. I used 0.040 gauge magnet wire to connect an adapter that was inserted into the 20 pin ribbon cable supplied with the RIFF box.`

|                                                                     |
|---------------------------------------------------------------------|
| <figure>
 <img src="8-Lumia620-Pinouts.jpg" title="8-Lumia620-Pinouts.jpg"
 width="800" alt="8-Lumia620-Pinouts.jpg" />
 <figcaption aria-hidden="true">8-Lumia620-Pinouts.jpg</figcaption>
 </figure>                                                            |
| <figure>
 <img src="9-Lumia620-Soldered.jpg" title="9-Lumia620-Soldered.jpg"
 width="800" alt="9-Lumia620-Soldered.jpg" />
 <figcaption aria-hidden="true">9-Lumia620-Soldered.jpg</figcaption>
 </figure>                                                            |
|                                                                     |

`* Re-connect the LCD display connector to the mainboard.`
`* Connect the PCB battery terminal connections to the DC power supply. The positive (+) connection is the outermost pin (1) and the negative (-) pin is the outermost pin (3). You can configure your power supply to match the battery specifications which in this case is 3.7V and 1.30A but do not apply power at this time.`
`* Now we can start the RIFF JTAG software, configure it for the LG E960, and connect the phone to the RIFF box. See the picture for more detail.`

|                                                                          |
|--------------------------------------------------------------------------|
| <figure>
 <img src="10-Lumia620-Riff.jpg" title="10-Lumia620-Riff.jpg" width="800"
 alt="10-Lumia620-Riff.jpg" />
 <figcaption aria-hidden="true">10-Lumia620-Riff.jpg</figcaption>
 </figure>                                                                 |
|                                                                          |

`* Apply power from the DC power supply to the phone and turn the phone on using the button on the side of the PCB. After powering the phone on, select "READ" under the "DCC Read/Write" tab. If all goes well the "READ" button will become the "STOP" button and the phone will begin reading. If not, the RIFF software provides troubleshooting steps that should be taken to assist in diagnosing some of the issues you may experience.`