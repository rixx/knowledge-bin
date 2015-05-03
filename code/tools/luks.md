#LUKS

## new LUKS
1. New partitioning: fdisk /dev/sdb
2. Generate: cryptsetup -v luksFormat /dev/sdb
3. Open: cryptsetup open /dev/sdb blakeks
4. Format: mkfs.ext4 /dev/mapper/blakeks
5. Name: e2label /dev/mapper/blakeks MeinKeks

## Existing LUKS: Manual

    cryptsetup open --type luks open /dev/sdb blakeks
    mount /dev/mapper/blakeks /bla

    umount /bla
    cryptsetup close /dev/mapper/blakeks

## Existing LUKS: automatic

udiskie ftw
