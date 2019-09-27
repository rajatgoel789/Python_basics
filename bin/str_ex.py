#str=>class
a=10
b=int(10)
c = 'PERSON'
d= 'PERSON\'S'
print(d)
e='''PERSON's  HEIGHT XYZ" '''
print(e)

f = """ PERSON """

g = ' LINE 1 \
      LINE3'

h=''' line1
line3
'''
print(h);

j = r'c:\newfodler\test.py'
print('j=',j)

k = 'Wel Come'
print(len(k), k[0])


#SLICING

print(k[2:6])

print(k[1:])

print(k[:7])

print(k[:])

l=  k[:]
print(id(l), id(k))

#step

print(k[1:6:1])
print(k[::-1]) # reverdse a string
print(k[6:1:-2]) #k[-2:-7:-2]

#last 4 chars
print(k[-4:])

r1 = k.startswith("Wel")
print('r1 = ', r1)

r2 = k.endswith("Come")
print("R2 =  ", r2)


r3 = k.isupper()
print(r3)
r4 = k.upper()
print(r4)

r5 = k.istitle()
r6=k.title()
r7 = k.capitalize()
print(r5, r6, r7)

s1 = 'Hello'
s2 = 'py'

r8 = s1+s2

print(r8)

r9 = s1*10

print("r9 => ",r9)

r10 = s1+" "+s2
print(r10)

line = '#'*40
print(line)

m = 'abc'
n='123'
p = 'abc123'
r11 = m.isalpha()
r12 = n.isdigit()
r13 = p.isalnum()

print(r11, r12, r13)

r14 = p[-3:].isdigit()
print(r14)


q='  wel  come    '
r15 = q.strip()
r16 = q.lstrip() #rstrip

s='[wel[come][]'
r18 = s.strip(']w[e')
print(r18)

k='WEL COME'
r21 = k.split()
print(r21)
r22 = k.split("E")
print(r22)


r23 = k.index("E")
r24 = k.find('E')
#In case Subsctring not there then .index will throw error. find wil return -1
print(r23, r24)

r25 = k.find('fddfs')
print(r25)

r26 = k.count("E")
r27 = k.replace("E",'e')
print(r26, r27)

x=10;
y=20
z=x+y
r27 = 'add of x and y is z'

r28 = 'add of {} and {} is {}'.format(x,y,z)

r29 = 'add of {2} and {0} is {1}'.format(x,y,z)

print(r28, r27)

print(r29)

r30 = f'add of {x} and {y} is {z}'  #Py 3.5 Pmwards
print('r30   =>', r30)
