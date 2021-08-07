import sys
import time
from datetime import datetime
start_time=datetime.now()
from collections import defaultdict
import os
from scipy import *
from scipy.linalg import norm, pinv
import pandas as pd
import numpy as np
from scipy.spatial.distance import cosine
import csv

 
beta=0.1
global sigma

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

def findPara(x):
	o=[]
	for c in x:
		temp=False
		for u in o:
			if (norm(c-u)**2)<beta:
				temp=True
				break
		if temp==False:
			o.append(c)
	
	return o

def sigma(numCenters,o):
	dTemp = 0
	final=0
	for i in range(0,numCenters):
		tdis=sys.maxint
		for k in range(0,numCenters):
			if k==i:
				continue
			dist = np.sqrt(cosine(o[i],o[k]))
			if dist < tdis :
				tdis = dist
		final=final+tdis
	
	#print final,numCenters
	sigma = (final/numCenters)
	
	return sigma
		
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
	
 
class RBF:
	def __init__(self, indim, numCenters, outdim):
		self.indim = indim
		self.outdim = outdim
		self.numCenters = numCenters
		self.centers = o # choose center vectors from findPara function
		self.beta = beta
		self.W = random.random((self.numCenters, self.outdim))
		
	def _basisfunc(self, c, d):
		return exp(-((sqrt(cosine(c,d)))**2/(2*(sigma**2))))
	
	def _calcAct(self, X):
		# calculate activations of RBFs
		G = zeros((X.shape[0], self.numCenters), float)
		for ci, c in enumerate(self.centers):
			for xi, x in enumerate(X):
				G[xi,ci] = self._basisfunc(c, x)
		return G

	def train(self, X, Y):
		""" X: matrix of dimensions n x indim 
		    y: column vector of dimension n x 1 """
		
		'''choose random center vectors from training set
		rnd_idx = random.permutation(X.shape[0])[:self.numCenters]
		self.centers = [X[i,:] for i in rnd_idx]'''
		
		# calculate activations of RBFs
		G = self._calcAct(X)

		print G
		
		# calculate output weights (pseudoinverse)
		self.W = dot(pinv(G), Y)
		
	def test(self, X):
		#X: matrix of dimensions n x indim
		
		G = self._calcAct(X)

		Y = dot(G, self.W)
		
		
		#for grouping the ranks
		Y=np.array(Y.tolist())
		print Y
		susp=[]

		for i in range(len(Y)):
			susp.append(Y[i][0])
				
		print susp

		susp = np.array(susp)
		susp = -susp
		susp = susp.tolist()

		ranks = rankify(susp)
		print ranks
		ranks.insert(0,line)

		csvfile=open(str_cwd+"/rbfnn.csv", "a+")
		spamwriter1 = csv.writer(csvfile, delimiter=',')
		spamwriter1.writerow(ranks);

		return Y


		
if __name__ == '__main__':
	
        #dataset
	df_train=pd.read_csv('statementResult.csv')

	#training output dataset
	y = np.array([df_train['Result']]).T

	#training input dataset
	df_train.drop(['Result'],1 , inplace=True)
	t_in = df_train.values.tolist()
	x = np.array(t_in)
	#print len(x[0])
	#print len(y)
	#virtual set for test data
        #vr=np.identity(len(x.T))
	df_test=np.identity(len(x.T))
	#test_in = df_test.values.tolist()
	VS = np.array(df_test)
	#print len(VS)
	#find centers

	o=findPara(x)
	
	#find sigma
	sigma=sigma(len(o),o)
	
        # rbf regression
	rbf = RBF(len(x), len(o),1)
	rbf.train(x, y)
	z = rbf.test(VS)
	#print z
	
