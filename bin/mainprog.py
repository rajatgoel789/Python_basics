# 1 Env    var name - PYTHONPATH , var path =C:\Users\Rajat.Goel1\Desktop\training\lib
# 2 Prog
import mymodule
import sys

print(sys.path)
# sys.path.append(r'C:\Users\Rajat.Goel1\Desktop\training\lib')
print(mymodule.msg)
print(mymodule.sub(20, 30))

import mymodule as m

print(m.msg)

from mymodule import msg, sub

print(msg)
print(sub(20, 10))

#####################
from mymodule import msg as m, sub as s

print(m)
print(s(60, 10))

#####USING PACKAGE

# 1st way
import project.net.mymodule

print(project.net.mymodule.msg)

# 2nd way
import project.net.mymodule as m

print(m.msg)

# 3rd way
from project.net.mymodule import msg, sub

print("#####", msg)
# Using Pip we can install using terminal