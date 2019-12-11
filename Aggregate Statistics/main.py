# Aggregate Statistics (Groupby)
import pandas as pd

# read data from csv file
df = pd.read_csv('modified.csv')

df['count'] = 1

# print(df.groupby(['Type 1']).mean())
# print(df.groupby(['Type 1']).mean().sort_values('HP'))
# print(df.groupby(['Type 1']).mean().sort_values('Attack', ascending=False))

# to sum up
# print(df.groupby(['Type 1']).sum())

# to count
# print(df.groupby(['Type 1']).count())
# print(df.groupby(['Type 1']).count()['count'])
print(df.groupby(['Type 1', 'Type 2']).count()['count'])
