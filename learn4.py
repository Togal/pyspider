from urllib.request import urlopen
from bs4 import BeautifulSoup
from urllib.error import HTTPError
import re

#导航树,父子标签
#bsObj.body.h1  选择body标签后代第一个h1标签
#bsObj.div.findAll("img") 找出文档第一个div，然后获取div后代里所有img标签列表

url = "http://www.pythonscraping.com/pages/page3.html"
html = urlopen(url)
bsObj = BeautifulSoup(html.read(),"html.parser")

images = bsObj.findAll("img",{"src":re.compile("\.\.\/img\/gifts/img.*\.jpg")})
for image in images:
    print(image["src"])

#对于一个标签对象，通过myTag.attrs获取它的全部树形。
#获取资源位置src,myImgTag.attrs["src"]
