import pandas as pd 
import numpy as np
import matplotlib.pyplot as plt
import random
from fpdf import FPDF
import os

url = os.path.dirname(os.path.abspath(__file__))
def open_data():
    name = "clean.csv"
   
    url_relative = url +  "/../dataset/output/"
    

    data = pd.read_csv(url_relative + name)
    return data


def description(pdf):
    """descripcion de lo que hace en eel terminal y en el pdf generado"""
    print("-----------------LIMPIANDO----------------------")
    print("Limpiando el dataset para su futuro analisis.\n")
    pdf.input_subtitle("Limpieza de datos")


def compare_city(cities,pdf):
    """compara las ciudades por comida pedida"""
    data = open_data()

    for city in cities:
        plt.hist(data[ (data.city == city )].city, alpha=1, label=city)
    
    url_image = url+'/../imgs/compare_cities.png'
    plt.savefig(url_image)
    pdf.image(url_image,w=175,h=140)


def compare_state(states,pdf):
    """ da el estado que mide mas comida rapida"""
    data = open_data()
 
    for state in states:
        plt.hist(data[(data.longNameProvince == state )].longNameProvince, alpha=1, label=state)

    url_image = url+'/../imgs/compare_states.png'
    plt.savefig(url_image)
    pdf.image(url_image,w=175,h=140)
    



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

    
    


