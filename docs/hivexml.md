---
tags:
  - No Category
---
Hivexml is a command-line program that is part of libguestfs that
extracts registry entries from a Hive file into an XML file.

Below is an pretty-printed example of what the XML looks like; note that
the <value> tags have not been pretty-printed to avoid changing the
semantics of the file.

    <?xml version="1.0" ?>
    <hive>
      <node name="CMI-CreateHive{6A1C4018-979D-4291-A7DC-7AED1C75B67C}">
        <node name="AppEvents">
          <node name="EventLabels">
            <node name=".Default">
              <value default="1" type="string">Default Beep</value>
              <value key="DispFileName" type="string">@mmres.dll,-5824</value>
            </node>
            <node name="ActivatingDocument">
              <value default="1" type="string">Complete Navigation</value>
              <value key="DispFileName" type="string">@ieframe.dll,-10321</value>
            </node>
            <node name="AppGPFault">
              <value default="1" type="string">Program Error</value>
              <value key="DispFileName" type="string">@mmres.dll,-5825</value>
            </node>

## See also

- <https://rwmj.wordpress.com/2009/10/29/hivexget-get-values-from-a-windows-registry-hive/>
  for information on how to extract individual entries.