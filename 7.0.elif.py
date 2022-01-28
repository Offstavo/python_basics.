# Python Basics
# elif

# part 1

print("This program checks if you are eligible for a bank loan or not")

salary = int(input("How much is your salary\n"))

if(salary > 1000):
    amount = 200
    print("You are eligible to get a bank loan by paying $",amount," monthly")
elif(salary == 1000):
    amount = 500
    print("You are eligible to get bank loan with higher monthly price $",amount," monthly")
else:
    print("Sorry you are not eligible")

# part 2
# elif 2
print("This program checks for zoo discounts")
print(", and entrance price is $120")

price = 120
times = int(input("How many times did you go to the zoo before\n"))

if(times == 3):
    price = 120 - 30
    print("Your total included discount will be $", price)
elif(times == 4):
    price = 120 - 50
    print("Your total included discount will be $", price)
elif(times == 5):
    price = 120 - 60
    print("Your total included discount will be $", price)
elif(times >= 6):
    price = 120 - 70
    print("Your total included discount will be $", price)

else:
    print("Your total price is $",price,"and you are not eligible for dicount in this item")

# code worked as expected
