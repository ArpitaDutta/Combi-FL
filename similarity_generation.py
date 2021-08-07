import os
import csv
import pandas as pd
import numpy as np
import scipy.stats as stats
import math

#----------------------------Ample----------------------------------#
df_ample=pd.read_csv('Ample.csv')
versions=np.array(df_ample['Faulty_Line']).T
versions=versions.tolist()
#print versions
df_ample.drop(['Faulty_Line'],1,inplace=True)
t_ample = df_ample.values.tolist()
rank_ample=np.array(t_ample)
rank_ample=rank_ample.tolist()
#print rank_ample

df_ample_m=pd.read_csv('Ample_m.csv')
fl=np.array(df_ample_m['Faulty_Line']).T
fl=fl.tolist()
#print fl
df_ample_m.drop(['Faulty_Line'],1,inplace=True)
t_ample_m = df_ample_m.values.tolist()
rank_ample_m=np.array(t_ample_m)
rank_ample_m=rank_ample_m.tolist()
#print rank_ample_m

suspicious_ample=[[0 for i in range(len(fl))] for j in range(len(versions))]

for i in range(len(versions)):
	for j in range(len(fl)):
		#print (i,j)
		tau, p_value = stats.kendalltau(rank_ample[i],rank_ample_m[j])
		if math.isnan(tau)==True :
			suspicious_ample[i][j]=0		
		else :
			suspicious_ample[i][j]=tau

#print suspicious_ample
#print np.array(suspicious_ample)
#----------------------------Ample-----------------------------------#


#----------------------------Barinel----------------------------------#

df_barinel=pd.read_csv('Barinel.csv')
versions=np.array(df_barinel['Faulty_Line']).T
versions=versions.tolist()
#print versions
df_barinel.drop(['Faulty_Line'],1,inplace=True)
t_barinel=df_barinel.values.tolist()
rank_barinel=np.array(t_barinel)
rank_barinel=rank_barinel.tolist()
#print rank_barinel

df_barinel_m=pd.read_csv('Barinel_m.csv')
fl=np.array(df_barinel_m['Faulty_Line']).T
fl=fl.tolist()
#print fl
df_barinel_m.drop(['Faulty_Line'],1,inplace=True)
t_barinel_m=df_barinel_m.values.tolist()
rank_barinel_m=np.array(t_barinel_m)
rank_barinel_m=rank_barinel_m.tolist()
#print rank_barinel_m


suspicious_barinel=[[0 for i in range(len(fl))] for j in range(len(versions))]

for i in range(len(versions)):
	for j in range(len(fl)):
		#print (i,j)
		tau, p_value = stats.kendalltau(rank_barinel[i],rank_barinel_m[j])
		if math.isnan(tau)==True :
			suspicious_barinel[i][j]=0		
		else :
			suspicious_barinel[i][j]=tau

#print suspicious_barinel
#print np.array(suspicious_barinel)
#----------------------------Barinel-----------------------------------#


#----------------------------bpnn--------------------------------#

df_bpnn=pd.read_csv('bpnn.csv')
versions=np.array(df_bpnn['Faulty_Line']).T
versions=versions.tolist()
#print versions
df_bpnn.drop(['Faulty_Line'],1,inplace=True)
t_bpnn=df_bpnn.values.tolist()
rank_bpnn=np.array(t_bpnn)
rank_bpnn=rank_bpnn.tolist()
#print rank_bpnn

df_bpnn_m=pd.read_csv('bpnn_m.csv')
fl=np.array(df_bpnn_m['Faulty_Line']).T
fl=fl.tolist()
#print fl
df_bpnn_m.drop(['Faulty_Line'],1,inplace=True)
t_bpnn_m=df_bpnn_m.values.tolist()
rank_bpnn_m=np.array(t_bpnn_m)
rank_bpnn_m=rank_bpnn_m.tolist()
#print rank_bpnn_m


suspicious_bpnn=[[0 for i in range(len(fl))] for j in range(len(versions))]

for i in range(len(versions)):
	for j in range(len(fl)):
		tau, p_value = stats.kendalltau(rank_bpnn[i],rank_bpnn_m[j])
		if math.isnan(tau)==True :
			suspicious_bpnn[i][j]=0		
		else :
			suspicious_bpnn[i][j]=tau

#print suspicious_bpnn
#print np.array(suspicious_bpnn)
#----------------------------bpnn----------------------------------#


#----------------------------cnn--------------------------------#

df_cnn=pd.read_csv('cnn.csv')
versions=np.array(df_cnn['Faulty_Line']).T
versions=versions.tolist()
#print versions
df_cnn.drop(['Faulty_Line'],1,inplace=True)
t_cnn=df_cnn.values.tolist()
rank_cnn=np.array(t_cnn)
rank_cnn=rank_cnn.tolist()
#print rank_cnn

df_cnn_m=pd.read_csv('cnn_m.csv')
fl=np.array(df_cnn_m['Faulty_Line']).T
fl=fl.tolist()
#print fl
df_cnn_m.drop(['Faulty_Line'],1,inplace=True)
t_cnn_m=df_cnn_m.values.tolist()
rank_cnn_m=np.array(t_cnn_m)
rank_cnn_m=rank_cnn_m.tolist()
#print rank_cnn_m


suspicious_cnn=[[0 for i in range(len(fl))] for j in range(len(versions))]

for i in range(len(versions)):
	for j in range(len(fl)):
		tau, p_value = stats.kendalltau(rank_cnn[i],rank_cnn_m[j])
		if math.isnan(tau)==True :
			suspicious_cnn[i][j]=0		
		else :
			suspicious_cnn[i][j]=tau

#print suspicious_cnn
#print np.array(suspicious_cnn)
#----------------------------cnn----------------------------------#


#----------------------------crosstab--------------------------------#

df_crosstab=pd.read_csv('Crosstab.csv')
versions=np.array(df_crosstab['Faulty_Line']).T
versions=versions.tolist()
#print versions
df_crosstab.drop(['Faulty_Line'],1,inplace=True)
t_crosstab=df_crosstab.values.tolist()
rank_crosstab=np.array(t_crosstab)
rank_crosstab=rank_crosstab.tolist()
#print rank_crosstab

df_crosstab_m=pd.read_csv('Crosstab_m.csv')
fl=np.array(df_crosstab_m['Faulty_Line']).T
fl=fl.tolist()
#print fl
df_crosstab_m.drop(['Faulty_Line'],1,inplace=True)
t_crosstab_m=df_crosstab_m.values.tolist()
rank_crosstab_m=np.array(t_crosstab_m)
rank_crosstab_m=rank_crosstab_m.tolist()
#print rank_crosstab_m


suspicious_crosstab=[[0 for i in range(len(fl))] for j in range(len(versions))]

for i in range(len(versions)):
	for j in range(len(fl)):
		tau, p_value = stats.kendalltau(rank_crosstab[i],rank_crosstab_m[j])
		if math.isnan(tau)==True :
			suspicious_crosstab[i][j]=0		
		else :
			suspicious_crosstab[i][j]=tau

#print suspicious_crosstab
#print np.array(suspicious_crosstab)
#----------------------------crosstab----------------------------------#


#----------------------------dnn--------------------------------#

df_dnn=pd.read_csv('dnn.csv')
versions=np.array(df_dnn['Faulty_Line']).T
versions=versions.tolist()
#print versions
df_dnn.drop(['Faulty_Line'],1,inplace=True)
t_dnn=df_dnn.values.tolist()
rank_dnn=np.array(t_dnn)
rank_dnn=rank_dnn.tolist()
#print rank_dnn

df_dnn_m=pd.read_csv('dnn_m.csv')
fl=np.array(df_dnn_m['Faulty_Line']).T
fl=fl.tolist()
#print fl
df_dnn_m.drop(['Faulty_Line'],1,inplace=True)
t_dnn_m=df_dnn_m.values.tolist()
rank_dnn_m=np.array(t_dnn_m)
rank_dnn_m=rank_dnn_m.tolist()
#print rank_dnn_m


suspicious_dnn=[[0 for i in range(len(fl))] for j in range(len(versions))]

for i in range(len(versions)):
	for j in range(len(fl)):
		tau, p_value = stats.kendalltau(rank_dnn[i],rank_dnn_m[j])
		if math.isnan(tau)==True :
			suspicious_dnn[i][j]=0		
		else :
			suspicious_dnn[i][j]=tau

#print suspicious_dnn
#print np.array(suspicious_dnn)
#----------------------------dnn----------------------------------#


#----------------------------dstar--------------------------------#

df_dstar=pd.read_csv('DStar.csv')
versions=np.array(df_dstar['Faulty_Line']).T
versions=versions.tolist()
#print versions
df_dstar.drop(['Faulty_Line'],1,inplace=True)
t_dstar=df_dstar.values.tolist()
rank_dstar=np.array(t_dstar)
rank_dstar=rank_dstar.tolist()
#print rank_dstar

df_dstar_m=pd.read_csv('DStar_m.csv')
fl=np.array(df_dstar_m['Faulty_Line']).T
fl=fl.tolist()
#print fl
df_dstar_m.drop(['Faulty_Line'],1,inplace=True)
t_dstar_m=df_dstar_m.values.tolist()
rank_dstar_m=np.array(t_dstar_m)
rank_dstar_m=rank_dstar_m.tolist()
#print rank_dstar_m


suspicious_dstar=[[0 for i in range(len(fl))] for j in range(len(versions))]

for i in range(len(versions)):
	for j in range(len(fl)):
		tau, p_value = stats.kendalltau(rank_dstar[i],rank_dstar_m[j])
		if math.isnan(tau)==True :
			suspicious_dstar[i][j]=0		
		else :
			suspicious_dstar[i][j]=tau

#print suspicious_dstar
#print np.array(suspicious_dstar)
#----------------------------dstar----------------------------------#


#----------------------------ochiai--------------------------------#

df_ochiai=pd.read_csv('Ochiai.csv')
versions=np.array(df_ochiai['Faulty_Line']).T
versions=versions.tolist()
#print versions
df_ochiai.drop(['Faulty_Line'],1,inplace=True)
t_ochiai=df_ochiai.values.tolist()
rank_ochiai=np.array(t_ochiai)
rank_ochiai=rank_ochiai.tolist()
#print rank_ochiai

df_ochiai_m=pd.read_csv('Ochiai_m.csv')
fl=np.array(df_ochiai_m['Faulty_Line']).T
fl=fl.tolist()
#print fl
df_ochiai_m.drop(['Faulty_Line'],1,inplace=True)
t_ochiai_m=df_ochiai_m.values.tolist()
rank_ochiai_m=np.array(t_ochiai_m)
rank_ochiai_m=rank_ochiai_m.tolist()
#print rank_ochiai_m


suspicious_ochiai=[[0 for i in range(len(fl))] for j in range(len(versions))]

for i in range(len(versions)):
	for j in range(len(fl)):
		tau, p_value = stats.kendalltau(rank_ochiai[i],rank_ochiai_m[j])
		if math.isnan(tau)==True :
			suspicious_ochiai[i][j]=0		
		else :
			suspicious_ochiai[i][j]=tau

#print suspicious_ochiai
#print np.array(suspicious_ochiai)
#----------------------------ochiai----------------------------------#



#----------------------------rbfnn--------------------------------#

df_rbfnn=pd.read_csv('rbfnn.csv')
versions=np.array(df_rbfnn['Faulty_Line']).T
versions=versions.tolist()
#print versions
df_rbfnn.drop(['Faulty_Line'],1,inplace=True)
t_rbfnn=df_rbfnn.values.tolist()
rank_rbfnn=np.array(t_rbfnn)
rank_rbfnn=rank_rbfnn.tolist()
#print rank_rbfnn

df_rbfnn_m=pd.read_csv('rbfnn_m.csv')
fl=np.array(df_rbfnn_m['Faulty_Line']).T
fl=fl.tolist()
#print fl
df_rbfnn_m.drop(['Faulty_Line'],1,inplace=True)
t_rbfnn_m=df_rbfnn_m.values.tolist()
rank_rbfnn_m=np.array(t_rbfnn_m)
rank_rbfnn_m=rank_rbfnn_m.tolist()
#print rank_rbfnn_m


suspicious_rbfnn=[[0 for i in range(len(fl))] for j in range(len(versions))]

for i in range(len(versions)):
	for j in range(len(fl)):
		tau, p_value = stats.kendalltau(rank_rbfnn[i],rank_rbfnn_m[j])
		if math.isnan(tau)==True :
			suspicious_rbfnn[i][j]=0		
		else :
			suspicious_rbfnn[i][j]=tau

#print suspicious_rbfnn
#print np.array(suspicious_rbfnn)
#----------------------------rbfnn----------------------------------#



#----------------------------tarantula--------------------------------#

df_tarantula=pd.read_csv('tarantula.csv')
versions=np.array(df_tarantula['Faulty_Line']).T
versions=versions.tolist()
#print versions
df_tarantula.drop(['Faulty_Line'],1,inplace=True)
t_tarantula=df_tarantula.values.tolist()
rank_tarantula=np.array(t_tarantula)
rank_tarantula=rank_tarantula.tolist()
#print rank_tarantula

df_tarantula_m=pd.read_csv('tarantula_m.csv')
fl=np.array(df_tarantula_m['Faulty_Line']).T
fl=fl.tolist()
#print fl
df_tarantula_m.drop(['Faulty_Line'],1,inplace=True)
t_tarantula_m=df_tarantula_m.values.tolist()
rank_tarantula_m=np.array(t_tarantula_m)
rank_tarantula_m=rank_tarantula_m.tolist()
#print rank_tarantula_m


suspicious_tarantula=[[0 for i in range(len(fl))] for j in range(len(versions))]

for i in range(len(versions)):
	for j in range(len(fl)):
		tau, p_value = stats.kendalltau(rank_tarantula[i],rank_tarantula_m[j])
		if math.isnan(tau)==True :
			suspicious_tarantula[i][j]=0		
		else :
			suspicious_tarantula[i][j]=tau

#print suspicious_tarantula
#print np.array(suspicious_tarantula)
#----------------------------tarantula----------------------------------#


suspicious_min=[[0 for i in range(len(fl))] for j in range(len(versions))]

for i in range(len(versions)):
	for j in range(len(fl)):
		x = min(suspicious_ample[i][j],suspicious_barinel[i][j],suspicious_bpnn[i][j],suspicious_cnn[i][j],suspicious_crosstab[i][j],suspicious_dnn[i][j],suspicious_dstar[i][j],suspicious_ochiai[i][j],suspicious_rbfnn[i][j],suspicious_tarantula[i][j])
		suspicious_min[i][j]=x


suspicious_max=[[0 for i in range(len(fl))] for j in range(len(versions))]

for i in range(len(versions)):
	for j in range(len(fl)):
		x = max(suspicious_ample[i][j],suspicious_barinel[i][j],suspicious_bpnn[i][j],suspicious_cnn[i][j],suspicious_crosstab[i][j],suspicious_dnn[i][j],suspicious_dstar[i][j],suspicious_ochiai[i][j],suspicious_rbfnn[i][j],suspicious_tarantula[i][j])
		suspicious_max[i][j]=x


suspicious_avg=[[0 for i in range(len(fl))] for j in range(len(versions))]

for i in range(len(versions)):
	for j in range(len(fl)):
		x = (suspicious_ample[i][j]+suspicious_barinel[i][j]+suspicious_bpnn[i][j]+suspicious_cnn[i][j]+suspicious_crosstab[i][j]+suspicious_dnn[i][j]+suspicious_dstar[i][j]+suspicious_ochiai[i][j]+suspicious_rbfnn[i][j]+suspicious_tarantula[i][j])/10.0
		suspicious_avg[i][j]=x


for i in range(len(fl)):
	fl[i]=int(fl[i])-1

f_susp_min=[[0 for i in range(len(rank_tarantula_m[0]))] for j in range(len(versions))]

for i in range(len(versions)):
	d = {}
	for j in range(len(fl)):
		key = int(fl[j])
		#print key
		if key not in d:
			d[key] = []
		d[key].append(suspicious_min[i][j])
	
	for j in range(len(rank_tarantula_m[0])):
		if j not in d:
			f_susp_min[i][j]=-1
		else:
			f_susp_min[i][j]=max(d[j])

#print f_susp_min

f_susp_max=[[0 for i in range(len(rank_tarantula_m[0]))] for j in range(len(versions))]

for i in range(len(versions)):
	d = {}
	for j in range(len(fl)):
		key = int(fl[j])
		#print key
		if key not in d:
			d[key] = []
		d[key].append(suspicious_max[i][j])

	for j in range(len(rank_tarantula_m[0])):
		if j not in d:
			f_susp_max[i][j]=-1
		else:
			f_susp_max[i][j]=max(d[j])

#print f_susp_max


f_susp_avg=[[0 for i in range(len(rank_tarantula_m[0]))] for j in range(len(versions))]

for i in range(len(versions)):
	d = {}
	for j in range(len(fl)):
		key = int(fl[j])
		#print key
		if key not in d:
			d[key] = []
		d[key].append(suspicious_avg[i][j])

	for j in range(len(rank_tarantula_m[0])):
		if j not in d:
			f_susp_avg[i][j]=-1
		else:
			f_susp_avg[i][j]=max(d[j])

#print f_susp_avg


with open('f_l.csv') as f:
    reader = csv.reader(f, delimiter=',')
    for row in reader:
        faulty_lines=row

print faulty_lines

cwd=os.getcwd()
p=0
i=-1
while i>= (-len(cwd)) :
	if cwd[i]=='/' :
		p=p+1
	if p==1 :
		break
	i=i-1
program=cwd[i+1:]
str_cwd=cwd[:i]


for i in range(len(versions)):
	v=versions[i]
	f_l=int(faulty_lines[i])+1
	d = {}
	for j in range(0,len(f_susp_min[i])):
		key = float(f_susp_min[i][j])
		#print key
		if key not in d:
			d[key] = []
		d[key].append(j)
	
	ct1=0
	ct2=0
	ct3=0
	fct=0
	print("Faulty line:"+str(f_l))
	for x in sorted(d):
		#print (x,len(d[x]))
		if f_l not in d[x] and fct==0:
			ct1=ct1+len(d[x])
		elif f_l not in d[x] and fct==1:
			ct3=ct3+len(d[x])
		else: 
			fct=1
			ct2=len(d[x])
	print("We have to search "+str(ct3+1)+" to "+str(ct3+ct2))


	csvfile=open(str_cwd+"/min.csv", "a+")
	spamwriter1 = csv.writer(csvfile, delimiter=',')
	stmt_complex=[]
	stmt_complex.append(program);
	stmt_complex.append(v);
	stmt_complex.append(f_l);
	stmt_complex.append(ct3+1);
	stmt_complex.append(ct2+ct3);
	spamwriter1.writerow(stmt_complex);

for i in range(len(versions)):
	v=versions[i]
	f_l=int(faulty_lines[i])+1
	d = {}
	for j in range(0,len(f_susp_max[i])):
		key = float(f_susp_max[i][j])
		#print key
		if key not in d:
			d[key] = []
		d[key].append(j)

	ct1=0
	ct2=0
	ct3=0
	fct=0
	print("Faulty line:"+str(f_l))
	for x in sorted(d):
		#print (x,len(d[x]))
		if f_l not in d[x] and fct==0:
			ct1=ct1+len(d[x])
		elif f_l not in d[x] and fct==1:
			ct3=ct3+len(d[x])
		else: 
			fct=1
			ct2=len(d[x])
	print("We have to search "+str(ct3+1)+" to "+str(ct3+ct2))


	csvfile=open(str_cwd+"/max.csv", "a+")
	spamwriter1 = csv.writer(csvfile, delimiter=',')
	stmt_complex=[]
	stmt_complex.append(program);
	stmt_complex.append(v);
	stmt_complex.append(f_l);
	stmt_complex.append(ct3+1);
	stmt_complex.append(ct2+ct3);
	spamwriter1.writerow(stmt_complex);


for i in range(len(versions)):
	v=versions[i]
	f_l=int(faulty_lines[i])+1
	d = {}
	for j in range(0,len(f_susp_avg[i])):
		key = float(f_susp_avg[i][j])
		#print key
		if key not in d:
			d[key] = []
		d[key].append(j)

	ct1=0
	ct2=0
	ct3=0
	fct=0
	print("Faulty line:"+str(f_l))
	for x in sorted(d):
		#print (x,len(d[x]))
		if f_l not in d[x] and fct==0:
			ct1=ct1+len(d[x])
		elif f_l not in d[x] and fct==1:
			ct3=ct3+len(d[x])
		else: 
			fct=1
			ct2=len(d[x])
	print("We have to search "+str(ct3+1)+" to "+str(ct3+ct2))


	csvfile=open(str_cwd+"/avg.csv", "a+")
	spamwriter1 = csv.writer(csvfile, delimiter=',')
	stmt_complex=[]
	stmt_complex.append(program);
	stmt_complex.append(v);
	stmt_complex.append(f_l);
	stmt_complex.append(ct3+1);
	stmt_complex.append(ct2+ct3);
	spamwriter1.writerow(stmt_complex);

