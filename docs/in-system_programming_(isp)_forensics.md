---
tags:
  - No Category
---
## Definition

In-System Programming (ISP) is the ability of to program devices while
installed in a complete system, rather than requiring the chip to be
programmed prior to installing it into the system. In-system programming
(ISP) can also be called In-Circuit Serial Programming (ICSP).

## Forensic Application

ISP, in a forensic application, is an acquisition procedure which
involves connecting to specific points on the device to directly read a
component. This process bypasses the devices CPU as it reads the
component directly. The specific points used are essentially the visible
points on the PCB which connect to the hidden points underneath the
chip. For this reason, these points are direct electrical connections to
the chip you are trying to read.

ISP can therefore be used to directly read the device storage such as
the eMMC which will provide you with a raw binary image of the chip.
Performing an ISP procedure on supported phones can be an extremely
effective technique to extract a full physical image from devices
without having to resort to a chip-off procedure which is destructive.
Once completed, the phone or device can be re-assembled and should
function normally.

## Tools and Equipment

- [JTAG and Chip-Off Tools and Equipment](jtag_and_chip-off_tools_and_equipment.md)

## Procedures

- [ISP Lumia 635/RM-975](isplumia635.md)
