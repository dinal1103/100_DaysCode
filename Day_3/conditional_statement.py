#if else statement
height = int(input("what is your height in cm?\n"))

if height>=120:
    print("You can ride!")
else:
    print("you can't ride")
    
print("\n")  

#modulo operator
num = 12
if num%2==0:
    print("num is even")
else:
    print("num is odd")
    
#nested if and elfi
height = int(input("what is your height in cm?\n"))
if height>=120:
    print("You can ride!")
    age = int(input("enter your age : "))
    if age<=12:
        print("your price is 5$")
    elif age<=18:
        print("your price is 7$")
    else:
        print("your price is 10$")
else:
    print("you can't ride")