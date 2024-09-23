import random
Cnumber=random.randrange(1,101)
userinput=int(input("enter your number:--"))
if userinput>Cnumber:
     
     print("your guess number is too high")
elif Cnumber>userinput:
    print("your guess number is too low")
else:
    print("computer number",Cnumber)
    print("your guess number is equal")