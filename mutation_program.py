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


	"<" : 
		[ "!=", ">", "<=", ">=", "==" ],
	">" : 
		[ "!=", "<", "<=", ">=", "=="  ],
	"<=" : 
		[ "!=", "<", ">", ">=",  "==" ],
	">=" : 
		[ "!=", "<", "<=", ">",  "==" ],
	"==" : 
		[ "!=", "<",  ">", "<=", ">=" ],
	"!=" : 
		[ "==", "<",  ">", "<=", ">=" ],


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



	"+" : 
		[ "-", "*", "/", "%" ],
	"-" : 
		[ "+", "*", "/", "%" ],
	"*" : 
		[ "+", "-", "/", "%" ],

	"/" : 
		[ "%", "*", "+", "-" ],
 	"%" : 
		[ "/", "+", "-", "*" ],

	

	" && " : 
		[ " || "," &&! " ," ||! "],

	" || " :
		[ " && ", " ||!" ,"  &&! "],

	" &&! ":
		[ " && ", " || " ," ||! " ],

	" ||! ":
		[ " && ", " || " , " &&! "],



	"&&" : 
		[ "||","&&!" ,"||!"],

	"||" :
		[ "&&", "||!" ,"&&!"],

	"&&!":
		[ "&&", "||" ,"||!" ],

	"||!":
		[ "&&", "||" , "&&!"],



	" += " :
		[" *= "," /= "," -= "],

	" *= " :
		[" += "," /= "," -= "],

	" -= " :
		[" += "," /= "," *= "],

	" /= " :
		[" += "," -= "," *= "],

	" %= " :
		[" += "," /= "," *= "," -= "],
		


	"+=" :
		["*=","/=","-="],

	"*=" :
		["+=","/=","-="],

	"-=" :
		["+=","/=","*="],

	"/=" :
		["+=","-=","*="],

	"%=" :
		["+=","/=","*=","-="],


	" >> " : [" << "],
	" << " : [" >> "],

	">>" : ["<<"],
	"<<" : [">>"],

	"++" : ["--"],
	"--" : ["++"],

	"++;" : 
		[ "--;"],
	"++)" : 
		[ "--)"],
	"--;" : 
		[ "++;"],
	"--)" : 
		[ "++)"],

	"/*" :
		["/*"],
	"*/" :
		["*/"],
	" /*" :
		[" /*"],
	" */" :
		[" */"],

	"//" :
		["//"],
	" // " :
		[" // "],
	

	
}

def main (input_file, output_file ) :
#
	counter = 1

	source_code = open(input_file).read().split('\n')
	source_code_temp = open(input_file).read().split('\n')
	number_of_lines_of_code = len(source_code) 

	
	mutant_operators = mutation_trick.keys()

	for i in range(0,number_of_lines_of_code) :
	
	
		if source_code[i].strip().startswith("#") or source_code[i].strip().startswith("assert") :
			continue

		if source_code[i].strip().startswith("/*") or source_code[i].strip().endswith("assert") :
			continue

		if source_code[i].strip().startswith("//") or source_code[i].strip().endswith("assert") :
			continue

		for m in mutant_operators :
	
	
			number_of_substrings_found = source_code[i].count(m)

			if number_of_substrings_found > 0 :
	
				mutate_at_index = 0 
		
				for r in xrange(1,number_of_substrings_found+1) :
	
					if mutate_at_index == 0 :
						mutate_at_index = source_code[i].index(m)
					else :
						mutate_at_index = source_code[i].index(m,mutate_at_index+1)
	

					for replace_op in mutation_trick[m]:
						mutated_line = ""
						mutate_with = replace_op

						mutated_line = source_code[i][0:mutate_at_index] + source_code[i][mutate_at_index:].replace(m,mutate_with,1)

						with open(output_file+"/Mutant"+str(counter)+".c","w") as output1,open(output_file+"/Mutant_log"+str(counter)+".txt","w") as output2:
							source_code_temp[i]=mutated_line

							output1.write("\n".join(source_code_temp))	
							source_code_temp[i]=source_code[i]

							output2.write("\n==> @ Line: "+str(i+1)+"\n\n")
							output2.write("Original Line  : "+source_code[i].strip()+"\n")
							output2.write("After Mutation : "+mutated_line.strip()+"\n")
							counter = counter+1
	return

def write_to_file ( mutant_file_name, source_code, mutated_line_number, mutated_line ) :
#
	output_file = open(mutant_file_name, "w")

	for i in xrange(0,len(source_code)) :
		if i == mutated_line_number : 
			output_file.write("/* XXX: original code was : "+source_code[i]+" */\n")
			output_file.write(mutated_line+"\n")
		else :
			output_file.write(source_code[i]+"\n")

	output_file.close()
#

if __name__ == "__main__":
#
	if len(sys.argv) == 2: # For testing 
		main(sys.argv[1]) 

	elif len(sys.argv) == 3: 
		assert(sys.argv[1] != sys.argv[2]) # Input file and Output file cannot be same
		main(sys.argv[1],sys.argv[2]) 

	else:
		print ("Usage: python mutate.py <file-to-mutate.c> [output-mutant-file-name.c]")
#