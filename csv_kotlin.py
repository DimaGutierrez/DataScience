import pandas as pd

data = pd.read_csv('data.csv')
df = pd.DataFrame(data)
print(df.head())
