# Python Basics
# Lists and for loops

# part 1
# create a list and print
animals = ["lion", "tiger", "dog", "parrot"]
print(animals)

print(animals[1].title())
print(animals[-1].title())

# part 2
# create a list and combine it with a string
mesg = "I love my"
print(mesg + " " + animals[-2].title())

# part 3
# change an element in a list
animals[3] = "cat"
animals[0] = "monkey"
print(animals)

# part 4
# delete an element
Toyota = ["Corolla", "Camry", "Nissan"]
del Toyota[2]
print(Toyota)

# part 5
# sort() and reverse() methods
List = ["Book", "Apple", "Dog", "Camel"]
List.sort()
print(List)
List.sort(reverse = True)
print(List)
List.reverse()
print(List)

# part 6
# len() method
print(len(List))

# part 7
# for loop
List = ["Book", "Apple", "Dog", "Camel"]
for L in List:
    print("I love my " + L)

# part 8
# for loop with range function
for value in range(1, 5):
    print(value)

# part 9
# min, max and sum
ListNum = [1,2,3,4,5,6,7,8,9,10]
print(min(ListNum))
print(max(ListNum))
print(sum(ListNum))

# code worked as expected