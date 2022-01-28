# Python Basics
# Classes

# part 1
# create a class
class Person():

    def insert(self,name,age,idNum):
        self.name = name
        self.age = age
        self.idNum = idNum

    def output(self):
        print("Your name is " + self.name + " your age is " 
        + self.age + " your ID is " + self.idNum )

# part 2
# create a class instance/object
j = Person()
j.insert("John", "33", "121292070")
j.output()

# part 3
# __init__(self) constructor
class Person():

    def __init__(self,name,age,idNum):
        self.name = name
        self.age = age
        self.idNum = idNum

    def output(self):
        print("Your name is " + self.name + " your age is " 
        + self.age + " your ID is " + self.idNum )

john = Person('john', '34', '01933808')
john.output()

# part 4
# Accessing variables or functions of an object
john = Person('john', '35', '019498488')
print(john.name)
print(john.age)
print(john.idNum)
john.output()

# part 5
# creating multiple instances of a class
p = Person('Peter', '46', '47897297')
m = Person('Melissa', '55', '89372213')

p.output()
m.output()

# code worked as expected