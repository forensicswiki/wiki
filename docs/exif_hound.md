---
tags:
  - File Analysis
  - Free Software
  - Linux
  - macOS
  - Open Source Software
  - Photo
  - Tools
  - Windows
---
EXIF Hound is a free and open source desktop application for inspecting
[Exif](exif.md) [metadata](metadata.md) in image files and plotting the
GPS coordinates stored in that metadata on a map. It is released under the
MIT license and built with Tauri (a Rust back end with a web-based user
interface). It has been distributed since 2020. Signed installers are
available for macOS (Apple Silicon), Windows (x64) and Linux (x64 and
ARM64). Version 2.7.0 was released on 2026-10-13.

EXIF Hound is local-first: metadata parsing runs on the examiner's computer,
and image files, metadata, filenames and investigation data are not
uploaded. The application has no user account and no telemetry. It uses the
network only for:

* map tiles (OpenStreetMap by default, or a custom tile server configured
  in the settings);
* signed update checks against a static feed hosted on GitHub Pages;
* optional reverse geocoding ("place names"), which is off by default. When
  enabled, only the latitude and longitude are sent to the OpenStreetMap
  Nominatim service.

## Caution

Pros:

* Images are not sent to a third-party web service, unlike many online Exif
  viewers. This lowers the risk of disclosing case material.
* Batch view of many images, map plotting and CSV/JSON export help with
  triage and with reporting location and timestamp findings.
* The source code is public, so its parsing behavior can be reviewed.

Cons and trade-offs:

* EXIF Hound is an analysis and triage tool, not a validated forensic
  acquisition tool. Findings that matter for a case should be confirmed
  with a second tool, for example [ExifTool](exiftool.md).
* As with any viewer, work on a verified working copy of the evidence
  (compare [hashes](hash.md) before and after) rather than the original.
* Exif data is easy to edit or remove. Timestamps and GPS coordinates may
  have been changed, stripped by a social media platform, or set wrongly
  by the device, so treat them as indicators that need corroboration.
* Loading map tiles sends tile requests to the tile server, which can show
  the general area being viewed. In sensitive cases, use a self-hosted tile
  server or work without a network connection; metadata inspection does not
  need the network.
* If the optional place-name lookup is enabled, the coordinates are shared
  with OpenStreetMap Nominatim. Leave it disabled when coordinates must not
  leave the examiner's computer.

## Use

* Review the full Exif metadata of one or many images (camera make and
  model, original and digitized timestamps, GPS fields) and compare images.
* Plot GPS-tagged photos on an interactive map, with routes and clusters,
  to reconstruct where and in what order photos were taken.
* Navigate a large set of imported images in a spreadsheet-style list view.
* Import KML and export metadata as CSV or JSON for timelines and reports.

## See Also

* [Exif](exif.md)
* [ExifTool](exiftool.md)
* [jhead](jhead.md)
* [libexif](libexif.md)
* [Metadata](metadata.md)
* [Document Metadata Extraction](document_metadata_extraction.md)

## External Links

* [EXIF Hound source code (GitHub)](https://github.com/minimallyexceptional/exif-hound)
* [EXIF Hound releases](https://github.com/minimallyexceptional/exif-hound/releases)
* [EXIF Hound security policy](https://github.com/minimallyexceptional/exif-hound/blob/main/SECURITY.md)
* [Nominatim usage policy](https://operations.osmfoundation.org/policies/nominatim/)
* [OpenStreetMap tile usage policy](https://operations.osmfoundation.org/policies/tiles/)
