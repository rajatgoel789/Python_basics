a = 0
while a < 10:
    print('a=', a)
    a = a + 1  # a+=1

S = "python"
b = 0
while b < len(S):
    print(S[b])
    b += 1

L = [10, 20, 30]
while L:
    x = L.pop()
    print("Processed:", x)

L = ["l1", "l2", "TS", "R1", "l1", "TS", "R2", "l1"]
i = 0
while i < len(L):
    if L[i].startswith("TS"):
        i = i + 1
        print("after Ts ==>", L[i])
        i = i + 1;
        # break
    else:
        i += 1

else:
    print("While completes")

j = 0;
while j < len(L):
    if L[j].startswith("R"):
        print("R found")
        break

    else:
        j += 1
else:
    print("NF ")

# Continue
k = 0
while k < len(L):
    if not L[k].startswith("R"):
        k = k + 1
        continue
    else:
        print(L[k])
        k = k + 1
    print("LAST STMT WHILE ")

# help and dir
L = []
print(dir(L), sep='\n')
print()

print(help(L.append))
# Reading from console
i = input("Enter your name")
print("i= ", i)

# pass
a = 10
if a != 11:
    pass
