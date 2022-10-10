---
tags:
  -  Tools
  -  Windows
  -  Memory Imaging
  -  Opensource Software
  -  Deprecated 
---
**mdd**, also known as **[ManTech dd](mantech.md)** or **Memory
dd**, is a command line program to acquire an image of the memory of a
running [Windows](windows.md) computer. The program has been
included in the [Helix](helix.md) incident response tool.

## Status

The current version of mdd (mdd_1.3.exe) runs on Window XP to SP3 and
Vista to SP 2, and may run on other versions.

The driver uses the [Physical Memory Object Memory Imaging
Mehod](memory_imaging.md) and returns a file handle to a
user-mode program via an IOCTL on the device file named:

    \\.\memdd

Once the file handle has been returned the driver and associated memdd
device is no longer required and can be removed, which is what the mdd
utility does.

## Building from source

1.  Load the x64 Free Build Environment from the WDK (in start menu)
2.  Go to the mdd directory, e.g. C:\src\mdd\driver\mdd\\ and run build
3.  You should now have mdd.sys in
    C:\src\mdd\driver\mdd\objfre_win7_amd64\amd64

### Signing the driver

- Make sure the WDK is installed, you need that for the signing.
- Get the right cross certificate file, see [Cross-Certificates for
  Kernel Mode Code
  Signing](http://msdn.microsoft.com/en-us/windows/hardware/gg487315)
- Convert the key you have to pfx, if its cert + key you want:
  - setup a secure spot to put the private key, this should not be on
    corp or unprotected at any time

<!-- -->

    openssl pkcs12 -export -out out.pfx -inkey in.key -in in.crt -certfile ca.crt

- - use a strong password
  - shred the .key immediately after use

- Sign the driver by running:

<!-- -->

    signTool sign /v /ac <crosscertificatefile> /f <pathtopfx> /p <pfx password> /t http://timestamp.verisign.com/scripts/timestamp.dll <driver.sys>

Also see: [Digital Signatures for Kernel Modules on
Windows](http://www.microsoft.com/whdc/winlogo/drvsign/kmsigning.mspx)

## Usage

To execute mdd, you must start cmd.exe. The options are:

- -o *filename* - required to actually run mdd
- -w - license information
- -v - verbose

To run mdd, the account you are using must have administrator access to
the machine you wish to image (however, it does not have to be the
Administrator account; it only needs to be in the local Administrator
group). The program works by installing a service, called mdd, although
see below for problems.

## Known Issues

These are the known problems with mdd.

### Error 1073

This is a Windows Service Manager error. mdd executes by registering
itself as a service, so it can run as administrator, although this does
not mean you can run mdd without having administrator access. At the end
of a normal execution, the service is deleted. However, mdd can
accidentally leave the service installed, and this prevents further
imaging. This could be caused by the system crashing (or an intentional
system crash) during imaging, or by attempting to stop the imaging with
control-c. If this happens, a knowledgeable Windows user will open up
the Services tab in Computer Manager, but unfortunately, Windows has a
wonderful feature that allows services, when they are registered, to
state whether or not they wish to be seen in the Service Manager. This
amazing concept allows services to run less visibly, and should be
considered a class-a security flaw. Fortunately, there's a way around
this, using the command line (cmd.exe).

- Run cmd.exe
- In cmd.exe, run "sc help" to see the service manager command line tool
- Run "sc query" to see all of the currently registered services, but
  note that this list will overflow the default line buffer of cmd.exe
  (this is adjustable, but not necessary for our purposes)
- Run "sc query mdd" and - ta-da - you'll see the mdd service
- Run "sc delete mdd" and it's gone, and mdd can now be run again.

### Error 1062

John Judd will be entering text here.

### Can't Use Network Share in Vista

In Vista, even if you are in the administrator group, you do not
necessarily run programs with administrator access (this is actually a
major improvement to the security model of Windows). You can start
programs, including cmd.exe, with admin privileges, but in this case,
that won't help. You will not be able to image to a Network Share from
Vista. There is no known workaround. This problem may exist in Windows
7.