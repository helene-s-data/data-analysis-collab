import pandas as pd

df = pd.read_csv("data/ventes.csv")


df["chiffre_affaires"] = df["quantite"] * df["prix_unitaire"]

print("Chiffre d'affaires total :", df["chiffre_affaires"].sum())