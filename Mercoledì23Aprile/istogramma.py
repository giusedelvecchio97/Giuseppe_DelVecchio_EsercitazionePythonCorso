import numpy as np
import matplotlib.pyplot as plt


data=np.random.rand(1000)

plt.figure()
plt.hist(data,bins=30)
plt.title('Istogramma')
plt.xlabel('Valori')
plt.ylabel('Frequenza')
plt.show()