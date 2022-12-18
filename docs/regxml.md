---
tags:
  - Digital Forensics XML
---
RegXML is an XML syntax analogous to [Digital Forensics XML](digital_forensics_xml_schema.md).
It represents the contents of a Windows Registry hive file, presenting key and
value cells of the hive as file and directories of a file system.

## Disambiguation

Please note that RegXML is \*also\* the name of a Windows command-line
utility that exports sections of the Windows Registry as XML-formatted
files. That program was released on Softpedia. It is a completely
separate effort from RegXML otherwise mentioned in this article.

## Sample XML

This RegXML is a sample of the System hive from the [M57-Patents
scenario](http://digitalcorpora.org/corpora/scenarios/m57-patents-scenario),
image Charlie 2009-11-16. Its structure is of the first version of
RegXML, a deep-hierarchy structure created by extending the
[Hivexml](http://libguestfs.org/hivexml.1.html) utility.

    <?xml version="1.0" encoding="UTF-8"?>
    <hive>
      <mtime>2009-11-17T00:33:57Z</mtime>
      <node name="$$$PROTO.HIV" root="1">
        <mtime>2009-11-13T04:47:33Z</mtime>
        <byte_runs>
          <byte_run file_offset="4128" len="92"/>
        </byte_runs>
        <node name="ControlSet002">
          <mtime>2009-11-09T01:26:39Z</mtime>
          <byte_runs>
            <byte_run file_offset="1480856" len="93"/>
          </byte_runs>
          <node name="Control">
            <mtime>2009-11-13T04:48:01Z</mtime>
            <byte_runs>
              <byte_run file_offset="1481240" len="87"/>
            </byte_runs>
            <value type="string" key="WaitToKillServiceTimeout" value="20000">
              <byte_runs>
                <byte_run file_offset="1481328" len="48"/>
                <byte_run file_offset="13448" len="16"/>
              </byte_runs>
            </value>
            <value type="string" key="SystemStartOptions" value="NOEXECUTE=OPTIN  FASTDETECT">
              <byte_runs>
                <byte_run file_offset="1481464" len="42"/>
                <byte_run file_offset="3006752" len="60"/>
              </byte_runs>
            </value>
            <value type="string" key="SystemBootDevice" value="multi(0)disk(0)rdisk(0)partition(1)">
              <byte_runs>
                <byte_run file_offset="3006856" len="40"/>
                <byte_run file_offset="3206056" len="76"/>
              </byte_runs>
            </value>
            <node name="Windows">
              <mtime>2009-11-13T03:08:00Z</mtime>
              <byte_runs>
                <byte_run file_offset="2355232" len="87"/>
              </byte_runs>
              <value type="expand" key="SystemDirectory" value="%SystemRoot%\system32">
                <byte_runs>
                  <byte_run file_offset="2355368" len="39"/>
                  <byte_run file_offset="3111128" len="48"/>
                </byte_runs>
              </value>
              <value type="binary" encoding="base64" key="ShutdownTime" value="RDGhgQ5kygE=">
                <byte_runs>
                  <byte_run file_offset="3203784" len="36"/>
                  <byte_run file_offset="1481592" len="12"/>
                </byte_runs>
              </value>
            </node>
            <node name="WOW">
              <mtime>2009-11-09T01:22:59Z</mtime>
              <byte_runs>
                <byte_run file_offset="2359096" len="83"/>
              </byte_runs>
              <value type="expand" key="cmdline" value="%SystemRoot%\system32\ntvdm.exe">
                <byte_runs>
                  <byte_run file_offset="2358720" len="31"/>
                  <byte_run file_offset="2359184" len="68"/>
                </byte_runs>
              </value>
              <value type="string" key="KnownDLLs" value="comm.drv commdlg.dll ctl3dv2.dll ddeml.dll
     keyboard.drv lanman.drv mmsystem.dll mouse.drv netapi.dll olecli.dll olesvr.dll pmspl.dll shell.dll
     sound.drv system.drv toolhelp.dll vga.drv wfwnet.drv win87em.dll winoldap.mod winsock.dll
     winspool.exe wowdeb.exe timer.drv rasapi16.dll compobj.dll storage.dll ole2.dll ole2disp.dll
     ole2nls.dll typelib.dll msvideo.dll avifile.dll msacm.dll mciavi.drv mciseq.drv mciwave.drv
     progman.exe avicap.dll mapi.dll">
                <byte_runs>
                  <byte_run file_offset="2359256" len="33"/>
                  <byte_run file_offset="2361648" len="904"/>
                </byte_runs>
              </value>
            </node>
          </node>
        </node>
      </node>
    </hive>

## See Also

- A. Nelson, “RegXML: XML conversion of the Windows Registry for
  forensic processing and distribution,” in Advances in Digital
  Forensics VIII, ser. IFIP Advances in Information and Communication
  Technology, K.-P. Chow and S. Shenoi, Eds. Springer, 2012.
- [RegXML Extractor](https://github.com/ajnelson/regxml_extractor) (on
  github)
