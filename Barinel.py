import sys
import time
from datetime import datetime
start_time=datetime.now()
import pandas as pd
import numpy as np
import math
import os
import csv


cwd = os.getcwd()
print(cwd)
p=0
i=-1
while i>= (-len(cwd)) :
	if cwd[i]=='/' :
		p=p+1
	if p==1 :
		break
	i=i-1
str_cwd=cwd[:i]
print(str_cwd)

with open("f_l.txt",'r') as f:
	line = f.readline()

df_train=pd.read_csv('statementResult.csv')

#training output dataset
y = np.array([df_train['Result']]).T
y=y.tolist()
#print y

#training input dataset
df_train.drop(['Result'],1 , inplace=True)
t_in = df_train.values.tolist()
x = np.array(t_in)
x=x.tolist()
#print len(y[0])
total_failed=np.count_nonzero(y)
total_passed=len(y)-total_failed



suspicious=[]

for i in range(0,len(x[0])):
	nsuccess=0
	nfailure=0
	for j in range(0,len(y)):
		#print x[j][i],y[j][0]
		if x[j][i]==1 and y[j][0]==0:
			nsuccess=nsuccess+1
		elif x[j][i]==1 and y[j][0]==1:
			nfailure=nfailure+1
	try:
		#print nfailure,nsuccess
		cef=nfailure
		cnf=total_failed-nfailure
		cep=nsuccess
		cnp=total_passed-nsuccess
		sus_score=1-(float(cep)/float(cep+cef))
		suspicious.append(sus_score)
		print(str(i)+"   "+str(sus_score))
	except ZeroDivisionError:
		sus_score=-999999
		suspicious.append(sus_score)
		print(str(i)+"   "+str(sus_score))

d = {}
for i in range(0,len(suspicious)):
	key = float(suspicious[i])
	#print key
	if key not in d:
		d[key] = []
	d[key].append(i)

lst=[]
lst.append(line)
for fl in range(0,len(x[0])):
	ct1=0
	ct2=0
	ct3=0
	fct=0
	# print("Faulty line:"+str(fl))
	for x in sorted(d):
		# print (x,len(d[x]))
		if fl not in d[x] and fct==0:
			ct1=ct1+len(d[x])
		elif fl not in d[x] and fct==1:
			ct3=ct3+len(d[x])
		else: 
			fct=1
			ct2=len(d[x])
	b=ct3+1
	w=ct3+ct2
	avg=(b+w)/2
	lst.append(avg)
	# print("We have to search "+str(ct3+1)+" to "+str(ct3+ct2))

print(lst)

csvfile=open(str_cwd+"/Barinel.csv", "a+")
spamwriter1 = csv.writer(csvfile, delimiter=',')
spamwriter1.writerow(lst);


