import pandas as pd


#https://en.wikipedia.org/wiki/List_of_states_and_territories_of_the_United_States_by_population
#https://en.wikipedia.org/wiki/Obesity_in_the_United_States


def open_data():
    name = "Datafiniti_Pizza_Restaurants_and_the_Pizza_They_Sell_May19.csv"
    url = "./dataset/input/"
    data = pd.read_csv(url + name)
    return data


def clean_null(data):
    print("Se puede ver que el dataset esta muy linpio salvo dos columnas que las voy a elimnar. Ademas de poner en U las 4 celdas de postalCode")

    data.drop(columns=["menuPageURL","menus.description"],inplace = True)

    print(data.head())
    data.update(data[["postalCode"]].fillna("UNKNOWN"))

    print(data.isnull().sum())



def main():
    data = open_data()
    #limpiamos de null
    clean_null(data)

    print(data[["name","city"]].head())

main()


