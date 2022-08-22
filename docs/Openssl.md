OpenSSL is an open source software system that provides the following:

- Forensic-grade implementations of the most widely used hash functions.
- Symmetric cryptographic functions
- Asymmetric cryptographic function
- Certificate management functions
- A complete S/MIME implementation
- A complete SSL/TLS implementation

OpenSSL is interesting for forensic practitioners and developers because
it provides a basic toolkit for building software, and because the
higher-level certificate management functions give you an easy way to
decode the contents of certificates that are used to secure computer
systems.

This web page contains step-by-step instructions on using OpenSSL from
the command line to perform specific tasks. There are a lot of online
OpenSSL guides and we'll try to link to some of them from here. But this
page is a handy reference just the same.

# File Extensions

OpenSSL doesn't care what you use for file extensions. However, the
following extensions to seem to be commonly used:

| File Extension | Meaning                                                                                                                                                            |
|----------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| .pem           | can contain a private key, public key, or certificate signing request.                                                                                             |
| .crt           | Windows file extension for a .pem file.                                                                                                                            |
| .p12           | a PKCS12 file, which contains a private key and a certificate, encrypted for transport with a passphrase. This is the format that Windows and MacOS like to import |

# Conversion

- convert pem to pkcs12:

` % openssl pkcs12 -export -in mpage.crt -inkey mpage.key -out mpage.p12 -name 'MPage Signing Key'`

- convert pkcs12 to pem, putting both private key and certificate in the
  same file

` % openssl pkcs12 -in mpage.p12 -out mpage.pem`

- The same, but with no encryption of file

` % openssl pkcs12 -in mpage.p12 -out mpage.pem -nodes`

- Decrypt a PEM file private key:

` % openssl rsa -in newreq.pem -out key.pem`

- Print the contents of a certificate

` % openssl x509 -in mpage.pem -text`

- Input the PKCS12 file and output a key file and a cert file:

`openssl pkcs12 -in slg.p12 -out slg.key -nocerts -nodes`
`openssl pkcs12 -in slg.p12 -out slg.pem -nokeys -nodes`

# Making Certificates

To make certificates all in one step:

` openssl req -new -x509 -nodes -out imapd.pem -keyout imapd.pem -days 3650`

Make a certificate request for a CA to sign:

` openssl req -newkey rsa:1024 -keyout mycert.key -out mycert.csr -nodes`

To make an RSA key and then use the key to make the certificate signing
request:

` openssl genrsa -out myfile.key 1024`
` openssl req -new -key myfile.key -out myfile.csr`

# Get a certificate from an SSL server

` openssl s_client -connect www.nitroba.com:443`

# Viewing Certificates

` openssl x509 -in ssl.crt-text`

# S/MIME

- to sign an outgoing mail:

``    from_email = `openssl x509 -email -in certfile.pem -noout` ``
``    x509_subject = `openssl x509 -subject -in certfile.pem -noout` ``
`   openssl smime -from %s  -to %s  -subject %s -sign -inkey file -signer %s -in tempfile.txt extra`

# See Also

- <http://www.macdevcenter.com/pub/a/mac/2002/08/23/jaguar_server.html?page=4>