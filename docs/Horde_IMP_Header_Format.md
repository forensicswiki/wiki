Horde Internet Messaging Program (IMP)

    Message-ID: <1186073825.46b20ce1ad3cd@sendinghost.com>
    Date: Thu,  2 Aug 2007 20:57:05 +0400
    From: username@sendinghost.com
    To: username@receivinghost.com
    Subject: Header test
    MIME-Version: 1.0
    Content-Type: text/plain; charset=ISO-8859-5
    Content-Transfer-Encoding: 8bit
    User-Agent: Internet Messaging Program (IMP) 3.2.2
    X-Originating-IP: 255.255.255.255

Message-ID format:

    horde/lib/Horde/MIME.php
    ...
        function generateMessageID()
        {
            return '<' . date('YmdHis') . '.' .
                substr(base_convert(microtime() . mt_rand(), 10, 36), -16) .
                '@' . $_SERVER['SERVER_NAME'] . '>';
        }