The Windows Boot Configuration Data (BCD) is stored in the BCD Windows
NT Registry file on the active (boot) partitions in '\Boot' or
'\EFI\Microsoft\Boot'.

On a running Windows system the contents of this Registry file can be
accessed via keys and values under 'HKEY_LOCAL_MACHINE\BCD00000000'.

'bcdedit.exe' can be used to modify the Windows Boot Configuration
Settings on a running Windows system.

The mappings of Registrys key to associated bcdedit commands are as
follows:

'HKEY_LOCAL_MACHINE\BCD00000000\Objects\\\*\Elements\\%MAPPING%', where
'%MAPPING%' consists of

- 16000009: 'bcdedit.exe /set {default} recoveryenabled \<yes\|no\>',
  where '00' gets stored for 'no', '01' gets stored for 'yes'
- 250000e0: 'bcdedit.exe /set {default} bootstatuspolicy
  ignoreallfailures', where '01 00 00 00 00 00 00 00' gets stored.
  Otherwise, the key is not present

The wildcard component of the Windows Registry key is the identifier
associated with the Windows Boot Loader instance on a given machine.
This identifier can be determined by running 'bcdedit.exe /v' and
looking at the 'identifier' under the Windows Boot Loader section.

## Misuse

Malware, like Cerber (ransomware), is known to change the Windows Boot
Configuration Settings and disable recovery options like the ability to
boot into safe mode.

## External Links

- [Modifications to Microsoft Boot Components:
  Update](http://download.microsoft.com/download/9/c/5/9c5b2167-8017-4bae-9fde-d599bac8184a/Boot_Modifications.doc),
  by [Microsoft](Microsoft "wikilink")
- [BCD System Store Settings for
  UEFI](https://docs.microsoft.com/en-us/windows-hardware/manufacture/desktop/bcd-system-store-settings-for-uefi?view=windows-11),
  by [Microsoft](Microsoft "wikilink"), October 8, 2021

### Malware analysis

- [Sodinokibi ransomware exploits WebLogic Server
  vulnerability](https://blog.talosintelligence.com/2019/04/sodinokibi-ransomware-exploits-weblogic.html),
  by Talos Intelligence, April 30, 2019