# for collection:
# While T/F:

S = "Python"
for a in S:
    print('a = ', a)

b = "java"
L = [10, 20, 30]
for b in L:
    print("b= ", b)

print(b)

D = {"A": 10, "B": 20}
for k in D:  # D.keys()
    print(k, D[k])

for v in D.values():
    print("v=", v)
print(D.items())

for i, j in D.items():
    print("==> ", i, j)

    hosts = ["h1", 'h2']
    ips = ["ip1", "ip2"]
    for h, i in zip(hosts, ips):
        print(h, i)

print(list(zip(hosts, ips)))

r1 = range(10)
r2 = range(1, 10)
r0 = range(-51, 10)
r3 = range(1, 10, 2)
r4 = range(10, 1, -1)
print(list(r1), list(r2), list(r3), list(r0), list(r4), sep="\n")

for i in range(2, 10, 2):
    print('i=', i)

comp = ["IBM", "SYN1", "SAP", "SYN2"]
for c in comp:
    if c.startswith("SYN"):
        print("FOUND", c)
        # break
else:  # Else will execute after success of for loop.
    print("Not Found")

for d in comp:
    # if not d.startswith("SYN"):
    #     continue
    if d.startswith("SYN"):
        print("SOME LOGIC")

    print(" LAST STMT OF FOR ")
