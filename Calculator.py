# miniproject
#calculator

num1=int(input("enter your first number: "))
operator=input("Enter oepration (+,-,/,x): ")
num2=int(input("Enter your second number: "))

if(operator=="/"):
    if(num1>num2):
        print(num1/num2)
    else:
        print(num2/num1)
elif(operator=='-'):
    if(num1>num2):
        print(num1-num2)
    else:
        print(num2-num1)
elif(operator=='*'):
    print(num1*num2)
else:
    print(num1+num2)