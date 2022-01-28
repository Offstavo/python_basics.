# Python Basics
# If else statements

# part 1
# If else
var = 10

if var == 10:
    print("var is = 10")
else:
    print("var is Not = 10")

# part 2
# greater,less or equal to

greater = 10
less = 5

if greater > less:
    print('Yes')
else:
    print('No')

# part 3
# compare strings using if else statements
name = "Python"
name2 = "c++"

if name == name2:
    print("Two strings are equal")
else:
    print("Two strings are not equal")

# part 4
# not equal to operand
num = 10
num2 = 15

if num != num2:
    print("num is not equal to num2")
else:
    print("num is equal to num2")

# part 5
# and 
ten = 10 
five = 5

if(ten >= five and five == ten):
    print("True")
else:
    print("False")

# part 6
# or statement
ten = 10
five = 5

if(ten == five or ten >= five):
    ten = 0
    print("True")
else:
    print("False")

# code worked as expected