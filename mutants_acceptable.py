import pandas as pd
import numpy as np
import math
import os
import csv


with open("mutants_working.txt",'w') as wf:
	
	for i in range(1,318):	
		if i==1 or i==2 or i==7 or i==17 or i==61 or i==70 or i==73 or i==78 or i==79 or i==81 or i==94 or i==95 or i==96 or i==97 or i==100 or i==119 or i==120 or i==138 or i==139 or i==140 or i==142 or i==144 or i==145 or i==146 or i==147 or i==173 or i==174 or i==184 or i==188 or i==211 or i==212 or i==213 or i==217 or i==225 or i==226 or i==227 or i==232 or i==233 or i==234 or i==235 or i==236 or i==237 or i==238 or i==239 or i==240 or i==241 or i==242 or i==248 or i==250 or i==253 or i==255 or i==256 or i==257 or i==259 or i==289 or i==290 or i==291 or i==294 or i==295 or i==296 or i==299 or i==300 or i==301 or i==302 or i==303 or i==304 or i==305 : continue
		os.chdir("mutants/m"+str(i))
		df = pd.read_csv('statementResult.csv')
		y = np.array([df['Result']]).T
		y = y.tolist()

		total_failed = np.count_nonzero(y)
		total_passed = len(y)-total_failed

		if total_failed != 0 and total_passed != 0 and len(y)==5542:
			wf.write(str(i)+"\n")
	


