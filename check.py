import zlib
import sys
import os


def RetDirList(MyDir):
	if os.path.isdir(sys.argv[2] + "/" + MyDir):
		return os.listdir(sys.argv[2] + "/" + MyDir)

def CheckBody(Dir):
	ll = RetDirList(Dir)
	pwd = sys.argv[2] + "/" + Dir
	size = 0
	cnt  = 0
	print ("[!] found " + str(len(ll)) + " file in "+ Dir)
	for tmp in ll:
		nsize = int(os.path.getsize(pwd+"/"+tmp))
		if nsize == size:
			++cnt
			size = nsize
	if cnt :
		print ("found the same size file : " + cnt)
	else :
		print ("[-] Not found the same size file")

def CheckPS(Dir):
	ll = RetDirList(Dir)
	pwd = sys.argv[2] + "/" + Dir
	flag = 0
	print ("[!] found "+ str(len(ll)) +" file in "+Dir)
	for tmp in ll:
		if (tmp.find("PS") > 0 or tmp.find("ps") > 0):
				print ("[+] Find Postscript : "+ Dir + " => " + tmp)
				d = open (pwd+"/"+tmp, 'rb').read()
				data = zlib.decompress(d, -15)
				open(pwd+"/"+tmp+".out",'wb').write(data)
