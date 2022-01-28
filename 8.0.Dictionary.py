# Python Basics 
# Dictionaries

# part 1
# intro
dic = {'Toyota':'Camry', 'Cylinder':'v6'}
print(dic['Toyota'])
print(dic['Cylinder'])

# part 2
# add key value
dic['Color'] = 'White'
print(dic)

# part 3
# create an empty dictionary
d = {}
d['Toyota'] = 'Land Cruiser'
d['Cylinder'] = 'V8'
d['Color'] = 'White'
print(d)

# part 4
# edit a value in dictionary
OS = {'Apple':'Mac', 'Microsoft':'Windows', 'At&t':'PC'}

print("Before " + OS['At&t'])

OS['At&t'] = 'Linux'

print("Now is " + OS['At&t'])
print(OS)

# part 5
# delete key and value
OS = {'Apple':'Mac', 'Microsoft':'Windows', 'At&t':'PC'}

print("Before deletion")
print(OS)

del OS['At&t']
print("After deletion")
print(OS)

# code worked as expected