# Filtering Data
import pandas as pd
import re

# read data from csv file
df = pd.read_csv('pokemon_data.csv')

# new_df = df.loc[(df['Type 1'] == 'Grass') & (df['Type 2'] == 'Poison') & (df['HP'] > 70)]
# new_df.to_csv('filtered.csv')
# new_df.reset_index(drop=True, inplace=True)

# filtering by a specific keyword
new_df = df.loc[df['Name'].str.contains('Mega')]
# new_df = df.loc[~df['Name'].str.contains('Mega')]

# another_df = df.loc[df['Type 1'].str.contains('Fire|Grass', regex=True)]
# another_df = df.loc[df['Type 1'].str.contains('fire|grass', flags=re.I, regex=True)]

# start with a specific example word
another_df = df.loc[df['Name'].str.contains('^pi[a-z]*', flags=re.I, regex=True)]
# another_df = df.loc[df['Name'].str.contains('pi[a-z]*', flags=re.I, regex=True)]

print(another_df)
