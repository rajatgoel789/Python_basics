# Core Data Types
# Numbers
# Strings

'''
LIST
TUPLE
'''

"""
DIsctionary
Set
"""




x = 10 #int
y=12.5 #float
z = 0b1010 #bin
d=0x12 #hex
e=0o12 #oct

print('Hello')
print('a')
print('result', x, y, z, d, e, sep='|', end='.')#file=, flush=
print('Test')

#Immutable - Numbers, String, Tuple - Can not be changed
#mutable - List, Dictionary, Set - Can be changed.

print(id(x))
print(type(x))
print(type(x).__name__)
b=x #ref copy
x=11
print(b)
# Gc is based on referece Count, we can also implement GC.
