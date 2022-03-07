import pandas as pd

df = pd.read_csv('df.csv', encoding='utf-8')
df.to_csv('df-utf-8.csv', index=False, encoding='utf_8_sig')