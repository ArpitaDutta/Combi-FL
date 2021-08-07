
import os

fp=open("mutants_working.txt")
for line in fp:
	line=line.rstrip("\n")
	#print line
	os.chdir("mutants/m"+str(line))
	#os.system("python tarantula.py")
	#os.system("python DStar.py")
	#os.system("python Ochiai.py")
	#os.system("python Ample.py")
	#os.system("python Barinel.py")
	os.system("python Crosstab.py")
	#os.system("python dnn.py")
	#os.system("python cnn.py")
	#os.system("python rbfnn.py")
	#os.system("python bpnn.py")
	


	
