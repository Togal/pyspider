from urllib.request import urlopen
from bs4 import BeautifulSoup
from urllib.error import HTTPError

url = "http://www.pythonscraping.com/pages/warandpeace.html"
html = urlopen(url)
bsObj = BeautifulSoup(html.read(),"html.parser")

#查找符合标签的内容
nameList = bsObj.findAll("span",{"class":"green"})
#bsObj.findAll(id="text")
#bsObj.findAll("", {"id":"text"})
#bsObj.findAll(class_="green")

for name in nameList:
    print(name.get_text())

#查找网页文本内容
textList = bsObj.findAll(text="the prince")
print(len(textList))
