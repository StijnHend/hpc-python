from cyt_module import subtract

'''
1. internal var result declared as int: 
for float intputs, subtraction is computed and then rounded down to the nearest integer

2. func arguments declared as int
for float inputs, arguments are first rounded down to nearest integer and then subtraction is computed

3. error: cannot assign type 'float' to 'int'

 '''

print(subtract(4, 3))
print(subtract(5.0, 2.4))