A = input('Enter your Operator: ')

op1 = int(input('Enter First Operand: '))
op2 = int(input('Enter Second Operand: '))

if A == "+":
    if op1 == 56 and op2 == 4:
        print('77')
    else:
        print("Sum is: ",op1+op2)
        
if A == "-":
    print("Subtract is: ",op1-op2)
    
if A == "*":
    if op1 == 45 and op2 == 3:
        print('555')
    else:
        print("Multiply is: ",op1*op2)
        
if A == "/":
    if op1 == 56 and op2 == 6:
        print("4")
    else:
        print("Divide is:",float(op1/op2))
