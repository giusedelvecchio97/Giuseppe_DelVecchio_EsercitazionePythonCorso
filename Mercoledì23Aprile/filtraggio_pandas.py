import pandas as pd


ages=df['eta']

#filtraggio
adults=df[df['eta']>18]


df_sorted= df.sort_values(by='eta')

merge_df=pd.merge(df,df_csv,on='nome')


df.to_csv('data_output.csv')   #trasforma il data frame in csv