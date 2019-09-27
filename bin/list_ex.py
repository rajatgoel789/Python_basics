#list->class

L1 = list([10,20,30])
L2 = [10,12.5,'python',['a','b']]


print(L2)
print(L2[1:3]) #Here Index 3 is exclusive

print(L2[2][1])


#Update

L2[1] = "java"

print(L2)

#Add
L2.append(200)

print(L2)
L2.insert(2,300);

print(L2)

L3 = [10,20]
L4 = ['a','b']
L5 = L3+L4
L6 = L3*10

print(L5,L6,sep = '\n')


L3.extend(L4)
print(L3)


#Remvoe
r1 = L2.pop()
print(r1,L2)

r2 = L2.pop(2)
print("POP2 = ", r2, L2)

r3 = L2.remove('python')
print(r3, L2)

#Some Other Functions
L7 = [30,10,40]
L7.sort()
print('sort asc = ', L7)


L8 = ['z',"a","b"]
L8.sort(reverse = True)
print("L8=>", L8)

L9 = [10,'a',20,'b']

L9.reverse()

print('reverse=', L9)


i=L9.index('a')
c=L9.count('a')
print(i, c)



L9.clear() # To make list Empty
print(L9)

L=[10,['a','b']]
M=L # Reference Copy
N = L.copy() #Shallow Copy

import copy
p=copy.deepcopy(N) #Deep Copy
print(p)














