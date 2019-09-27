#dict->class
L=['Python',5,'lr']

D = {'course':"Python", "dur":5 , "Loc":"BLR"}
print("D ", D,D["course"], D.items())

r1 = D.get('abc',"No Such Key")
print(r1)

#To add/Update

D["course"] = ["Java","C"]
print('update = ', D)


#To remove

E=D.copy()
r1 = D.pop('course')

print(r1, D)

del D['dur']


r2 = D.popitem()
print(r2, D.popitem)


k=E.keys()
v = E.values()
i = E.items()

print(k,v,i,sep="\n")
