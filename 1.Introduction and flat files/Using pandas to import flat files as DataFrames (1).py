# Import pandas as pd
import pandas as pd

# Assign the filename: file
file = 'titanic.csv'

# Read the file into a DataFrame: df
df = pd.read_csv('titanic.csv')

# View the head of the DataFrame
print(df.head())
