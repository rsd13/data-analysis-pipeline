import pandas as pd 
import numpy as np
import matplotlib.pyplot as plt
import random


def open_data():
    name = "clean.csv"
    
    url = "./dataset/output/"
    

    data = pd.read_csv(url + name)
    return data


def compare_city(data,city1="New York",city2="Phoenix"):
    """ da el estado que mide mas comida rapida"""
    x = data[ (data.city == city1 )]
    y = data[ (data.city == city2 )]

    plt.hist(x.city, alpha=1, label=city1)
    plt.hist(y.city, alpha=1, label=city2)
    plt.legend(loc='upper right')
    plt.show()



def compare_state(data,state1="New York",state2="California"):
    """ da el estado que mide mas comida rapida"""
    x = data[ (data.longNameProvince == state1 )]
    y = data[ (data.longNameProvince == state2 )]

    
    plt.hist(x.longNameProvince, alpha=1, label=state1)
    plt.hist(y.longNameProvince, alpha=1, label=state2)
    plt.legend(loc='upper right')
    plt.show()
    



    



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
    print(count_obese)
    print(max_obese.longNameProvince)

    print("Se puede veer que el estado con mayor obesidad es Misisipi y el estado con mayor pedidos es New York, por lo que \
    no se cumplee mi primera hipotesis. Una principal razon puede ser que los datos recogidos se hayan basado en New York.")

    a = data.groupby('population')
    print(a)
    
    
    #value counts para contar los tipos de valor
    count_obese = data.longNameProvince.value_counts()
    print(count_obese.head())

    max_population = data.sort_values("population",ascending = False)
    max_population = max_population.groupby(["population","longNameProvince"])
    
    

    print(max_population[["longNameProvince","population"]].head(10))

    
    




def main():
    data = open_data()
    
    #info_state_percentObese(data)
    #hypothesis(data)
    #compare_city(data)
    compare_state(data)

main()