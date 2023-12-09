import pandas as pd

df=pd.read_csv('Play_1.csv')
#print(df.head(4))

cond_recid = (df['two_year_recid'] == 1)

recid_df=df[cond_recid]
print(recid_df.head(8))

cond_BW = (df['race'] == 'African-American') | (df['race'] == 'Caucasian')

BW_df=recid_df[cond_BW]
print(BW_df.head(8))

BW_df.to_csv('sample.csv',index=False)
# print(df[(df[Two_yr_Recidivism] == 1) & (df[])])