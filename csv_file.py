import os
import csv
cwd = os.getcwd()
lst=[]
lst.append('Faulty_Line')
for i in range(255):
	lst.append(i)
csvfile=open(cwd+"/tarantula.csv", "w")
spamwriter=csv.writer(csvfile, delimiter=',')
spamwriter.writerow(lst)


	
	


	
