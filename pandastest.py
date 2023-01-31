import pandas as pd

#sample csv and read
#csv_path = 'csvTest.csv'
#dataFrame = pd.read_csv(csv_path)

#dataframes are made with dictionaries - dictionaries can be used to make nosql databases

dfDict = {"a": [11, 21, 44], "b": [9, 17, 30]}
df = pd.DataFrame(dfDict)

print(df.head(3))