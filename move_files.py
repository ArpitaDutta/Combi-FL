import os



for i in range(1,318):
	os.system("mv faulty_line_m"+str(i)+".txt mutants/m"+str(i))
	os.system("mv replace_m"+str(i)+".c mutants/m"+str(i))


	
