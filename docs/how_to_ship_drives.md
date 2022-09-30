---
tags:
  -  Howtos
---
I was recently asked about shipping drives for forensic analysis, and
since I've seen this done successfully and seen failures, I thought I
would write this advice up for general consumption.

Shipping disks is tricky, but often needs to be done. Copying entire
images over networks is often impossible due to the sheer size of the
image. If you must ship disks, here are some instructions:

1.  Never ship the original drive (unless necessary for legal reasons).
    Regardless of the ultimate disposition of the original drive, always
    start by shipping an [image](:category:disk_imaging.md).
2.  Use one of the [Write Blockers](write_blockers.md) mentioned
    on this page. The write blocker goes on the original drive to ensure
    that nothing is changed on the drive by the host OS of the imaging
    workstation.
3.  A drive can be imaged by a number of free software
    [tools](:category:disk_imaging.md), such as [FTK
    Imager](ftk_imager.md). Some of these tools compress and/or
    encrypt data; I recommend both, as you don't want someone getting
    their hands on your data, and if you have multiple images to send,
    you can put them on one, say, 1TB drive.
4.  Image to a bare (internal) hard drive, such as [these internal hard
    drives](http://www.google.com/products?q=1tb+internal+hard+drive&aq=0&oq=1tb+inter).
5.  To write to the image drive use either a [Firewire/USB2/eSATA
    docks](http://eshop.macsales.com/item/Newer%20Technology/FWU2ES2HDK/)
    or [USB2/eSATA
    docks](http://eshop.macsales.com/item/Newer%20Technology/U2ES2HDK/).
    I recommend getting two of these.
6.  Keep the original drive safe and intact (and unshipped) until you
    verify that the image has been received intact.
7.  In addition, keep a copy of the images, if possible. This will
    double your image storage needs, but if you are doing this
    regularly, you don't want to have to re-image the drives, and I
    guarantee that failures will occur if you do this long enough. Also,
    you may have concerns about this original drive, as it may fail.
8.  ALWAYS ALWAYS ALWAYS SHIP PROPERLY! Don't ship a drive in an
    enclosure, as these provide minimal protection, and the drive
    interface is plugged into something that can move. Not a good idea.
    Take the drives out of the enclosure (if there is one - if you've
    followed my advice above, you're working with images on bare
    drives). Then get either a [hard drive shipping
    kit](http://www.aquaphoenix.com/misc/sale/hdd_box/), if you are
    shipping multiple drives, or a [single drive
    case](http://www.amazon.com/Hard-Drive-Transporter/dp/B002IY6B9U).
    If you can't do this, wrap the drive in foam sheeting or bubble wrap
    (three times is good), and tape up the wrapped drive. If you don't
    have access to any other packing material, then use towels or other
    thick cloth. The key is something to absorb impact when the package
    is inevitably dropped.
9.  Make sure you properly unmount the drive from the imaging station
    before you disconnect it. If you don't know how
    - [Ejecting Media on a
      Mac](http://macs.about.com/od/faq1/f/ejectcddvd.htm)
    - [Ejecting Media on
      Windows](http://ask-leo.com/safely_remove_hardware_where_did_the_icon_go_how_do_i_safely_remove_hardware_without_it.html)
    - [Ejecting Media on
      Linux](http://www.scottklarr.com/topic/133/how-to-mount-and-unmount-a-drive-in-linux/)

NB 1: This is advice, not a set of rules. Do what you can to secure your
media and data.

NB 2: This does NOT take account of chain-of-evidence issues, obviously.
This is about imaging and packing ONLY.

