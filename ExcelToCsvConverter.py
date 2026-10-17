import pandas as pd

df = pd.read_excel('DocumentName.xlsx')

df.to_csv('DocumentName.csv', index=False)