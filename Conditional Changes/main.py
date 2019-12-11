# Conditional Changes
import pandas as pd

# read data from csv file
df = pd.read_csv('modified.csv')

# replace a value against another one
# df.loc[df['Type 1'] == 'Fire', 'Type 1'] = 'Flamer'

# change value corresponding to a value
# df.loc[df['Type 1'] == 'Fire', 'Legendary'] = True

# change multiple columns' value under a condition
# df.loc[df['Total'] > 500, ['Legendary', 'Generation']] = 'TEST'

# change column specific value
df.loc[df['Total'] > 500, ['Generation', 'Legendary']] = ['TEST 1', 'TEST 2']

print(df)
