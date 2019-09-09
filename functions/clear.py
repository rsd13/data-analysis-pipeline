import pandas as pd
from trya import get_start,get_page
from we_scraping import  get_state,get_population,get_obese
import spacy
import nltk


#https://en.wikipedia.org/wiki/List_of_states_and_territories_of_the_United_States_by_population
#https://en.wikipedia.org/wiki/Obesity_in_the_United_States


def open_data():
    name = "Datafiniti_Pizza_Restaurants_and_the_Pizza_They_Sell_May19.csv"
    url = "../dataset/input/"
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
    data.to_csv('../dataset/output/clean.csv')


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
    """metodo que dado un codigo de estado da
    su nombre largo"""
    try:
        return dic[col].strip()
    except:
        return "u"

def get_poblation(col,dic = {}):
    """metodo que dado un nombre dee estado
    consiguee su rango de obesidad"""
    
    try:
        return dic[col]
    except:
        return 0.0

def get_categories(col):

    if "italian" in col.lower() or "pizza" in col.lower():
        return "italian"
    elif "american" in col.lower():
        return "american"
    else:
        return "u"

def get_categorias(data):
    """metodo que a través de nlp mira el top 5 de 
    categorias"""

    #obtengo la cadena
    string = " "
    result = string.join(data["categories"].apply(lambda col: col))
    
    nlp = spacy.load('en_core_web_sm')
    doc = nlp(result)
    #lo tokenizo
    #frecuencias = nltk.FreqDist(corpus)
    corpus = []
    for token in doc:
        #me quedo con las 'keywords'
        if(token.pos_ == "NOUN"  or token.pos_ == "VERB"  or
          token.pos_ == "ADJ" or token.pos_ == "ADV" ):
            corpus.append(token.lemma_)
    #lo transformo en lista por que nltk trabaja con listas

    frecuencias = nltk.FreqDist(corpus)
    print(frecuencias.most_common(50))

    print("veo que las categorias unicas son italian, american. Por lo tanto voy \
        hacer el analisis sobre esas dos, además si en la frasee hay pizza lo etiquetaré \
        como italian")


    data["categories"] = data["categories"].apply(get_categories)


def data_clear():
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
    data["percentObese"] = data["longNameProvince"].apply(get_poblation,dic=dic)
    
    #por último en categoría voy a ver que categorias se repiten mas
    get_categorias(data)

    save_data(data)
    



