## JTAG LG Nexus 4

The LG Nexus 4 is an Android based smartphone. At the time of this
writing (2013Nov28), I am unaware of any method other than JTAG to
acquire a physical image of the NAND on a locked LG Nexus 4.

For the purpose of this document, a LG Nexus 4 was disassembled, read
via JTAG, reassembled.

### Getting Started

What you need to dump the NAND:

1.  A RIFF Box [Box](http://www.riffbox.org/%7CRIFF)
2.  Soldering skills and fine tip soldering iron (a JTAG jig is
    available for this device).
3.  Optional: JTAG Molex Adapter Set by MOORC.
4.  A DC Power supply capable of supplying 3.8V/2.1A output. The power
    supply used for this was an [U8002A DC Power
    Supply](http://www.home.agilent.com/agilent/product.jspx?pn=u8002a&cc=CA&lc=eng%7CAgilent).

### NAND Dump Procedure

1.  Disassemble the phone down to the PCB.
2.  Connect the RIFF JTAG Box to the PC via USB.
3.  Connect the RIFF JTAG Box to the PCB via the JTAG pins.
4.  Connect the PCB to the DC power supply.
5.  Start the "RIFF BOX JTAG" software.
6.  Enable the power on the DC power supply.
7.  Power the phone via the power button.
8.  Dump the NAND via the RIFF Box software.

Instructions for disassembly can be found on Internet and are summarized
as follows:

- Using a Torx-5 (T5) screw driver remove the 2 screws from the bottom
  of the phone.
- Use a pry tool (guitar pick) to remove the back cover.

|                                                                        |                                                                          |
|------------------------------------------------------------------------|--------------------------------------------------------------------------|
| <figure>
 <img src="1-Nexus4-Phone.jpg" title="1-Nexus4-Phone.jpg" width="500"
 alt="1-Nexus4-Phone.jpg" />
 <figcaption aria-hidden="true">1-Nexus4-Phone.jpg</figcaption>
 </figure>                                                               | <figure>
                                                                          <img src="2-Nexus4-Phone1.jpg" title="2-Nexus4-Phone1.jpg" width="445"
                                                                          alt="2-Nexus4-Phone1.jpg" />
                                                                          <figcaption aria-hidden="true">2-Nexus4-Phone1.jpg</figcaption>
                                                                          </figure>                                                                 |
| <figure>
 <img src="3-Nexus4-RemoveScrews.jpg" title="3-Nexus4-RemoveScrews.jpg"
 width="450" alt="3-Nexus4-RemoveScrews.jpg" />
 <figcaption aria-hidden="true">3-Nexus4-RemoveScrews.jpg</figcaption>
 </figure>                                                               | <figure>
                                                                          <img src="4-Nexus4-RemoveBackCover.jpg"
                                                                          title="4-Nexus4-RemoveBackCover.jpg" width="450"
                                                                          alt="4-Nexus4-RemoveBackCover.jpg" />
                                                                          <figcaption aria-hidden="true">4-Nexus4-RemoveBackCover.jpg</figcaption>
                                                                          </figure>                                                                 |
|                                                                        |                                                                          |

- Using a Philips (PH00) screw driver, remove the 9 screws securing the
  plastic shield on the backside of the phone as well as the 2 screws
  securing the battery connector.

|                                                                        |
|------------------------------------------------------------------------|
| <figure>
 <img src="5-Nexus4-RemoveScrews.jpg" title="5-Nexus4-RemoveScrews.jpg"
 width="1000" alt="5-Nexus4-RemoveScrews.jpg" />
 <figcaption aria-hidden="true">5-Nexus4-RemoveScrews.jpg</figcaption>
 </figure>                                                               |
|                                                                        |

- Once the plastic shield has been removed, you can see the JTAG
  connection port located next to the power button. This JTAG port has a
  Molex connector installed and as such it is possible to use a JTAG jig
  to connect to the device. However, on this phone I soldered 0.040
  gauge magnet wire directly to the Molex pins as I did not have a JTAG
  jig available.

|                                                                      |
|----------------------------------------------------------------------|
| <figure>
 <img src="6-Nexus4-JtagPort.jpg" title="6-Nexus4-JtagPort.jpg"
 width="500" alt="6-Nexus4-JtagPort.jpg" />
 <figcaption aria-hidden="true">6-Nexus4-JtagPort.jpg</figcaption>
 </figure>                                                             |
| <figure>
 <img src="7-Nexus4-JtagPortMap.jpg" title="7-Nexus4-JtagPortMap.jpg"
 width="500" alt="7-Nexus4-JtagPortMap.jpg" />
 <figcaption aria-hidden="true">7-Nexus4-JtagPortMap.jpg</figcaption>
 </figure>                                                             |
|                                                                      |

''Alternatively, if you have the JTAG Molex adapter set, you can use the
JTAG Molex adapter to connect the phone directly to the RIFF box sans
soldering as follows.

|                                                                            |                                                                            |
|----------------------------------------------------------------------------|----------------------------------------------------------------------------|
| <figure>
 <img src="8.1-Nexus4-JtagPort-JTAG-molex-adapter.jpg"
 title="8.1-Nexus4-JtagPort-JTAG-molex-adapter.jpg" width="500"
 alt="8.1-Nexus4-JtagPort-JTAG-molex-adapter.jpg" />
 <figcaption
 aria-hidden="true">8.1-Nexus4-JtagPort-JTAG-molex-adapter.jpg</figcaption>
 </figure>                                                                   | <figure>
                                                                              <img src="8.2-Nexus4-JtagPort-JTAG-molex-adapter.jpg"
                                                                              title="8.2-Nexus4-JtagPort-JTAG-molex-adapter.jpg" width="500"
                                                                              alt="8.2-Nexus4-JtagPort-JTAG-molex-adapter.jpg" />
                                                                              <figcaption
                                                                              aria-hidden="true">8.2-Nexus4-JtagPort-JTAG-molex-adapter.jpg</figcaption>
                                                                              </figure>                                                                   |
|                                                                            |                                                                            |

**NOTE:** Initially we attempted to read the phone using power supplied
via the phone's battery and the USB port. The results were inconsistent
with the phone disconnecting throughout the read which resulted in read
failures. We opted to use a DC power supply which provided a much more
stable connection to the device.

- The battery on the Nexus 4 uses a blade style connector. In order to
  connect to the power supply, we used a pair of Pomona Micro Grabbers
  attached to an RJ45 cable inserted into an RJ45 receptacle that was
  connected to our DC power supply. See the picture for more detail.

|                                                                        |                                                                          |
|------------------------------------------------------------------------|--------------------------------------------------------------------------|
| <figure>
 <img src="9-Nexus4-MicroGrabber.jpg" title="9-Nexus4-MicroGrabber.jpg"
 width="500" alt="9-Nexus4-MicroGrabber.jpg" />
 <figcaption aria-hidden="true">9-Nexus4-MicroGrabber.jpg</figcaption>
 </figure>                                                               | <figure>
                                                                          <img src="10-Nexus4-MicroGrabber.jpg" title="10-Nexus4-MicroGrabber.jpg"
                                                                          width="500" alt="10-Nexus4-MicroGrabber.jpg" />
                                                                          <figcaption aria-hidden="true">10-Nexus4-MicroGrabber.jpg</figcaption>
                                                                          </figure>                                                                 |
|                                                                        |                                                                          |

- Connect the PCB battery terminal connections to the DC power supply.
  The positive (+) connection is the outermost pin 1 and the negative
  (-) connection is pin 3. You can configure your power supply to match
  the battery specifications which in this case is 3.8V and 2.1A but do
  not apply power at this time. During the JTAG procedure the phone will
  draw about 0.4A.

|                                                                   |
|-------------------------------------------------------------------|
| <figure>
 <img src="11-Nexus4-Reading.jpg" title="11-Nexus4-Reading.jpg"
 width="1000" alt="11-Nexus4-Reading.jpg" />
 <figcaption aria-hidden="true">11-Nexus4-Reading.jpg</figcaption>
 </figure>                                                          |
|                                                                   |

- Now we can start the RIFF JTAG software, configure it for the LG E960,
  and connect the phone to the RIFF box. See the picture for more
  detail.

|                                                                   |
|-------------------------------------------------------------------|
| <figure>
 <img src="12-Nexus4-RIFFBox.jpg" title="12-Nexus4-RIFFBox.jpg"
 width="1000" alt="12-Nexus4-RIFFBox.jpg" />
 <figcaption aria-hidden="true">12-Nexus4-RIFFBox.jpg</figcaption>
 </figure>                                                          |
|                                                                   |

- Apply power from the DC power supply to the phone and turn the phone
  on using the button on the side of the PCB. After powering the phone
  on, select "READ" under the "DCC Read/Write" tab. If all goes well the
  "READ" button will become the "STOP" button and the phone will begin
  reading. If not, the RIFF software provides troubleshooting steps that
  should be taken to assist in diagnosing some of the issues you may
  experience.

**NOTE:** In the event of read errors the RIFF software keeps track of
where the failure occurred and gives you option to restart the read
where it left off.