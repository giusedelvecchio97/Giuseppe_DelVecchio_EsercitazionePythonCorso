
import pandas as pd


dati={
    
    'Data' :['2021-01-01','2021-01-01','2021-01-02'],
    'Città' : [ 'Roma','Milano','Napoli'],
    'Prodotto':['Mouse','Tastiera','Mouse'],
    'Vendite' :[100,200,150,]}
    
    
df=pd.DataFRame(dati)
pivot_dt=df.pivot_table(values='Vendite',index='Prodotto')    



group_df= df.groupby('Prodotto').sum()

print(group_df)

