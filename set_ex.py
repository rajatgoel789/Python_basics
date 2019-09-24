# set->class
# unordered Collection
# No Index
# No Key
# Mutable
# Hold only immutable Objects
# Unique Values

S1 = {10, 10, 'Py', 'Py'}
S1.add(20)
print("S1 = ", S1)
#####################
r1 = S1.remove(20)
r2 = S1.pop()
print(r1, r2, S1)

#############
l1 = [10, 10, 20, 20]
S2 = set(l1)
#####
S3 = {10, 20, 30, 30}
L2 = list(S3)
print('S2 & L2', S2, L2)
#########Set OPERATIONS######

S4 = {10, 20, 30, 40}
S5 = {30, 40, 50, 60}

S6 = S4.union(S5)
S7 = S4.intersection(S5)
S8 = S4.difference(S5)

print(S6, S7, S8, sep='\n')
