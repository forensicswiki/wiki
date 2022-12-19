---
tags:
  - Digital Forensics XML
---
The '''

    ''' tag is used to introduce the source of forensic data. Currently we are using these for disk images, as the example below illustrates:

    <pre>
    <source type='Disk Image'>
      <imagefile>/corp/images/nus/1040.aff</imagefile>
      <sectorsize>512</sectorsize>
      <device_model>SEAGATE ST32550W SUN2.1G 0418</device_model>
      <device_sn>01806486</device_sn>
      <acquisition_commandline>aimage scsi1 /project2/b28.aff</acquisition_commandline>
      <acquisition_device>/dev/sda1</acquisition_device>
      <device_capabilities>pass2: >SEAGATE ST32550W SUN2.1G 0418< Fixed Direct Access SCSI-2 device
    pass2: Serial Number 01806486
    pass2: 20.000MB/s transfers (10.000MHz, offset 15, 16bit), Tagged Queueing Enabled
      </device_capabilities>
      <sectorsize coding='base10'>512</sectorsize>
      <devicesectors coding='base10'>4194995</devicesectors>
      <acquisition_macaddr>00:0f:b5:42:6a:fe</acquisition_macaddr>
      <acquisition_date>2006-07-25T10:56:42</acquisition_date>

</pre>

After the **source** tag you may find some **fileobject** tags. They may
be grouped within a **volume** tag:

      <volume offset='32256'>
        <byte_runs>
          <byte_run offset='0' img_offset='114688' len='32768'>
          <byte_run offset='0' img_offset='1523712' len='32768'>
          <byte_run offset='0' img_offset='6356992' len='39659'>
        </byte_runs>
        <ftype>1</ftype>
        <ftype_str>ntfs</ftype_str>
        <block_size>4096</block_size>
        <block_count>4980142</block_count>
        <first_block>0</first_block>
        <last_block>4980141</last_block>
        <fileobject>
        ...
        </fileobject>
      </volume>

## Encoding

Encoding is assumed to be base10, except for hash codes, which are assumed to
be base16.
