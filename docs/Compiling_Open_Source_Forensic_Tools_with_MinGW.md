Many open source computer forensic tools can be cross-compiled with
MinGW. This allows you to create Windows executable directly from a
Macintosh computer or Linux machine without using the Microsoft VC++
environment.

## Installing MinGW

On a Mac using MacPorts:

<!-- -->

    $ sudo port selfupdate
    $ sudo port install i386-mingw32-binutils i386-mingw32-gcc  \
                        i386-mingw32-libunicows i386-mingw32-runtime \
                        i386-mingw32-w32api

*note: If you get the error message 'warnings treated as errors' you
will need to find the Makefile where -Werror is defined and erase it*