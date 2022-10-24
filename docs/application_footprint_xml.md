---
tags:
  -  Articles that need to be expanded
---
The Application Footprint XML provides a means for distributing
information about an application's distribution format, it's
installation footprint, and the residual information left on a hard
drive after it has been installed.

    <?xml version='1.0' encoding='ISO-8859-1'?>
    <application_footprint>
    <metadata ns='http://forensicswiki.org/app_print/'
              xmlns:xsi='http://www.w3.org/2001/XMLSchema-instance'
              xmlns:dc='http://purl.org/dc/elements/1.1/'>
    <dc:creator>Your Organization Here</dc:creator>
    <dc:title>iTunes 9.0.2</dc:title>
    <dc:description>Application Print of Apple MacOS iTunes 9.0.2</dc:description>
    <dc:date>2009-11-23</dc:date>
    <dc:type>Application Print</dc:type>
    </metdata>

    <distribution>
      <!-- In this section goes information consistent with the distribution files -->
    </distribution>

    <install>
      <!-- In this section goes information consistent with the installed files -->

      <fileobject>     <!-- this is a standard fiwalk fileobject -->
      </fileobject>

    </install>

    <residual>
      <!-- In this section goes information consistent with information left after an uninstall -->
    </residual>

    <documentfiles>
      <!-- Descriptions of the document files that the application makes -->
    </documentfiles>

    <network>
      <!-- Information that is sent over the network that is characteristic for the application -->
    </network>

    <memory>
      <!-- Characteristic information in memory -->
    </memory>

    </application_footprint>

For each of the blocks above, we would like to indicate:

- Files (hashes & fuzzy hashes)
- Registry entries
- Magic Numbers (perhaps there is an 8-byte code left in memory or in an
  executable that's descriptive)
- Tool artifacts