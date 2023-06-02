
# open file
file1 = open('kakascript.txt', 'r')
Lines = file1.readlines()
# find lines

def handleCMD(cmd,at1='0',at2='0'):
    if cmd == '#say':
        return 'print("'+at1+'")'
    if cmd == '#laka':
        return 'print("'+(at1+at2)+'")'


for line in Lines:
    code = line.strip()
    #   VARIABLE ASSIGNMENT
    if "is" in code and code.endswith('.'): 
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
        # EXECUTING COMMANDS
        if len(n7) == 5:
            exec('if '+n7[0]+'=='+n7[1]+': '+handleCMD( n7[2] , n7[3] ,n7[4] ))
        elif len(n7) == 4:
            exec('if '+n7[0]+'=='+n7[1]+': '+handleCMD( n7[2] , n7[3] ))
