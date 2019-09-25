L1 = [i for i in range(10)]
print("L1 = ", L1)

L2 = [j * j for j in L1 if j % 2 == 0]

print("L2 = ", L2)

L3 = [j + j if j % 2 == 0 else j + 1 for j in L1]
print("L3 = ", L3)

T1 = (j + j if j % 2 == 0 else j + 1 for j in L1)
print("T1 = ", T1)

keys = ["A", "B"]
values = [10, 20]
D = {k: v for k, v in zip(keys, values)}
print("D = ", D)

L4 = [(lambda i: i * i)(a) for a in L1]

print("L4=", L4)

D3 = {k: (lambda i: i + i)(v) for k, v in zip(keys, values)}
print("D3 =", D3)
