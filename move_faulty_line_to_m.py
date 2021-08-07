import os


for i in range(1,318):
	with open("create_faulty_line1.py", "rt") as fin:
	    with open("create_faulty_line.py", "wt") as fout:
		for line in fin:
		    fout.write(line.replace('$$$$$', '_m'+str(i)))	
		os.system("chmod +x create_faulty_line.py")	
	os.system("mv create_faulty_line.py mutants/m"+str(i))
	


	
