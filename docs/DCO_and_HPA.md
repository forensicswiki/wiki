Device Configuration Overlay (DCO) and Host Protected Area (HPA).

## Detection

### Linux

#### Using hdparm

**HPA**

Command:

    # hdparm -N /dev/sda

Disabled HPA:

    /dev/sda:
     max sectors   = 1465149168/1465149168, HPA is disabled

Enabled HPA:

    /dev/sdc:
     max sectors   = 586070255/586072368, HPA is enabled

**DCO**

Command:

    # hdparm --dco-identify /dev/sda

Example output:

    /dev/sda:
    DCO Revision: 0x0001
    The following features can be selectively disabled via DCO:
        Transfer modes:
             mdma0 mdma1 mdma2
             udma0 udma1 udma2 udma3 udma4 udma5 udma6(?)
        Real max sectors: 1465149168
        ATA command/feature sets:
             SMART self_test error_log security HPA 48_bit
             (?): selective_test conveyance_test write_read_verify
             (?): WRITE_UNC_EXT
        SATA command/feature sets:
             (?): NCQ SSP

## Removing HPA

### Linux

#### Using hdparm

Command:

    # hdparm -N p586072368 /dev/sdc

(**permanently** (!) set max visible number of sectors, see example
above)

## Other Tools

- [TAFT (The ATA Forensics Tool)](http://www.vidstrom.net/stools/taft/)
  claims the ability to look at and change the HPA and DCO settings.
- [SAFE-Block](http://www.softpedia.com/get/Security/Security-Related/SAFE-Block.shtml),
  claims the ability to temporarily remove the HPA and remove the DCO
  and later return it to its original state.
- [HDD Capacity
  Restore](http://hddguru.com/content/en/software/2007.07.20-HDD-Capacity-Restore-Tool/),
  a reportedly Free utility that removed the DCO (to give you more
  storage for your hard drive!)
- [Tableau
  TD1](http://www.tableau.com/pdf/en/Tableau_TD1_Product_Brief.pdf) can
  remove the HPA and DCO.
- [Blancco-Pro
  4.5](http://www.mp3cdsoftware.com/blancco---pro-download-292.htm)
  reportedly removes the HPA and DCO to completely obliterate all of
  that pesky information which might get in the way.

## External Links

- [Methods of discovery and exploitation of Host Protected Areas on IDE
  storage devices that conform to
  ATAPI-4](http://www.sciencedirect.com/science?_ob=ArticleURL&_udi=B7CW4-4HR72JM-2&_user=3326500&_rdoc=1&_fmt=&_orig=search&_sort=d&view=c&_acct=C000060280&_version=1&_urlVersion=0&_userid=3326500&md5=030e6e2928779b385c76658736d11b98),
  Mark Bedford, Digital Investigation, Volume 2, Issue 4, December 2005,
  Pages 268-275
- [Hidden Disk Areas: HPA and
  DCO](http://www.utica.edu/academic/institutes/ecii/publications/articles/EFE36584-D13F-2962-67BEB146864A2671.pdf),
  Mayank R. Gupta, Michael D. Hoeschele, Marcus K. Rogers, International
  Journal of Digital Evidence, Fall 2006, Volume 5, Issue 1
- [REMOVING HOST PROTECTED AREAS (HPA) IN
  LINUX](http://www.sleuthkit.org/informer/sleuthkit-informer-20.txt),
  Brian Carrier, SleuthKit Informer \#20
- [Wikipedia article on Device Configuration
  Overlay](http://en.wikipedia.org/wiki/Device_configuration_overlay)
- [Wikipedia article on Host Proteced
  Area](http://en.wikipedia.org/wiki/Host_protected_area)
- [Hiding Data in Hard-Drive’s Service
  Areas](http://www.recover.co.il/SA-cover/SA-cover.pdf), by [Ariel
  Berkman](Ariel_Berkman "wikilink"), February 14, 2013