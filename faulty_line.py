import os


for i in range(1,318):
	os.chdir("mutants/m"+str(i))
	os.system("python create_faulty_line.py")
	
	


	
