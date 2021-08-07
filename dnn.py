import sys
import time
from datetime import datetime
start_time=datetime.now()
import pandas as pd
import numpy as np
import math
import os
import csv
import sklearn
from sklearn.metrics import matthews_corrcoef as mcc
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import accuracy_score

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
#y=y.tolist()
#print y

#training input dataset
df_train.drop(['Result'],1 , inplace=True)
t_in = df_train.values.tolist()
x = np.array(t_in)
#x=x.tolist()
#print len(y[0])
total_failed=np.count_nonzero(y)
total_passed=len(y)-total_failed


#print len(y)
#print len(x[0])
#print total_passed,total_failed

M=len(y)
l=len(x[0])

I=np.identity(len(x[0]))


x_train=x
print x_train
y_train=y
print y_train

from keras.models import Sequential
from keras.layers import Dense
from keras.utils import to_categorical

best=0
worst=0
suspicious=[0 for z in range(l)]
for kappa in range(1):
	
	# Initializing the ANN
	classifier = Sequential()
	
	# Adding the first hidden layer 
	layer_info = Dense(units=l+10 ,activation='relu',input_dim=l)
	classifier.add(layer_info)
	
	# Adding second hidden layer
	layer_info = Dense(units=l+10,activation='relu')
	classifier.add(layer_info)
	
	# Adding third hidden layer
	layer_info = Dense(units=l+10,activation='relu')
	classifier.add(layer_info)
	
	# Adding output layer
	layer_info = Dense(units=1,activation='sigmoid')
	classifier.add(layer_info)
	
	
	# Compiling the ANN
	classifier.compile( loss='mean_squared_error',optimizer='adam', metrics=['accuracy'])
	
	# Fitting the ANN to the training set
	classifier.fit(x_train, y_train, epochs=1000 , batch_size=200)
		
	x_test=I
	
	
	# Predicting the Test set results
	y_pred = classifier.predict(x_test)
	#print (y_pred)
	
	for i in range(l):
		suspicious[i]=suspicious[i]+y_pred[i]

for i in range(l):
	suspicious[i]=suspicious[i]/1.0


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

csvfile=open(str_cwd+"/dnn.csv", "a+")
spamwriter1 = csv.writer(csvfile, delimiter=',')
spamwriter1.writerow(lst);


