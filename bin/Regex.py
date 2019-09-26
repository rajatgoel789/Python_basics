import sqlite3

con = sqlite3.connect("mydb.sqlite3")
# import pymysql
# con=mymysql.connect(host="",port="",user="",password="",db="")
cur = con.cursor()
query = '''CREATE TABLE IF NOT EXISTS LOGDATA( 
    IP VARCHAR(100),
    DATE VARCHAR(100),
    PICS VARCHAR(100),
    URL VARCHAR(100))
'''
cur.execute(query)

myurl = "https://www.jafsoft.com/searchengines/log_sample.html"
import urllib.request as u
import re

F = u.urlopen(myurl)

# \d digit
# \D non digit
# . Any Char
# {} Quantifier
# [.] -> inside square
# [0-9] => \d
# modifiers *=>0 or more
#             +=> 1 or more
#             ?=> 0 OR 1
# r[ea]+d
# () Grouping
# * is greedy operator
# *? non greedy
# \s space
# \S non space Char
# \w Word Character [0-9a-zA-Z_]
# \W non word Character[^0-9a-zA-Z_]
for line in F:
    # print(type(line), line)
    line = line.decode()
    # print(type(line))
    m = re.match(
        '(\d\d\d\.\d{1,3}[.]\d{1,3}\.[0-9]{3}).*?(\d{1,2}/[A-Za-z]{3}/\d{4}).*GET\s+/(pics/(\w+\.\w+))?.*(http[s]?://\S+)</A>.*',
        line)
    if m is not None:
        ip = m.group(1)
        dt = m.group(2)
        im = m.group(4)
        url = m.group(5)
        if im == None:
            im = "No Image"
        print(ip, dt, im, url)
        query = f" INSERT INTO LOGDATA VALUES('{ip}','{dt}','{im}','{url}')"
        cur.execute(query)

con.commit()
cur.execute("Select * from LOGDATA")
result = cur.fetchall()
print("Result = ", result)
# Date

# [0-9]{2}

# FOR URL
# http[s]?://\S+
# http[s]?://[a-zA-Z123.]+


# 2 way using csv
import csv

F = open('dbdump.csv', 'w', newline='')
wt = csv.writer(F)
wt.writerow(['IP', 'DATE', 'PICS', 'URL'])
#
for r in result:
    wt.writerow(r)

F.close()

'''
Pandas 
-DataFrame - for 2D data
-Series - for 1D
'''

import pandas as pd

L1 = [[10, 20, 30], [40, 50, 60]]
L2 = list([[10, 20, 30], [40, 50, 60]])
df1 = pd.DataFrame([[10, 20, 30], [40, 50, 60]], index=["r1", "r2"], columns=["c1", "c2", "c3"])
print(L1, L2, df1, sep="\n")

df2 = pd.DataFrame(result)
df2.to_csv("out5.csv", index=None, header=["IP", "Date", "Pics", "Url"])


df2.to_excel("out6.xlsx")
df2.to_json("out7.json")

cur.execute("select * from LOGData")

df3 = pd.DataFrame(cur)
df3.to_json("out8.json")