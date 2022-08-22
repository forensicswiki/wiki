Increasingly digital signatures and encryption are being used in digital
forensics. Rather than developing your own digital signature algorithms
or trying to shoe-horn PGP into a situation, you can use OpenSSL and
S/MIME.

In this section you will learn how to:

- Make a digital certificate authority
- Making certificates for S/MIME and OpenSSL.
- Sign an S/MIME message
- Verify a message.

### Background and terminology

key
OpenSSL uses the word *key* to refer to a private key.

private key
Half of the public/private key pair, the private key is used for
decrypting information that is encrypted with the public key, and for
signing signatures that are verified by decrypting the signature with
the public key. With x509v3 the private key is kept in the key file and
is encrypted by default (specify -nodes to avoid encryption, -des3 to
specify Triple-DES encryption of the private key). Public keys are
stored in the Certificate Signing Request and Certificate Files.

Certificate Signing Request (CSR)
A Certificate Signing Request contains a user's public key and a set of
Relative Distinguished Names (RDNs) which are essentially name=value
pairs.

Certificate
A certificate contains a set of RDNs and a public key and a certifying
signature. You can think of a certificate as a signed CSR.

The examples below use the openssl command. Although many examples
online use openssl's *ca* command, these examples use the *x509* command
instead as it has more options (such as the addtrust and addreject).

## Make the CA

First create a CA root key and make a self-signed certificate. Here we
make one with a 4096-bit key. Rather than specifying the password
through the CLI, we specify it with the command line. Note that the
-passout and -passin options allow the password to be in a file, on the
command line, specified on a file descriptor, or even provided by the
console. Please review the openssl documentation for additional
information.

`   $ openssl genrsa -aes256 -passout pass:rootpassword -out root-ca.key 4096`

Now use the key to sign itself. This example below will use the default
openssl.cnf configuration file. You might want to make a copy of this
file and make modifications. Note that the CA key is specified as being
good for a little less than 10 years. The -subj option specifies the
certificate's subject because using OpenSSL's CLI for entering this
information is error prone and tedious.

`   $ openssl req -new -x509 -days 3650 -key root-ca.key -out root-ca.crt  -subj '/C=US/ST=California/L=Monterey/CN=Naval Postgraduate School Experimental Certificate Authority' -passin pass:rootpassword`

The root CA is now in root-ca.crt

View the certificate with this command:

`   $ openssl x509 -text -in root-ca.crt`

If you want to see just the certificate fields and not reprint the
certificate, try:

`   $ openssl x509 -noout -text -in root-ca.crt`

Notice that you do not need to provide the keyfile or the password to
print the root certificate. That's because certificates contain no
confidential information; that's stored in the key.

## S/MIME Demonstration

### Create a User certificate

Users have the Real Name as the CN (Common Name) and an email address.

S/MIME has two ways of representing the email address. The original but
deprecated approach is to put it in the CN field, like this:

`  -subj '/C=DE/ST=state/L=city/CN=hostname/emailAddress=user@company.com'`

First the user creates the certificate signing request. Although the
'req' command and create the private key and the CSR at the same time,
in this case we create them separately so you can be aware that there
are two steps. We specify that the key is encrypted with AES256
encryption and with the password userpassword.

`   $ openssl genrsa -aes256 -passout pass:userpassword -out user.key 4096`

`   $ openssl req -new -key user.key -passin pass:userpassword -out user.csr -subj '/C=US/ST=California/L=Monterey/CN=Captain Peacock/emailAddress=peacock@nps.edu' -out user.req`

Now we will use the root CA that we created above to sign the CSR. We
will make a certificate that can be used for both client authentication
and email protection. The password specified is the ROOT password
because the Root's private key is used to sign the request.

`   $ openssl x509 -req -days 365 -in user.req -CA root-ca.crt -CAkey root-ca.key -set_serial 1 -out user.crt -setalias "Peacock email certificate" -addtrust emailProtection -addtrust clientAuth -addreject serverAuth -trustout -passin pass:rootpassword`

The certificate needs to be in PKCS12 format for use by most mail
clients. Here we need to use the user's password because we are using
the user's private key. We also specify a password for the PKCS12 file.
Here that password is *p12password*.

`   $ openssl pkcs12 -export -in user.crt -inkey user.key -out user.p12 -passin pass:userpassword -passout pass:p12password`

You can print what's in the PKCS12 file with this command:

`   $ openssl pkcs12 -info -noout -in user.p12 -passin pass:p12password`

### Signing an S/MIME signature with OpenSSL

Here we sign the message. Notice that we use -passin pass:aaaa to
specify the password.

First we need a message. Put this in the file message.txt:

`   To: everybody@nps.edu`
`   From: Captain Peacock <peacock@nps.edu>`
`   Subject: My first signed message`
`   `
`   Heads up, Sailors! This message is signed.`

Now let's sign the message and put the result in a file called
message-signed.txt

`   $ openssl smime -sign -in message.txt  -signer user.crt -inkey user.key -passin pass:aaaa -out message-signed.txt`

The command will read the to:, from: and subject: lines from the message
file. However, you can also specify them on the command line with the
-to, -from and -subject options. That's useful sometimes.

### Verifying an S/MIME signature with OpenSSL

You can now verify the signed message. Notice that verifying the message
prints that the verification is successful on stderr and puts the
message in the file message-to-view.txt:

`   $ openssl smime -verify -CAfile root-ca.crt  -in message-signed.txt -out message-to-view.txt`

If you want to have some fun, try making a modification to the signed
message file and see if it still verifies. You can modify the message
body or the certificate. However, if you modify the certificate, you'll
probably get an internal error when you try to verify.

### Printing the S/MIME certificate from an email message

You can strip off the certificate and print it. Here the certificate is
turned into a PKCS7 file and then printed:

`   $ openssl smime -pk7out -in message-signed.txt | openssl pkcs7 -text -noout -print_certs`

## Server-Side SSL Demonstration

Host certificates put the fully qualified domain name in the CN; the
email address field should be the address of the requester. Once again
we first create the request, then sign it. Notice that we use the
-addtrust and -addreject to specify that this certificate can ONLY be
used for server authentication.

`   $ openssl req -newkey rsa:1024 -keyout host.key -nodes -out host.csr`
`   `
`   $ openssl x509 -req -days 365 -in host.csr -CA ca.crt -CAkey ca.key -set_serial 2 -out host.crt -setalias "Host's certificate" -addtrust serverAuth -addreject clientAuth -addreject emailProtection`

## References

- <http://pages.cs.wisc.edu/~zmiller/ca-howto/>
- <http://serverfault.com/questions/103263/can-i-create-my-own-s-mime-certificate-for-email-encryption>
- <http://publib.boulder.ibm.com/infocenter/rsthelp/v8r0m0/index.jsp?topic=%2Fcom.ibm.rational.test.lt.doc%2Ftopics%2Ftcreatecertopenssl.html>
- <http://security.stackexchange.com/questions/17583/how-do-i-create-a-valid-email-certificate-for-outlook-s-mime-with-openssl>