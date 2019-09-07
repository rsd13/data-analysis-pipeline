import pandas as pd
from trya import get_start,get_page
from we_scraping import  get_state,get_population,get_obese


#https://en.wikipedia.org/wiki/List_of_states_and_territories_of_the_United_States_by_population
#https://en.wikipedia.org/wiki/Obesity_in_the_United_States


def open_data():
    name = "Datafiniti_Pizza_Restaurants_and_the_Pizza_They_Sell_May19.csv"
    url = "./dataset/input/"
    data = pd.read_csv(url + name)
    return data


def clean_null(data):
    print(data.isnull().sum())
    print(data.columns)
    print("Se puede ver que el dataset esta muy linpio salvo dos columnas que las voy a elimnar. Ademas de poner en U las 4 celdas de postalCode. \
    Ademas borro información que no me intereesa")

    data.drop(columns=["menuPageURL","menus.description","latitude","keys","longitude"],inplace = True)

    print(data.head())
    data.update(data[["postalCode"]].fillna("UNKNOWN"))

       
def save_data(data):
    data.to_csv('./dataset/output/clean.csv')


def put_start(data):
    """Este metodo funciona pero no lo he ejecutado debido al tiempo.
    lo que hace es ir a tripadisor con selenium y busca el nombre y el pais
    y recoge las puntuacion, pero debido al tiempo de ejecuicon de 100000 filas....
    no lo hee ejecutado"""
    driver = get_page('https://www.tripadvisor.es/')
    driver.find_element_by_css_selector('div.brand-global-nav-action-search-Search__searchButton--b9-IK').click()

    data["start"] = data[["name","city"]].apply(get_start,driver=driver,axis = 1)
    driver.close()

def get_longName_state(col,dic = {}):
    try:
        return dic[col].strip()
    except:
        return "u"

def get_poblation(col,dic = {}):
    


    try:
        return dic[col]
    except:
        return 0.0



def main():
    data = open_data()
    #limpiamos de null
    clean_null(data)
      
    """Este metodo funciona pero no lo he ejecutado debido al tiempo.
    lo que hace es ir a tripadisor con selenium y busca el nombre y el pais
    y recoge las puntuacion, pero debido al tiempo de ejecuicon de 100000 filas....
    no lo hee ejecutado"""
    #put_start(data)
    
    #obtengo el nombre largo
    dic = get_state()
    data["longNameProvince"] = data["province"].apply(get_longName_state,dic=dic)
    
    #obtengo la pobación
    dic = get_population()
    data["population"] = data["longNameProvince"].apply(get_poblation,dic=dic)
    #obtengo el indice de obesidad
    dic = get_obese()
    data["percetOvese"] = data["longNameProvince"].apply(get_poblation,dic=dic)
    

    print(data[["longNameProvince","population","percetOvese"]])
    save_data(data)
    
main()


