import os


for i in range(1,318):
	
	os.system("cp -r input mutants/m"+str(i))
	os.system("cp -r moni mutants/m"+str(i))
	os.system("cp -r temp-test mutants/m"+str(i))
	os.system("cp universe mutants/m"+str(i))

	
