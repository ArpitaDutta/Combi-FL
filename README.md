# Mutator_
Program in python to generate mutans

Class 1 Faults

    1. Arithmetic operator replacement(e.g., `+' in place of `-' and vice-versa)
	2. Logical operator replacement(e.g., `||' in place of `&&' and vice-versa)
	3. Relational operator replacement(e.g., `>' in place of `<' and vice-versa)
	4. Increment/ Decrement operator replacement(e.g., `++' in place of `--' and vice-versa)
	5. Bitwise operator  replacement(e.g., `&' in place of `|' and vice-versa)
	6. Shift operator replacement(e.g., `<<' in place of `>>' and vice-versa)
	7. Assignment  operator replacement(e.g., `*=' in place of `/=' and vice-versa)

Command to run the python script:
---------------------------------------

python2 mutation_program.py original.c directory_name
-------------------------------------------------------

All Class-1 mutants are saved in "ProgramName_class1_mutants.tar.xz" named directory.


Class 2 Faults

	1. Statement missing (e.g., delete the else part in an `if-else' statement)
	2. Statement addition (e.g., addition of the else part in an `if-else' statement)
	3. Swapping of `if-else' statement 
	4. Variable replacement(e.g., `a= b+c' instead of `a=d+c')
	5. Sign inversion(e.g., `a= b' instead of `a=-b' and vice-versa)
	6. `return' Statement Replacement(e.g., `return(1)' instead of `return(0)' and vice-versa)
	7. `continue' Replacement by `break' and vice-versa
	8. `switch-case' Statement Mutation
	9.  Replacement of a operand with a constant value.
    
Manually created Class-2 mutants are stored in "ProgramName_class2_mutants.tar.xz" named directory.
