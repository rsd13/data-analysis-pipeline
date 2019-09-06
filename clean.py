import pandas as pd

name = "Datafiniti_Pizza_Restaurants_and_the_Pizza_They_Sell_May19.csv"
url = "./dataset/input/"
#https://en.wikipedia.org/wiki/List_of_states_and_territories_of_the_United_States_by_population
#https://en.wikipedia.org/wiki/Obesity_in_the_United_States


data = pd.read_csv(url + name)
print(data.head())


print("Se puede ver que el dataset esta muy linpio salvo dos columnas que las voy a elimnar. Ademas de poner en U las 4 celdas de postalCode")

data.drop("menuPageURL",axis=1,)

print(data.head())
data.update(data[["postalCode"]].fillna("UNKNOWN"))

print(data.isnull().sum())