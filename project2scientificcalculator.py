import math
def Addition(x,y):
    return(x+y)
def Subtraction(x,y):
    return(x-y)
def Multiplication(x,y):
    return(x*y)
def Division(x,y):
    return(x/y)
def Square(x):
    return(x*x)
def SquareRoot(x):
    return(math.sqrt(x))
def SineFunc(x):
    return(math.sin(x))
def CosineFunc(x):
    return(math.cos(x))
def TangentFunc(x):
    return(math.tan(x))
b=1
print("""
Choose a number for the following operations
1 - Addition(x,y)
2 - Subtraction(x,y)
3 - Multiplication(x,y)
4 - Division(x,y)
5 - Square(x)
6 - Square Root(x)
7 - sin(x)
8 - cos(x)
9 - tan(x)""")
while(b!=0):
    a=int(input("What operation do you want to perform?"))
    if(a==1):
        x=int(input("Enter x"))
        y=int(input("Enter y"))
        print("Addition=",Addition(x,y))
    elif(a==2):
        x=int(input("Enter x"))
        y=int(input("Enter y"))
        print("Subtraction=",Subtraction(x,y))
    elif(a==3):
        x=int(input("Enter x"))
        y=int(input("Enter y"))
        print("Multiplication=",Multiplication(x,y))
    elif(a==4):
        x=int(input("Enter x"))
        y=int(input("Enter y"))
        print("Division=",Division(x,y))
    elif(a==5):
        x=int(input("Enter x"))
        print("Square=",Square(x))
    elif(a==6):
        x=int(input("Enter x"))
        print("SquareRoot=",SquareRoot(x))
    elif(a==7):
        x=int(input("Enter x"))
        print("Sin=",SineFunc(x))
    elif(a==8):
        x=int(input("Enter x"))
        print("Cos=",CosineFunc(x))
    elif(a==9):
        x=int(input("Enter x"))
        print("Tan=",TangentFunc(x))
    b=int(input("Do you want to continue (1-Yes),(0-No)"))
    if(b==0):
        print("Thanks for using the scientific calculator")
        break
