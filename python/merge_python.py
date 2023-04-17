#Example script
#Aim: merging/joining two dataframes (tables) based on a common column

print('hello world')
#import pandas library

import pandas as pd

#make dataframes
df1 = pd.DataFrame({'lkey': ['ARG','FRA', 'GBR', 'VNM'],
                    'value': [100, 200, 300, 500]})
df2 = pd.DataFrame({'rkey': ['ARG','FRA','VNM'],
                    'country': ["Argentina", "France", "Vietnam" ],
                    'region': ["Latin America", "Europe", "Asia Pacific"]})

print ("df1: \n",df1)
print ("df2: \n", df2)

#Merge df1 and df2 on the lkey and rkey columns. 
df_merged = df1.merge(df2, left_on='lkey', right_on='rkey',how="outer")
print ("df_merged: \n", df_merged)

#for more info on merge function see here: https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.merge.html
