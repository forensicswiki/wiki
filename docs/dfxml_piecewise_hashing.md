---
tags:
  - Digital Forensics XML
---
[Digital Forensics XML](digital_forensics_xml_schema.md) can be used to
represent the results of piecewise hashing of individual files. The
[md5deep](md5deep.md) suite now generates piecewise hashing results in DFXML
when the `-d` option is provided.

Here is an example:

    <?xml version='1.0' encoding='UTF-8'?>
    <md5deep>
    <fileobject>
    <filename>sample/bar.txt</filename>
    <filesize>46</filesize>
    <mtime format='time_t'>1296497502.0</mtime>
    <byte_runs><byte_run file_offset='0' len='46'><hashdigest type='MD5'>0e886f6b08986269af98aedde53df23f</hashdigest><hashdigest type='SHA256'>21c35b5698f1e54d11ca8a41321d40d75797425013dfa1b640ab34d7efa7f1ac</hashdigest></byte_run>
    </byte_runs>
    <hashdigest type='MD5'>0e886f6b08986269af98aedde53df23f</hashdigest>
    <hashdigest type='SHA256'>21c35b5698f1e54d11ca8a41321d40d75797425013dfa1b640ab34d7efa7f1ac</hashdigest>
    </fileobject>
    <fileobject>
    <filename>sample/foo.txt</filename>
    <filesize>193</filesize>
    <mtime format='time_t'>1296497462.0</mtime>
    <byte_runs><byte_run file_offset='0' len='193'><hashdigest type='MD5'>06f63e03ed5e1770a2ff753a76d04906</hashdigest><hashdigest type='SHA256'>82a217a76ebe5e6c0f768576a3e8fd9ba6de504c42360c23e08ddfa22e711ba0</hashdigest></byte_run>
    </byte_runs>
    <hashdigest type='MD5'>06f63e03ed5e1770a2ff753a76d04906</hashdigest>
    <hashdigest type='SHA256'>82a217a76ebe5e6c0f768576a3e8fd9ba6de504c42360c23e08ddfa22e711ba0</hashdigest>
    </fileobject>
    <fileobject>
    <filename>sample/somedir/baz.txt</filename>
    <filesize>19</filesize>
    <mtime format='time_t'>1296497486.0</mtime>
    <byte_runs><byte_run file_offset='0' len='19'><hashdigest type='MD5'>362aa248563e453588755f280387a3d4</hashdigest><hashdigest type='SHA256'>7a7c62947561b0b00c213d37d04edbe0c8de46282098b7216a23b25fa336f150</hashdigest></byte_run>
    </byte_runs>
    <hashdigest type='MD5'>362aa248563e453588755f280387a3d4</hashdigest>
    <hashdigest type='SHA256'>7a7c62947561b0b00c213d37d04edbe0c8de46282098b7216a23b25fa336f150</hashdigest>
    </fileobject>
    </md5deep>
