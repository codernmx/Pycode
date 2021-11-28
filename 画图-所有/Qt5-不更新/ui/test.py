import pandas as pd
df = pd.read_excel(r'E:\test.xlsx').head(100)
print(df.info())