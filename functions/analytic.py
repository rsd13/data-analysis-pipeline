import pandas as pd 
import numpy as np
import matplotlib.pyplot as plt



def open_data():
    name = "clean.csv"
    url = "../dataset/output/"
    data = pd.read_csv(url + name)
    return data


def top_state_food(data):
    """ da el estado que mide mas comida rapida"""
    pass



def info_state(data,city= "Arizona"):
    
    info = data[( data.longNameProvince == city  )]

    print(info.hist())

def info_state_percentObese(data):
    
    info = data['population'].max()
    info = data.loc[data[['percentObese']].idxmax()]
    print(info)

    plt.hist(data['province'])

    plt.show()

    #print(data.longNameProvince.hist())


def hypothesis(data):
    """funcion que daba la hipotesis principal,
    si el estado con mayor indice de obesidad pide mas comida o
    si el estado con mayor poblacion pide mas comida"""

    #primero mido la obesidad
    max_obese = data.loc[data[['percentObese']].idxmax()]
    #value counts para contar los tipos de valor
    count_obese = data.longNameProvince.value_counts()
    print(count_obese.head())
    print(max_obese.longNameProvince)

    print("Se puede veer que el estado con mayor obesidad es Misisipi y el estado con mayor pedidos es New York, por lo que \
    no se cumplee mi primera hipotesis")

    a = data.groupby('population')
    print(a.head())
    """
    max_poblation = data.population.value_counts()
    #value counts para contar los tipos de valor
    count_obese = data.longNameProvince.value_counts()
    print(count_obese.head())
    #print(max_poblation.longNameProvince)
    """




def main():
    data = open_data()
    
    #info_state_percentObese(data)
    hypothesis(data)

main()