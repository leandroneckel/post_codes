import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans, DBSCAN
from sklearn.datasets import make_blobs

# Gerar dados de exemplo
X, _ = make_blobs(n_samples=300, centers=4, cluster_std=0.60, random_state=0)
df = pd.DataFrame(X, columns=['Atributo1', 'Atributo2'])


kmeans = KMeans(n_clusters=4)
df['KMeans_Cluster'] = kmeans.fit_predict(X)

dbscan = DBSCAN(eps=0.4, min_samples=5)
df['DBSCAN_Cluster'] = dbscan.fit_predict(X)

# Plotar resultados KMeans
plt.figure(figsize=(14, 6))
plt.subplot(1, 2, 1)
unique_clusters = np.unique(df['KMeans_Cluster'])
for cluster in unique_clusters:
    plt.scatter(df[df['KMeans_Cluster'] == cluster]['Atributo1'], df[df['KMeans_Cluster'] == cluster]['Atributo2'], 
                label=f'Cluster {cluster}', s=50)
plt.title('KMeans Clustering')
plt.xlabel('Atributo1')
plt.ylabel('Atributo2')
plt.legend()

# Plotar resultados DBSCAN
plt.subplot(1, 2, 2)
unique_clusters = np.unique(df['DBSCAN_Cluster'])
for cluster in unique_clusters:
    if cluster == -1:
        plt.scatter(df[df['DBSCAN_Cluster'] == cluster]['Atributo1'], df[df['DBSCAN_Cluster'] == cluster]['Atributo2'], 
                    edgecolor='black', facecolor='white', label='Outliers', s=50)
    else:
        plt.scatter(df[df['DBSCAN_Cluster'] == cluster]['Atributo1'], df[df['DBSCAN_Cluster'] == cluster]['Atributo2'], 
                    label=f'Cluster {cluster}', s=50)
plt.title('DBSCAN Clustering')
plt.xlabel('Atributo1')
plt.ylabel('Atributo2')
plt.legend()

plt.tight_layout()
plt.show()
