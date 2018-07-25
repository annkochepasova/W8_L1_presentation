# Dependencies
import pandas as pd
import numpy as np
# Name of the CSV file
file = 'Resources/donors2008.csv'
# The correct encoding must be used to read the CSV in pandas
df = pd.read_csv(file, encoding="ISO-8859-1") 
# Delete extraneous column
del df['FIELD8']
# Drop all rows with missing information
df = df.dropna(how='any')