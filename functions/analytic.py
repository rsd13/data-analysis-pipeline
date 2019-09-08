import pandas as pd 


def open_data():
    name = "clean.csv"
    url = "./dataset/output/"
    data = pd.read_csv(url + name)
    return data


    

def main():
    data = open_data()
    


main()