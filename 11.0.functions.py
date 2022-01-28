# Python Basics
# Functions

# part 1
# intro
def function():
    print("Hello, this is code from the function")

print("This is code from our main program")

function()

# part 2
# arguments and parameters
def names(Fname, Lname):
    print("Your first name is " + Fname)
    print("Your last name is " + Lname)

names('John','Doe')

# part 3
# multiple function call
names('Nancy', 'Marco')
names('Maria', 'Chris')

# part 4
# default values 
def names(Fname = 'John', Lname = 'Doe'):
    print("Your first name is " + Fname)
    print("Your last name is " + Lname)

names()
names('Donald','Jack')

# part 5
# order of matter in functions
def names(Fname, Lname):
    print("Your first name is " + Fname)
    print("Your last name is " + Lname)

names('John','Doe')
names(Lname = 'John', Fname = 'Doe')

# part 6
# return value
def addition(a, b):
    total = a + b
    return total

print(addition(10,5))

# code worked as expected
