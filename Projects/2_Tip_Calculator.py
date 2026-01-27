print("Welcome to the tip calculator!")
bill = float(input("What was the total bill?\n"))
tip = int(input("How much tip would you like to give? 10, 20, or 15?\n"))
spilt = int(input("How many people to split the bill?\n"))
total = (bill + tip)/spilt
print(f"Each person should pay: {total}")