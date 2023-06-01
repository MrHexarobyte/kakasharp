count = 0
# open file
file1 = open('kakascript.txt', 'r')
Lines = file1.readlines()
#
for line in Lines:
    code = line.strip()
    #   VARIABLE ASSIGNMENT
    if "is" in code and code.endswith('.'): 
        count += 1
        n3 = code.replace('.','') 
        n4 = n3.replace('is','') 
        n5 = n4.split()
        exec(n5[0]+'='+n5[1])
    #   IF CONDITION
    if "(" in code and code.endswith(')'): 
        n1 = code.replace('(','') 
        n2 = n1.replace(')','') 
        n6 = n2.replace('is','') 
        n7= n6.split()
        exec('if '+n7[0]+'=='+n7[1]+': print("THE ARGUMENT IS TRUE")')
        exec('if '+n7[0]+'!='+n7[1]+': print("THE ARGUMENT IS WRONG")')
