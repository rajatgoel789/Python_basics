#tuple-> Class
#imutable
T1 = (10,12.5,'python',['a','b'], (10, 20),'python')
T2 = tuple([10,20,30])
print(T1, T2[0])
print(T1[0])
print(T1[1:4])
print(T1.index(12.5))
print(T1.count('python'))

T3 = (10,20,30)
L2 = list(T3)
print(L2)


L3 = [10,20,30]
T4 = tuple(L3);
print(T4)

#Tuple to list
#1st way

e= enumerate(L3)
print('e=', list(e), e)

D = dict(enumerate(L3))
print('D=', D)

#2nd
Keys = ['A','B']
Values = [10,20,30,40]
Z = zip(Keys, Values)
print('z=', list(Z))
D2 = dict(zip(Keys, Values))
d2 = dict(Z)
print('D2=',D2, d2)