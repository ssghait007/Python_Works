from selenium import webdriver

import time

import urllib

import urllib2

import requests

import ctypes

import sys

import os

import pyautogui

from win10toast import ToastNotifier

 

SPI_SETDESKWALLPAPER = 20

head='Wallpaper Changed'

msg='National Geographic Photo of The Day'

proxi = {

  'http': 'http://10.201.51.71:8080'

}

 

br=webdriver.Chrome()

br.maximize_window()

pyautogui.moveTo(1165,11)

pyautogui.click()

br.get("https://www.nationalgeographic.com/photography/photo-of-the-day/")

time.sleep(2)

try:

    close=br.find_element_by_xpath('//*[@id="1440664_ltBoxMap"]/area[2]')

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

 

 

print(url)

#urllib.urlretrieve(url, "1.jpg")

 

#C:\Users\sa358861\Desktop\py\eff

 

img = urllib2.urlopen(url)

with open('1.jpg','wb') as output:

  output.write(img.read())

ctypes.windll.user32.SystemParametersInfoA(20, 0, os.path.abspath("1.jpg") , 0)

try:

    toaster = ToastNotifier()

    toaster.show_toast(head,msg,duration=100)

except:

    pass

 

br.close()

sys.exit()
