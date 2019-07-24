import pandas as pd
import os

path = 'data/'

df = pd.DataFrame()
for file in os.listdir(path):
	dfi = pd.read_csv(path+file)
	# print(dfi.head)
	df = df.append(dfi)

print(df.head())

df.to_csv(r'file2400-2699.csv', header=True, index=False)