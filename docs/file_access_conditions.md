---
tags:
  - No Category
---
## File Access Conditions

In GSM every file has File Access Condition placed on it. File Access
Conditions are restrictions placed upon the file. There are 15 codes
that pertain to File Access Conditions.

<table border = '1'>
<tr>
<th>

Level

</th>
<th>

Condition

</th>
<th>

Description

</th>
</tr>
<tr>
<td>

0

</td>
<td>

Always

</td>
<td>

No Restrictions For Access

</td>
</tr>
<tr>
<td>

1

</td>
<td>

CHV1 (Card Holder Verification 1)

</td>
<td>

Access shall only be granted is one of the following condition is
fulfilled: The correct CHV1 has been presented to the sim card, CHV1 is
enabled/disabled indicator is set to disabled, or the UNBLOCK CHV1 has
been successfully performed during the current session.

</td>
</tr>
<tr>
<td>

2

</td>
<td>

CHV2

</td>
<td>

Access shall only be granted is one of the following condition is
fulfilled: The correct CHV2 has been presented to the sim card or the
UNBLOCK CHV2 has been successfully performed during the current session.

</td>
</tr>
<tr>
<td>

3

</td>
<td>

Reserved

</td>
<td>
</td>
</tr>
<tr>
<td>

4 - 14

</td>
<td>

ADM

</td>
<td>

Responsibility of the Administrative Authority (Conditions set by the
Carrier or other Governing Bodies).

</td>
</tr>
<tr>
<td>

15

</td>
<td>

Never

</td>
<td>

Access can only be granted internally within the phone and can not be
performed over a SIM/ME interface.

</td>
</tr>
</table>


Warning: After 3 failed attempts at entering a CHV1 or CHV2 all access
privileges granted to those numbers are lost immediately

## References

GSM 11.11 Version 5.0.0 December 1995 ISBN 2-7437-0447-0