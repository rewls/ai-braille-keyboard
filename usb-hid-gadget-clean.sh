#! /bin/bash

CONFIGFS_HOME=/config
GADGET_NAME=braille-keyboard

cd $CONFIGFS_HOME/usb_gadget/$GADGET_NAME

rm configs/c.1/hid.usb0
rmdir configs/c.1/strings/0x409
rmdir configs/c.1
rmdir functions/hid.usb0
rmdir strings/0x409

cd ..
rmdir $GADGET_NAME

cd ../..
umount /config
rmdir /config
