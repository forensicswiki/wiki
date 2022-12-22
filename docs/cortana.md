---
tags:
  - No Category
---
Cortana is a digital personal assistant originally introduced in Windows
Phone 8.1.

With the release of [Windows 10](windows_10.md) Cortana become
integrated with the desktop operating system (OS). Cortana can be used
for a number of tasks within the OS; setting a reminder, searching the
local files and the web, answering simple queries.

## Artefacts

There are a number of artefacts associated with Cortana; 2 backend
Extensible Storage Engine (ESE) databases, and other configuration
files. The 2 Cortana Databases are located:

•
*\Users\user_name\AppData\Local\Packages\Microsoft.Windows.Cortana_xxxx\AppData\Indexed
DB\IndexedDB.edb* •
*\Users\user_name\AppData\Local\Packages\Microsoft.Windows.Cortana_xxxx\LocalState\ESEDatabase_CortanaCoreInstance\CortanaCoreDb.dat*

The IndexedDB.edb contains the following tables:

\- DatabaseAndObjectStoreCatalog - HeaderTable - IndexCatalog -
MSysDefrag - MSysLocales - MSysObjects - MSysObjectsShadow -
MSysObjids - T-*n* - T-*n*

The other database, CortanaCoreDb.dat, contains table data that relates
to a users’ interaction with Cortana; it contains the following tables:

\- Attachments - Contact - ContactPermissions - ContactTriggers -
Diagnostic - Geofences - LocationTriggers - Metadata - MSysLocales -
MSysObjects - MSysObjectsShadow - MSysObjids - Notification -
Reminders - RulesDescriptions - RulesInstances -
RulesInstancesDisplayParameters - RulesInstancesParameters -
RulesTemplates - RulesTemplatesParameters -
RulesTemplatesParameterTypes - Signals - TimeTriggers - Triggers

Unlike IndexedDB.edb, CortanaCoreDB.dat is a goldmine for evidentiary
artefacts, some of the more interesting tables are:

• *Geofences*

This table contains Latitude/Longitude for where location based
reminders are triggered.

• *LocationTriggers*

This table contains Latitude/Longitude as well as the actual Name of
place results for reminders.

• *Reminders*

This table contains actual text inputed by the user, as well as
Creation, Access, and Completion times.

• *Triggers*

This table contains the ReminderID value matches with the ID field in
the Reminders table.

What is interesting, especially for a forensic investigator, is that
Cortana will keep track of when Reminders are completed, including where
and when a reminder was finalised. This is particularly invasive, but
can provide a wealth of information useful for pinning someone to a time
and place.

--Bsmuir
11:56, 23 August 2015 (UTC)

## External Links

* Microsoft (2015), [What is Cortana](http://windows.microsoft.com/en-us/windows-10/getstarted-what-is-cortana)
* Muir, B. (2015), [Windows 10 - Cortana & Notification Center Forensics](http://bsmuir.kinja.com/windows-10-cortana-notification-center-forenics-1724511442)
