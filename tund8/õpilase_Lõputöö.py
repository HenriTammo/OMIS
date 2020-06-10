import requests
from bs4 import BeautifulSoup
def soupify(url):
    source_code = requests.get(url)
    plain_text = source_code.text
    soup = BeautifulSoup(plain_text,'html.parser')
    return soup
def ranna_nimi(soup):
    title_list = []
    for rand in (soup.find_all("span", {"class" : "title"})):
        title = rand.get_text()
        title_list.append(title)
    return title_list

def air_temp(soup):
    air_list = []
    for air in (soup.find_all("span", {"class" : "temp-label air"})):
        air_temp = air.get_text()
        air_list.append(air_temp)
    return air_list

def water_temp(soup):
    water_list = []
    for water in (soup.find_all("span", {"class" : "temp-label water"})):
        water_temp = water.get_text()
        water_list.append(water_temp)
    return water_list

ilmataat ="https://www.ilmataat.ee/rannailm/nimekiri"
soup = soupify(ilmataat)

titles = ranna_nimi(soup)
air = air_temp(soup)
water = water_temp(soup)

for x in range (len(titles)):
    print(titles[x], air[x], water[x])