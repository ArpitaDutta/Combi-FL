import os



for i in range(1,318):
	os.chdir("mutants/m"+str(i))
	os.system("gcc replace_m"+str(i)+".c ")
	os.system("gcc replace_m"+str(i)+".c -o replace_m"+str(i)+".exe")
	


	
