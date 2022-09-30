---
tags:
  - No Category
---
Registryasxml is a GUI tool by Stephane Rodriguez that exports and
imports Microsoft Registry files with a simple key/value syntax that
looks like this:

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

## See Also

- [Windows Registry](windows_registry.md)

## External Links

- <http://www.codeproject.com/KB/system/registryasxml.aspx>