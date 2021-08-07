# Mutator_
Program in python to generate mutans

Class 1 Faults

1. AOR: Arithmetic Operator Replacement(e.g., `+' in place of `-' and vice-versa)
2. LOR: Logical Operator Replacement(e.g., `||' in place of `&&' and vice-versa)
3. ROR: Relational Operator Replacement(e.g., `>' in place of `<' and vice-versa)
4. (I/D)OR: Increment/Decrement Operator Replacement(e.g., `++' in place of `--' and vice-versa)
5. BOR: Bitwise Operator Replacement(e.g., `&' in place of `|' and vice-versa)
6. SOR: Shift Operator Replacement(e.g., `<<' in place of `>>' and vice-versa)
7. AsOR: Assignment Operator Replacement(e.g., `*=' in place of `/=' and vice-versa)

Command to run the python script:
---------------------------------------

python2 mutation_program.py original.c directory_name
-------------------------------------------------------

All Class-1 mutants are saved in "ProgramName_class1_mutants.tar.xz" named directory.


Class 2 Faults

1. SM: Statement Missing
2. SA: Statement Addition
3. SIE: Swapping of `if-else' Statement 
4. VR: Variable Replacement(e.g., `a= b+c' instead of `a=d+c')
5. SI: Sign Inversion(e.g., `a= b' instead of `a=-b' and vice-versa)
6. RSR: `return' Statement Replacement(e.g., `return(1)' instead of `return(0)' and vice-versa)
7. CBR: `continue' Replacement by `break' and vice-versa
8. SWCR: `switch-case' Statement Mutation
    
Manually created Class-2 mutants are stored in "ProgramName_class2_mutants.tar.xz" named directory.



