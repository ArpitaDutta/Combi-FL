# Latest version 13/09/2020

import os
import re
import sys
import random



NULL_STRING = " "

mutation_trick = {
	" < " : 
		[ " != ", " > ", " <= ", " >= ", " == " ],
	" > " : 
		[ " != ", " < ", " <= ", " >= ", " == "  ],
	" <= " : 
		[ " != ", " < ", " > ", " >= ",  "==" ],
	" >= " : 
		[ " != ", " < ", " <= ", " > ",  "==" ],
	" == " : 
		[ " != ", " < ",  " > ", " <= ", " >= " ],
	" != " : 
		[ " == ", " < ",  " > ", " <= ", " >= " ],



	" + " : 
		[ " - ", " * ", " / ", " % " ],
	" - " : 
		[ " + ", " * ", " / ", " % " ],
	" * " : 
		[ " + ", " - ", " / ", " % " ],

	" / " : 
		[ " % ", " * ", " + ", " - " ],
 	" % " : 
		[ " / ", " + ", " - ", " * " ],

	" && " : 
		[ " || "],

	" || " :
		[ " && "],

	

}

def findnth(haystack, needle, n):
    parts= haystack.split(needle, n+1)
    if len(parts)<=n+1:
        return -1
    return len(haystack)-len(parts[-1])-len(needle)



def main (input_file, output_file ) :

	#--------------Check whether directory exits or not-----
	#os.system("[ -d "+output_file+" ] && echo Already directory exists!!!!")
	#os.system("echo Enter Y/y to re-write on the same directory or N/n to enter New Directory Name which doesnot exists")
	#os.system(read varname)
	os.system("mkdir "+str(output_file))
	c_n=0 # It contains the condition number
	p_n=0 # It contains the predicate number
	counter = 1

	source_code = open(input_file).read().split('\n')
	source_code_temp = open(input_file).read().split('\n')
	number_of_lines_of_code = len(source_code) 
	
	
	#---------------------------
	ano_log_file = open(output_file+"/Orig_log_file.txt", "w") 
	types_faults=open(output_file+"/Types_of_faults_log.txt", "w") 
	LOF=0
	ROF=0
	AOF=0
	PNF=0
	LNF=0


	mutant_operators = mutation_trick.keys()

	for i in range(0,number_of_lines_of_code) :
		flag_p=0
	
		if source_code[i].strip().startswith("#") or source_code[i].strip().startswith("assert") :
			continue

		if source_code[i].strip().startswith("/*") or source_code[i].strip().endswith("assert") :
			continue

		if source_code[i].strip().startswith("//") or source_code[i].strip().endswith("assert") :
			continue
		if "if(" in source_code[i] or "if (" in source_code[i] or "for (" in source_code[i] or "for(" in source_code[i] or "while (" in source_code[i] or "while(" in source_code[i]:
			p_n=p_n+1
			flag_p=1
		else:
			flag_p=0
		
		#print(len(mutant_operators))
		#cond_present=0 # This variable will help to count the number of relational operators present
		if flag_p==1:
			if "&&" not in source_code[i] and "||" not in source_code[i]:
				c_n=c_n+1
		pnf=0  #it will show either the mutant for pnf is created or not
		#-------------SNF Statement/ Predicate negation faults------------------------------------------
				
		if flag_p==1 and pnf==0:
			
			mutated_line = ""
		
			#print(source_code[i])
			if "if (" in source_code[i] or "if(" in source_code[i] or "while (" in source_code[i] or "while(" in source_code[i]:
				ind1= source_code[i].rindex(")")
				ind2= source_code[i].index("(")
				#print(source_code[i])
				mutated_line= source_code[i][0:ind2+1]+"!("+source_code[i][ind2+1: ind1]+")"+source_code[i][ind1:]
				#print(mutated_line)
				pnf=1
			elif "for (" in source_code[i] or "for(" in source_code[i]:
				ind1= source_code[i].rindex(";")
				ind2= source_code[i].index(";")
				#print(source_code[i])
				mutated_line= source_code[i][0:ind2+1]+"!("+source_code[i][ind2+1: ind1]+")"+source_code[i][ind1:]
				#print(mutated_line)
				pnf=1
			else:
				continue
			mutant_file=output_file+"/PNF_Line_"+str(i+1)+"_Pred_"+str(p_n)+"_Cond_"+str("PNF")+"_Mutant"+str(counter)+".c"
			mutant_log_file=output_file+"/PNF_Line_"+str(i+1)+"_Pred_"+str(p_n)+"_Cond_"+str("PNF")+"_Mutant_log"+str(counter)+".txt"
			ano_log_file.write("PNF_Line_"+str(i+1)+"_Pred_"+str(p_n)+"_Cond_"+str("PNF")+"_Mutant"+str(counter)+"\n")
			PNF=PNF+1
			#If I am maintaing the condition number then the predicates with more than 1 conditions are getting assigned with the wrong index
			with open(mutant_file,"w") as output3,open(mutant_log_file,"w") as output4:
				source_code_temp[i]=mutated_line

				output3.write("\n".join(source_code_temp))	
				source_code_temp[i]=source_code[i]
				
				ano_log_file.write("\n==> @ Line: "+str(i+1)+"\n")
				ano_log_file.write("Original Line  : "+source_code[i].strip()+"\n")
				ano_log_file.write("After Mutation : "+mutated_line.strip()+"\n\n\n")
				output4.write("\n==> @ Line: "+str(i+1)+"\n\n")
				output4.write("Original Line  : "+source_code[i].strip()+"\n")
				output4.write("After Mutation : "+mutated_line.strip()+"\n")
				counter = counter+1

#------------------------------------------------------------------------------------------------------	

#-------------VNF variable/literal/ condition negation faults------------------------------------------
		if flag_p==1:
			mutated_line = ""
			if "if (" in source_code[i] or "if(" in source_code[i] or "while (" in source_code[i] or "while(" in source_code[i]:
				ind1= source_code[i].index("(")
				ind2= source_code[i].rindex(")")
			elif "for (" in source_code[i] or "for(" in source_code[i]:
				ind1= source_code[i].index(";")
				ind2= source_code[i].rindex(";")
		
			ext_pred=source_code[i][ind1+1:ind2]
			vnf1=[]
			#print("..."+str(source_code[i]))
			if "&&" in ext_pred or "||" in ext_pred:
				#print(ext_pred)
				vnf1=ext_pred.replace("||","&&").split("&&")
				vnf2=vnf1
				#print(vnf1)
				cvnf_c=0
				count_take=0
			for vn1 in vnf1:
				count_take=count_take+1
				cvnf_c=cvnf_c+1
				mod_act1=vn1.replace("!=","=neg=").replace("(","").replace(")","").replace("!","")
				mod_act1=mod_act1.replace("=neg=","!=")
				#print(ext_pred)
				#print("mod_act1:",mod_act1)
				css=str(ext_pred).count(str(mod_act1.strip()))
				#print("Susbstring", css)
				#print("line: "+str(line))
				#print("mod_act1: "+str(mod_act1))
				count_occur=0
				if (count_take>1):
					for it in range(0,count_take-1):
						#print("....",vnf1[it])
						if mod_act1.strip() in vnf1[it]:
							count_occur=count_occur+1
				inx1=findnth(source_code[i], str(mod_act1.strip()), count_occur)
				#inx1=source_code[i].index(str(mod_act1.strip()))
				inx2=inx1+len(mod_act1.strip())
				mod_act=vn1.replace("!=","=neg=").replace("(int )", "int_cast_type").replace("(int)", "int_cast_type1").replace("(","").replace(")","").replace("!","")
				
				mod_lnv="!("+mod_act+")"
				#print(mod_lnv)
				mod_lnv=mod_lnv.replace("=neg=", "!=").replace("int_cast_type","(int )").replace("int_cast_type1", "(int)")
				#print(mod_lnv)
				#print (line[:inx1])
				#print (mod_lnv)
				#print (line[inx2-1:])
				line1=source_code[i][:inx1]+mod_lnv+source_code[i][inx2:]
				#print("***************")
				#print(line1)
				mutated_line=line1
				LNF=LNF+1
				mutant_file=output_file+"/CNF_Line_"+str(i+1)+"_Pred_"+str(p_n)+"_Cond_"+str(c_n+cvnf_c)+"_Mutant"+str(counter)+".c"
				mutant_log_file=output_file+"/CNF_Line_"+str(i+1)+"_Pred_"+str(p_n)+"_Cond_"+str(c_n+cvnf_c)+"_Mutant_log"+str(counter)+".txt"
				ano_log_file.write("CNF_Line_"+str(i+1)+"_Pred_"+str(p_n)+"_Cond_"+str(c_n+cvnf_c)+"_Mutant"+str(counter)+"\n")
				with open(mutant_file,"w") as output3,open(mutant_log_file,"w") as output4:
					source_code_temp[i]=mutated_line

					output3.write("\n".join(source_code_temp))	
					source_code_temp[i]=source_code[i]
					
					
					ano_log_file.write("\n==> @ Line: "+str(i+1)+"\n")
					ano_log_file.write("Original Line  : "+source_code[i].strip()+"\n")
					ano_log_file.write("After Mutation : "+mutated_line.strip()+"\n\n\n")

					output4.write("\n==> @ Line: "+str(i+1)+"\n\n")
					output4.write("Original Line  : "+source_code[i].strip()+"\n")
					output4.write("After Mutation : "+mutated_line.strip()+"\n")
					counter = counter+1	
#------------------------------------------------------------------------------------------


		for m in mutant_operators :
	
	
			number_of_substrings_found = source_code[i].count(m)
			
				

			if number_of_substrings_found > 0 :
	
				mutate_at_index = 0 
		
				for r in range(1,number_of_substrings_found+1) :

			
					if mutate_at_index == 0 :
						mutate_at_index = source_code[i].index(m)
					else :
						mutate_at_index = source_code[i].index(m,mutate_at_index+1)
	

					for replace_op in mutation_trick[m]:
						mutated_line = ""
						mutate_with = replace_op

						mutated_line = source_code[i][0:mutate_at_index] + source_code[i][mutate_at_index:].replace(m,mutate_with,1)
						#print(mutated_line)
						keep1=[]
						keep2=[]

						cond_change=0
						cond_num=0
						cd_count=0

						if "&&" in mutated_line or "||" in mutated_line:
							k1=mutated_line.split("||")
							#print("mutated_line", mutated_line)
							#print("k1..", k1)
							if "&&" in mutated_line:
								for k2 in k1:
									if "&&" in k2:
										kn2=k2.split("&&")
										#print("kn21 ", kn2)
										for knn in kn2:
											keep1.append(knn)
									else:
										keep1.append(k2)
							else: 
								keep1=k1


							k3=source_code[i].split("||")
							#print("k3..", k3)
							#print("sc....",source_code[i])
							if "&&" in source_code[i]:
								for k4 in k3:
									if "&&" in k4:
										kn2=k4.split("&&")
										#print("kn22 ", kn2)
										for knn in kn2:
											keep2.append(knn)
									else:
										keep2.append(k4)
							else:
								keep2=k3

							#print("keep1"+str(keep1))
							#print("keep2"+str(keep2))
							#print(len(keep2[0]), "   ", keep2[0])
							#print(len(keep1[0]), "   ", keep1[0])
							#print("......................")
							#print(mutated_line)
							for k5 in range(0, len(keep2[0])):
								#print(" keep1[0][k5]!= keep2[0][k5]"+str( keep1[0][k5])+"    "+str( keep2[0][k5]))
								str1=str(keep1[0][k5])
								str2=str(keep2[0][k5])
								if str1!= str2:
									cond_change=1
									cd_count=cd_count+1
									#print("k5:"+str(k5))
									cond_num=k5+1
									break;		
							
						#print("condnum: "+str(cond_num))
						#print("cd_count: "+str(cd_count))
						#print("counter")
						#print(counter)	
						#print("Replacement_operator")	
						#print(replace_op)
						rep_op=""
						if "+" in replace_op or "-" in replace_op or "*" in replace_op or "/" in replace_op or "%" in replace_op:
							rep_op="AOF"
							AOF=AOF+1
						elif "<=" in replace_op or "<" in replace_op or ">=" in replace_op or ">" in replace_op or "==" in replace_op or "!=" in replace_op:
							rep_op="ROF"
							ROF=ROF+1
						elif "&&" in replace_op or "||" in replace_op:
							rep_op="LOF"
							LOF=LOF+1

						if flag_p==1 and ("&&" not in replace_op and "||" not in replace_op) and ("&&" in mutated_line or "||" in mutated_line) :
							mutant_file=output_file+"/"+rep_op+"_Line_"+str(i+1)+"_Pred_"+str(p_n)+"_Cond_"+str(c_n+cond_num)+"_Mutant"+str(counter)+".c"
							mutant_log_file=output_file+"/"+rep_op+"_Line_"+str(i+1)+"_Pred_"+str(p_n)+"_Cond_"+str(c_n+cond_num)+"_Mutant_log"+str(counter)+".txt"
							ano_log_file.write(rep_op+"_Line_"+str(i+1)+"_Pred_"+str(p_n)+"_Cond_"+str(c_n+cond_num)+"_Mutant"+str(counter)+"\n")
						elif flag_p==1 and "&&" not in mutated_line and "||" not in mutated_line:
							mutant_file=output_file+"/"+rep_op+"_Line_"+str(i+1)+"_Pred_"+str(p_n)+"_Cond_"+str(c_n)+"_Mutant"+str(counter)+".c"
							mutant_log_file=output_file+"/"+rep_op+"_Line_"+str(i+1)+"_Pred_"+str(p_n)+"_Cond_"+str(c_n)+"_Mutant_log"+str(counter)+".txt"
							ano_log_file.write("Line_"+str(i+1)+"_Pred_"+str(p_n)+"_Cond_"+str(c_n)+"_Mutant"+str(counter)+"\n")
						elif flag_p==1 and ("&&"  in replace_op or "||"  in replace_op):
							mutant_file=output_file+"/"+rep_op+"_Line_"+str(i+1)+"_Pred_"+str(p_n)+"_Cond_NOC_Mutant"+str(counter)+".c"
							mutant_log_file=output_file+"/"+rep_op+"_Line_"+str(i+1)+"_Pred_"+str(p_n)+"_Cond_NOC_Mutant_log"+str(counter)+".txt"
							ano_log_file.write(rep_op+"_Line_"+str(i+1)+"_Pred_"+str(p_n)+"_Cond_NOC_Mutant"+str(counter)+"\n")					
						else:
							mutant_file=output_file+"/"+rep_op+"_Line_"+str(i+1)+"_Pred_"+str("NO")+"_Mutant"+str(counter)+".c"
							mutant_log_file=output_file+"/"+rep_op+"_Line_"+str(i+1)+"_Pred_"+str("NO")+"_Mutant_log"+str(counter)+".txt"
							ano_log_file.write(rep_op+"Line_"+str(i+1)+"_Pred_"+str("NO")+"_Mutant"+str(counter)+"\n")					
		

						with open(mutant_file,"w") as output1,open(mutant_log_file,"w") as output2:
							source_code_temp[i]=mutated_line

							output1.write("\n".join(source_code_temp))	
							source_code_temp[i]=source_code[i]

							ano_log_file.write("\n==> @ Line: "+str(i+1)+"\n")
							ano_log_file.write("Original Line  : "+source_code[i].strip()+"\n")
							ano_log_file.write("After Mutation : "+mutated_line.strip()+"\n\n\n")

							output2.write("\n==> @ Line: "+str(i+1)+"\n\n")
							output2.write("Original Line  : "+source_code[i].strip()+"\n")
							output2.write("After Mutation : "+mutated_line.strip()+"\n")
							counter = counter+1
		if "&&" in source_code[i] or "||" in source_code[i]:
			ct=source_code[i].split("&&")
			ct2=[]
			for ct1 in ct:
				ct2.append(ct1.split("||"))
			c_n=c_n+len(ct2)
				
	types_faults.write("Logical Operator Faults: "+str(LOF)+"\n")
	types_faults.write("Arithmetic Operator Faults: "+str(AOF)+"\n")
	types_faults.write("Relational Operator Faults: "+str(ROF)+"\n")
	types_faults.write("Literal Negation Faults: "+str(LNF)+"\n")
	types_faults.write("Predicate Negation Faults: "+str(PNF)+"\n")		
	return

def write_to_file ( mutant_file_name, source_code, mutated_line_number, mutated_line ) :
#
	output_file = open(mutant_file_name, "w")

	for i in range(0,len(source_code)) :
		if i == mutated_line_number : 
			output_file.write("/* XXX: original code was : "+source_code[i]+" */\n")
			output_file.write(mutated_line+"\n")
		else :
			output_file.write(source_code[i]+"\n")

	output_file.close()
#

if __name__ == "__main__":
#
	
	print("--------------------------")
	if len(sys.argv) == 2: # For testing 
		#os.system("indent sys.argv[1] -o program.c")
		main(sys.argv[1]) 

	elif len(sys.argv) == 3: 
		assert(sys.argv[1] != sys.argv[2]) # Input file and Output file cannot be same
		#main(sys.argv[1],sys.argv[2])
		#print(sys.argv[1])
		#print("indent "+sys.argv[1]+" -o program.c")
		#os.system("indent "+sys.argv[1]+" -o program.c")
		main(sys.argv[1],sys.argv[2])  

	else:
		print ("Usage: python mutator.py <file-to-mutate.c> [output-directory-name.c]")
#
