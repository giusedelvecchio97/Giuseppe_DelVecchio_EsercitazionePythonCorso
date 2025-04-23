import seaborn as sns 
import matplotlib.pyplot as plt 

data=sns.load_dataset("penguins")


sns.histplot(data=data, x="flipper_lenght_mm",kde=True)
plt.title('Distribuzione Lunghezza Pinnne dei pinguini')
plt.show()