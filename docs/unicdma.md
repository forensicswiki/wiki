---
tags:
  -  Cell Phone Tools
---
## Features

[Media:Example.ogg](media:example.ogg.md)===Modes===

- Hyndai HWT /HWP-110/120/220
- Hyndai HGC-310e, HGC-600e
- LG
- Qualcomm[Media:Example.ogg](media:example.ogg.md)
- Samsung SPH-A460
- Samsung (general)
- Samsung SCH-X127/X250/X350/…
- Sky IM-1200/1400/2000/etc.
- Withus

### Read

- Hardware date
- Software date
- Software version
- CAI rev
- SCM
- ESN
- Analog MIN
- Digital MIN
- Security Code
- Lock Code
- EEPROM
  - Size
    - custom or 16384, 32768, 65536
  - Memory
    - Starting Address
    - Length (bytes)
      - custom or 524288, 786432, 1310720, 1703936

### Write

- ESN
- SCM
- A-KEY

### Scan

- Memory
  - Range
  - Step (bytes)
    - custom or 256, 512, 1024, 2048, 4096, 8192, 16384, 32768, 65536,
      131072, 262144, 524288, 1048576

### Settings

- COM Port
  - 1 to 4
- Baud rate
  - 19200, 38400, 57600, 115200

## Forensics

UniCDMA can be used in cell phone forensics to access or modify the
phone's ESN, security code, lock code, firmware, or filesystem.

## Troubleshooting

### LG

If UniCDMA cannot be used to place an LG cell phone in DM Mode, the
following procedures may be followed:

- Close UniCDMA
- Connect LG cell phone to computer using USB data cable
- Open Hyperterminal
- Connect to LG cellphone on correct COM port at 115200 bits per second
- Place LG cellphone into DM mode by typing "AT\$QCDMG"
- Close Hyperterminal

