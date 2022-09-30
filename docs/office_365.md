---
tags:
  - No Category
---
Office 365 is a package of software provided as service on cloud
platform. The cloud based service offers productivity through
subscription packages that enable on-premise services to be available on
cloud for different levels of organizational usage. The platform
altogether promotes a new method of purchasing the applications of
Office suite. The extensive usage of this software-service provider in
businesses and enterprises makes it a platform known best for the rich
exchange & storage of confidential information using Exchange online
service. The Exchange mailbox repository holds sensitive corporate
storage in Office 365, which turns out to be a critical element during
investigative procedures carried out on cloud for the discovery of
artifacts.

## Administrators and Exchange Online

The administration of Exchange online is executable via:

1.  A Web Console
2.  Remote Session for PowerShell

Web Console represents a collection of consoles where the top-level
console is of Office 365 featuring the basic settings for the offered
services. In addition, there is a respective product based consoles each
for; Exchange, Lync, and SharePoint.

### Investigative Standpoint

Before the 2013 release, Web Console acted as a second-class interface
whereas, PowerShell did most of the tasks. Soon, the platform underwent
evolution and resulted in became the primary interface for
Administrators of Office 365.

## In-Place eDiscovery & Hold - Office 365

In-Place eDiscovery is a powerful integrated facility with which, a user
having required permissions, can gain access of the entire messaging
records of an Exchange organization. The Discovery Management role group
is a crucial element. Therefore, it is important to ensure proper
control & monitoring on the discovery related activities.

**Measures to be taken to ensure a controlled Discovery Management
Group:**

1.  Limited & careful addition of members to the role group
2.  A check on the discovery activities performed on the role group
3.  The allotment of roles like the Mailbox Search management
4.  Access permission for discovery mailbox usage allotment

**Advantage:** The feature is offered in a user-friendly manner with
self-descriptive options that can easily be adopted by record managers,
legal & compliance officer, along with professionals from the human
resource department for eDiscovery purposes. Search feature comes with a
variety of criteria to be implemented for detailing the search for
particular messages from selected mailboxes.

**Limitation:** A maximum of only 2 In-Place eDiscovery searches can be
conducted at a time within an organization. Moreover, there also exists
a limit on the number of source mailboxes to be searched (applicable
mostly on large-scale enterprises).

## Office 365 Forensics - In-Place eDiscovery

The Exchange Admin Center provided on the web console for Exchange
features a user-friendly search option that can be implemented for
eDiscovery purposes.

#### Stages of eDiscovery

For users with authorized permission, it is feasible to execute an
In-Place eDiscovery lookup in the following stages:

- Selection of the preferred mailbox
- Specification of search criteria in the form of:
  - Keywords
  - Dates from start to end
  - Addresses of the recipient and sender
  - Message type, etc.
- Post search completion, users can choose one from the given actions to
  be performed on the search result:
  - **Estimate**: An estimate value of the total size along with number
    of items is returned for the performed search (based on the
    specified criteria).
  - **Preview**: Preview of the search results is provided, i.e.
    messages targeted from the selected mailbox(s) are offered for
    preview.
  - **Copy**: Enables the copying of messages to a discover mailbox
  - **Export**: Post copying of messages to discover mailbox, export to
    a PST file can be performed for their local storage.

## Audit Trails in Office 365

Audit trails are a facility using which, the track of target mailbox(s)
can be maintained. Performing a mailbox audit logging can help track the
actions executed by mailbox owners, delegates, and administrators on the
target mailbox. The three ways in which auditing can be carried out are:

- Mailbox access auditing
- Admin auditing
- Canned reports

**Advantage:** Audit Trails offers great benefit for tracking certain
number of mailboxes and keeping a check on the activities performed on
them whether by delegates, administrators or users.

**Limitation:** Auditing is not enabled by default and has to be
activated for use. The default settings in auditing are awful and
therefore, the criteria must be specified before starting up with the
investigation.

## Auditing Office 365 Mailboxes

Before performing the auditing of mailboxes, residing on Office 365 it
is important to know that:

1.  Audit log entries are only sustained for duration of 90 days within
    the mailbox by default. Change it.
2.  Administrator with Full Access permission to a mailbox is officially
    a delegate user.
3.  Exchange Admin Center cannot be used for audit logging instead
    remote PowerShell in connection with Exchange online is required.
4.  On enabling the option for audit logging of mailbox(s), a certain
    number of actions carried out by admin or mailbox delegates are
    automatically logged. Change it.

### Stages of Auditing

- Establish connection with Exchange Online remotely accessing
  PowerShell

\$UserCredential = Get-Credential \$Session = New-PSSession
–ConfigurtionName Microsoft.Exchange –ConnectionUri
<https://outlook.office365.com/powershell-liveid/> -Credential
\$UserCredential –Authentication Basic –AllowRedirection
Import-PSSession \$Session Get-Mailbox

- Enable the audit logging of mailbox

***Set-Mailbox –Identity “PiPi” –AuditEnabled \$true***

***Get-Mailbox –ResultSize Unlimited –Filter {RecipientTypeDetails -eq
“UserMailbox”} \| Set-Mailbox -AuditEnabled \$true***

- Mention the owner actions for auditing (Optional)

***Set-Mailbox “PiPi” –AuditOwner MailboxLogin,HardDelete***

***Set-Mailbox “Doll” –AuditEnabled \$true –AuditOwner HardDelete***

- Change retention duration for the entries in mailbox audit log
  (Optional)

***Set-Mailbox –Identity “PiPi” –AuditLogAgeLimit 180***

***Get-Mailbox –ResultSize Unlimited –Filter {RecipientTypeDetails –eq
“UserMailbox”} \| Set-Mailbox –AuditLogAgeLimit 60***

## External Links

- [Backup Office 365
  Mailbox](https://www.systoolsgroup.com/office365-backup/), by the
  [SysTools](systools.md)