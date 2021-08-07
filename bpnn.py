import numpy as np
import pandas as pd
import csv
import os
import sys
from scipy import stats


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

alphas = [0.001,0.01,0.1]
hiddenSize = 4

# compute sigmoid nonlinearity
def sigmoid(x):
	output = 1/(1+np.exp(-x))
	return output

# convert output of sigmoid function to its derivative
def sigmoid_output_to_derivative(output):
	return output*(1-output)



def chunks(l, n):
	return [l[i:i+n] for i in range(0, len(l), n)]

'''X = np.array([[0,0,1],
            [0,1,1],
            [1,0,1],
            [1,1,1]])
                
y = np.array([[0],
			[1],
			[1],
			[0]])'''


def rankify(A): 
  
	R = [0 for x in range(len(A))] 

	for i in range(len(A)): 
		(r, s) = (1, 1)
 
		for j in range(len(A)): 
			if j != i and A[j] < A[i]: 
				r += 1
			if j != i and A[j] == A[i]: 
				s += 1       
	 
		R[i] = r + (s - 1) / 2

	return R 

df_train=pd.read_csv('statementResult.csv')
y = np.array([df_train['Result']]).T
df_train.drop(['Result'],1 , inplace=True)
t_in = df_train.values.tolist()
X = np.array(t_in)

susp = [0 for k in range(len(X[0]))]

for alpha in alphas:
	
	print "\nTraining With Alpha:" + str(alpha)
	#dataset
	df_train=pd.read_csv('statementResult.csv')

	#training output dataset
	y = np.array([df_train['Result']]).T

	#training input dataset
	df_train.drop(['Result'],1 , inplace=True)
	t_in = df_train.values.tolist()
	X = np.array(t_in)

	
	vr=np.identity(len(X.T))
	VS =vr
	np.random.seed(1)
	print("length of x"+str(len(X.T)))
	print("length of x..."+str(len(y.T)))
	# randomly initialize our weights with mean 0
	synapse_0 = 2*np.random.random((len(X.T),hiddenSize)) - 1
	synapse_1 = 2*np.random.random((hiddenSize,1)) - 1

	if alpha==0.001 : kappa=2000
	elif alpha==0.01 : kappa=1000
	else : kappa=500
 
	for j in xrange(kappa):
		#print("calculating")
		# Feed forward through layers 0, 1, and 2
		layer_0 = X
		layer_1 = sigmoid(np.dot(layer_0,synapse_0))
		layer_2 = sigmoid(np.dot(layer_1,synapse_1))
		#layer_3 = sigmoid(np.dot(layer_2,synapse_2))
		#layer_3_error = layer_3 - y
		#layer_3_delta = layer_3_error*sigmoid_output_to_derivative(layer_3)
		layer_2_error = layer_2 - y
		layer_2_delta = layer_2_error * sigmoid_output_to_derivative(layer_2)
		layer_1_error = layer_2_delta.dot(synapse_1.T)
		layer_1_delta = layer_1_error * sigmoid_output_to_derivative(layer_1)
		#synapse_2 -= alpha * (layer_2.T.dot(layer_3_delta))
		synapse_1 -= alpha * (layer_1.T.dot(layer_2_delta))
		synapse_0 -= alpha * np.dot(zip(*layer_0),(layer_1_delta))
		print j

	a = sigmoid(np.dot(VS,synapse_0))
	b = sigmoid(np.dot(a,synapse_1))
	#c = sigmoid(np.dot(b,synapse_2))
	print("length of b"+str(len(b)))
	#print b[64][0]
	
	for i in range(len(X[0])):
		susp[i] = susp[i] + b[i][0]

for i in range(len(X[0])):
	susp[i] = susp[i]/3.0

print susp

susp = np.array(susp)
susp = -susp
susp = susp.tolist()

ranks = rankify(susp)

print ranks

with open("f_l.txt",'r') as f:
	line = f.readline()

ranks.insert(0,line)

csvfile=open(str_cwd+"/bpnn.csv", "a+")
spamwriter1 = csv.writer(csvfile, delimiter=',')
spamwriter1.writerow(ranks);

	

      
