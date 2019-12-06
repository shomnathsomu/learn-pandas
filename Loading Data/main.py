# Loading data into Pandas
import pandas as pd

# read data from csv file
df = pd.read_csv('pokemon_data.csv')

# to see all the data
print(df)

# to see just the top of the data
print(df.head(3))

# to see the bottom three rows
print(df.tail(3))

# read data from excel file
# df_excel = pd.read_excel("pokemon_data.xlsx")
# print(df_excel.head(3))
# print(df_excel.tail(5))

# read data from text file
# df_txt = pd.read_csv("pokemon_data.txt", delimiter='\t')
# print(df_txt.head(5))


