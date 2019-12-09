# Making changes to the data
import pandas as pd

# read data from csv file
df = pd.read_csv('pokemon_data.csv')

# df['Total'] = df['HP'] + df['Attack'] + df['Defense'] + df['Sp. Atk'] + df['Sp. Def'] + df['Speed']
df['Total'] = df.iloc[:, 4:10].sum(axis=1)

# To drop a column
# df = df.drop(columns=['Total'])

# shuffle the columns among themselves
cols = list(df.columns)
df = df[cols[0:4] + [cols[-1]] + cols[4:12]]

print(df.head(5))
