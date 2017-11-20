from urllib.request import urlretrieve,urlopen
from bs4 import BeautifulSoup

html = urlopen("http://www.pythonscraping.com")
bsObj = BeautifulSoup(html)
imageLocation = bsObj.find("a",{"id":"logo"}).find("img")['src']
#下载图片
urlretrieve(imageLocation,"logo.jpg")
