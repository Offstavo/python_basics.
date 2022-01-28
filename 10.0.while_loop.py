# Python Basics
# While loop

# part 1
# intro
i = 1
while(i <= 6):
    print(i)
    i += 1

# part 2
# using flag to stop looping
i = ""
name = "Write any name\n"

while(i!='q'):
    i = input(name)

# part3
# infinit loop
# i = 1
# while(i == 1):
#     name = input("Enter your name")
#     print("Your name is: " + name)

# part 4
# break and continue
i = 1
user = ""

while(i <= 5):
    user = input("Insert any name.\n")
    print("You inserted" + user)
    if(user == "John"):
        break
    elif(user == "Mic"):
        continue
    i += 1

# code worked as expected