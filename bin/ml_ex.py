from sklearn.neighbors import KNeighborsClassifier as Kn
import pandas as pd
from sklearn.metrics import accuracy_score as acc

knn = Kn()
df = pd.read_csv("iris.csv")
x = df.iloc[:, 0:4]
y = df.iloc[:, 4]

knn.fit(x, y)

r1 = knn.predict([[3, 5, 4, 2]])

print(r1)

r2 = knn.predict(x)
print("r2", r2)
a1 = acc(r2, y)
print("a1 = ", a1)
print("#2 way")
from sklearn.model_selection import train_test_split as tts

x_train, y_train, x_test, y_test = tts(x, y)

k2 = Kn()
k2.fit(x_train, y_train)
r3 = k2.predict(x_test)
a2 = acc(r3, y_test)
print("a2=", a2)
