# map

L = [100, 200, 300, 400]


def func(i):
    print(i)
    return i - 10


r1 = map(func, L)
print("r1 =", list(r1))
print("r2 =", list(r1))


# Genetrator - at the time of initialize it wil not create an object.
# on the fly it will create the object and its for 1 time use only

# filter
def filt(j):
    return j > 100


r3 = filter(filt, L)
print("r3", list(r3), r3)

# reduce not a builtins
# but available ib standard lib

from functools import reduce


def red(p, q):
    print("P", p, "Q", q)
    return p + q


r4 = reduce(red, L)
print("r4=", r4)

# lambda functions - are the functions only but it does n't have a name
# it is one liner

# lambda i:i-10
r5 = map(lambda i: i - 10, L)
print("r5=", list(r5))
r6 = filter(lambda j: j > 200, L)
r7 = reduce(lambda p, q: p + q, L)
print("r6=", list(r6))
print("r7=", r7)

a = lambda x, y: x + y
r8 = a(10, 20)
print("R8 = ", r8)
