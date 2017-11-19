from urllib.request import urlopen
from bs4 import BeautifulSoup
from urllib.error import HTTPError

url = "http://www.pythonscraping.com/pages/warandpeace.html"
html = urlopen(url)
bsObj = BeautifulSoup(html.read(),"html.parser")
nameList = bsObj.findAll("span",{"class":"green"})

for name in nameList:
    print(name.get_text())


