# multiple Objects
# Inheritance
# Operator Overloading
x = 10
y = 20


# print(x + y)
# print(x.__add__(y))


class Account1:
    bankname = "ICICI"  # class variable

    def adduser(self, n):
        # print(self)
        self.name = n

    def viewuser(self):
        return self.name

    @classmethod
    def bankrules(cls, area):
        return "B Rules" + area

    @staticmethod
    def bankinfo():
        return "Bank Info"

    def __init__(self):
        print("SB LOGIC HERE ")


acc = Account1()
acc1 = Account1()
acc.adduser("Rajat")  # adduser(acc,"Rajat")
# It will create a instance variable
acc1.adduser("Goel")

print(acc.viewuser(), acc1.viewuser(), acc.bankname, Account1.bankname, Account1.adduser, sep="\n")

print(acc1.bankrules("BLR"))
print(Account1.bankrules("BLR"))

print(Account1.bankinfo())
print(acc1.bankinfo())


class Account2(Account1):
    def addAdhar(self, a):
        self.adhar = a

    def viewAdhar(self):
        return self.adhar

    def viewuser(self):
        return "Welcome" + self.name

    def __init__(self):
        super().__init__()
        # Account1.__init__(self)
        print("CA LOGIC TO BE HERE")


print("---------------------------------")
cus3 = Account2()
cus3.adduser("Raj")
cus3.addAdhar("w737237823")

print(cus3.viewAdhar(), cus3.viewuser(), sep="\n")


class RBI:
    def viewrules(self):
        return "RBI RULES"


class Account3(Account1, RBI):
    pass


class GOV:
    def viewrules(self):
        return "GOVT RULES"


class Account4(Account3, GOV):
    pass


print("*******************************")
cus4 = Account3();
print(cus4.viewrules())
print("*******************************")

cus5 = Account4()
print(cus5.viewrules())

print(GOV.viewrules(cus5))


#############
class Account5(Account3):
    def __init__(self):
        self.gov = GOV


cus6 = Account5()
print(cus6.viewrules())


# print(cus6.gov.viewrules())


class Account6:
    def __init__(self, a):
        self.name = a

    def __add__(self, x):
        return "Hello" + self.name + x.name

    def __str__(self):
        return self.name

    def __len__(self):
        return len(self.name)

    def __iter__(self):
        self.count = 0
        return self

    def __next__(self):
        c = self.count
        if c < len(self.name):
            self.count +=1
            return self.name[c]
        else:
            raise StopIteration


print("+++++++++++++++++++++++++++++++++++++++++++++++++++")
cus7 = Account6("c7")
cus8 = Account6("c8")
result = cus7 + cus8
print("result=", result)

print("cust7 = ", cus7)

print("len of cust7 = ", len(cus7))

for i in cus7:
    print("i=", i)

# Generic Class

from abc import ABC, abstractmethod
class Account(ABC):
    def adduser(self, a):
        self.name = a

    @abstractmethod
    def viewuser(self):
        pass

class MyAccount(Account):
    def viewuser(self):
        return self.name;




a = MyAccount()
a.adduser("Raj")
print(a.viewuser())