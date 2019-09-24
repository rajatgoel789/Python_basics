def add1():
    a = 10
    b = 20
    c = a + b
    # return c
    # print("c = " , c )
    # return a,b,c #Tuple
    # return [a,b,c] # List
    D = {"A": a}
    # return D # Dictionary
    return (a + b) / (a - b)


r1 = add1()
print(r1)


# Passing an argument
# Positional ARGS
def add3(a, b):
    return a + b


r2 = add3(10, 20)
print("r2=", r2)

x = 10
y = 20
r3 = add3(x, y)
print("r3=", r3)

S1 = "py"
S2 = " py"
r4 = add3(S1, S2)
print("r4=", r4)


# DEFAULT values arg
def add4(a, b=10):
    return a + b


r5 = add4(10)
r6 = add4(10, 20)
print(r5, r6)


# VARIABLE ARGUMENT
def add5(a, b=10, *c):  # *c here used for packing
    print("Extra Args => ", c)
    r = a + b
    for i in c:
        r += i
    return r


r8 = add5(10, 20, 30, 40, 50, 60, 40)
print("r8=>", r8)

L = [10, 20, 30, 40, 50, 60, 70]
r9 = add5(*L)  # UNPACKING
print("r9 = ", r9)


# Keywork only args
def add6(a, b=10, *c, d, e):
    r = a + b + d + e
    print("C =>", c)
    for i in c:
        r += i
    return r


r10 = add6(10, 20, 30, 40, 50, 60, 70, e=70, d=80)
print("r10=", r10)


# Variable Keyword only Argd

def add7(a, b=10, *c, d, e, **f):
    print("Remaining keywiords only args", f)
    r = a + b + d + e
    for i in c:
        r += i
    return r


r11 = add7(10, 20, 30, 40, 50, d=60, e=70, x=80, y=90)
print("r11=", r11)

# def add()
# def add(a,b)
# def add(a, b=10)
# def add(a=10, b) # not working
# def add(*a)
# def add(**a)
# def add(*a, **b)
# def add(*,a,b)
