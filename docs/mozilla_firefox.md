---
tags:
  -  Applications
  -  Web Browsers
---
Mozilla Firefox is a Free and Open Source [web
browser](web_browser.md) developed by the Mozilla Foundation.

It can have many [add-ons](https://addons.mozilla.org/en-US/firefox/) which give it
extra capabilities.

## Anonymous Browsing

Mozilla Firefox can be used in anonymous browsing (see [The Onion
Router](the_onion_router.md). However, it is known that Firefox
reveals computer's uptime in TLS (SSL) "Client Hello" packets allowing
investigator correlate anonymous and non-anonymous traffic
[1](https://archives.seul.org/or/talk/Apr-2008/msg00050.html).

This bug affects Firefox 2 (all versions) and Firefox 3 Beta3.

## History

Firefox 3 stores the history of visited sites in a file named
**places.sqlite**. This file uses the [SQLite database
format](sqlite_database_format.md).

**places.sqlite** can be found in the following locations:

On Linux

    /home/$USER/.mozilla/firefox/$PROFILE.default/places.sqlite

On MacOS-X

    /Users/$USER/Library/Application Support/Firefox/Profiles/$PROFILE.default/places.sqlite

On Windows XP

    C:\Documents and Settings\%USERNAME%\Application Data\Mozilla\Firefox\Profiles\%PROFILE%.default\places.sqlite

On Windows Vista, 7

    C:\Users\%USERNAME%\AppData\Roaming\Mozilla\Firefox\Profiles\%PROFILE%.default\places.sqlite

### Timestamps

The places.sqlite uses the following timestamps.

The **moz_historyvisits.visit_date** is in (the number of) microseconds
since January 1, 1970 UTC

Some Python code to do the conversion into human readable format:

    date_string = datetime.datetime( 1970, 1, 1 )
                + datetime.timedelta( microseconds=timestamp )

### Example queries

Some example queries:

To get an overview of the visited sites:

    SELECT datetime(moz_historyvisits.visit_date/1000000, 'unixepoch', 'localtime'), moz_places.url FROM moz_places, moz_historyvisits WHERE moz_places.id = moz_historyvisits.place_id;

## Downloads

Firefox 3 stores the history of downloads sites in a file named
**downloads.sqlite**. This file uses the [SQLite database
format](sqlite_database_format.md).

**downloads.sqlite** can be found in the same location as
**places.sqlite**.

**Note it looks that Firefox 21 (or earlier?) stores the downloads as
part of the bookmarks in moz_bookmarks and moz_annos in places.sqlite**

### Timestamps

The places.sqlite uses the following timestamps.

The **moz_downloads.startTime** and **moz_downloads.endTime** are in
(the number of) microseconds since January 1, 1970 UTC.

### Example queries

Some example queries:

To get an overview of the downloaded files:

    SELECT moz_downloads.startTime, moz_downloads.source, moz_downloads.currBytes, moz_downloads.maxBytes FROM moz_downloads;

## Disk Cache

The Mozilla Firefox disk cache uses the [Firefox Disk Cache
Format](firefox_disk_cache_format.md) and can be found in:

### Version 1

On Linux

    /home/$USER/.mozilla/firefox/$PROFILE.default/Cache/

On MacOS-X

    /Users/$USER/Library/Caches/Firefox/Profiles/$PROFILE.default/Cache/

On Windows XP

    C:\Documents and Settings\%USERNAME%\Local Settings\Application Data\Mozilla\Firefox\Profiles\%PROFILE%.default\Cache\

On Windows Vista, 7

    C:\Users\%USERNAME%\AppData\Local\Mozilla\Firefox\Profiles\%PROFILE%.default\Cache\

### Version 2 - Firefox 32 and later

On Linux

    /home/$USER/.mozilla/firefox/$PROFILE.default/cache2/

On MacOS-X

    /Users/$USER/Library/Caches/Firefox/Profiles/$PROFILE.default/cache2/

On Windows XP

    C:\Documents and Settings\%USERNAME%\Local Settings\Application Data\Mozilla\Firefox\Profiles\%PROFILE%.default\cache2\

On Windows Vista, 7

    C:\Users\%USERNAME%\AppData\Local\Mozilla\Firefox\Profiles\%PROFILE%.default\cache2\

## Settings

URL:

    about:config

## See Also

- [Firefox Disk Cache Format](firefox_disk_cache_format.md)
- [Mozilla Firefox History File
  Format](mozilla_firefox_history_file_format.md)
- [SQLite database format](sqlite_database_format.md)

## External Links

- [Official website](http://www.mozilla.com/firefox/)
- [Profile folder -
  Firefox](http://kb.mozillazine.org/Profile_folder_-_Firefox)
- [Firefox 3 –
  downloads.sqlite](https://wiki.mozilla.org/images/3/3d/Downloads.sqlite.schema.pdf)
- [Mozilla Firefox
  Releases](http://download.cdn.mozilla.net/pub/firefox/releases/)
