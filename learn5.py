from urllib.request import urlopen
from bs4 import BeautifulSoup
from urllib.error import HTTPError
import re

#导航树,父子标签
#bsObj.body.h1  选择body标签后代第一个h1标签
#bsObj.div.findAll("img") 找出文档第一个div，然后获取div后代里所有img标签列表

url = "http://en.wikipedia.org/wiki/Kevin_Bacon"
html = urlopen(url)
bsObj = BeautifulSoup(html.read(),"html.parser")

for link in bsObj.find("div",{"id":"bodyContent"}).findAll("a",href=re.compile("^(/wiki/)((?!:).)*$")):
    if 'href' in link.attrs:
        print(link.attrs['href'])
