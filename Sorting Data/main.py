# Sorting/Describing Data
import pandas as pd

# read data from csv file
df = pd.read_csv('pokemon_data.csv')

# print(df.describe())

# print(df.sort_values('Name'))
# print(df.sort_values('Name', ascending=False))
# print(df.sort_values(['Type 1', 'HP'], ascending=True))
print(df.sort_values(['Type 1', 'HP'], ascending=False))

# sort ascending by Type 1 and descending by HP
print(df.sort_values(['Type 1', 'HP'], ascending=[1, 0]))
