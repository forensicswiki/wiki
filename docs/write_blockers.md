---
tags:
  - Disk Imaging
  - Hardware
---
In the field of digital forensics, the integrity of [evidence](digital_evidence.md) is essential.
The foundational rule of data acquisition is simple: the examiner must never alter the original
storage medium. To enforce this, forensic investigators rely on write blockers-technological
safeguards designed to guarantee the preservation of original data. In its original sense, write
blockers act as a strict gatekeeper between a host forensic workstation and a target storage
device. They permit seamless read-only access to the source data while intercepting and discarding
all write commands, modifications, or metadata updates attempted by the host operating system.

Architecturally, write blockers are designed using one of two functional philosophies.

* A blocker can either allow all commands to pass from the computer to the drive except for those
explicitly compiled on a prohibited list,
* or it can specifically isolate and block known write commands while letting all other traffic
through.

Furthermore, some devices include integrated drive protection mechanisms. If a failing drive
experiences frequent read errors, a write blocker can force the storage interface to drop from
high-speed data transfer modes (such as UDMA) to slower, more stable modes (such as Programmed
Input/Output (PIO)). This minimizes mechanical strain on the drive head and prevents accidental
media destruction during data retrieval.

## Hardware versus software write blockers

Forensic examiners distinguish between two main categories of these tools: hardware and software
write blockers.

Hardware write-blockers are physical bridge devices containing embedded microcontrollers. They
inspect command packets directly at the bus controller layer-for instance, blocking low-level ATA
Write Commands like 0x30 or 0x35. Because they function at the hardware level, they are operating
system independent. Hardware blockers are categorized as "Native" when they utilize the same
interface for input and output (such as an IDE-to-IDE block) or "Tailgate" when they bridge two
different interfaces (such as a Firewire-to-SATA block).

In contrast, software write-blockers rely on operating system-level modifications, such as
modifying Windows Registry keys (e.g., `StorageDevicePolicies\WriteProtect`) or applying specific
OS mount options (e.g., `mount -r`).  Software mechanisms are inherently OS-dependent and operate
higher in the protocol stack.  Organizations like the Scientific Working Group on Digital Evidence
(SWGDE) warn that software solutions do not guarantee absolute device-level protection, as
background journaling mechanisms, unmounted file systems, or low-level kernel drivers may still
execute write operations.

Because of these architectural differences, standards bodies and legal frameworks strictly dictate
tool utilization.

* The National Institute of Standards and Technology (NIST) conducts standardized evaluations of
  these devices through its Computer Forensic Tool Testing (CFTT) project, validating their
  effectiveness across various interfaces including SATA, IDE, NVMe, USB, and PCIe.
* SWGDE standard operating procedures mandate using hardware write-blockers whenever a writable
  medium is connected to a Windows or Linux workstation for preview or imaging. Adhering to these
  specifications provides the technical proof required to satisfy strict legal standards, such as the
  non-alteration rule mandated by UK ACPO Principle 1.
* Under US Federal Rules of Evidence (FRE) Rule 902(14), documenting the specific make, model, and
  firmware version of the write-blocker within a sworn certificate is standard practice to establish
  tool validation.

Failing to use a write-blocker shifts the legal burden onto the examiner to prove that the host
operating system did not alter hidden files, modify dynamic Windows Registry hives, or update
system timestamps during the investigation.

Despite their necessity, write blockers present an operational tension during modern
investigations. While highly effective for static, "dead" disk acquisitions, they cannot be
utilized during live memory captures, cloud storage extractions, or direct mobile device
extractions over USB. Interposing a hardware write blocker on an active system requires powering
the device down, an action that instantly purges volatile RAM evidence. This creates a critical
conflict for digital investigators: they must choose whether to enforce hardware write-blocking to
completely protect the physical disk, or bypass it entirely to capture active network sockets,
temporary encryption keys, and dynamic processes running in volatile memory.

## External Links

* [NIST: Computer Forensics Tool Testing Program (CFTT) - Hardware Write Block](https://www.nist.gov/itl/csd/secure-systems-and-applications/computer-forensics-tool-testing-program-cftt/cftt-6)

## Tools

### Open Source

* [Linux software write blocker](linux_write_blocker.md)

### Commercial

* [MyKey Technology, Inc.](https://www.mykeytech.com/),
  NoWrite FPU and FlashBlock II 1.8", 2.5" and 3.5" IDE to IDE, FireWire or USB to IDE and SATA,
  NIST Ver. 2 accepted.
* [SAFE Block XP](forensicsoft.md#safe-block-xp),
  NIST Ver. 1.2 accepted.
* [Tableau write blockers](https://www.opentext.com/products/digital-forensic-hardware),
  for IDE, SATA, SCSI, USB. NIST Ver. 1 accepted.
* [WiebeTech write-blockers](https://www.digistor.com/wiebetech),
  for almost any disk drive: 2.5" and 3.5" IDE, SCSI, SATA. NIST Ver. 1 accepted.
