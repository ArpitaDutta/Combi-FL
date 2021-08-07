import os



for i in range(1,318):
	os.chdir("mutants/m"+str(i))
	os.system("cp replace_m"+str(i)+".exe source")
	


	
