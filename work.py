import pandas as pd
df = pd.read_excel('namelist.xlsx')
df.to_csv('namelist.csv', index=False)

print('Excel file converted to CSV file')
print(df)