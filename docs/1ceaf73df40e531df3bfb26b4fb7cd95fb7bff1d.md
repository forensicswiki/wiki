1ceaf73df40e531df3bfb26b4fb7cd95fb7bff1d is the SHA-1 for a block of
4096 NULL bytes:

    $ dd if=/dev/zero of=4k bs=4096 count=1
    1+0 records in
    1+0 records out
    4096 bytes transferred in 0.000059 secs (69273666 bytes/sec)
    $ sha1 4k
    filename  size                    SHA1
    ========================================================
    4k  4096  1ceaf73df40e531df3bfb26b4fb7cd95fb7bff1d