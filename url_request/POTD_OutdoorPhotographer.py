import requests
from bs4 import BeautifulSoup
import re
from win10toast import ToastNotifier
import ctypes
import urllib
import sys

head='Wallpaper Changed'
msg='National Geographic Photo of The Day'

r=requests.get("https://www.outdoorphotographer.com/category/photo-of-the-day/")
soup = BeautifulSoup(r.text, 'lxml')

k=soup.findAll("div",{"class":"btn btn-round-c btn-xlg btn-outline-b btn-read-more"})
url=re.findall(r'http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+',str(k))
r=requests.get(url[0])
soup = BeautifulSoup(r.text, 'lxml')
k=soup.findAll("img",{"class":"size-full wp-image-579489"})
url=re.findall(r'http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+',str(k))
# resource = urllib.urlopen(url[0])#python2
resource = urllib.request.urlopen(url)
output = open("2.jpg","wb")
output.write(resource.read())
output.close()
print(url[0])
#urllib.urlretrieve(url, "1.jpg")
ctypes.windll.user32.SystemParametersInfoA(20, 0, "C:/Users/pc/Desktop/py/2.jpg" , 2)#python2
#ctypes.windll.user32.SystemParametersInfoW(SPI_SETDESKWALLPAPER, 0, "C:/Users/pc/Desktop/py/1.jpg" , 2)#python 3

toaster = ToastNotifier()
toaster.show_toast(head,msg,duration=10)

sys.exit()
print ("done")
