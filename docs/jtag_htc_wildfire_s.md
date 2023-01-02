---
tags:
  - Mobile
---
## JTAG HTC Wildfire S

The HTC Wildfire S is an Android based smartphone. At the time of this
writing (2012MAR30) I am unaware of any method to bypass the PIN,
password, or pattern locks on a HTC Wildfire S that is not rooted and
does not have ADB enabled. JTAG to the rescue! Using JTAG, a copy of the
NAND can be extracted, and the pin or pattern lock decoded from it.

For the purpose of this document, a Virgin Mobile HTC Wildfire S was
disassembled, read via JTAG, reassembled, the pattern lock changed, and
the process repeated. This process was done to get 2 reads from the
device with different pattern locks each time. The first pattern lock
was set to represent a "T" character while the second pattern lock was
set to represent a "C" character.

### Getting Started

What you need to extract the lock from the device:

1.  A RIFF Box with the latest JTAG Manager software. The RIFF Box used
    for this was purchased from <http://www.multi-com.pl>.
2.  HTC Wildfire S JTAG adapter (or soldering skillz). The adapter used
    for this was purchased from <http://www.multi-com.pl>.
3.  A DC Power supply capable of supplying 3.7V/1.3A output. The power
    supply used for this was an Agilent U8002A DC Power Supply.
4.  PatternLockScripts from CCL Forensics
    ('GenerateAndroidGestureRainbowTable.py' and
    'Android_GestureFinder.py').

### NAND Dump Procedure

1.  Disassemble the phone down to the PCB.
2.  Connect the RIFF Box to the PCB via USB.
3.  Connect the RIFF Box to the PCB via the JTAG adapter.
4.  Connect the RIFF Box to the PC via USB.
5.  Connect the PCB to the DC power supply.
6.  Start the "JTAG Manager" software and configure.
7.  Power the PCB.
8.  Dump the NAND.

Instructions for disassembly can be found on Internet but it can be
summarised as follows:

1.  Remove the rear cover and battery.
2.  Remove the Torx and Phillips screws.
3.  Split the phone case using a case opening tool (guitar pick).
4.  Disconnect the 3 tiny ribbon cables (tweezers on either side).
5.  Remove the PCB.

You are now ready to connect the PCB to the RIFF Box and the RIFF Box to
the PC. See the pictures for more detail. Note: The JTAG adapter
indicates pin 1 on the top of the PCB with a small dot (covered by the
rubber band in these pictures).

|                                                                         |                                                                         |
|-------------------------------------------------------------------------|-------------------------------------------------------------------------|
| <figure>
 <img src="riff-to-htc-wildfire-s-connection-1.png"
 title="riff-to-htc-wildfire-s-connection-1.png" width="550"
 alt="riff-to-htc-wildfire-s-connection-1.png" />
 <figcaption
 aria-hidden="true">riff-to-htc-wildfire-s-connection-1.png</figcaption>
 </figure>                                                                | <figure>
                                                                           <img src="riff-to-htc-wildfire-s-connection-2.png"
                                                                           title="riff-to-htc-wildfire-s-connection-2.png" width="550"
                                                                           alt="riff-to-htc-wildfire-s-connection-2.png" />
                                                                           <figcaption
                                                                           aria-hidden="true">riff-to-htc-wildfire-s-connection-2.png</figcaption>
                                                                           </figure>                                                                |
|                                                                         |                                                                         |

|                                                                         |
|-------------------------------------------------------------------------|
| <figure>
 <img src="riff-to-htc-wildfire-s-connection-3.png"
 title="riff-to-htc-wildfire-s-connection-3.png" width="800"
 alt="riff-to-htc-wildfire-s-connection-3.png" />
 <figcaption
 aria-hidden="true">riff-to-htc-wildfire-s-connection-3.png</figcaption>
 </figure>                                                                |
|                                                                         |

Now we can start the RIFF Box JTAG Manager software and configure it.

Connect the PCB battery terminal connections to the DC power supply. The
negative (-) connection is the innermost PIN and the positive (+) pin is
the outside PIN.

Apply power to the DC power supply and turn the phone on using the tiny
little button on the ribbon cable attached to the top of the PCB. After
powering the phone on, start the NAND dump by clicking the "Read Memory"
button in the JTAG Manager software. The NAND dump read needs to be
started shortly after the phone is powered on. Once the NAND read is
complete you can click on the "Save" button to save the binary dump to a
file.

If you receive errors that the PCB could not be connected to, try the
following:

- Confirm that the PCB is receiving power from the DC power supply. If
  you can measure current draw of the PCB, you should see that the PCB
  is pulling about 0.07A. If the PCB is pulling more current, it is
  likely already booted and the read may fail.
- Power off the PCB, power it back on, and immediately start the JTAG
  Manager read.
- Check the JTAG adapter to ensure it is correctly orientated and that
  all the pogo pins are touching the PCB JTAG pads.
- Recheck the JTAG to PCB connections.
- Upon receiving a successful JTAG dump you can process the file with
  the CCL Forensics Android scripts to extract the gesture or pin lock.

## References

* <http://forensics.spreitzenbarth.de/2012/02/>
