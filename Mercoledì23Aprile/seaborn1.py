import seaborn as sns 
import matplotlib.pyplot as plt 

#dati esempio
tips=sns.load_dataset("tips")

#creare grafico a barre
sns.barplot(x="day",y="total_bill", data=tips)
plt.title('Conto Totale del Giorno')
plt.show()


