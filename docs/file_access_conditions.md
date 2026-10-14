---
tags:
  - Articles that need to be expanded
---
## File Access Conditions

In GSM every file has File Access Condition placed on it. File Access
Conditions are restrictions placed upon the file. There are 15 codes
that pertain to File Access Conditions.

| Level | Condition | Description |
| --- | --- | --- |
| 0 | Always | No Restrictions For Access |
| 1 | CHV1 (Card Holder Verification 1) | Access shall only be granted is one of the following condition is fulfilled: The correct CHV1 has been presented to the sim card, CHV1 is enabled/disabled indicator is set to disabled, or the UNBLOCK CHV1 has been successfully performed during the current session. |
| 2 | CHV2 | Access shall only be granted is one of the following condition is fulfilled: The correct CHV2 has been presented to the sim card or the UNBLOCK CHV2 has been successfully performed during the current session. |
| 3 | Reserved | |
| 4 - 14 | ADM | Responsibility of the Administrative Authority (Conditions set by the Carrier or other Governing Bodies). |
| 15 | Never | Access can only be granted internally within the phone and can not be performed over a SIM/ME interface. |

Warning: After 3 failed attempts at entering a CHV1 or CHV2 all access
privileges granted to those numbers are lost immediately

## References

GSM 11.11 Version 5.0.0 December 1995 ISBN 2-7437-0447-0
