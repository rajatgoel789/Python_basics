x = 10;


def f1():
    x = 20

    def f2():
        print("F2 = ", x)

    f2()
    print("F1 = ", x)


f1()
print("Global = ", x)

# NON LOCAL

x = 10;


def f1():
    x = 20

    def f2():
        nonlocal x
        x = 200
        print("F2 = ", x)

    f2()
    print("F1 = ", x)


f1()
print("Global = ", x)

# Global
# NON LOCAL

x = 10;


def f1():
    x = 20

    def f2():
        global x
        x = 200
        print("F2 = ", x)
        global y
        y = 150

    f2()
    print("F1 = ", x, y)


f1()
print("Global = ", x, y)

# Local
# Enclosed
# Globals
# BuiltIn

print(dir(__builtins__))

count = 0


def CA():
    global count
    count += 1


def DA():
    global count
    count -= 1


CA()
CA()
print("TOTAL ACCTS = ", count)
count = 100
DA()
print("TOTAL ACCTS = ", count)


##################################

def Acc():
    c = 0

    def CAC():
        nonlocal c
        c = c + 1

    def DAC():
        nonlocal c
        c = c - 1

    def TAC():
        nonlocal c
        return c

    return CAC, DAC, TAC


a, b, c = Acc()

a()
a()
a()
a()
a()
b()
print("TOTAL", c())
# Docstring
# 1st multiline comments is treated as docstring that can be access by using help()
def f():
    '''
      c-1
      c-2
    '''
    # c-3
    '''
    c-4
    '''
print(help(f))