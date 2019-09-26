F1 = open('out1.txt', "w")
x = 10
S = "Python \n"

x = str(x) + "\n"
F1.write(x)
F1.write(S)
F1.flush()  # flush will flush the buffer

L = [x, S]
F1.writelines(L)
F1.close()

F2 = open("out1.txt", "r")
r1 = F2.read()  # output is in string
print("r1 ", r1)

F2.seek(0)
r2 = F2.read()
print("r2 = ", r2)

F2.seek(0)
r3 = F2.readline()
print('r3 = ', r3)
while True:
    line = F2.readline()
    if line == '':  # EOF
        break
    else:
        print("line =", line)

F2.seek(0)
r4 = F2.readlines()
print("r4=", r4)  # read all file , output is in list

F2.seek(0)
for line in F2:
    print('line =>>', line)

F2.close()
print(F2)

#
F3 = open("out1.txt", "a")
F4 = open("out2.csv", "a")
print(20, "java", sep="\n", file=F3, flush=True)

print(20,"JJava",sep=",", file=F4)
F3.close()
F4.close()

# "r" => Read only
# "w" => Write only
# "a" => Append only
# "r+" => RW
# "w+" => WR
# "a+" => AR
