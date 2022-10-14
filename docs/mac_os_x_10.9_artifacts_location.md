---
tags:
  -  MacOS
  -  Operating Systems
---
The content of this page is automatically generated from the "Mac OS X
artifacts location" of the [mac4n6
project](https://github.com/pstirparo/mac4n6). Please refer to that for
any mistake/correction or if you wish to contribute.

## SYSTEM ARTIFACTS

### Autorun Locations

------------------------------------------------------------------------

Launch Agents files

<!-- -->

    /Library/LaunchAgents/*
    /System/Library/LaunchAgents/*

Launch Daemons files

<!-- -->

    /Library/LaunchDaemons/*
    /System/Library/LaunchDaemons/*

Startup Items file

<!-- -->

    /Library/StartupItems/*
    /System/Library/StartupItems/*

### System Logs

------------------------------------------------------------------------

System Log files main folder

<!-- -->

    /var/log/*

Apple System Log

Filename format as YYYY.MM.DD.\[UID\].\[GID\].asl, while
YYYY.MM.DD.\[UID\].\[GID\].asl of logs per user

    /var/log/asl/*

Audit Log

<!-- -->

    /var/audit/*

Installation log

It contains install date of system, as well as date of system and
software updates

    /var/log/install.log

### System Preferences

------------------------------------------------------------------------

System Preferences files

<!-- -->

    /Library/Preferences/*

Global Preferences

It contains Global Preferences information such as the local time zone,
geographical coordinates, etc.

    /Library/Preferences/.GlobalPreferences.plist

Software Update

Plist describing last attempt and last successful attempt at updating OS
X software

    /Library/Preferences/com.apple.SoftwareUpdate.plist

Login Window Info

Plist containing last user logged in

    /Library/Preferences/com.apple.loginwindow.plist

Bluetooth Preferences and paierd device info

Bluetooth preferences and paired devices

    /Library/Preferences/com.apple.Bluetooth.plist

Time Machine Info

Time Machine backup info

    /Library/Preferences/com.apple.TimeMachine.plist

### System Settings and Informations

------------------------------------------------------------------------

OS Installation time

Empty file. Its last modification time represent the date/time the OS
was installed

    /var/db/.AppleSetupDone

OS name and version

Plist describing the installed Operating System

    /System/Library/CoreServices/SystemVersion.plist

Users Log In Password Hash Plist

Contains the salted SHA-512 hash value for the user's log in password

    /var/db/dslocal/nodes/Default/users/*

### Sleep/Hibernate and Swap Image File

------------------------------------------------------------------------

Sleep Image File

Contents of RAM are written to this file when the computer is put to
sleep

    /var/vm/sleepimage

Swap Files

Numerous swap files may be found in this directory with the naming
convention of swapfile# (swapfile0, swapfile1, swapfile2, etc.)

    /var/vm/swapfile#

### Kernel Extension

------------------------------------------------------------------------

Kernel Extension

Kext files are essentially drivers for Mac OS X.

    /System/Library/Extensions/*
    /Library/Extensions/*

### Software Installation

------------------------------------------------------------------------

Software Installation History

It contains a history of installed applications and updates

    /Library/Receipts/InstallHistory.plist

Software Update

Plist describing last attempt and last successful attempt at updating OS
X software

    /Library/Preferences/com.apple.SoftwareUpdate.plist

Applications

<!-- -->

    /Applications/*

### System Info Misc.

------------------------------------------------------------------------

Current Time Zone

Simlink pointing to /usr/share/zoneinfo/XYZ

    /etc/localtime

Mac OS X at jobs

<!-- -->

    /usr/lib/cron/jobs/*

Cron tabs

<!-- -->

    /etc/crontab
    /usr/lib/cron/tabs/*

Periodic system functions scripts and configuration

<!-- -->

    /etc/defaults/periodic.conf
    /etc/periodic.conf
    /etc/periodic.conf.local
    /etc/periodic/**2
    /usr/local/etc/periodic/**2
    /etc/daily.local/*
    /etc/weekly.local/*
    /etc/monthly.local/*

### Networking

------------------------------------------------------------------------

Hosts file

<!-- -->

    /etc/hosts

Remembered Wireless Networks

Remembered wireless networks

    /Library/Preferences/SystemConfiguration/com.apple.airport.preferences.plist

## USER ARTIFACTS

### Autorun Locations

------------------------------------------------------------------------

Login Items

Plists listing applications that automatically start when the user is
logged in

    %%users.homedir%%/Library/Preferences/com.apple.loginitems.plist

### Users

------------------------------------------------------------------------

Users directories in /Users

<!-- -->

    /Users/*

### User Directories

------------------------------------------------------------------------

Downloads Directory

<!-- -->

    %%users.homedir%%/Downloads/*

Documents Directory

<!-- -->

    %%users.homedir%%/Documents/*

Music Directory

<!-- -->

    %%users.homedir%%/Music/*

Desktop Directory

<!-- -->

    %%users.homedir%%/Desktop/*

Library Directory

<!-- -->

    %%users.homedir%%/Library/*

Movies Directory

<!-- -->

    %%users.homedir%%/Movies/*

Pictures Directory

<!-- -->

    %%users.homedir%%/Pictures/*

Public Directory

<!-- -->

    %%users.homedir%%/Public/*

Applications

<!-- -->

    /Applications/*

### Preferences

------------------------------------------------------------------------

User preferences directory

Directory containing user preference settings for applications and
utilities

    %%users.homedir%%/Library/Preferences/*

iCloud user preferences

<!-- -->

    %%users.homedir%%/Library/Preferences/MobileMeAccounts.plist

Sidebar Lists Preferences

Lists the names of volumes mounted on the desktop that have appeared in
the sidebar list

    %%users.homedir%%/Preferences/com.apple.sidebarlists.plist

Global Preferences

Global Preferences Plist

    %%users.homedir%%/Library/Preferences/.GlobalPreferences.plist

Dock database

It containing directories, files, and apps that have appeared in the
Dock

    %%users.homedir%%/Library/Preferences/com.apple.Dock.plist

Attached iDevices

Attached iDevices

    %%users.homedir%%/Library/Preferences/com.apple.iPod.plist

Quarantine Event Database

SQLite database that keeps track of files that have the quarantine
extended attribute that is given to applications, scripts, and
executables downloaded from potentially untrustworthy locations/people.
The SQLite database contains URLS, email addresses, email subjects, and
other potentially useful information.

    %%users.homedir%%/Library/Preferences/com.apple.LaunchServices.QuarantineEvents
    %%users.homedir%%/Library/Preferences/com.apple.LaunchServices.QuarantineEventsV2

### Logs

------------------------------------------------------------------------

User and Applications Logs Directory

Directory containing numerous application's log files user specific

    %%users.homedir%%/Library/Logs/*

Misc. Logs

Miscellaneous logs and diagnostic reports

    /Library/Logs/*

Terminal Commands History

Terminal commands history

    %%users.homedir%%/.bash_history

### User's Accounts

------------------------------------------------------------------------

User's Social Accounts

<!-- -->

    %%users.homedir%%/Library/Accounts/Accounts3.sqlite

### iDevice Backup

------------------------------------------------------------------------

iOS device backups directory

<!-- -->

    %%users.homedir%%/Library/Application Support/MobileSync/Backup/*

iOS device backup information

It's a plist file in plain text. It stores data about the backed up
device (such as device name, GUID, ICCID, IMEI, Product type, iOS
version, serial numbers, UDID etc.) and the iTunes software used to
create the backup (iTunes version number, iTunes settings).

    %%users.homedir%%/Library/Application Support/MobileSync/Backup/*/info.plist

iOS device backup apps information

It's a plist file in plain text and it describes the content of the
backup. Inside this file we can find the list of applications installed
on the backed up device. For every application there are the name and
the particular version. Inside the file there is also the date the
backup was made, the backup type (encrypted vs. unencrypted) and some
information about the iDevice and the iTunes software used.

    %%users.homedir%%/Library/Application Support/MobileSync/Backup/*/Manifest.plist

iOS device backup files information

It's a binary file that stores the descriptioons of all the other files
in the backup directory. It contains a record for each element in the
backup.

    %%users.homedir%%/Library/Application Support/MobileSync/Backup/*/Manifest.mdbd

iOS device backup status information

It's a plist file in binary format and it stores information about the
completion of the backup

    %%users.homedir%%/Library/Application Support/MobileSync/Backup/*/Status.plist

### Recent Items

------------------------------------------------------------------------

Recent Items

Recently opened applications, files, and servers

    %%users.homedir%%/Library/Preferences/com.apple.recentitems.plist

Recent Items application specific

Recently opened files specific for each application

    %%users.homedir%%/Library/Preferences/*LSSharedFileList.plist

### Misc.

------------------------------------------------------------------------

Application Support Directory

Contains application-specific folders used to support applications and
utilities

    %%users.homedir%%/Library/Application Support/*

Keychain Directory

Directory containing user keychain files

    %%users.homedir%%/Library/Keychains/*

User Trash Folder

User Trash directory

    %%users.homedir%%/.Trash/

## APPLICATIONS ARTIFACTS

### iCloud

------------------------------------------------------------------------

iCloud Accounts

<!-- -->

    %%users.homedir%%/Library/Application Support/iCloud/Accounts/

### Skype

------------------------------------------------------------------------

Skype Directory

Directory containing Skype user artifacts

    %%users.homedir%%/Library/Application Support/Skype/*

Skype User profile

Directory containing Skype user artifacts

    %%users.homedir%%/Library/Application Support/Skype/*/*

Skype Preferences and Recent Searches

Skype preferences and recent user searches

    %%users.homedir%%/Library/Preferences/com.skype.skype.plist

Main Skype database

Database of contacts, SMS's, calls, conversations, videos, messages,
etc.

    %%users.homedir%%/Library/Application Support/Skype/*/Main.db

Chat Sync Directory

Directory containing chat logs

    %%users.homedir%%/Library/Application Support/Skype/*/chatsync/*

### Safari

------------------------------------------------------------------------

Safari Main Folder

<!-- -->

    %%users.homedir%%/Library/Safari/*

Safari Bookmarks

Plist listing default and user-added Safari bookmarks

    %%users.homedir%%/Library/Safari/Bookmarks.plist

Safari Downloads

Plist listing files downloaded using Safari Browser

    %%users.homedir%%/Library/Safari/Downloads.plist

Safari Installed Extensions

Plist describing installed Safari Extensions

    %%users.homedir%%/Library/Safari/Extensions/Extensions.plist
    %%users.homedir%%/Library/Safari/Extensions/*

Safari History

Plist listing Safari web browsing history

    %%users.homedir%%/Library/Safari/History.plist

Safari History Index

An index of Safari History allowing a user to perform keyword searches
of visited webpages

    %%users.homedir%%/Library/Safari/HistoryIndex.sk

Safari Last Session

A plist describing the state of Safari when it was last closed

    %%users.homedir%%/Library/Safari/LastSession.plist

Safari Local Storage Directory

A directory for webpage-specific storage. Each webpage stores data in a
SQLite database with the file extension of .localstorage.

    %%users.homedir%%/Library/Safari/LocalStorage/*

Safari Local Storage Database

A database listing the webpage specific databases

    %%users.homedir%%/Library/Safari/LocalStorage/StorageTracker.db

Safari Top Sites

A Plist listing the webpages belonging to a Safari's Top Sites

    %%users.homedir%%/Library/Safari/TopSites.plist

Safari Webpage Icons Database

A database containing saved web page icons for webpages visited

    %%users.homedir%%/Library/Safari/WebpageIcons.db

Safari Webpage Databases

A directory for webpage-specific database storage

    %%users.homedir%%/Library/Safari/Databases/*

Safari Cache Directory

A directory containing Safari-specific cache items

    %%users.homedir%%/Library/Caches/com.apple.Safari/*

Safari Cache

A cache of data from visited webpages

    %%users.homedir%%/Library/Caches/com.apple.Safari/Cache.db

Safari Extensions Cache

A directory containing cached items for Safari Extensions

    %%users.homedir%%/Library/Caches/com.apple.Safari/Extensions/*

Safari Webpage Previews

A directory containing images of viewed webpages in .png and .jpg
formats. The file name is a hash of the webpage URL.

    %%users.homedir%%/Library/Caches/com.apple.Safari/Webpage Previews/*

Safari Cookies

Cookies from visited webpages

    %%users.homedir%%/Library/Cookies/Cookies.binarycookies

Safari Preferences and Search terms

Contains recent safari search strings and downloads folder location in
addition to preferences

    %%users.homedir%%/Library/Preferences/com.apple.Safari.plist

Safari Extension Preferences

Contains preferences of Safari installed extensions

    %%users.homedir%%/Library/Preferences/com.apple.Safari.Extensions.plist

Safari Bookmark Cache

Each bookmark entry in Bookmarks.plist is stored as an individual file
in this directory for more efficient use with Spotlight and to allow the
user to select the bookmark entry from Spotlight and have Safari launch
the corresponding webpage

    %%users.homedir%%/Library/Caches/Metadata/Safari/Bookmarks/*

Safari History Cache

Each website entry in History.plist is stored as an individual file in
this directory for more efficient use with Spotlight and to allow the
user to select the webpage entry from Spotlight and have Safari launch
the corresponding webpage

    %%users.homedir%%/Library/Caches/Metadata/Safari/History/*

Safari Temporary Images

It contains the images present/viewed in the web pages visited by the
user

    %%users.homedir%%/Library/Caches/com.apple.Safari/fsCachedData/*

### Firefox

------------------------------------------------------------------------

Firefox Directory

Directory containing user artifacts for Mozilla Firefox web browser

    %%users.homedir%%/Library/Application Support/Firefox/*

Firefox Profiles

<!-- -->

    %%users.homedir%%/Library/Application Support/Firefox/Profiles/*

Firefox Cookies

<!-- -->

    %%users.homedir%%/Library/Application Support/Firefox/Profiles/*/Cookies.sqlite

Firefox Downloads

Download history. Removed in Firefox 26.0.

    %%users.homedir%%/Library/Application Support/Firefox/Profiles/*/Downloads.sqlite

Firefox Form History

Text entered into forms including search terms, email addresses, and
login information.

    %%users.homedir%%/Library/Application Support/Firefox/Profiles/*/Formhistory.sqlite

Firefox History

<!-- -->

    %%users.homedir%%/Library/Application Support/Firefox/Profiles/*/Places.sqlite

Firefox Signon

Encrypted saved passwords (and URL exceptions where "NEVER SAVE
PASSWORD" is selected), requires key3.db to work.

    %%users.homedir%%/Library/Application Support/Firefox/Profiles/*/signons.sqlite

Firefox Key

It contains a key used to encrypt and decrypt saved passwords.

    %%users.homedir%%/Library/Application Support/Firefox/Profiles/*/key3.db

Firefox Permissions

Permission database for cookies, pop-up blocking, image loading and
add-ons installation.

    %%users.homedir%%/Library/Application Support/Firefox/Profiles/*/permissions.sqlite

Firefox Add-ons

Stores AMO data for installed add-ons such as screenshots, ratings,
homepage, and other details.

    %%users.homedir%%/Library/Application Support/Firefox/Profiles/*/addons.sqlite
    %%users.homedir%%/Library/Application Support/Firefox/Profiles/*/addons.json

Firefox Extension

Installed extension information

    %%users.homedir%%/Library/Application Support/Firefox/Profiles/*/extensions.sqlite
    %%users.homedir%%/Library/Application Support/Firefox/Profiles/*/extensions.json

Firefox Pages Settings

Individual settings for pages.

    %%users.homedir%%/Library/Application Support/Firefox/Profiles/*/content-prefs.sqlite

### Google Chrome

------------------------------------------------------------------------

Chrome Main Folder

Directory containing user artifacts for Google Chrome web browser

    %%users.homedir%%/Library/Application Support/Google/Chrome/*

Chrome Default profile

Directory containing user artifacts for Google Chrome web browser

    %%users.homedir%%/Library/Application Support/Google/Chrome/default/*

Chrome History

It contains the URL visited, a list of searched keywords/terms, a list
of downloaded items

    %%users.homedir%%/Library/Application Support/Google/Chrome/*/History
    %%users.homedir%%/Library/Application Support/Google/Chrome/*/Archived History

Chrome Bookmarks

<!-- -->

    %%users.homedir%%/Library/Application Support/Google/Chrome/*/Bookmarks

Chrome Cookies

<!-- -->

    %%users.homedir%%/Library/Application Support/Google/Chrome/*/Cookies

Chrome Local Storage

Local Storage is a common name for part of HTML5 Web Storage. It is the
newest version of cookies, and it serves the same purpose as “normal”
cookies: enabling websites to store persistent data locally.

    %%users.homedir%%/Library/Application Support/Google/Chrome/*/Local Storage/*.localstorage

Chrome Login Data

<!-- -->

    %%users.homedir%%/Library/Application Support/Google/Chrome/*/Login Data

Chrome Top Sites

Rank of the most visited websites

    %%users.homedir%%/Library/Application Support/Google/Chrome/*/Top Sites

Chrome Web Data

The Web Data database records text a user enters into web forms to let
Chrome to automatically fill in similar future forms.

    %%users.homedir%%/Library/Application Support/Google/Chrome/*/Web Data

Chrome Extensions

It contains the databases of Chrome extensions, filled with the related
usage data

    %%users.homedir%%/Library/Application Support/Google/Chrome/*/databases/*
    %%users.homedir%%/Library/Application Support/Google/Chrome/*/databases/Databases.db

Chrome Cache

Google Chrome cache

    %%users.homedir%%/Library/Caches/com.google.Chrome/Cache.db

Chrome Preferences Files

<!-- -->

    %%users.homedir%%/Library/Preferences/com.google.Chrome.plist

### Mail

------------------------------------------------------------------------

Mail Main Folder

Apple Mail main directory

    %%users.homedir%%/Library/Mail/V2/*

Mail Mailbox Directory

Apple Mail Mailboxes

    %%users.homedir%%/Library/Mail/V2/Mailboxes/*

Mail IMAP Synched Mailboxes

Synched IMAP Account(s)

    %%users.homedir%%/Library/Mail/V2/IMAP-<name@address>/*

Mail POP Synched Mailboxes

Synched POP Account(s)

    %%users.homedir%%/Library/Mail/V2/POP-<name@address>/*

Mail BackupTOC

Backup Plist that defines the mailbox structure

    %%users.homedir%%/Library/Mail/V2/MailData/BackupTOC.plist

Mail Envelope Index

SQLite db. Keeps track of the location of Mail messages - the content of
some messages is present as well

    %%users.homedir%%/Library/Mail/V2/MailData/Envelope Index

Mail Opened Attachments

Plist listing opened Mail attachments (although often empty. more to do
here)

    %%users.homedir%%/Library/Mail/V2/MailData/OpenedAttachmentsV2.plist

Mail Signatures by Account

Plist containing Mail signatures

    %%users.homedir%%/Library/Mail/V2/MailData/Signatures/*

Mail Downloads Directory

Directory containing files downloaded from email messages

    %%users.homedir%%/Library/Containers/com.apple.mail/Data/Library/Mail Downloads/*

Mail Preferences

Mail preferences

    %%users.homedir%%/Library/Preferences/com.apple.Mail.plist

Mail Recent Contacts

SQLite database stored in Address Book's support directory containing
recent Mail contacts

    %%users.homedir%%/Library/Application Support/AddressBook/MailRecents-v4.abcdmr

Mail Accounts

Accounts configured in Mail.app

    %%users.homedir%%/Library/Mail/V2/MailData/Accounts.plist

## External Links

- [How to use a single download to remotely steal proprietary files from
  MacOS](https://lab.wallarm.com/hunting-the-files-34caa0c1496/), August
  1, 2017
- [Apple forensic: advanced look onto Apple
  security](https://hackmag.com/security/apple-forensic/), by hackmag
- [mac4n6: Collection of forensics artifacts location for Mac OS X and
  iOS](https://github.com/pstirparo/mac4n6)
- [Known Networks settings moved in Big
  Sur](https://www.alansiu.net/2021/01/27/known-networks-settings-moved-in-big-sur/),
  by Alan Siu, January 27, 2021