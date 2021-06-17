import pandas as pd
import os


df = pd.read_excel(r'/Users/xxxx/Documents/Bookmo.xlsx')
print(df)
for index, row in df.iterrows():
    os.rename(row['Old'], row['New'])



