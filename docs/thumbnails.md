---
tags:
  - No Category
---
**Thumbnails** are reduced-size versions of pictures, serving the same
role for images as a normal text index does for words.

## [Windows](windows.md)

See [Thumbs.db](thumbs.db.md).

## [Windows](windows.md) Vista

*See [Windows thumbcache](windows_thumbcache.md)*

Thumbs.db no longer exists in Vista. This data has been moved to
*\Users\\\AppData\Local\Microsoft\Windows\Explorer*

[Windows](windows.md) Vista will save thumbnails for files on
mounted encrypted file systems (except
[EFS](windows_encrypted_file_system.md).

## KDE & GNOME

KDE and GNOME are popular desktop environments for
[Linux](linux.md) and [UNIX](unix.md) platforms. They
are storing thumbnails in *\~/.thumbnails*.

Example thumbnail in GNOME:

    $ hachoir-metadata .thumbnails/normal/0d97afdc637ac86d75d13e72172dc77c.png
    Metadata:
    - Image width: 128 pixels
    - Image height: 122 pixels
    - Bits/pixel: 24
    - Pixel format: RGB
    - Compression rate: 1.6x
    - Compression: deflate
    - Producer: GNOME::ThumbnailFactory
    - Comment: Thumb::Image::Width=779
    - Comment: Thumb::Image::Height=744
    - Comment: Thumb::URI=file:///media/truecrypt1/123.jpg
    - Comment: Thumb::MTime=1216153400
    - MIME type: image/png
    - Endian: Big endian

GNOME will save thumbnails for files on mounted encrypted filesystems.

Example thumbnail in KDE:

    $ hachoir-metadata .thumbnails/normal/2e4bc7bf05bd57e19c6f2a01cf4a8f71.png
    Metadata:
    - Image width: 96 pixels
    - Image height: 128 pixels
    - Bits/pixel: 24
    - Pixel format: RGB
    - Compression rate: 1.6x
    - Compression: deflate
    - Producer: KDE Thumbnail Generator
    - Comment: Thumb::MTime=1236952299
    - Comment: Thumb::Mimetype=image/jpeg
    - Comment: Thumb::Size=827837
    - Comment: Thumb::URI=file:///home/fuf/10032009(002).jpg
    - MIME type: image/png
    - Endian: Big endian

## External Links
