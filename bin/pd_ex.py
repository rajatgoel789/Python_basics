import pandas as pd

df = pd.read_csv("out5.csv")
print(df)

df1 = df.head(5)
print(df1)
df2 = df.tail(5)

print(df2)

df3 = df.describe()
print(df3)

df4 = df["IP"].describe()

print(df4)

df5 = df["Pics"].describe()
print(df5)

print(df["Pics"])
print(df["Pics"].count())

df6 = df["Pics"].value_counts()
print("DF6", df6)

import matplotlib.pyplot as plt

df6.plot()
# plt.show()
df6.plot.bar()
plt.savefig("graph.png")

writer = pd.ExcelWriter("myreport.xlsx", engine="xlsxwriter")
df6.to_excel(writer, sheet_name="DATA")
wb = writer.book
ws = wb.add_worksheet("Graph")
ws.insert_image("B2", "graph.png")
writer.close()

df7 = df[df["ID"] > 10]
print(df7)
df8 = df[df["ID"] == df["ID"].max()]
print(df8)

df9 = df[df['Pics'].str.endswith("jpg")]
print(df9)

df10 = df.groupby(["Pics"]).count()

print(df10)

# iloc - Index location
df11 = df.iloc[1, 2]
df12 = df.iloc[1]  # row 1
df13 = df.iloc[:, 1]  # col 1
df14 = df.iloc[1:10]  # ROW 1-10
df15 = df.iloc[1:10, ::2]  # ROW 1-10 and columns with step2
df16 = df.iloc[[1, 3, 5]]  # Row 1,3,5
df17 = df.iloc[[1, 3, 5], [1, 3]]  # Row 1,3,5 and Col 1,3


print(df17)
