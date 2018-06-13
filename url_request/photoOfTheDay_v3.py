import requests
from bs4 import BeautifulSoup
import re
from win10toast import ToastNotifier
import ctypes
import urllib
import sys

head='Wallpaper Changed'
msg='National Geographic Photo of The Day'

#requests.get("https://www.nationalgeographic.com/photography/photo-of-the-day/")
r=requests.get("https://www.nationalgeographic.com/photography/photo-of-the-day/")
soup = BeautifulSoup(r.text, 'lxml')

k=soup.findAll("meta",{"property":"og:image"})
#url=re.findall(r'http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+',str(k))
url=k[0]["content"]
print url
resource = urllib.urlopen(url)#python2
#resource = urllib.request.urlopen(url)
with open('1.jpg','wb') as output:
    output.write(resource.read())
print('getting imange from....\n'+url)
#urllib.urlretrieve(url, "1.jpg")
ctypes.windll.user32.SystemParametersInfoA(20, 0, "C:/Users/pc/Desktop/py/1.jpg" , 2)#python2
#ctypes.windll.user32.SystemParametersInfoW(SPI_SETDESKWALLPAPER, 0, "C:/Users/pc/Desktop/py/1.jpg" , 2)#python 3
try:
    title=soup.title.text
    print title
    descr=soup.findAll("p",{"itemprop":"caption"})
    print descr[0].text
    toaster = ToastNotifier()
    toaster.show_toast(title,msg,duration=10)
except:
    pass
sys.exit()
