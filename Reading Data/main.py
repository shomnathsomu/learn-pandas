# Reading data into Pandas
import pandas as pd

# read data from csv file
df = pd.read_csv('pokemon_data.csv')

# Read headers
# print(df.columns)

# Read each Column
# print(df['Name'])

# Read top 5 data
# print(df['Name'][0:5])

# Read some columns
# print(df[['Name', 'Type 1', 'HP']])
# print(df[['Name', 'Type 1', 'HP']][0:5])

# Read each row
# print(df.iloc[1])
# print(df.iloc[1:4])

for index, row in df.iterrows():
    # print(index, row)
    print(index, row['Name'])

# Read a specific location (R, C)
# print(df.iloc[2, 1])

# specific rows based on more textual/numerical information
print(df.loc[df['Type 1'] == "Fire"])
