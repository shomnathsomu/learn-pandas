# Working with large amounts of data
import pandas as pd

# for df in pd.read_csv('modified.csv', chunksize=5):
#     print("CHUNK DF")
#     print(df)

# read data from csv file
df = pd.read_csv('modified.csv')
new_df = pd.DataFrame(columns=df.columns)

for df in pd.read_csv('modified.csv', chunksize=5):
    results = df.groupby(['Type 1']).count()
    new_df = pd.concat([new_df, results], sort=False)

print(new_df)
