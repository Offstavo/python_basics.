# Python Basics
# Slice list

# part 1
# simple slicing
OS = ['Mac', 'Windows', 'Linux', 'Android', 'iOS']
print(OS[0:5])
print(OS[0:4])
print(OS[2:3])
print(OS[:])
print(OS[:5])
print(OS[2:5])
print(OS[-3:])

# part 2
# using for loop with slice
for os in OS[2:4]:
    print(os)

# part 3
# copying lists using slicing lists
ProgLang = ['c++', 'python', 'php', 'swift4']
cpy_ProgLang = ProgLang[:]

print("Priting programming languages list here")
print(ProgLang)

print("Printing the copy one")
print(cpy_ProgLang)

cpy_ProgLang.append('Java')
print(cpy_ProgLang)

# code worked as expected