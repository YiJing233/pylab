from urllib.request import urlopen
from bs4 import BeautifulSoup
html = urlopen('https://cloud.tencent.com/developer/article/1173754')

bs = BeautifulSoup(html.read(),'html.parser')
print(bs.h1)