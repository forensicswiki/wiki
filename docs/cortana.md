---
tags:
  - Articles that need to be expanded
  - Windows
---
Cortana is a digital personal assistant originally introduced in Windows
Phone 8.1.

With the release of [Windows 10](windows_10.md) Cortana become
integrated with the desktop operating system (OS). Cortana can be used
for a number of tasks within the OS; setting a reminder, searching the
local files and the web, answering simple queries.

## Artifacts

There are a number of artifacts associated with Cortana; 2 backend
[Extensible Storage Engine (ESE) databases](extensible_storage_engine_(ese)_database_file_(edb)_format.md),
and other configuration files. The 2 Cortana Databases are located:

```text
\Users\user_name\AppData\Local\Packages\Microsoft.Windows.Cortana_xxxx\AppData\Indexed DB\IndexedDB.edb
\Users\user_name\AppData\Local\Packages\Microsoft.Windows.Cortana_xxxx\LocalState\ESEDatabase_CortanaCoreInstance\CortanaCoreDb.dat
```

The IndexedDB.edb contains the following tables:

* DatabaseAndObjectStoreCatalog
* HeaderTable
* IndexCatalog
* MSysDefrag
* MSysLocales
* MSysObjects
* MSysObjectsShadow
* MSysObjids
* T-*n*
* T-*n*

The other database, CortanaCoreDb.dat, contains table data that relates
to a users’ interaction with Cortana; it contains the following tables:

* Attachments
* Contact
* ContactPermissions
* ContactTriggers
* Diagnostic
* Geofences
* LocationTriggers
* Metadata
* MSysLocales
* MSysObjects
* MSysObjectsShadow
* MSysObjids
* Notification
* Reminders
* RulesDescriptions
* RulesInstances
* RulesInstancesDisplayParameters
* RulesInstancesParameters
* RulesTemplates
* RulesTemplatesParameters
* RulesTemplatesParameterTypes
* Signals
* TimeTriggers
* Triggers

Unlike IndexedDB.edb, CortanaCoreDB.dat is a goldmine for evidentiary
artifacts, some of the more interesting tables are:

* Geofences, which contains Latitude/Longitude for where location based
  reminders are triggered.
* LocationTriggers, which contains Latitude/Longitude as well as the actual
  name of place results for reminders.
* Reminders, which contains actual text inputted by the user, as well as
  Creation, Access, and Completion times.
* Triggers, which contains the ReminderID value matches with the ID field
  in the Reminders table.

What is interesting, especially for a forensic investigator, is that
Cortana will keep track of when Reminders are completed, including where
and when a reminder was finalised. This is particularly invasive, but
can provide a wealth of information useful for pinning someone to a time
and place.
