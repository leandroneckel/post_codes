import numpy as np
import matplotlib.pyplot as plt
num_classes = 2
confusion_matrix = np.random.randint(0, 1500, size=(num_classes, num_classes))
fig, ax = plt.subplots()
cax = ax.matshow(confusion_matrix, cmap='Blues')
fig.colorbar(cax)
class_names = ['Falso','Verdadeiro']
ax.set_xticks(np.arange(num_classes))
ax.set_yticks(np.arange(num_classes))
ax.set_xticklabels(class_names)
ax.set_yticklabels(class_names)
plt.xticks(rotation=45)
labels = [['Verdadeiro Negativo', 'Falso Positivo\nErro Tipo I'],
          ['Falso Negativo\nErro Tipo II', 'Verdadeiro Positivo']]
for i in range(num_classes):
    for j in range(num_classes):
        ax.text(j, i, f'{confusion_matrix[i, j]}\n{labels[i][j]}', ha='center', va='center', color='black')

plt.xlabel('Categoria prevista')
plt.ylabel('Categoria verdadeira')
plt.title('Matriz de confusão')
plt.show()
