# Saving our data ( exporting into Desired format )
import pandas as pd

# read data from csv file
df = pd.read_csv('pokemon_data.csv')

# copy into a csv/excel/txt file
df.to_csv('modified.csv', index=False)
df.to_excel('modified.xlsx', index=False)
df.to_csv('modified.txt', index=False, sep='\t')

print(df.head(5))
