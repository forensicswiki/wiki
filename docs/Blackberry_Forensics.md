**Blackberry Forensics** is a page dedicated to the forensics world.
This page should contain all the necessary steps to acquire data from a
BlackBerry Device.


## Warning for BlackBerry Forensics

[BlackBerry](BlackBerry "wikilink") devices come with password
protection. The owner has the capability to protect all data on the
phone with a password. The user may also specify the amount of attempts
for entering the password before wiping all data from the device.

![](Image1.jpg "Image1.jpg")

If you exceed your password attempts limit (defaults to 10, but you can
set it as low as 3), you will be prompted one last time to type the word
BlackBerry.

![](Image2.jpg "Image2.jpg")

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
Download and install Blackberry Desktop Manager.
Use the following link to select and download the install file that fits
your system or version.
<https://www.blackberry.com/Downloads/entry.do?code=A8BAA56554F96369AB93E4F3BB068C22>

Once Desktop Manager is installed:
1. Open Blackberry’s Desktop Manager.
2. Click “Options” then “Connection Settings”
![](BBManager4_6_Options.JPG "BBManager4_6_Options.JPG")

4. If the Desktop Manager hasn't already done so, select “USB-PIN:
Device \#” for connection type. Your device \# may not be the same as
the image below.
![](BBManager4_6_Connect.JPG "BBManager4_6_Connect.JPG")
5. Click "OK" to return to the main menu.

6. Click “Backup and Restore”.
![](BBManager4_6_Backup.JPG "BBManager4_6_Backup.JPG")

7. Click the "Back up" button for a full backup of the device or use the
Advanced section for specific data.
![](BBManager4_6_Backup1.JPG "BBManager4_6_Backup1.JPG")

8. Select your destination and save the ".ipd" file.
![](BBManager4_6_Save.JPG "BBManager4_6_Save.JPG")

### Using Older Versions of Desktop Manager

Visit the archived instructions for use with older versions of Desktop
Manager [click here](Blackberry_Forensics_Backup_File_Old "wikilink").




## Opening Blackberry Backup Files (.ipd)\*

The IPD file can be read using several commercial utilities, including
the [MagicBerry IPD Reader](MagicBerry_IPD_Reader "wikilink") and the
[Amber Blackberry Converter](Amber_Blackberry_Converter "wikilink"). The
example below was created using version 6.7 of the latter.


1. Use File \| Open and point the program to the BlackBerry backup file
(.ipd).

![](ABCOpen.JPG "ABCOpen.JPG")


2. Navigate to the appropriate content by using the navigation icons on
the left and/or top.
![](ABCView.JPG "ABCView.JPG")
<small>click for enlarged version</small>

### Advanced Export Options

You may also export each subsection of acquired data to different file
types such as pdf, txt, and html, etc.
1. Select the appropriate content from the navigation items on the
left.
2. Either select an individual row or click "Select All" to export all
rows.
![](ABCExportSelectAll.JPG "ABCExportSelectAll.JPG")

3. Click "Fields to export" button
![](ABCExportButton.JPG "ABCExportButton.JPG")

4. Select all the criteria for that subsection in which you wish to
export and click "OK"
![](ABCExportFields.JPG "ABCExportFields.JPG")

5. Select your output type from the bottom list of selections and click
"Save As..."
![](ABCExportOptions.JPG "ABCExportOptions.JPG")


## Blackberry IPD File Format (.ipd)

For a more advanced and in depth look at the file format of (.ipd)
backup files visit the following site.

<http://na.blackberry.com/eng/devjournals/resources/journals/jan_2006/ipd_file_format.jsp>


## Blackberry BBB File Format (Mac OS X) (.bbb)

Blackberry backups generated via Mac OS X are given the extension .bbb,
these are simply .zip compressed files containing a standard .ipd file.

## Acquisition with Paraben's Device Seizure

`* You may purchase a copy of Device Seizure on Paraben's Website `[`here`](http://www.paraben.com/device-seizure.html)`.`

As an alternative to acquiring the Blackberry through Amber Blackberry
Converter, Paraben's Device Seizure is a simple and effective method to
acquire the data. The only drawback, is that this method takes
significantly more time to acquire than using Amber Blackberry
Converter.

1\. Create a new case in Device Seizure with File \| New.

2\. Give the case a name and fill in any desired information about the
case on the next two screens. The third screen is a summary of the data
entered. If all data is correct click Next and then Finish.

3\. You are now ready to acquire the phone. Go to Tools \| Data
Acquisition.

4\. You are prompted for the supported manufacturer. Select RIM
Blackbery (Physical).
![](Image10.JPG "Image10.JPG")

5. Leave supported models at the default selection of autodetect.
![](Image11.JPG "Image11.JPG")

6. Connection type should be set to USB.
![](Image12.JPG "Image12.JPG")

7. For data type selection select Logical Image (Databases).
![](Image13.jpg "Image13.jpg")

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
[BlackBerry
website](https://www.blackberry.com/Downloads/entry.do?code=060AD92489947D410D897474079C1477).

- For this example look through the list and download BlackBerry
  Handheld Simulator v4.0.2.51.

2\. Then click *Next*.

3\. Enter your proper user credentials and click *Next* to continue.

4\. On the next page, reply accordingly to the eligibility prompt and
click *Next* to continue.\*

5\. Agree or disagree to the SDK agreement and click *Submit* to
continue.\*

6\. The next page will provide you with a link to download the .ZIP file
containing the wanted simulator.

- \- If you disagree at any of these points you will not be able to
  continue to the download.

7\. Extract the files to a folder that can easily be accessed (I used
the desktop).

8\. In that folder, find the xxxx.bat file (where xxxx is the model
number of the device that is being simulated). The simulator should now
open an image that resembles the phone.

9\. In the *BlackBerry 7230 Simulator* window, select *Simulate* \| *USB
Cable Connected*. Refer to *Figure BS-1* for further assistance.

![](7230_1.JPG "7230_1.JPG")

*Figure BS-1*

10\. Open BlackBerry Desktop Manager. If there are no Outlook profiles
created there will be a prompt on how to create one. Click *OK* to
continue. If the BlackBerry xxxx Simulator has properly connected to the
BlackBerry Desktop Manager, *Connected* should be displayed at the
bottom of the BlackBerry Desktop Manager window. Refer to *Figure BS-2*
for further assistance.

![](BBDM_1.JPG "BBDM_1.JPG")

*Figure BS-2*

11\. Double click *Backup and Restore* \| select *Restore...*. Refer to
*Figure BS-2* for further reference.

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

- [phoneMiner](http://www.amraksoftware.com/), phoneMiner
- [ABC](http://www.processtext.com/abcblackberry.html), Amber BlackBerry
  Converter
- [BlackBerry
  Simulator](https://www.blackberry.com/Downloads/entry.do?code=060AD92489947D410D897474079C1477),
  Simulator Download website
- [Blackberry](http://www.forensicswiki.org/wiki/BlackBerry), BlackBerry
  Forensics Wiki page
- [Desktop
  Manager](https://www.blackberry.com/Downloads/entry.do?code=A8BAA56554F96369AB93E4F3BB068C22),
  BlackBerry Desktop Manager Download website
- [IPD](http://na.blackberry.com/eng/devjournals/resources/journals/jan_2006/ipd_file_format.jsp),
  IPD File Format
- [Older Desktop Manager
  Versions](Blackberry_Forensics_Backup_File_Old "wikilink"), Using
  older versions of BlackBerry Desktop
- [Paraben](http://www.paraben-forensics.com/catalog/index.php), Paraben
  Corporation website
- [Blackberry
  Protocol](http://www.off.net/cassis/protocol-description.html)
- [Forensic Examination of a RIM (BlackBerry) Wireless
  Device](http://www.rh-law.com/ediscovery/Blackberry.pdf)