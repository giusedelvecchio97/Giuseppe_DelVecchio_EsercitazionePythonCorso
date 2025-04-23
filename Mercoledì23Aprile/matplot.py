import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

#imposta la dimensione
plt.rcParams['figure.figsize']=[10,6]


 #imposta la risoluzione
plt.rcParams['figure.dpi']=100


plt.rcParams['figure.facecolor']='white'  #color della figura


#configurazione seaborn
sns.set_theme(style="darkgrid")

#crea alcuni dati
data=np.random.normal(size=100)

#crea grafico
sns.histplot(data,kde=True)
plt.title('Distribuzione dei dati')
plt.show()



fig=plt.figure()

ax=fig.add_subplot(111)