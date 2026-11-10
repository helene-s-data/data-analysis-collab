import pandas as pd
df_ventes = pd.read_csv("data/ventes.csv")
print("nombre de vente :", len(df_ventes))
df_ventes.shape