#!python2
from selenium import webdriver
import time
import urllib#python2
#import urllib.request
import ctypes
import sys
from win10toast import ToastNotifier
import pyautogui

SPI_SETDESKWALLPAPER = 20
head='Wallpaper Changed'
msg='National Geographic Photo of The Day'

br=webdriver.Chrome()
br.maximize_window()
pyautogui.moveTo(1276,7)
pyautogui.click()
#br.minimize_window()
br.get("https://www.nationalgeographic.com/photography/photo-of-the-day/")
time.sleep(2)
try:
    close=br.find_element_by_xpath('/html/body/div[1]/div[2]/div/map/area[2]')
    #/html/body/div[1]/div[2]/div/map/area[2]
    close.click()
    

except:
    pass
time.sleep(5)
title=br.find_element_by_xpath('/html/body/div[4]/section/article/div/div[2]/div[2]/span[2]/div/div[1]/div/div/div/div/figcaption/div/div[1]/span[2]')
head=title.text
title_msg=br.find_element_by_xpath('/html/body/div[4]/section/article/div/div[2]/div[2]/span[2]/div/div[1]/div/div/div/div/figcaption/div/div[1]/span[3]/p')
msg=title_msg.text
img=br.find_element_by_xpath('//*[@id="article__body"]/span[2]/div/div[1]/div/div/div/div/div/div/div[1]/div[1]/figure/div/div/div/div/div/picture/source')
lst=img.get_attribute("srcset")
urlst=lst.split(" ")
try:
    url=urlst[urlst.index(u'2048w')-1]
except:
    url=urlst[-2]
resource = urllib.urlopen(url)#python2
#resource = urllib.request.urlopen(url)
output = open("1.jpg","wb")
output.write(resource.read())
output.close()
print(url)
#urllib.urlretrieve(url, "1.jpg")
ctypes.windll.user32.SystemParametersInfoA(SPI_SETDESKWALLPAPER, 0, "C:/Users/pc/Desktop/py/1.jpg" , 2)#python2
#ctypes.windll.user32.SystemParametersInfoW(SPI_SETDESKWALLPAPER, 0, "C:/Users/pc/Desktop/py/1.jpg" , 2)#python 3

toaster = ToastNotifier()
toaster.show_toast(head,msg,duration=100)

br.close()
sys.exit()



