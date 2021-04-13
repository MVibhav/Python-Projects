import random
import time
a=random.randint(1,100)
b=0
turns=15
print("You will be given 15 turns to make the right guess")
time.sleep(4)
while(turns>0 and a!=b):
    b=int(input("Enter your guess"))
    if(a>b):
        print("Almost there, increase your number")
        turns=turns-1
        print("You have",turns,"turns left")
    elif(a<b):
        print("Almost there, decrease your number")
        turns=turns-1
        print("You have",turns,"left")
    else:
        print("Your number is",b)
        break
if(turns==0):
    print("You lost")
