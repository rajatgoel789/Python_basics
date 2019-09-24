a = 10
if a == 10:
    print("a eq 10")
    a = 11
if a > 10:
    print('a gt 10')
if a < 10:
    print('a lt 10')

#####Elif###

a = 11
if a == 10:
    print("a eq 10")
elif a > 10:
    print('a gt 10')
elif a < 10:
    print('a lt 10')

# Else


a = 9
if a == 10:
    print("a eq 10")
elif a > 10:
    print('a gt 10')
else:
    print('Else ')

#
s = "python"
if s != "java":
    print("Not java")
if not s.startswith('c'):
    print("not C")

if 'th' in s:
    print("Substring th found")

#
L1 = [10, 20, 30]
L2 = L1
L3 = L1.copy()
if L1 == L3:
    print("Content matched")

if L1 is L2:
    print("Ids are same or Refers same object")

if 30 in L1:
    print("30 Found")

D = {"A": 10, "B": 20}

if 'B' in D:  # or D.keys()
    print("Key B found")

if ('B', 20) in D.items():
    print("Items Found")

L = [["Hi", "IPI"]]

if ["Hi", "IPI"] in L:
    print("Found")
