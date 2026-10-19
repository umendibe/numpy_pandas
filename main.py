import pandas as pd
import numpy as np

url = "https://raw.githubusercontent.com/justmarkham/pandas-videos/master/data/chipotle.tsv"

chipo = pd.read_csv(url, sep="\t")
chipo["item_price"] = (
 	chipo["item_price"]
 	.str.replace("$", "", regex=False)
 	.astype(float)
)

def lehen_ariketa():
    # 1. ARIKETA
        print(chipo[:5])
        print(chipo[-10:])
        errenkada = chipo.shape[0]
        zutabe = chipo.shape[1]
        print(f"ERRENKADA kop: {errenkada}")
        print(f"ZUTABE kop: {zutabe}")
        zutabe_izenak = chipo.columns.tolist()
        print(f"ZUTABE IZENAK: {zutabe_izenak}")
        print("INFORMAZIOA: ")
        print(chipo.info())
        

def bigarren_ariketa():
    print(f"QUANTITY BATAZBESTEKOA: {chipo['quantity'].mean()}")
    print(f"KANTITATE MAXIMOA: {chipo['quantity'].max()}")
    print(f"PREZIO HANDIENA: {chipo['item_price'].max()}")
    print(f"PREZIO TXIKIENA: {chipo['item_price'].min()}")
    print(f"PREZIOEN MEDIANA: {chipo["item_price"].median()}")
    print(f"DESCRIBE: {chipo.describe()}")
        

def hirugarren_ariketa():
    produktu_handiak = chipo[["item_name", "item_price", "quantity"]]
    print(f"LEHEN 15 ERRENKADAK: {produktu_handiak.head(16)}")
    
    
def laugarren_ariketa():
    cb = chipo[chipo['item_name'] == 'Chicken Bowl']
    print(f"CHICKEN BAUL: {cb.shape[0]} ERRENKADA")
    print(cb)
    sb = chipo[chipo['item_name'] == 'Steak Burrito']
    print(f"STEAK BURRITO: {sb.shape[0]} ERRENKADA")
    print(sb)
    k_handia = chipo[chipo['quantity'] > 1]
    print(f"QUANTITY 1 BAINO HANDIAGOA: {k_handia.shape[0]} ERRENKADA")
    print(k_handia)
     
     
def bostgarren_ariketa():
    bost_gehio = chipo[chipo["item_price"] > 5]
    bost_gehio_ordenatua = bost_gehio.sort_values(by="item_price", ascending=False)
    print("5$ BAINO GEHIO: ")
    print(bost_gehio_ordenatua)
    hamar_gehio = chipo[chipo["item_price"] >= 10]
    hamar_gehio_ordenatua = hamar_gehio.sort_values(by="item_price", ascending=False)
    print("10$ EDO GEHIAGO: ")
    print(hamar_gehio_ordenatua)
    bi_bost = chipo[(chipo['item_price'] >= 2) & (chipo['item_price'] <= 5)]
    bi_bost_ordenatua = bi_bost.sort_values(by="item_price", ascending=False)
    print("2 eta 5 DOLAR ARTEAN: ")
    print(bi_bost_ordenatua)
        
        
def seigarren_ariketa():
    errenkada_prezio_arabera = chipo.sort_values(by="item_price", ascending=True)
    print("EMAITZAK PREZIOAREN ARABERA TXIKITIK HANDIRA")
    print(errenkada_prezio_arabera)
    kantitate_arabera = chipo.sort_values(by="quantity", ascending=False)
    print("EMAITZAK KANTITATEAREN ARABERA: ")
    print(kantitate_arabera)
    hamar_prezio_altuenak = chipo.sort_values(by="item_price", ascending=False).head(10)
    print("HAMAR PREZIO ALTUENAK: ")
    print(hamar_prezio_altuenak)
    # ascending=True --> Txikienetik handienera     ascending=False --> Handienetik txikienera
    

def zazpigarren_ariketa():
    hutsak_zutabea = chipo['choice_description'].isnull().sum()
    print(f"ZUTABEAREN BALIO HUTSAK: {hutsak_zutabea}")
    zutabe_hutsak = chipo.isnull().sum()
    print(f"GUZTIRA ZUTABE HUTSAK: {zutabe_hutsak}")
    chipo_berria = chipo.dropna(subset=["choice_description"])
    print("CHIPO BERRIA BALIO HUTSIK GABE: ")
    print(chipo_berria)
    geratutako_errenkadak = chipo_berria.shape[0]
    print(f"GELDITUTAKO ERRENKADAK: {geratutako_errenkadak}")
    # Ez da egokia beti ezabatzea balio hutsak dituzten errenkadak beste zutabeetako informazioa galtzen delako. Errenkada bat ez egoteak ez du esan nahi errenkadak ez duela balio, agian ez da beharrezkoa zutabe horretako informazioa eta null bezala jartzen da.
    
   
def main():
    while True:
        ariketa = int(input("Sartu ariketa zenbakia (1-7) (balio desegokia irtetzeko): "))
        match ariketa:
            case 1:
                lehen_ariketa()
            case 2:
                bigarren_ariketa()
            case 3:
                hirugarren_ariketa()
            case 4:
                laugarren_ariketa()
            case 5:
                bostgarren_ariketa()
            case 6:
                seigarren_ariketa()
            case 7:
                zazpigarren_ariketa()
            case _:
                break
            
            
            
if __name__ == "__main__":
    main()