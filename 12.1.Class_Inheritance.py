# Python Basics
# Class Inheritance

# part 1
# inheritance
class Person():

    def __init__(self,name,age,idNum):
        self.name = name
        self.age = age
        self.idNum = idNum

    def output(self):
        print("Your name is " + self.name + " your age is " 
        + self.age + " your ID is " + self.idNum )

class Child(Person):
    pass

kid = Child('Johnny', '5', '4793793')
kid.output()

# part 2
# more about class inheritance
class Man():
    def strong(self):
        print("Men are strong")

class Child(Person, Man):
    pass

kid = Child('Johnny', '5', '283937')    
kid.output()
kid.strong()

# code worked as expected