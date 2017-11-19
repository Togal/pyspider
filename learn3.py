from urllib.request import urlopen
from bs4 import BeautifulSoup
from urllib.error import HTTPError

#导航树,父子标签
#bsObj.body.h1  选择body标签后代第一个h1标签
#bsObj.div.findAll("img") 找出文档第一个div，然后获取div后代里所有img标签列表

url = "http://www.pythonscraping.com/pages/page3.html"
html = urlopen(url)
bsObj = BeautifulSoup(html.read(),"html.parser")

for sibling in bsObj.find("table",{"id":"giftList"}).tr.next_siblings:
    print(sibling)

print("price: "+bsObj.find("img",{"src":"../img/gitfs/img1.jpg"}).parent.previous_sibling.get_text())
