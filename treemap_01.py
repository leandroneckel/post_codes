import pandas as pd
import plotly.express as px
data = {
    'Categoria': ['A', 'A', 'A', 'B', 'B', 'C', 'C', 'C', 'C'],
    'Subcategoria': ['A1', 'A2', 'A3', 'B1', 'B2', 'C1', 'C2', 'C3', 'C4'],
    'Valor': [10, 20, 30, 15, 25, 5, 35, 45, 10]
}
df = pd.DataFrame(data)
fig = px.treemap(
    df,
    path=['Categoria','Subcategoria'],
    values='Valor',
    title='Treemap de Exemplo'
)
fig.update_traces(textinfo='label+value')
fig.write_image("treemap.jpg", width=1024, height=768)
