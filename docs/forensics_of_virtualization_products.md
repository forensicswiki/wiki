---
tags:
  - Howtos
---
## Dealing with Virtual Machine Images

It is becoming increasingly common to find evidence drives with Virtual
Machines (VM) on them. The VMs may contain evidence of their own, but
with their unique file structure, care must be taken during examination.
Running the virtual machine could destroy artifacts that are important.

### Virtual Box

There are two methods for creating a way to mount or inspect a Virtual
Box VM. Virtual Box disks typically have the extension "vdi" for Virtual
Desktop Infrastructure. The mount method requires a Linux system and
"qemu". The other method converts a vdi to a raw image format which can
then be inspected with traditional forensics tools.

#### Mount

1.  Install qemu-kvm using your preferred installation tool (apt-get,
    etc)
2.  Load the network block device module \>sudo modprobe nbd
3.  Use Qemu to load the VDI file as a loop back device \>sudo qemu-nbd
    -c /dev/nbd0 infile.vdi
4.  Mount \>sudo mount /dev/nbd0p1 /mnt
5.  Inspect the file system as needed

To undo:

1.  \>sudo umount /mnt
2.  \>qemu-nbd -d /dev/nbd0

\[<http://bethesignal.org/blog/2011/01/05/how-to-mount-virtualbox-vdi-image/>\|
Source Blog\]

#### Convert

Conversion requires the Virtual Box tool kit, if you don't already have
it.

1.  Install virtualbox-ose using your preferred installation tool
    (apt-get, download from VirtualBox.org, etc)
2.  Convert to raw format \>VBoxManage internalcommands converttoraw
    infile.vdi outfile.img
3.  Inspect the raw image as per usual, either with TSK, EnCase, or
    mount

### VMWare

