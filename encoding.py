import pandas as pd
import numpy as np
vinhos = ['Cabernet Sauvignon', 'Malbec', 'Merlot']
avaliacoes = ['Muito Ruim', 'Ruim', 'Moderado', 'Aceitável', 'Bom', 'Muito Bom', 'Excelente']
np.random.seed(42)
dados = {
    'Vinho': np.random.choice(vinhos, 10),
    'Avaliacao': np.random.choice(avaliacoes, 10),
}
df = pd.DataFrame(dados)
vinho_dummies = pd.get_dummies(df[['Vinho']],columns=['Vinho'],dtype=int)
avaliacao_dict = {
    'Muito Ruim':1,
    'Ruim':2,
    'Moderado':3,
    'Aceitável':4,
    'Bom':5,
    'Muito Bom':6,
    'Excelente':7
}
avaliacoes = df[['Avaliacao']]
avaliacoes['Avaliacao_Map'] = avaliacoes['Avaliacao'].map(avaliacao_dict)
novo_df = pd.concat([vinho_dummies,avaliacoes['Avaliacao_Map']],axis = 1)
novo_df
