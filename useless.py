import pandas as pd
a = pd.read_csv(r'/home/kamla/Desktop/project/Uploaded_Files/sales.csv')
for i in a.columns:
    print(a[i].dtypes)