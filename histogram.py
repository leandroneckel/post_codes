import numpy as np
import matplotlib.pyplot as plt
dados = np.random.normal(100,5,1000)
fig, ax = plt.subplots(1,figsize = (5,5),dpi = 150)
ax.hist(dados, bins=30, edgecolor='black')
ax.set_title('Histograma')
ax.set_xlabel('Valor')
ax.set_ylabel('Contagem')
fig.tight_layout()
