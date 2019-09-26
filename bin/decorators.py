def add1(a, b):
    print("Results = ")
    print(a + b + a)
    print("End of res")


def sub1(a, b):
    print("Results = ")
    print(a - b - a)
    print("End of res")


# add1(10, 20)
# sub1(10, 20)


def mydec(func):
    def decorated_func(x, y):
        print("Result is:")
        func(x, y)
        print("END OF RES")
    return decorated_func


def mydec1(func):
    def decorated_func(*x, **y):
        print("Result is:")
        # func(x, y)
        func(*x)
        print("END OF RES")
    return decorated_func


@mydec
def add2(a, b):
    print(a + a + a)

add2(100, 200)

#

def add3(a,b):
    print(a+b)

f=mydec(add3)
f(10,10)
