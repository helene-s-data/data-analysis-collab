import pandas as pd
df_ventes = pd.read_csv("data/ventes.csv")
print("nombre de vente :", len(df_ventes))
print(df_ventes.head(15))
print ("nettoyage terminé")