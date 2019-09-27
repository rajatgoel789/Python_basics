a = 10
b = 0

# try:
#     r = a / b
#     print("r=", r)
# except:
#     print("SOME ERROR")
# print("Remaining code")

try:
    r = a / b
    print("r=", r)
except ZeroDivisionError:
    print("ZDE")
except (NameError, IndexError):
    print("NAME ERROR")
except KeyError as k:
    print("msg = ", k)
except:
    print("ANY ERROR")

print("Remaining code")

###########
L = []
try:
    print(L[1])
except Exception as e:
    print("e===", e)
    print("type = ", type(e))

##### If try got success, else block will exceute else except block excecutes
try:
    r = a / b
except:
    print("SOME  ERROR ")
else:
    r = a / a
    print("In Else")

print("---------------------------------")
try:
    r = a / b
except:
    print("IN except ")
finally:
    print("In Finally")

print("---------------------------------")

result = "Test case failed"
try:
    assert "success" in result, "Some test failed"
    print("Test success")
except AssertionError as ae:
    print("ae =", ae)
print("---------------------------------")

x = 10
y = 0

try:
    if y == 0:
        raise ZeroDivisionError
    print("STMT-100")
    r = x / y
except:
    print("from raise")


# OWN EXCEPTION CLASS

class MyError(Exception):
    def __init__(self, m):
        self.msg = m

    def __str__(self):
        return "MORE DESC = " + self.msg


try:
    if y == 0:
        raise MyError("Y IS 0")
except MyError as me:
    print("me==", me)
