import pandas as pd
from sklearn.preprocessing import MinMaxScaler, StandardScaler
import numpy as np
uniform_col = np.linspace(40, 120, 1000)
normal_col = np.random.normal(loc=30, scale=5, size=1000)
df = pd.DataFrame({
    'Dados uniformes': uniform_col,
    'Dados normais': normal_col
})
scaler = MinMaxScaler()
df['Dados uniformes normalizados'] = scaler.fit_transform(df[['Dados uniformes']])
scaler = StandardScaler()
df['Dados normais padronizados'] = scaler.fit_transform(df[['Dados normais']])
print(df.describe())
