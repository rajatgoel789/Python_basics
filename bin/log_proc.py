F1 = open("out3.txt", "w")
F2 = open("out4.csv", "w")
F1.write("IP\tDate\tPICS\tURL\n")

F2.writelines(["IP,", "DATE,", "PICS,", "URL\n"])

F3 = open(r'C:\Users\Rajat.Goel1\Desktop\training\log\server_log.txt')  # r means rawstring
# print(F3)
for line in F3:
    if line[:3].isdigit():
        print(line)
        sp = line.split()
        print(sp)
        ip = sp[0]
        print(ip, sp[3])
        dt = sp[3]
        dt = dt.split(":")
        dt = dt[0]
        d1 = dt.lstrip("[")
        d2 = dt.replace("[", "")
        d3 = dt[1:]
        print(d3)
        # if sp[6].startswith("/pics")
        # if sp[6][:5] =="/pics"
        if "pics" in sp[6]:
            im = sp[6].split("/")
            print("IM IS ", im)
            im = im[-1]
        else:
            im = "No Image"
        print(im)
        url = sp[10]
        print(ip, d1, im, url, sep="\t", file=F1)
        print(ip, d1, im, url, sep=",", file=F2)


F1.close()
F2.close()
F3.close()