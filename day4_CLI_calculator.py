a=int(input("Enter first number: "))
b=int(input("Enter second number: "))
o = input("Enter Operator: ")
if (o=='/' and b==0):
    raise ZeroDivisionError("Dividend can't be zero")
match o:
    case '+':
        print (f"{a} + {b} = {a+b}")
        
    case '-':
        print (f"{a} - {b} = {a-b}")
       
    case '*':
        print (f"{a} * {b} = {a*b}")
        
    case '/':
        print (f"{a} / {b} = {a/b}")
        
    case _:
        print("Enter Valid Input")
