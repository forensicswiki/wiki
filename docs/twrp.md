---
tags:
  -  Tools
  -  Android
  -  Data Recovery
  -  Howtos
  -  Articles that need to be expanded
---
# TWRP (Team Win Recovery Project)

TWRP (Team Win Recovery Project) is a recovery bootloader for Android
cell phones. It is useful in the following situations:

You can't brute force the password using automated tools.

You can't get a physical image using an existing tool or ADB (root).

You want a physical image without resorting to JTAG/ISP/Chip-Off

This works primarily on Samsung devices given the ease of flashing using
Odin and not needing USB debugging enabled. Some phones may have an OEM
lock or FRP lock enabled, and should tell you in download mode. The
guide written is for the Samsung Galaxy series.

Before starting the process make sure your exhibit is 100% fully charged
and always try the process on a R&D device first. On some devices,
installing a recovery bootloader can unlock the bootloader thereby
erasing all user data hence the reason to R&D first! *Note: Installing a
recovery bootloader \*does\* alter the device from it's original state
but only in that it installs a small bit of software on the system
partition which allows recovery to happen. The separate user data
partition is untouched and remains identical to the data that was on the
device before you started the process.*

The process of using TWRP is as follows:

`* Download the newest version of Odin from `[`http://odindownload.com/`](http://odindownload.com/)`.`
`* Download a TWRP recovery image in .tar format from `[`http://teamw.in/Devices/`](http://teamw.in/Devices/)`. They are specific to your device.`
`* Remove any removable media as TWRP could install to an SD card if one is inserted.`
`* Place the phone in download mode (varies per phone - commonly Vol Down+Home+Power.`
`* Connect the phone to your PC.`
`* Start Odin (phone should be identified in the left side box as 'ID:COM 0:[COMxx]'.`
`* Select the 'Options' tab.`
`* Disable Auto Reboot`
`* Click on the 'AP' button.`
`* Browse to and select your TWRP .tar recovery image.`
`* Click on the 'Start' button.`
`* The download should take a few seconds and will hopefully report "PASS!".`
`* Unplug the phone from the computer.`
`* Remove the battery from the phone to turn it off. Phones without a removable battery will reset after a couple seconds by holding Vol Down+Power. `
`* As soon as the screen goes black, quickly shift to Vol Up+Home to boot into recovery. `
`* Allowing the phone to fully boot may wipe out your freshly installed recovery bootloader and you'll have to start over.`

Physical Method: DD image the device to the internal SD card. This
physical extraction will contain all partitions and files just like a
physical image you would acquire in Cellebrite, Oxygen, XRY, etc.

`* Place the phone in recovery mode by holding Volume Up + Home + Power.  Continue holding for a few seconds until the recovery mode starts booting`
`* Place your microSD card into the device.`
`* Select 'Mount' and select all devices.`
`* Hit the < back button on the device.`
`* Select 'Advanced' and then 'Terminal'.`
`* ~# ls /external_sd (ensure that the SD card is mounted)`
`* ~# dd if=/dev/block/mmcblk0 of=/external_sd/out.bin`
`* The physical image will take a while to complete.`
`* Power off the device by selection Back, Back, Reboot, and Power off.`
`* Remove the microSD card.`

## Alternate Method: dd image the device over the network with netcat

Note: The below instructions can be done in Linux or Windows with the
Android SDK and Netcat. Netcat for Windows commonly comes with Nmap if
you need to download it.

`* Place the phone in recovery mode by holding Volume Up + Home + Power.`

All of the below commands are done from your computer:

`* Download and install the Android SDK tools (http://developer.android.com/sdk/index.html#Other).`
`* Start the Android SDK Manager and install the 'Android SDK Platform-tools'.`
`* Open up a command prompt window in 'C:\Program Files (x86)\Android\android-sdk\platform-tools'.`
`* Confirm your device is visible to the computer:`
`* adb start-server`
`* adb devices (device should be shown as attached)`
`* adb forward tcp:8888 tcp:8888' and leave the command prompt window open.`
`* adb shell `

(you are now issuing commands inside the phone through the shell)

`* # cd /dev/block`
`* # ls  (find if your structure is in mmcblk or sda as it differs between phones. sda devices you will image sda, mmcblk devices you will image mmcblk0)`
`* # dd if=/dev/block/mmcblk0 | busybox nc -l -p 8888`

(back on your computer, second command prompt window)

`* nc 127.0.0.1 8888 > test.bin   (or ncat.exe if using Windows)`
`* The physical image will take a while to complete, and will image out to your current directory, or you can specify - C:\temp\phone\galaxy.bin).`
`* Power off the device by selection Back, Back, Reboot, and Power off.`
`* If the extraction does not start, re-run 'adb.exe forward tcp:8888 tcp:8888' then run 'netstat -n' on a Windows machine to confirm that 127.0.0.1 show's that it's listening on port 8888.`

## Unbricking a phone

Note: Prior to v3.0.2.0, there was more of a chance that after uploading
TWRP, the phone will be bricked and go into a boot loop upon restarting,
even if it's able to get into TWRP recovery. The newer versions of TWRP
(v3.1.0.0 as of 17APR03) have tested a lot more successfully on a wider
range of phones.

`* Go into the recovery bootloader -> Wipe -> Advanced Wipe -> Dalvik/ART Cache and Cache -> Wipe.`

Restart the phone in the regular boot mode, and see if it will boot past
the loop. If not, you will have to flash a stock image to the phone.

`* Download a stock ROM image for the phone. `[`http://www.sammobile.com`](http://www.sammobile.com)` provides firmware images for every kind of Samsung phone, Android version, and even cell carrier. `
`* Put the phone back into download mode and connect to your computer.`
`* Use ODIN to push the ROM to the phone using the same process as TWRP. Enable Auto Reboot. This process will take a significantly longer time as a ROM is around 1 GB depending on the OS.`

The phone will reboot and take a minute or two to fully boot. It should
now be like factory new. If the phone still goes into a bootloop, try a
different image. If the phone appears frozen on a splash screen, give it
a good half hour before re-trying the process.