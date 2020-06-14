import requests
from bs4 import BeautifulSoup
 
url = "https://pokemondb.net/sprites"
    
html_doc = requests.get(url).text
soup = BeautifulSoup(html_doc, 'html.parser')
    
icons = soup.find_all("span", class_="img-fixed icon-pkmn")
    
for icon in icons:
    image = requests.get(icon["data-src"])
    open(icon["data-alt"][:-5] + ".png", "wb").write(image.content)