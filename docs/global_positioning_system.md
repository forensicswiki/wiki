---
tags:
  - No Category
---
The **Global Positioning System** (**GPS**) is a satellite navigation
system.

## Forensics

There are several places where GPS information can found. It can be very
useful for forensic investigations in certain situations. GPS devices
have expanded their capabilities and features as the technology has
improved. Some of the most popular GPS devices today are made by
[TomTom](http://www.TomTom.com). Some of the other GPS manufacturers
include [Garmin](http://www.garmin.com) and
[Magellan](http://www.magellangps.com).

### TomTom

TomTom provides a wide range of devices for biking, hiking, and car
navigation. Depending on the capabilities of the model, several
different types of digital evidence can be located on these devices. For
instance, the [TomTom
910](http://www.tomtom.com/products/product.php?ID=212&Category=0&Lid=1)
is basically a 20GB external harddrive. This model can be docked with a
personal computer via a USB cable or through the use of Bluetooth
technology. The listed features include the ability to store pictures,
play MP3 music files, and connect to certain cell phones via bluetooth
technology. Data commonly found on cell phones could easily be found on
the TomTom910. Via the Bluetooth, the TomTom can transfer the entire
contact list from your phone. The GPS unit also records your call logs
and SMS messages. Research needs to be done to see if the TomTom stores
actual trips conducted with the unit. This would include routes, times,
and travel speeds.

The TomTom unit connects to a computer via a USB base station. An
examiner should be able to acquire the image of the harddrive through a
USB write blocker. If not, it may be necessary to remove the hard drive
from the unit.

TomTom models such the TomTom One Regional, TomTom Europe, Go 510, Go
710 and the Go 720 store map data, favourites, and recent destinations
on a removable SD card. This allows the forensic examiner to remove the
SD card and make a backup with a write blocked SD card reader. The most
important file for the forensic examiner will be the CFG file that is
held in the map data directory. This holds a list of all recent
destinations that the user has entered into the device. The information
is held in a hex file and stores the grid coordinates of these
locations.

Certain TomTom models (Go 510, Go 910, Go 920 etc.) allow the user to
pair their mobile phone to the device so they can use the TomTom as a
hands free kit. If the user has paired their phone to the TomTom device,
then the TomTom will store the Bluetooth MAC ID for up to five phones,
erasing the oldest if a sixth phone is paired. Depending on the phone
model paired with the TomTom, there may also be Call lists, contacts and
text messages (sent & received) stored in the device too.

The newer TomTom models do not appear as a mass storage device when
connected to Windows. They run a Linux operating system and are only
accessed via their built in Webserver using the myTomTom program (a
replacement for TomTomHome). They cannot currently by examined
forensically.

Another tool for forensically analysing TomToms is
[TomTology](http://www.forensicnavigation.com). This will retrieve all
journey details from both live and unallocated space. It will tell you
which is the home, favourites and recent destinations and will also tell
you the last journey that was plotted and where the TomTom last had a
GPS fix. It will also extract phone numbers if the device has been
paired with a phone and will find deleted phone numbers, useful for
potentially tracing a previous owner. As of 2012, TomTology has been
superseded by TomTology2. This new program has the same functionality as
TomTology but also deals with Garmins (live and deleted) and Navmans. It
also include inbuilt mapping.

### Garmin

Garmin units connect to a PC in the same way as TomTom, via a USB cable.
The unit will mount as a Mass Storage Unit, similar to a USB Memory
Stick. After drivers for the unit have loaded, it is possible to
navigate the Garmin unit's file system. Many of the files inside can
easily be opened in a text or Hex editor.

Raw trip data including waypoints, date & time stamps, latitude &
longitude coordinates and elevations can be extracted from the
Current.gpx file located in the \Garmin\GPX\\ folder. It can be viewed
by opening the file with a text editor such as
[Notepad++](http://notepad-plus.sourceforge.net/). All recent trips are
stored in this file.

Data can also be easily viewed via [Google
Earth](http://earth.google.com/)'s import feature. If available, Google
Earth will import waypoints, tracks and routes from the unit. A slider
bar in the program will show saved routes by date and time. When a
specific waypoint is selected, a window will open that shows Lat/Long
Coordinates, Altitude, Speed, Heading and Date/Time (Zulu).

With this data, raw or when viewed in Google Earth, entire trips can
easily be reproduced giving exact time and locations for the GPS unit.
It is unknown how many trips the unit is capable of storing or will
store by default, but the [Garmin Nuvi
260W](https://buy.garmin.com/shop/shop.do?pID=37418#nuvi260w) test unit
had 16 days of trip data stored to memory.

### Magellan

Magellan GPS units also connect to a PC via a USB cable. The [Magellan
Roadmate
1400](http://www.magellangps.com/products/product.asp?segID=354&prodID=2053)
unit tested runs a version of Windows CE. The operating system did not
appear to be tailored to the specific unit and had options included in
the menus that were not available (e.g. backup and restore functionality
via a SD memory card slot that did not exist). Upon connecting the unit
to a PC, it will mount as a Mass Storage Unit when and if it is
recognized.

Files that may contain useful information when opened in a text editor:

- /App/Unit.xml
  - This file contains information about the unit such as Model and
    Serial number.
- /App/Media.cfg
  - This file is a short list of what types of files are stored in the
    file structure. (e.g. User data is stored in /USR)
- /Sys/USBTRANS/Unit_ID.dat
  - This file is similar to Unit.xml. It contains more information such
    as Operating System Version and Firmware version.
- /USR/TGUSERA.dat
  - This file may contain addresses, phone numbers and some user set
    points such as "Home". There is no recognizable structure to this
    data so finding useful data is difficult.
- /USR/CITYHIST.dat
  - This file may contain cities entered into the unit by a user. Like
    TGUSERA.dat, there is little structure here. Unfortunately, only
    City and State may be listed here.

Magellan provides
[VantagePoint](http://www.magellangps.com/products/map.asp?PRODID=1903)
software to view map and waypoint data. In order to use this software,
the Magellan unit must be powered on prior to connecting it to a PC. It
is unknown how useful the VantagePoint software is in collecting data as
the software would not recognize the Roadmate 1400 unit. VantagePoint
also did not support the .dat or .cfg files stored on the unit. [Google
Earth](http://earth.google.com/) also supports Magellan units via its
import feature. Earth lists Explorist and Serial as available import
options.

### Digital Camera Images with GPS Information

Some recent digital cameras have built-in GPS receivers (or external modules
you can connect to the camera). This makes it possible for the camera to record
where exactly a photo was taken. This positioning information (latitude,
longitude) can be stored in the [Exif](exif.md) [metadata](metadata.md) header
of [JPEG](jpeg.md) files. Tools such as [jhead](jhead.md) can display the GPS
information in the [Exif](exif.md) headers.  In iOS, the [Photo
Investigator](photo_investigator.md) can extract, view, and remove metadata
from all images, as well as easily identify images with GPS metadata while
scrolling through the images.

### Cell Phones with GPS

Some recent cell phones (e.g. a [Motorola EZX
phone](http://wiki.openezx.org) such as the Motorola A780) have a
built-in GPS receiver and navigation software. This software might
record the paths travelled (and the date/time), which can be very useful
in forensic investigations.

## External Links

- [GPSForensics.org - A communitiy dedicated to GPS device
  forensics](http://www.gpsforensics.org)

<!-- -->

- [Wikipedia:
  GPS](http://en.wikipedia.org/wiki/Global_Positioning_System)

<!-- -->

- [Paraben's Device
  Seizure](http://www.paraben-forensics.com/catalog/product_info.php?cPath=25&products_id=405)

<!-- -->

- [TomTology2 by Forensic Navigation](http://www.forensicnavigation.com)

<!-- -->

- [Blackthorn \| GPS
  Forensics](http://www.berlacorp.com/blackthorn.html)
