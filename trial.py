import pandas as pd
a = pd.read_csv('/home/kamla/Desktop/sales.csv')
b = a.columns
z = []
for i in b:
    z.append(i)
z = tuple(z)
print(z)


