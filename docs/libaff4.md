---
tags:
  -  Disk Imaging
---
LibAFF4 is an implementation of the AFF4 standard. It is still in a very
early stage of development but it allows people to have a play with the
new standard. This page documents it.

## Installing LibAFF4

The source code is currently kept under version control on Google code (
<http://code.google.com/p/aff4/> ). It can be obtained using the
Mercurial Source Control Management (SCM) tools. To create a new copy of
the AFF4 source tree.

`hg clone `[`https://aff4.googlecode.com/hg/`](https://aff4.googlecode.com/hg/)` aff4`

Once the AFF4 source tree is downloaded in the aff4 directory, it can be
build and installed as following:

- First check and edit **config.py**.
- Make sure you have the necessary access privileges for the
  installation location then run:

`./scon install`

Check **INSTALL** in the aff4 directory for more information.

AFF4 requires the following packages:

- OpenSSL development package (Debian: openssl-dev, Fedora:
  openssl-devel)
- UUID development package (Debian: uuid-dev, Fedora (recent version):
  libuuid-devel)

The following are optional but recommended packages:

- libcurl4-openssl-dev
- libfuse-dev

## Taking an image

Probably the first step is to actually acquire the image. Right now
there is no fancy interface or GUI - its just a simple commandline:

    AFF4/tools$ sudo aff4imager -i -o /tmp/test.zip /dev/sda1
    Imaging Mode selected
    Dumping segment urn:aff4:dd3102c1-370d-4b15-83e7-5a1991b5a9e1/00000000 (55425084 bytes)
    Dumping segment urn:aff4:dd3102c1-370d-4b15-83e7-5a1991b5a9e1/00000001 (33314018 bytes)
    Dumping segment urn:aff4:dd3102c1-370d-4b15-83e7-5a1991b5a9e1/00000002 (3011613 bytes)
    Dumping segment urn:aff4:dd3102c1-370d-4b15-83e7-5a1991b5a9e1/00000003 (51756091 bytes)
    Creating a link object 'default' for stream 'urn:aff4:dd3102c1-370d-4b15-83e7-5a1991b5a9e1'

We can see the imager dumping a new zip file with the default settings.
By default bevies are 64Mb in size. The aff4imager tool reports each new
bevy which is saved to disk and the size it ended up taking (after
compression). Finally we see a link object is created to the new stream
to make it easier to access it (so we dont need to remember the long URN
for it).

## Applying the Sleuthkit patch

There is a patch to sleuthkit for adding support to AFF4. The patch is
against sleuthkit-3.0.1.

    tar -xvzf sleuthkit-3.0.1.tgz
    cd sleuthkit-3.0.1
    patch -p1 < /path/to/AFF4/patches/sleuthkit-3.0.1.patch

    ## The following is needed to get the autoconf system to pick up the changes
    libtoolize --force
    aclocal -I config
    autoheader
    automake
    autoconf

    ## Now build it as normal
    ./configure
    make install

Currently the Sluethkit patch does not work with autodetection - hence
it must be specified explicitely using `-i aff4`.

AFF4 is a bit different since it refers not only to a volume, but to a
stream within the volume. The convension is to specify the stream as the
last parameter after the volumes. So for example, to open the stream
created in the example above:

    $ fls -i aff4 /tmp/test.zip default
    zip.c:51 - FileBackedObject_Con: Can't open file:///tmp/test.zip/__URN__ (Not a directory)
    libaff4.c:27 - open_volume: Loaded zip volume file:///tmp/test.zip
    zip.c:51 - FileBackedObject_Con: Can't open file://default/__URN__ (No such file or directory)
    zip.c:51 - FileBackedObject_Con: Can't open file://default (No such file or directory)
    libaff4.c:100 - aff4_open: Trying to open stream default relative to all volumes
    libaff4.c:107 - aff4_open: Trying urn:aff4:aeb9ed57-8dbe-4506-9fb8-e4106bf0767d/default
    libaff4.c:122 - aff4_open: Using urn:aff4:dd3102c1-370d-4b15-83e7-5a1991b5a9e1 as the stream name
    d/d 11: lost+found
    r/r 10043:  System.map-2.6.22-14-generic
    r/r 6025:   vmlinuz-2.6.22-14-generic
    r/r 10041:  config-2.6.22-14-generic
    r/r 10042:  abi-2.6.22-14-generic
    r/r 13: initrd.img-2.6.22-14-generic
    d/c 44177:  grub
    r/r 6029:   initrd.img-2.6.24-21-generic
    r/r 12: initrd.img-2.6.22-14-generic.bak
    .....

The debugging messages above are instructive to explain the logic of how
libaff4 opens the volumes. Since you can specify any number of volumes
of the command line you can see that libaff4 first tries to open the
volume as a directory volume, if that fails, it tries to open it as a
zip file. The last element is assumed to be a volume name and if no such
volume is found, its assumed to be a stream name. Then the stream name
is searched in all the volumes specified. Finally the stream name is
resolved (since its a link it returns the URN of the original stream).

## Signing images

The easiest way to get a private key and a corresponding X.509
certificate is to make a self-signed certificate using the openssl
command.

        openssl req -x509 -newkey rsa:1024 -keyout sign.key -out sign.key -nodes

This command will ask you a bunch of questions; the results are stored
in the file sign.crt. When you create a signed AFF4 file the certificate
will be stored in the file, so be careful what you say. Alternatively,
you can create an RSA private/public key pair, create a certificate
request (CSR), send the CSR to a certificate authority, and use the
certificate that the authority sends you back.

Note that this puts both the key and the self-signed certificate in the
same file. That's fine for our purposes. The certificate will be copied
into the AFF4 volume, but the private key will never be copied.

You can view the contents the certificate with this openssl command:

        openssl x509 -text -in sign.key

By loading the key and crt files, libaff4 will add the hash of each new
segment written to a new statement. When the file is closed, the
statement will be written to the volume.

    $ aff4imager -i -o /tmp/test.zip --key sign.key --cert sign.key /dev/sda1
    Imaging Mode selected
    identity.c:58 - Identity_load_certs: Will now sign using private key file://sign.key
    identity.c:88 - Identity_load_certs: Will use public key from file://sign.key to verify signatures
    Dumping segment urn:aff4:fda4d4fa-c378-4a06-acac-06ff54f49d5f/00000000 (55425084 bytes)
    Dumping segment urn:aff4:fda4d4fa-c378-4a06-acac-06ff54f49d5f/00000001 (33314018 bytes)
    Dumping segment urn:aff4:fda4d4fa-c378-4a06-acac-06ff54f49d5f/00000002 (3011613 bytes)
    Dumping segment urn:aff4:fda4d4fa-c378-4a06-acac-06ff54f49d5f/00000003 (51756091 bytes)
    Creating a link object 'default' for stream 'urn:aff4:fda4d4fa-c378-4a06-acac-06ff54f49d5f'

    zip.c:746 - ZipFile_open_member: Volume does not contain member urn:aff4:identity/41:38:13:1b:96:d3:f6:65:e0:87:60:07:f5:ff:31:19:24:93:e0:13/cert.pem

The last debug statement indicates that the certificate file in not
present in the volume, therefore it is added. It is instructive to see
what segments are present in the zip volume:

    $ unzip -l /tmp/test.zip
    Archive:  /tmp/test.zip
    urn:aff4:89f8ec58-13f0-4ad4-b1f2-74da7f3aed40
      Length     Date   Time    Name
     --------    ----   ----    ----
     55425084  04-25-09 21:54   urn%3Aaff4%3Afda4d4fa-c378-4a06-acac-06ff54f49d5f/00000000
         8196  04-25-09 21:54   urn%3Aaff4%3Afda4d4fa-c378-4a06-acac-06ff54f49d5f/00000000.idx
     33314018  04-25-09 21:54   urn%3Aaff4%3Afda4d4fa-c378-4a06-acac-06ff54f49d5f/00000001
         8196  04-25-09 21:54   urn%3Aaff4%3Afda4d4fa-c378-4a06-acac-06ff54f49d5f/00000001.idx
      3011613  04-25-09 21:54   urn%3Aaff4%3Afda4d4fa-c378-4a06-acac-06ff54f49d5f/00000002
         8196  04-25-09 21:54   urn%3Aaff4%3Afda4d4fa-c378-4a06-acac-06ff54f49d5f/00000002.idx
     51756091  04-25-09 21:54   urn%3Aaff4%3Afda4d4fa-c378-4a06-acac-06ff54f49d5f/00000003
         6552  04-25-09 21:54   urn%3Aaff4%3Afda4d4fa-c378-4a06-acac-06ff54f49d5f/00000003.idx
          209  04-25-09 21:54   urn%3Aaff4%3Afda4d4fa-c378-4a06-acac-06ff54f49d5f/properties
          115  04-25-09 21:54   default/properties
         1251  04-25-09 21:54   urn%3Aaff4%3Aidentity/41%3A38%3A13%3A1b%3A96%3Ad3%3Af6%3A65%3Ae0%3A87%3A60%3A07%3Af5%3Aff%3A31%3A19%3A24%3A93%3Ae0%3A13/00000000
          128  04-25-09 21:54   urn%3Aaff4%3Aidentity/41%3A38%3A13%3A1b%3A96%3Ad3%3Af6%3A65%3Ae0%3A87%3A60%3A07%3Af5%3Aff%3A31%3A19%3A24%3A93%3Ae0%3A13/00000000.sig
         3820  04-25-09 21:54   urn%3Aaff4%3Aidentity/41%3A38%3A13%3A1b%3A96%3Ad3%3Af6%3A65%3Ae0%3A87%3A60%3A07%3Af5%3Aff%3A31%3A19%3A24%3A93%3Ae0%3A13/cert.pem
          242  04-25-09 21:54   urn%3Aaff4%3Aidentity/41%3A38%3A13%3A1b%3A96%3Ad3%3Af6%3A65%3Ae0%3A87%3A60%3A07%3Af5%3Aff%3A31%3A19%3A24%3A93%3Ae0%3A13/properties
     --------                   -------
    143543711                   14 files

As can be seen, the certificate is stored within the volume. Lets have a
look at the statement:

    $ unzip -p /tmp/test.zip urn%3Aaff4%3Aidentity/41%3A38%3A13%3A1b%3A96%3Ad3%3Af6%3A65%3Ae0%3A87%3A60%3A07%3Af5%3Aff%3A31%3A19%3A24%3A93%3Ae0%3A13/00000000
    urn:aff4:fda4d4fa-c378-4a06-acac-06ff54f49d5f/00000000 aff4:sha256=RaOr4ksNZo+bXKMYDw2hwaAMqV9/4/TXqTE1P/7ERO8=
    urn:aff4:fda4d4fa-c378-4a06-acac-06ff54f49d5f/00000000.idx aff4:sha256=k4uSgGyYp0xeBdnpCWAY4sJilijn9sU9nmRkbzPl5LQ=
    urn:aff4:fda4d4fa-c378-4a06-acac-06ff54f49d5f/00000001 aff4:sha256=0Xf/VVaJe2RZ8eH9ACUTHWp8TXYdq5a/7hkdTn1eYGU=
    urn:aff4:fda4d4fa-c378-4a06-acac-06ff54f49d5f/00000001.idx aff4:sha256=9szVqgGIFHT7OxtWiopk7rP4HSsl4H+nHmnNVhqSjLg=
    urn:aff4:fda4d4fa-c378-4a06-acac-06ff54f49d5f/00000002 aff4:sha256=P6jENcyLn137Jl5QNCauQvviIXR/VSp7o7r0iNUDHX0=
    urn:aff4:fda4d4fa-c378-4a06-acac-06ff54f49d5f/00000002.idx aff4:sha256=EzXJ4eyJNYzKCUVc1U3vRzgLA+GhLCmsSkkcwholeqs=
    urn:aff4:fda4d4fa-c378-4a06-acac-06ff54f49d5f/00000003 aff4:sha256=ImM/kFyvDqkWa3A6HitIFtJaXf2gWpEx8knYWSMiVoE=
    urn:aff4:fda4d4fa-c378-4a06-acac-06ff54f49d5f/00000003.idx aff4:sha256=Lm2yB+tVw8yB1ia9MXIxkdRT8oXk1/2db9sFg48ZuoM=
    urn:aff4:fda4d4fa-c378-4a06-acac-06ff54f49d5f/properties aff4:sha256=9h9x5sd7ZxCKqWbcdLYVq7MM9AH7c6BI5DpCJrxCXUc=
    urn:aff4:fda4d4fa-c378-4a06-acac-06ff54f49d5f aff4:sha256=fuy15WT9G5YpAh6PdLGxeCezoWtV6QryqnOhYvnV1Fc=
    urn:aff4:89f8ec58-13f0-4ad4-b1f2-74da7f3aed40/default/properties aff4:sha256=2uxWY7B51oUa94B3hMU1iF1vZUNUdFPo/hNDUIrduCA=

## Verifying signatures and inspecting AFF4 files

We wish to verify the above volume and learn more about the objects
contained within it:

    $ aff2imager -l /tmp/test.zip -V -I
    zip.c:51 - FileBackedObject_Con: Can't open file:///tmp/test.zip/__URN__ (Not a directory)
    libaff4.c:27 - open_volume: Loaded zip volume file:///tmp/test.zip
    Info mode selected
    identity.c:88 - Identity_load_certs: Will use public key from urn:aff4:identity/41:38:13:1b:96:d3:f6:65:e0:87:60:07:f5:ff:31:19:24:93:e0:13/cert.pem to verify signatures
    urn:aff4:fda4d4fa-c378-4a06-acac-06ff54f49d5f/00000000 (segment): (OK)
    urn:aff4:fda4d4fa-c378-4a06-acac-06ff54f49d5f/00000000.idx (segment): (OK)
    urn:aff4:fda4d4fa-c378-4a06-acac-06ff54f49d5f/00000001 (segment): (OK)
    urn:aff4:fda4d4fa-c378-4a06-acac-06ff54f49d5f/00000001.idx (segment): (OK)
    urn:aff4:fda4d4fa-c378-4a06-acac-06ff54f49d5f/00000002 (segment): (OK)
    urn:aff4:fda4d4fa-c378-4a06-acac-06ff54f49d5f/00000002.idx (segment): (OK)
    urn:aff4:fda4d4fa-c378-4a06-acac-06ff54f49d5f/00000003 (segment): (OK)
    urn:aff4:fda4d4fa-c378-4a06-acac-06ff54f49d5f/00000003.idx (segment): (OK)
    urn:aff4:fda4d4fa-c378-4a06-acac-06ff54f49d5f/properties (image): (OK)
    urn:aff4:fda4d4fa-c378-4a06-acac-06ff54f49d5f (segment): (OK)
    urn:aff4:89f8ec58-13f0-4ad4-b1f2-74da7f3aed40/default/properties (segment): 0 MB
    ******** Object urn:aff4:89f8ec58-13f0-4ad4-b1f2-74da7f3aed40 ***********
        aff4:stored = file:///tmp/test.zip
        aff4:type = zip_volume
        aff4:interface = volume
        aff4:contains = urn:aff4:fda4d4fa-c378-4a06-acac-06ff54f49d5f/00000000
        aff4:contains = urn:aff4:fda4d4fa-c378-4a06-acac-06ff54f49d5f/00000000.idx
        aff4:contains = urn:aff4:fda4d4fa-c378-4a06-acac-06ff54f49d5f/00000001
        aff4:contains = urn:aff4:fda4d4fa-c378-4a06-acac-06ff54f49d5f/00000001.idx
        aff4:contains = urn:aff4:fda4d4fa-c378-4a06-acac-06ff54f49d5f/00000002
        aff4:contains = urn:aff4:fda4d4fa-c378-4a06-acac-06ff54f49d5f/00000002.idx
        aff4:contains = urn:aff4:fda4d4fa-c378-4a06-acac-06ff54f49d5f/00000003
        aff4:contains = urn:aff4:fda4d4fa-c378-4a06-acac-06ff54f49d5f/00000003.idx
        aff4:contains = urn:aff4:fda4d4fa-c378-4a06-acac-06ff54f49d5f/properties
        aff4:contains = urn:aff4:89f8ec58-13f0-4ad4-b1f2-74da7f3aed40/default/properties
        aff4:contains = urn:aff4:identity/41:38:13:1b:96:d3:f6:65:e0:87:60:07:f5:ff:31:19:24:93:e0:13/00000000
        aff4:contains = urn:aff4:identity/41:38:13:1b:96:d3:f6:65:e0:87:60:07:f5:ff:31:19:24:93:e0:13/00000000.sig
        aff4:contains = urn:aff4:identity/41:38:13:1b:96:d3:f6:65:e0:87:60:07:f5:ff:31:19:24:93:e0:13/cert.pem
        aff4:contains = urn:aff4:identity/41:38:13:1b:96:d3:f6:65:e0:87:60:07:f5:ff:31:19:24:93:e0:13/properties

    ******** Object file:///tmp/test.zip ***********
        aff4:contains = urn:aff4:89f8ec58-13f0-4ad4-b1f2-74da7f3aed40

    ******** Object urn:aff4:fda4d4fa-c378-4a06-acac-06ff54f49d5f/00000000 ***********
        aff4:stored = urn:aff4:89f8ec58-13f0-4ad4-b1f2-74da7f3aed40
        aff4:type = segment
        aff4:interface = stream
        aff4:timestamp = 0x49F2F9E2
        aff4:size = 0x34DB83C
        aff4:sha256 = RaOr4ksNZo+bXKMYDw2hwaAMqV9/4/TXqTE1P/7ERO8=
            ---> Signed by urn:aff4:identity/41:38:13:1b:96:d3:f6:65:e0:87:60:07:f5:ff:31:19:24:93:e0:13

    ....

There is no need to specify certificates now since the certificate is
given in the volume itself. The -V flag asks each object in the
statement to be verified. We see as each object's hash is matched, an
"(OK)" is printed.

Finally we see all the attributes of all the objects stored in the
volumes specified. If any of these fact are also verified in an identity
statement, we see a message indicating who signed this segment (The
identity name is the certificate fingerprint).

## Fuse support

Fuse is a library to create a filesystem in userspace. Its very easy to
use and very powerful since it allows userspace programs to create
abstracted filesystem like views into data. LibAFF4 has a fuse interface
to allow access to the streams within a set of volumes. This feature is
useful in order to allow other software to have access to the streams
without needing specific AFF4 support.

    $ affuse -d -- /tmp/test.zip /tmp/fuse
    zip.c:51 - FileBackedObject_Con: Can't open file:///tmp/test.zip/__URN__ (Not a directory)
    libaff4.c:27 - open_volume: Loaded zip volume file:///tmp/test.zip
    unique: 1, opcode: INIT (26), nodeid: 0, insize: 56
    ...

The trick here is that the aff4use program uses the `--` option to
separate options specific to fuse (before the --) to options specific to
libaff4 (after the --). The `-d` option requests fuse not fork into the
background, but instead remain at the terminal and provide debugging
messages. The `/tmp/fuse` directory is just somewhere to mount the fuse
filesystem over.

Note that aff4fuse provides access to all objects with a stream
interface. This will include all segments, but does not include
identities or volumes. All relative URNs (like links) are placed at the
root of the filesystem, and the full complicated URNs are placed in
__URN__/ subdirectory (just in case we need to access a stream
without a link).

    $ ls -l /tmp/fuse/
    total 0
    drwxr-xr-x 2 root root         1 2009-04-25 21:54 default
    -r--r--r-- 1 root root 254951424 1970-01-01 10:00 default.dd
    drwxr-xr-x 2 root root         1 2009-04-25 21:54 __URN__

    $ fls /tmp/fuse/default.dd
    d/d 11: lost+found
    r/r 10043:  System.map-2.6.22-14-generic
    r/r 6025:   vmlinuz-2.6.22-14-generic
    r/r 10041:  config-2.6.22-14-generic
    r/r 10042:  abi-2.6.22-14-generic
    ....

When you are finished and wish to unmount the filesystem:

    $ fusermount -u /tmp/fuse

## Creating map streams for filesystems

Map streams are a great idea since they allow different mutations of the
same data to be stored with zero cost. One application is to extract the
block allocation table of a filesystem using sleuthkit and create maps
for each file in the filesystem. This way applications dont know or care
how to parse filesystems, since the underlying forensic format can
present the data to them.

The map streams can be put into a new volume which simply refer to the
old volume:

    $ fsbuilder -o /tmp/test2.zip /tmp/test.zip default
    zip.c:51 - FileBackedObject_Con: Can't open file:///tmp/test.zip/__URN__ (Not a directory)
    libaff4.c:27 - open_volume: Loaded zip volume file:///tmp/test.zip
    zip.c:51 - FileBackedObject_Con: Can't open file://default/__URN__ (No such file or directory)
    zip.c:51 - FileBackedObject_Con: Can't open file://default (No such file or directory)
    zip.c:51 - FileBackedObject_Con: Can't open file://default/__URN__ (No such file or directory)
    zip.c:51 - FileBackedObject_Con: Can't open file://default (No such file or directory)
    libaff4.c:100 - aff4_open: Trying to open stream default relative to all volumes
    libaff4.c:107 - aff4_open: Trying urn:aff4:89f8ec58-13f0-4ad4-b1f2-74da7f3aed40/default
    libaff4.c:122 - aff4_open: Using urn:aff4:fda4d4fa-c378-4a06-acac-06ff54f49d5f as the stream name
    File name urn:aff4:fafe0c11-0544-4eab-ae8a-3ee568f53f7c/System.map-2.6.22-14-generic
    File name urn:aff4:fafe0c11-0544-4eab-ae8a-3ee568f53f7c/vmlinuz-2.6.22-14-generic
    File name urn:aff4:fafe0c11-0544-4eab-ae8a-3ee568f53f7c/config-2.6.22-14-generic
    File name urn:aff4:fafe0c11-0544-4eab-ae8a-3ee568f53f7c/abi-2.6.22-14-generic
    ....

As can be seen the fsbuilder tool creates new map streams for each new
file found in the stream. The map streams are pushed to a new volume.
Its possible now to fuse mount everything.

## Using HTTP for evidence management

In practice, most large practitioners will need to manage and archive
vast quantity of evidence. Its generally impossible to keep all the
evidence you will ever need on the drive of your analysis system, and
even if you get a vary large SAN its challanging to keep everything
handy.

By allowing evidence to be managed by HTTP its possible to distribute
the evidence around any number of HTTP servers, which can be deployed at
any location throughout the corporate WAN. This allows very cheap
storage to be used and the flexibility to move images around the network
at will.

Similarly, current technologies for remote imaging are complex and
proprietary. In a corporate LAN environment, for example, its beneficial
to push the image directly to an imaging server from the target machine
booted from a boot CD for example. Its nice to be able to do so with no
prior preparation.

Since AFF4 uses URNs to describes all objects in the AFF4 universe, and
a URL is just a special kind of URN, it is possible to describe
everything in terms of URLs too. For example, its possible to specify
certificates, keys, and other file names as a URL as well (which means
they can reside on a HTTP server). For example, its possible to encrypt
the private key and place it on a HTTP server to allow an investigator
to sign an acquisition from anywhere on the network without having to
manage their own keys and certificates.

Similarly its possible for investigators to create the image directly on
the HTTP server using webdav. This section will discuss how to do this
with an Apache2 server, but clearly since webdav is a standard its
possible to use any other webserver too.

Note: Windows XP webdav support is widely known to be very buggy. If it
works it may be possible to "open a web folder" to mount the remote
webdav folder.

### Apache configuration

Our goal with this configuration is to allow anyone read access to the
images with no authentication, but to require authentication for writing
on the webdav directory:

    <VirtualHost *:80>
    <Directory /var/www/webdav>
         DAV On
         AuthType Basic
         AuthName "test"
         AuthUserFile /etc/apache2/passwd.dav

         <Limit PUT POST DELETE PROPFIND PROPPATCH MKCOL COPY MOVE LOCK UNLOCK>
            Require valid-user
         </Limit>
    </Directory>
    </VirtualHost>

You can add usernames to the password file /etc/apache2/passwd.dav using
the htpasswd utility.

Now its possible to image directly there:

     aff2imager -i -o http://test:password@localhost/webdav/test.zip /dev/sda1