---
tags:
  - Anti-Forensics
  - Network Forensics
---
**Proxy server** is a server which services the requests of its clients
by forwarding requests to other servers.

## Overview

Proxy servers are widely used by organizations and individuals for
different purposes:

- Internet sharing (like NAT);
- Traffic compression;
- Accelerating service requests by retrieving content from cache;
- In China, proxy servers are commonly used by individuals to get around
  national connectivity policies. (User A can't reach website Z, but A
  can reach proxy server P which can reach website Z);
- Criminals frequently use proxy servers to hide the origin of their
  connections. (User A connects to website Z through proxy server P; the
  packets appear to come from P, and not A).

Tor presents a SOCKS proxy interface to applications,
so any application that supports SOCKS (versions 4, 4a and 5) can be
anonymized using Tor.

### HTTP proxies

*These proxy servers are using HTTP.*

Example request (direct; with relative URI):

    GET / HTTP/1.1
    Host: cryptome.org
    User-Agent: Mozilla/5.0 (X11; U; Linux i686; en; rv:1.9.0.3) Gecko/20080528 Epiphany/2.22 Firefox/3.0
    Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8
    Accept-Encoding: gzip,deflate
    Accept-Charset: ISO-8859-1,utf-8;q=0.7,*;q=0.7
    Keep-Alive: 300
    Connection: keep-alive
    If-Modified-Since: Tue, 14 Oct 2008 13:59:19 GMT
    If-None-Match: "e01922-62e9-45937059ec2de"
    Cache-Control: max-age=0

Example request (using proxy; with absolute URI):

    GET http://cryptome.org/ HTTP/1.1
    Host: cryptome.org
    User-Agent: Mozilla/5.0 (X11; U; Linux i686; en; rv:1.9.0.3) Gecko/20080528 Epiphany/2.22 Firefox/3.0
    Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8
    Accept-Encoding: gzip,deflate
    Accept-Charset: ISO-8859-1,utf-8;q=0.7,*;q=0.7
    Keep-Alive: 300
    Proxy-Connection: keep-alive
    If-Modified-Since: Tue, 14 Oct 2008 13:59:19 GMT
    If-None-Match: "e01922-62e9-45937059ec2de"
    Cache-Control: max-age=0

*Note:* this HTTP request was intercepted on the way to proxy server.

According to RFC 2068 (section 5.1.2):

    The absoluteURI form is required when the request is being made to a proxy.

*Note:* proxy server will convert absolute URI to relative URI.

### HTTPS proxies

*The same as above, but using HTTPS (HTTP over SSL/TLS).*

Sometimes HTTP proxies that support CONNECT method are called *"HTTPS
proxies"*. These HTTP proxies can tunnel almost every TCP-based
protocol.

Example request:

    CONNECT home.netscape.com:443 HTTP/1.0
    User-agent: Mozilla/1.1N

### SOCKS proxies

SOCKS is an Internet protocol that allows client-server applications to
transparently use the services of a network firewall.

### Web proxies (CGI proxies)

These are web sites that allow a user to access a site through them.
They generally use PHP or CGI to implement the proxy functionality.

Example GET request from [Anonymouse](http://anonymouse.ws/) (to a web
server):

    GET / HTTP/1.0
    Host: [scrubbed server host]:8080
    User-Agent: http://Anonymouse.org/ (Unix)
    Connection: keep-alive

Example GET request from [HideMyAss.com](http://www.hidemyass.com/):

    GET / HTTP/1.0
    Host: [scrubbed server host]:8080
    User-Agent: Mozilla/5.0 (X11; U; Linux i686; en; rv:1.9.0.3) Gecko/20080528 Epiphany/2.22 Firefox/3.0
    Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8

## Proxy detection

### Server-side

#### New HTTP headers

Some proxy servers add new HTTP headers to request, for example:

    GET / HTTP/1.1
    Host: [scrubbed server host]:8080
    Connection: keep-alive
    Accept: image/gif, image/x-xbitmap, image/jpeg, image/pjpeg, application/x-ms-application, application/vnd.ms-xpsdocument, application/xaml+xml, application/x-ms-xbap, */*
    Accept-Language: ru
    UA-CPU: x86
    Accept-Encoding: gzip, deflate
    User-Agent: Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.0; SLCC1; .NET CLR 2.0.50727; .NET CLR 3.0.04506)
    X-Forwarded-For: [scrubbed client's real IP address]
    Via: 1.1 proxy11 (NetCache NetApp/5.6.1D24)

*Note:* this HTTP request was received from a proxy server using
[netcat](netcat.md).

New HTTP headers are *X-Forwarded-For* and *Via*.

#### Mixed HTTP headers

Some proxy servers mix HTTP headers in the original request (see example
above). [Internet Explorer](internet_explorer.md) 7 puts *Host*
and *Connection* headers at the end of request, not at the beginning.

#### Modified HTTP header values

Some proxy servers modify HTTP headers replacing the original values
(see.md). [Internet Explorer](internet_explorer.md) 7
sends header *Connection: Keep-Alive*, not *Connection: keep-alive*.

#### [OS fingerprinting](os_fingerprinting.md) and User-Agent

The following *User-Agent* header was received by a web server (see
example above):

    User-Agent: Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.0; SLCC1; .NET CLR 2.0.50727; .NET CLR 3.0.04506)

The request was generated by using [Internet
Explorer](internet_explorer.md) 7 (*MSIE 7.0*) on
[Windows](windows.md) Vista or [Windows](windows.md)
Server 2008 (*Windows NT 6.0*). However, this connection was initiated
with TCP SYN packet with following options:

    MSS
    NOP
    NOP
    SACK permitted
    NOP
    Window scale
    NOP
    NOP
    Timestamps

While [Windows](windows.md) Vista commonly uses these options:

    MSS
    NOP
    Window scale
    NOP
    NOP
    SACK permitted

This means that:

- User-Agent header was forged;
- The request was sent using a proxy server with different operating system.

#### Other methods

- Active detection: see [Metasploit Decloaking
  Engine](http://decloak.net/);
- Comparing source IP address with a list of known proxy servers.

### On the way to proxy server

#### Absolute URI

HTTP clients (such as web browsers) will only generate them in requests
to proxies.

#### Other methods

- Comparing destination IP address with a list of known proxy servers.

## See Also

- Tor
- [VPN](vpn.md)
