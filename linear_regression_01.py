import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score
np.random.seed(42)
x = np.random.rand(100, 1) * 10  
y = 2.5 * x + np.random.randn(100, 1) * 4
model = LinearRegression()
model.fit(x, y)
y_pred = model.predict(x)
r2 = r2_score(y, y_pred)
plt.figure(figsize=(10, 6))
plt.scatter(x, y, color='blue', label='Dados')
plt.plot(x, y_pred, color='red', linewidth=2, label='Melhor reta de ajuste')
plt.title('Gráfico de Dispersão com Reta de Ajuste')
plt.xlabel('Variável Independente')
plt.ylabel('Variável Dependente')
plt.legend()
plt.text(1, 25, f'$R^2 = {r2:.2f}$', fontsize=12, color='red')
plt.grid(True, ls = ':')
plt.show()
