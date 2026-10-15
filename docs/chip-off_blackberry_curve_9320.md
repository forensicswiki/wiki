---
tags:
  - Mobile
---
The hardware used in the BlackBerry 9315's and 9320's are almost
identical. The following link describes the differences between the
models.

Step 1. Remove the back panel.

![1-bb9320-BackPanelRemoved.jpg](assets/images/1-bb9320-BackPanelRemoved.jpg){width="300"}

Step 2. Remove the SIM and SD Memory Card.

Step 3. Using a torx-6 screw driver remove the 2 visible screws on the back
of the phone.

![2-bb9320-ScrewRemoval.jpg](assets/images/2-bb9320-ScrewRemoval.jpg){width="300"}

Step 4. Remove the screen protector using a shim, guitar pick, or prying
tool.

![3-bb9320-ScreenRemoval.jpg](assets/images/3-bb9320-ScreenRemoval.jpg){width="300"}

Step 5. Remove 2 torx-5 screws.

![4-bb9320-ScrewRemoval.jpg](assets/images/4-bb9320-ScrewRemoval.jpg){width="300"}

Step 6. Use the shim to detach the outer bezel/keyboard from the device.

![5-bb9320-TopPlate.jpg](assets/images/5-bb9320-TopPlate.jpg){width="300"}

![5-1-bb9320-TopPlate.jpg](assets/images/5-1-bb9320-TopPlate.jpg){width="300"}

Step 7. Remove 4 additional torx-6 screws. The main board will now easily be
separated from the back plate

![6-bb9320-ScrewRemoval.jpg](assets/images/6-bb9320-ScrewRemoval.jpg){width="300"}

Step 8. Peel off the vendor sticker.

![7-bb9320-VendorPlate.jpg](assets/images/7-bb9320-VendorPlate.jpg){width="300"}

Step 9. Remove the plastic cover protecting the track pad ribbon cable, and
disconnect the track pad.

Step 10. Remove the final torx-4 screw located beneath the plastic protector,
to remove the plastic keyboard overlay.

![8-bb9320-ScrewRemoval.jpg](assets/images/8-bb9320-ScrewRemoval.jpg){width="300"}

Step 11. Disconnect the ribbon cable connected to the LCD. Then using a pick
separate the display from the main board.

![9-bb9320-ScreenRemoval.jpg](assets/images/9-bb9320-ScreenRemoval.jpg){width="300"}

Step 12. The tear down is now complete

![9-1-bb9320-TearDownComplete.jpg](assets/images/9-1-bb9320-TearDownComplete.jpg){width="300"}

## eMMC Removal

Step 1. The eMMC is located beneath the heat shield directly above the Micro
SD card slot.

![10-bb9320-EMMC-Location.jpg](assets/images/10-bb9320-EMMC-Location.jpg){width="300"}

Step 2. Place the main board in a stand or holder and position it
approximately 2 1/2" - 3" inches away from a heat gun or device the
blows super hot air.

![11-bb9320-HeatShield.jpg](assets/images/11-bb9320-HeatShield.jpg){width="300"}

Step 3. Monitoring the temperature the heat shield will come off easily
between 190-200 Centigrade.

![12-bb9320-HeatShield.jpg](assets/images/12-bb9320-HeatShield.jpg){width="300"}

![13-bb9320-HeatShieldRemoved.jpg](assets/images/13-bb9320-HeatShieldRemoved.jpg){width="300"}

Step 4. Continue working under the high heat. With the 9315/9320's I've
worked on the eMMC has been ready to lift off of the main board
using tweezers immediately after removing the heat shield.

![14-bb9320-EMMC-Removed.jpg](assets/images/14-bb9320-EMMC-Removed.jpg){width="300"}

Step 5. Using liquid flux, or flux paste and a soldering iron clean the pads
on the eMMC in preparation for a read

![15-bb9320-EMMC-Cleanup.jpg](assets/images/15-bb9320-EMMC-Cleanup.jpg){width="300"}

![16-bb9320-EMMC-Clean.jpg](assets/images/16-bb9320-EMMC-Clean.jpg){width="300"}

Step 6. The eMMC is now ready to read using the appropriate
adapter/programmer and software.

At the time of this writing (2013OCT29) the eMMC that was removed in
this example was read using an UP828 programmer via the "VBGA169E"
adapter and using the "eNAND_H9DP4GG4JJACGR-4EM/459MB" device settings.
The resulting image was then parsed via the Cellebrite Physical Analyzer
(V. 3.8.5.108).
