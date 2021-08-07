import sys
import time
from datetime import datetime
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

#==============================origial Maccon===================
st1=datetime.now()
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
#print len(y)
#print len(x[0])
#print total_passed,total_failed


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
		
		n_f=np.count_nonzero(y)
		n_s=len(y)-n_f
		n= len(y)
		n_cf=nfailure
		n_cs=nsuccess
		#print("statement covered by number of succesful test cases:"+ str(n_cs))
		#print("statement covered by number of failed test cases: "+str(n_cf))
		n_c=n_cs+n_cf
		#print("statement covered by number of test cases: "+ str(n_c))
		n_u=n-n_c
		#print("statement not covered by number of test cases: "+ str(n_u))
		n_uf=n_f-n_cf
		#print("statement not covered by number of failed test cases: "+ str(n_uf))
		n_us=n_s-n_cs
		#print("statement not covered by number of sucessful test cases: "+ str(n_us))
		e_cf=float((n_c*n_f))/n
		#print(e_cf)
		e_cs=float((n_c*n_s))/n
		#print(e_cs)
		e_uf=float((n_u*n_f))/n
		#print(e_uf)
		e_us=float((n_u*n_s))/n
		#print(e_us)
		if e_cf!=0:
			factor1=float(((n_cf-e_cf)*(n_cf-e_cf)))/e_cf
		else:
			factor1=0
		#print("Factor 1: "+str(factor1))
		if e_cs!=0:
			factor2=float(((n_cs-e_cs)*(n_cs-e_cs)))/e_cs
		else:
			factor2=0
		#print("Factor 2: "+str(factor2))
		if e_uf!=0:
			factor3=float(((n_uf-e_uf)*(n_uf-e_uf)))/e_uf
		else:
			factor3=0
		#print("Factor 3: "+str(factor3))
		if e_us!=0:
			factor4=float(((n_us-e_us)*(n_us-e_us)))/e_us
		else:
			factor4=0
		#print("Factor 4: "+str(factor4))
		x2_w=factor1+factor2+factor3+factor4
		#print("The x2_w value is: " +str(x2_w))
		m_w=float(x2_w)/n
		#print("The m_w value is: " +str(m_w))
		chi_w=0		
		if n_f!=0:
			chi_w_num= float(n_cf)/n_f
		if n_s!=0:
			chi_w_den= float(n_cs)/n_s
		if chi_w_den!=0:
			chi_w= chi_w_num/chi_w_den
		if chi_w>1:
                	fail_score=m_w
		elif chi_w==1:
			fail_score=1
		else: 
			fail_score= -m_w

		
		sus_score=fail_score
		suspicious.append(sus_score)
		#print(str(i)+"   "+str(sus_score))
	except ZeroDivisionError:
		suspicious.append(0)

d = {}
for i in range(0,len(suspicious)):
	key = float(suspicious[i])
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

csvfile=open(str_cwd+"/Crosstab.csv", "a+")
spamwriter1 = csv.writer(csvfile, delimiter=',')
spamwriter1.writerow(lst);
