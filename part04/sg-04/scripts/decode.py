import base64,sys

def main(argv):
	fileIn = open(argv[0],'r')
	fileOut = open(argv[1] , "w")
	fileOut.write(base64.b64decode(fileIn.read()))
	fileIn.close()
	fileOut.close()

if __name__ == "__main__":
	if len(sys.argv) > 2:
		main(sys.argv[1:])
	else:
		print "Error"
