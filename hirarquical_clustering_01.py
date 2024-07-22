import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from sklearn.datasets import load_iris
from sklearn.preprocessing import StandardScaler
from scipy.cluster.hierarchy import dendrogram, linkage

# Carregar o conjunto de dados Iris
data = load_iris()
df = pd.DataFrame(data.data, columns=data.feature_names)
labels = data.target

# Normalizar os dados
scaler = StandardScaler()
df_scaled = scaler.fit_transform(df)

# Gerar o linkage matrix usando o método 'ward'
Z = linkage(df_scaled, method='complete')

# Função para plotar o dendrograma
def plot_dendrogram(Z, labels):
    plt.figure(figsize=(7, 5))
    plt.title("Dendrograma do Agrupamento Hierárquico")
    plt.xlabel("Índice da amostra")
    plt.ylabel("Distância")
    dendrogram(Z, labels=labels, leaf_rotation=90, leaf_font_size=10)
    plt.xticks([])
    plt.show()

# Plotar o dendrograma
plot_dendrogram(Z, labels=data.target)
