import os


for i in range(1,318):
	with open("funcStatementInfo1.py", "rt") as fin:
	    with open("funcStatementInfo.py", "wt") as fout:
		for line in fin:
		    fout.write(line.replace('$$$$$', '_m'+str(i)))	
		os.system("chmod +x funcStatementInfo.py")	
	os.system("mv funcStatementInfo.py mutants/m"+str(i))
	


	
