#! /bin/bash

CONFIGFS_HOME=/config
GADGET_NAME=braille-keyboard

modprobe libcomposite
mkdir $CONFIGFS_HOME
mount -t configfs none $CONFIGFS_HOME

mkdir $CONFIGFS_HOME/usb_gadget/$GADGET_NAME
cd $CONFIGFS_HOME/usb_gadget/$GADGET_NAME

echo 0x1d6b > idVendor
echo 0x0104 > idProduct

mkdir strings/0x409
echo "BRKB-20240920-01" > strings/0x409/serialnumber
echo "Dot to dots" > strings/0x409/manufacturer
echo "Braille Keyboard" > strings/0x409/product

mkdir configs/c.1
mkdir configs/c.1/strings/0x409
echo "Braille Keyboard Configuration" > configs/c.1/strings/0x409/configuration
echo 500 > configs/c.1/MaxPower

mkdir functions/hid.usb0
echo 1 > functions/hid.usb0/protocol
echo 8 > functions/hid.usb0/report_length
echo -ne "\x05\x01\x09\x06\xa1\x01\x05\x07\x19\xe0\x29\xe7\x15\x00\x25\x01\x75\x01\x95\x08\x81\x02\x95\x01\x75\x08\x81\x03\x95\x05\x75\x01\x05\x08\x19\x01\x29\x05\x91\x02\x95\x01\x75\x03\x91\x03\x95\x06\x75\x08\x15\x00\x25\x65\x05\x07\x19\x00\x29\x65\x81\x00\xc0" > functions/hid.usb0/report_desc

ln -s functions/hid.usb0 configs/c.1

echo dwc2 > UDC
