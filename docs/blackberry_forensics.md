---
tags:
  - BlackberryOS
  - Howtos
  - Mobile Forensics
  - Tools
---
**Blackberry Forensics** is a page dedicated to the forensics world.
This page should contain all the necessary steps to acquire data from a
BlackBerry Device.

## Warning for BlackBerry Forensics

[BlackBerry](blackberry.md) devices come with password
protection. The owner has the capability to protect all data on the
phone with a password. The user may also specify the amount of attempts
for entering the password before wiping all data from the device.

If you exceed your password attempts limit (defaults to 10, but you can
set it as low as 3), you will be prompted one last time to type the word
BlackBerry.

The device will then wipe. It will be reset to the factory
out-of-the-box condition (default folder structure), and the password
reset. You will lose everything in the device memory, with no
possibility of recovery. It will not reformat the microSD card, since
that's not part of the factory configuration. The phone will still be
usable, and the operating system will be unchanged. So this technique
cannot be used to roll back from an OS upgrade problem.

Obviously this is a serious problem if you need to perform forensics on
the device. The best work around is to work with the owner of the device
and hopefully get them to disclose the password.

## Acquiring BlackBerry Backup File (.ipd)

`* Version 4.6 was used in this example`

Prerequisites:

* Download and install Blackberry Desktop Manager.

Once Desktop Manager is installed:

1. Open Blackberry’s Desktop Manager.

2. Click “Options” then “Connection Settings”

3. If the Desktop Manager hasn't already done so, select “USB-PIN:
Device \#” for connection type. Your device \# may not be the same as
the image below.

4. Click "OK" to return to the main menu.

5. Click “Backup and Restore”.

6. Click the "Back up" button for a full backup of the device or use the
Advanced section for specific data.

7. Select your destination and save the ".ipd" file.

## Opening Blackberry Backup Files (.ipd)

The IPD file can be read using several commercial utilities, including the
MagicBerry IPD Reader and the Amber Blackberry Converter. The example below was
created using version 6.7 of the latter.

1. Use File \| Open and point the program to the BlackBerry backup file
(.ipd).

2. Navigate to the appropriate content by using the navigation icons on
the left and/or top.

### Advanced Export Options

You may also export each subsection of acquired data to different file
types such as pdf, txt, and html, etc.

1. Select the appropriate content from the navigation items on the
left.

2. Either select an individual row or click "Select All" to export all
rows.

3. Click "Fields to export" button

4. Select all the criteria for that subsection in which you wish to
export and click "OK"

5. Select your output type from the bottom list of selections and click
"Save As..."

## Blackberry IPD File Format (.ipd)

For a more advanced and in depth look at the file format of (.ipd)
backup files visit the following site.

<https://www.blackberry.com/us/en>

## Blackberry BBB File Format (Mac OS X) (.bbb)

Blackberry backups generated via Mac OS X are given the extension .bbb,
these are simply .zip compressed files containing a standard .ipd file.

## Acquisition with Paraben's Device Seizure

`* You may purchase a copy of Device Seizure on Paraben's Website `[`here`](https://paraben.com/paraben-for-mobile-forensics/)`.`

As an alternative to acquiring the Blackberry through Amber Blackberry
Converter, Paraben's Device Seizure is a simple and effective method to
acquire the data. The only drawback, is that this method takes
significantly more time to acquire than using Amber Blackberry
Converter.

1. Create a new case in Device Seizure with File \| New.

2. Give the case a name and fill in any desired information about the
case on the next two screens. The third screen is a summary of the data
entered. If all data is correct click Next and then Finish.

3. You are now ready to acquire the phone. Go to Tools \| Data
Acquisition.

4. You are prompted for the supported manufacturer. Select RIM
Blackbery (Physical).

5. Leave supported models at the default selection of autodetect.

6. Connection type should be set to USB.

7. For data type selection select Logical Image (Databases).

8. Confirm your selections on the summary page and click Next to start
the acquisition.
Now wait until the program is done acquiring data from the device.

Please Note: In some instances the wait can be up to 30-45 minutes.

## BlackBerry Simulator

`* For simulating a backup copy of the physical device. This is helpful if the device is low on battery, needs to be turned off, `
`* or you don't want to alter the data on the physical device.`

This is a step by step guide to downloading and using a BlackBerry
simulator. In this example the version 4.0.2 was used in order to
simulate the 7230 series.

1. Select a simulator to download from the drop-down list on the
[BlackBerry website](https://www.blackberry.com/Downloads/entry.do?code=060AD92489947D410D897474079C1477).

- For this example look through the list and download BlackBerry
  Handheld Simulator v4.0.2.51.

2. Then click *Next*.

3. Enter your proper user credentials and click *Next* to continue.

4. On the next page, reply accordingly to the eligibility prompt and
click *Next* to continue.\*

5. Agree or disagree to the SDK agreement and click *Submit* to
continue.\*

6. The next page will provide you with a link to download the .ZIP file
containing the wanted simulator.

- If you disagree at any of these points you will not be able to
  continue to the download.

7. Extract the files to a folder that can easily be accessed (I used
the desktop).

8. In that folder, find the xxxx.bat file (where xxxx is the model
number of the device that is being simulated). The simulator should now
open an image that resembles the phone.

9\. In the *BlackBerry 7230 Simulator* window, select *Simulate* \| *USB
Cable Connected*.

10\. Open BlackBerry Desktop Manager. If there are no Outlook profiles
created there will be a prompt on how to create one. Click *OK* to
continue. If the BlackBerry xxxx Simulator has properly connected to the
BlackBerry Desktop Manager, *Connected* should be displayed at the
bottom of the BlackBerry Desktop Manager window.

11\. Double click *Backup and Restore* \| select *Restore...*.

12\. Navigate to the directory where an .ipd file that has been
previously backed up is stored and select Open to load that file to the
Simulator. See the Acquiring BlackBerry Backup File section above on
information on how to backup a physical BlackBerry.

## Blackberry Protocol

<http://www.off.net/cassis/protocol-description.html>

Here is a useful link to the Blackberry Protocol as documented by Phil
Schwan, Mike Shaver, and Ian Goldberg. The article goes into great
description of packet sniffing and the protocol as it relates to data
transfer across a USB port.

## References

- [phoneMiner](https://www.amraksoftware.com/), phoneMiner
- [ABC](http://www.processtext.com/abcblackberry.html), Amber BlackBerry
  Converter
- [BlackBerry Simulator](https://www.blackberry.com/Downloads/entry.do?code=060AD92489947D410D897474079C1477),
  Simulator Download website
- [IPD](https://www.blackberry.com/us/en),
  IPD File Format
- [Blackberry Protocol](http://www.off.net/cassis/protocol-description.html)
