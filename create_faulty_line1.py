import csv
import os
import sys
import subprocess
with open('f_l.txt','w') as wf:
	with open("faulty_line$$$$$.txt") as f:
		l = f.readline()
		l = int(l)+1
		fp=open("replace$$$$$.c.gcov");
		j=1
		for line in fp:
			flag1=line.split(":")[0]
			flag2=int(line.split(":")[1])
			if "-" in flag1:
				continue
			elif "#####" in flag1 and flag2==l :
				wf.write(str(j))
				break
			elif "#####" in flag1 and flag2!=l :
				j=j+1
			else:
				if flag2==l :			
					wf.write(str(j))
					break
				else :
					j=j+1
			
		
    


