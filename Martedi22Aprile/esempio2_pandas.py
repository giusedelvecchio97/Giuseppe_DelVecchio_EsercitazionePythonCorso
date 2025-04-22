
import pandas as pd

data={
    
    'Nome': ['Alice','Bob'],
    'Età':[25,78],
    'Cittaà':['Roma','Milano','Napoli']
    
    
}

df=pd.DataFrame(data)

df_older=df[df['Età']>23]  #creo un nuovo dataset con quel vincolo


df['Maggiorenne']=df['Età']>18   #aggiunga una nuovo campo al maggiorenne

df['Età']
df.fillna(df['Età'].mean(),inplace=True)
df=df.drop_duplicates()
