
import os

fp=open("mutants_working.txt")
for line in fp:
	line=line.rstrip("\n")
	#print line
	#os.system("cp tarantula.py mutants/m"+str(line))
	#os.system("cp DStar.py mutants/m"+str(line))
	#os.system("cp Ochiai.py mutants/m"+str(line))
	#os.system("cp Ample.py mutants/m"+str(line))
	#os.system("cp Barinel.py mutants/m"+str(line))
	os.system("cp Crosstab.py mutants/m"+str(line))	
	#os.system("cp dnn.py mutants/m"+str(line))	
	#os.system("cp cnn.py mutants/m"+str(line))
	#os.system("cp rbfnn.py mutants/m"+str(line))
	#os.system("cp bpnn.py mutants/m"+str(line))
	
