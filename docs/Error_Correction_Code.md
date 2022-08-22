**Error Correction Code (ECC Errors)**


All modern hard disk drives are ATA (Advanced Technology Attachment)
compliant. Part of this compliancy means that drives must have the
ability to detect errors while reading data from individual sectors on
the drive. This is to prevent corrupted data from being propagated
through to the operating system which would lead to system crashes.

<!-- -->


In order to accomplish this, every sector has a built in checksum and
error correction code that is written at the time that data is written
to the sector. Upon reading the sector, the drive recalculates the
checksum and compares it to the one previously written. If it does not
match, the error correction code will attempt to correct the data. Every
sector has a standard 512 bytes of user data. A typical ECC is capable
of correcting between 10 and 12 bytes. If repairing the corruption is
beyond the capability of the ECC, the data will not be returned to the
operating system. The drive will then return an error. This is typically
a UNC (uncorrectable) error.

<!-- -->


These types of errors occur when data is written to the sector
improperly or inadvertently. Additionally, these errors can be due to
read instability in the drive where the data itself is not actually
corrupted but the drive is incapable of reading it correctly. This can
be due to factors such as minute mechanical wear of the parts inside the
head disk assembly.