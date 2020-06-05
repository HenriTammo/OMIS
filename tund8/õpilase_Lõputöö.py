import requests
from bs4 import BeautifulSoup
def soupify(url):
    source_code = requests.get(url)
    plain_text = source_code.text
    soup = BeautifulSoup(plain_text,'html.parser')
    return soup
def ranna_nimi(soup):
    for rand in (soup.find_all("span", {"class" : "title"})):
        title = rand.get_text()
        print( title)

def air_temp(soup):
    for air in (soup.find_all("span", {"class" : "temp-label air"})):
        air_temp = air.get_text()
        print (air_temp)

def water_temp(soup):
    for water in (soup.find_all("span", {"class" : "temp-label water"})):
        water_temp = water.get_text()
        print(water_temp)


ilmataat ="https://www.ilmataat.ee/rannailm/nimekiri"
soup = soupify(ilmataat)

ranna_nimi(soup)
air_temp(soup)
water_temp(soup)
