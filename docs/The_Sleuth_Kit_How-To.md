To find which file maps to a given sector number on the first partition
of a Windows volume:

` ifind -o63 -d `<sector-number>` `<disk-image>

This returns an inode number.

` ffind -o63 `<disk-image>` `<inode-number>

For example, if we want to find which file maps to sector 1249 of the
file image.iso, use:

` $ ifind -o63 -d 1249 image.iso`
` 6`
` $ ffind -o63 image.iso 6`
` /TCLAIM.TXT`

You can print out the contents of the file with the icat command:

    $ icat -o63 image.iso  6
    �����������������������������������������������������������������������������ͻ
    � ������������    �����������  ��              ��      ��������   ���     ��� �
    �      ��         ��       ��  ��             ����        ��      ����   ���� �
    �      ��         ��           ��            ��  ��       ��      �� �� �� �� �
    �      ��         ��           ��           ��    ��      ��      ��  ���  �� �
    �      ��         ��           ��          ��      ��     ��      ��       �� �
    �      ��         ��           ��          ��      ��     ��      ��       �� �
    �      ��         ��           ��          ����������     ��      ��       �� �
    �      ��         ��       ��  ��          ��      ��     ��      ��       �� �
    �      ��         �����������  ����������� ��      ��  ��������   ��       �� �
    �                                                                             �
    �����������������������������������������������������������������������������ͼ

[Category:Howtos](Category:Howtos "wikilink")