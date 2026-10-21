---
tags:
  - Analysis
  - Discontinued
  - Registry Analysis
  - Tools
  - Windows
---
Registryasxml was a Windows graphical utility created by Stephane Rodriguez
that allowed users to export and import sections of the Windows Registry
into a structured XML format. Registryasxml is no longer maintained.

## Caution

Names in Windows Registry files can contain code points not supported by strict XML.

## Example

Example of XML output.

```xml
<?xml version="1.0" encoding="UTF-8"?>
 <registry>
  <k name="HKEY_LOCAL_MACHINE">
   <k name="SYSTEM">
    <k name="Setup">
     <v name="CmdLine" value="setup -newsetup"/>
     <v name="OsLoaderPath" value="\"/>
     <v name="SetupType" value="0x00000000 (0)" type="REG_DWORD"/>
     <v name="SystemPartition" value="\Device\HarddiskVolume1"/>
     <v name="SystemPrefix" value="cf 03 00 00 00 a0 3d e0" type="REG_BINARY"/>
     <v name="SystemSetupInProgress" value="0x00000000 (0)" type="REG_DWORD"/>
     <k name="AllowStart">
      <k name="AFD"/>
      <k name="EventLog"/>
      <k name="PlugPlay"/>
      <k name="ProtectedStorage"/>
      <k name="Rpcss"/>
      <k name="SamSs"/>
      <k name="Seclogon"/>
      <k name="WS2IFSL"/>
     </k>
    </k>
   </k>
  </k>
 </registry>
```

## See Also

* [Unpaired Surrogates](unpaired_surrogates.md)
* [Windows Registry](windows_registry.md)
