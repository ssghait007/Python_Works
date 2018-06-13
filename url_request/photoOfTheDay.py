from selenium import webdriver
import time
import urllib
import ctypes
import sys

SPI_SETDESKWALLPAPER = 20


br=webdriver.Chrome()
br.maximize_window()
br.get("https://www.nationalgeographic.com/photography/photo-of-the-day/")
time.sleep(2)
try:
    close=br.find_element_by_xpath('//*[@id="1440664_ltBoxMap"]/area[2]')
    close.click()
except:
    pass
time.sleep(5)

img=br.find_element_by_xpath('//*[@id="article__body"]/span[2]/div/div[1]/div/div/div/div/div/div/div[1]/div[1]/figure/div/div/div/div/div/picture/source')
lst=img.get_attribute("srcset")
urlst=lst.split(" ")
try:
    url=urlst[urlst.index(u'2048w')-1]
except:
    url=urlst[-2]


#print(url)
urllib.urlretrieve(url, "1.jpg")
ctypes.windll.user32.SystemParametersInfoA(SPI_SETDESKWALLPAPER, 0, "C:/Users/pc/Desktop/py/1.jpg" , 0)

br.close()
sys.exit()
