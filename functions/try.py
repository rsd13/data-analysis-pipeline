import requests
from selenium import webdriver
from bs4 import BeautifulSoup


import time

def get_page(url):
    try:
        driver = webdriver.Firefox()
        driver.get(url)
        html = driver.page_source
    except:
        ValueError ("Conexión incorrecta")
       

    return driver
    

def find_restaurant(driver,name,city):
    boton = driver.find_element_by_css_selector('div.brand-global-nav-action-search-Search__searchButton--b9-IK')
    boton.click()
    time.sleep(2)
    
    name_restaurant = driver.find_element_by_id("mainSearch")
    name_restaurant.send_keys("Sauce Pizza Wine")

    name_state = driver.find_element_by_id("GEO_SCOPED_SEARCH_INPUT")
    name_state.send_keys("Phoenix")
    
    
    time.sleep(2)
    boton = driver.find_element_by_id("SEARCH_BUTTON")


    boton.click()
    time.sleep(2)

    #driver.find_element_by_class_name('location-meta-block').click()

    html = driver.page_source
    #prw_rup prw_common_responsive_rating_and_review_count
    soup = BeautifulSoup(html,'html.parser')
  
    div = soup.find("div","prw_rup prw_common_responsive_rating_and_review_count")
    span = div.find("span")
   
    start = span.get("alt")
    start = start.split(" ")[0]
    return start
    


def main():

    driver = get_page('https://www.tripadvisor.es/')
    find_restaurant(driver,"Sauce Pizza Wine","Phoenix")
    
main()