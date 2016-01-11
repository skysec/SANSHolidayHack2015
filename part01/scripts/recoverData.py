from scapy.all import *
import base64,sys



def recoverCommands(pcap_file, result_file):
    capture=rdpcap(pcap_file)
    f = open(result_file, 'w')
				
    for p in capture:
        try:
            f.write(p.src)
            f.write(" : ")
            f.write(p.an.rdata)
            f.write("\n")
            f.write(base64.b64decode(p.an.rdata))
            f.write("\n")
        except:
            pass
    f.close() 


def recoverImage(pcap_file, image_file):
	capture=rdpcap(pcap_file)
	image = open(image_file, 'w')
	found = False
	for p in capture:
	    try:
		if found:
		    
		    image.write(base64.b64decode(p.an.rdata)[5:])
		if 'RklMRTpTVEFSVF9TVEFURSx' in p.an.rdata: found = True
		if 'RklMRTpTVE9QX1NUQVRF' in p.an.rdata: found = False
	    except:
		pass
	image.close()

if __name__ == "__main__":
	if len(sys.argv) != 4:
		print "Usage: script <path_to_pcap> <path_to_result> <image|command>"
		exit()
	if sys.argv[3] == "image":
		recoverImage(sys.argv[1],sys.argv[2])
	else:
		recoverCommands(sys.argv[1],sys.argv[2])
	
        
