import numpy as np
import pandas as pd
import tensorflow as tf
import csv
import math
import os
#print tf.shape(new_X)

#F_W = tf.get_variable("f_w", [1,1,X.shape[1],1],initializer = tf.random_normal())



#print tf.shape(f_w)

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


def model(alpha):
    
	global X

	#F_W = tf.get_variable("F_W", [1,X.shape[1],1,1],dtype=tf.float32,initializer=tf.random_normal_initializer(seed=0))
	F_W = tf.get_variable("F_W", [1,X.shape[1],1,1],dtype=tf.float32,initializer=tf.random_uniform_initializer(minval=0,maxval=1,seed=0))
	#F_W = tf.get_variable("F_W",[1,X.shape[1],1,1],tf.random_uniform("F_W", 0, 1, dtype=tf.int32, seed=0))
	#F_W = tf.Variable(tf.random_uniform([1,X.shape[1],1,1]),0,1)
	x_place = tf.placeholder(tf.float32, shape=(1,new_X.shape[1],new_X.shape[2],1))
	y_place = tf.placeholder(tf.float32, shape=(1,new_Y.shape[1],1,1))

	learning_rate = tf.placeholder(tf.float32, shape=[])

	#conv_1 = tf.nn.softmax(tf.nn.conv2d(x_place,F_W,strides = [1,1,1,1], padding = 'VALID'))
	conv_1 = tf.nn.conv2d(x_place, F_W, strides=[1, 1, 1, 1], padding='VALID')

	conv_1_shape = tf.squeeze(conv_1)


	#print conv_1.shape,
	#print conv_1_shape.shape
	y_place_shape = tf.squeeze(y_place)
	#print new_Y.shape,    
	  
	loss = tf.losses.mean_squared_error(conv_1_shape,y_place_shape)



	l2_loss = 0.05 * tf.nn.l2_loss(F_W)

	#l1_regularizer = tf.contrib.layers.l1_regularizer(scale=0.005, scope=None)
	reg_loss = tf.add(loss,l2_loss,name = 'loss')
	#weights = tf.trainable_variables()
	#regularization_penalty = tf.contrib.layers.apply_regularization(l1_regularizer, weights)
	#reg_loss = tf.add(loss,regularization_penalty,name = 'loss')



	train_step = tf.train.AdamOptimizer(learning_rate = alpha).minimize(reg_loss)
	#train_step = tf.train.AdamOptimizer(learning_rate = lr).minimize(loss)

	correct_prediction = tf.equal(y_place_shape,conv_1_shape)




	sess = tf.Session()
	sess.run(tf.global_variables_initializer())
	#alphas = [0.01,0.001,0.0001,0.00001,0.000001]
	#for alpha in alphas:

	#print("Calculating for learning rate =",alpha),
	#print new_Y.shape,

	for epoch in range(100):
	    
		f,c,ts,l = sess.run([F_W,conv_1_shape,train_step,loss],{x_place:new_X,y_place:new_Y})
		#print epoch

		#print f

		#saver = tf.train.Saver()
		#save_path = saver.save(sess, "weights/conv_weights.ckpt")

	print 'Training Complete'

	print 'Testing.....'

	#saver.restore(sess, "weights/conv_weights.ckpt")

	x_test = tf.placeholder(tf.float32, shape=(1, new_vm.shape[1], new_vm.shape[2], 1))
	conv_2 = tf.nn.conv2d(x_test, F_W, strides=[1, 1, 1, 1], padding='VALID')
	conv_2_shape = tf.squeeze(conv_2)

	susp_score = sess.run(conv_2_shape, feed_dict={x_test : new_vm})
	print("************")
	print susp_score

	global column_list
	global column_list2

	#complexity_df = pd.read_csv('k_allv2.csv')
	susp_line = []
	for i in range(len(susp_score)):
		susp_score[i] += 0
		susp_line.append((susp_score[i],column_list2[i]))
	print susp_line
	susp_line.sort(reverse = True)


	print("************")
	print susp_line

	#column_list.sort_values()
	#print column_list

	global score_df

	#print score_df   
	score_dict = {}     
	    
	rank_list = []
	for i in range(len(susp_line)):
		score_dict[susp_line[i][1]] =  susp_line[i][0]
		#score_df[susp_line[i][1]+1] = susp_line[i][0] 
		if(int(susp_line[i][1])==fault_line_no+1):
		    rank_list.append(i+1)
	#print score_dict
	#print rank_list,
	score_df = pd.DataFrame(score_dict,columns = column_list, index = [0])

	score_df.to_csv('cnn_stats1.csv',sep = ',', index = False)
	print score_df

	print '--------------\n'

	for i in required_sentences:
		print i	
	print '---------------\n'



	if not rank_list:
		for i,ele in enumerate(required_sentences):
		    if(int(ele) == fault_line_no+1):
			rank_list.append(len(susp_line)+i+1)	 	



	print rank_list,	



	'''    
	print '\n'


	susp_line_abs = [];
	for i in susp_line:
		susp_line_abs.append((abs(i[0]),i[1]))

	susp_line_abs.sort(reverse = True);     
	rank_list_abs = []
	for i in range(len(susp_line_abs)):
		if(susp_line_abs[i][1]==fault_line_no):
		    rank_list_abs.append(i+1)
		
		print rank_list_abs,	
	'''
    
     
            
fault_line_no = 3 #int(raw_input("Enter faulty line number"))    


#df_train = pd.read_csv('statementResult.csv')



statement_data = pd.read_csv('statementResult.csv')
column_list = list(statement_data.columns)
column_list.remove('Result')

#print column_list



reduced_statement_data = pd.DataFrame()
reduced_statement_data = statement_data[statement_data.Result != 0]
statement_data2 = reduced_statement_data
statement_data2 = statement_data2.reset_index()
statement_data2 = statement_data2.drop(['index'],axis = 1)
#print statement_data2
col_list = reduced_statement_data.columns


for col in col_list:
	#statement_info = statement_data[col]
	if (0 in reduced_statement_data[col].values) and col != 'Result':
		#print statement_data[col]
		reduced_statement_data = reduced_statement_data.drop([col],axis = 1)
	else:
		continue

#print reduced_statement_data.columns
statement_data =    statement_data[reduced_statement_data.columns]

column_list2 = list(statement_data.columns)
#print column_list2
#print statement_data


min_sent_df = (((statement_data2.drop(['Result'],axis=1)) == 1).astype(int).sum(axis=1))
min_val = min(min_sent_df)

min_sent_index = min_sent_df[min_sent_df==min_val].index.values.astype(int)
#print min_sent_index
min_row_index = min_sent_index[0]

#print min_row_index

executed_sentence = statement_data2.iloc[[min_row_index]]
#print executed_sentence
executed_sentence_col = executed_sentence.columns
#print e
for col in executed_sentence_col:
	if (0 in executed_sentence[col].values) and col != 'Result':
		executed_sentence = executed_sentence.drop([col],axis = 1)            

sentences_from_SI = statement_data.columns
sentences_from_tfm = executed_sentence.columns
#print sentences_from_SI
#print sentences_from_tfm

required_sentences = list(set(sentences_from_tfm) - set(sentences_from_SI))

#print statement_data




y = np.array([statement_data['Result']]).T
#new_Y = tf.squeeze(y)

#print new_Y.shape,
#new_Y = tf.reshape(y,[1,y.shape[0],1,1])
new_Y = y.reshape(1,y.shape[0],1,1)
statement_data.drop(['Result'],1 , inplace=True)

t_in = statement_data.values.tolist()
X = np.array(t_in)
f_w = tf.Variable(tf.random_normal([1,1,X.shape[1],1]),name="f_w")
#new_X = tf.reshape(X,[1,X.shape[0],X.shape[1],1])
new_X = X.reshape(1,X.shape[0],X.shape[1],1)
virtual_matrix = np.zeros((X.shape[1],X.shape[1]), int)
np.fill_diagonal(virtual_matrix, 1)
new_vm = virtual_matrix.reshape(1,virtual_matrix.shape[0],virtual_matrix.shape[1],1)


alpha = 0.1 # float(raw_input("Enter alpha value"))

model(alpha)



print("data val")
rearrange=pd.read_csv('cnn_stats1.csv')
print(rearrange)
for i in rearrange: 
	print(rearrange[i][0]);
with open('cnn_stat.csv','w') as csvfile:
	write1=csv.writer(csvfile, delimiter=',')
	value=[]
	value.append('line_number');
	value.append('cnn_score');
	write1.writerow(value);
	value=[]
	l_no=0;
	for val_data in rearrange: 
		value.append(l_no);
		if math.isnan(rearrange[val_data][0]): #rearrange[val_data][0] suspiciousness score
			value.append("0")
		else: 
			value.append(rearrange[val_data][0])
		write1.writerow(value);
		l_no=l_no+1;
		value=[];

df = pd.read_csv("cnn_stat.csv")
susp = np.array(df["cnn_score"]).T
susp = susp.tolist()
#print susp

susp = np.array(susp)
susp = -susp
susp = susp.tolist()

ranks = rankify(susp)
print ranks

with open("f_l.txt",'r') as f:
	line = f.readline()

ranks.insert(0,line)

csvfile=open(str_cwd+"/cnn.csv", "a+")
spamwriter1 = csv.writer(csvfile, delimiter=',')
spamwriter1.writerow(ranks);

