#import check
from check import *
import sys
import os

if len(sys.argv[1:]) != 2:
	print("Usage : python3 main.py \"Input Hwp\" \"Output Directory\"")
	sys.exit(0)
 
if os.path.isdir(sys.argv[2]):
	print (sys.argv[2] + " is Exist")
	sys.exit(0)

unzip = "7z x " + sys.argv[1] + " -o" + sys.argv[2] + " 1>/dev/null"
print ("[!] Run : " + unzip)
os.system(unzip)

for Dir in os.listdir(sys.argv[2]):
	if Dir == "BinData" :
		CheckPS(Dir)
	elif Dir == "BodyText" : 
		CheckBody(Dir)
