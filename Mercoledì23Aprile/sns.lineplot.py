import seaborn as sns 
import matplotlib.pyplot as plt 
fmri=sns.load_dataset("fmri")

sns.lineplot(x="timepoint",y="signal", data=fmri, hue="region",style="event")
plt.title('Segnale FMRI')
plt.show()