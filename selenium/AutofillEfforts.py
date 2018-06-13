#! python2.7
from selenium import webdriver
import base64
import time
import datetime
import pyautogui
from secrets import wipromail, passcode
br=webdriver.Chrome()
br.maximize_window()
br.get("https://web.whatsapp.com/")
time.sleep(10)
print("success")


'''
wipro_lim = br.find_element_by_xpath("/html/body/div[2]/div[2]/div[1]/div[2]/div/form/div[1]/div[2]/div/span")
wipro_lim.click()
time.sleep(2)

user = br.find_element_by_id('userNameInput')
user.send_keys(wipromail)

passw = br.find_element_by_id('passwordInput')
passw.send_keys(base64.b64decode(passcode))

submit = br.find_element_by_id('submitButton')
submit.click()
time.sleep(10)

mytime = br.find_element_by_xpath("/html/body/div[11]/div[4]/div/section/article/div[2]/ul/li[1]/a/div/span/p")
mytime.click()
time.sleep(10)
'''
#Day of week
t_day=datetime.datetime.today().weekday()


frame = br.find_element_by_xpath('//*[@id="divMainmyWiproPortalViewFrame"]')
br.switch_to.frame(frame)
efforts=br.find_element_by_id('tmsMobileId')
efforts.click()
time.sleep(10)

#frame = br.find_element_by_xpath('//*[@id="divMainmyWiproPortalViewFrame"]')
#br.switch_to.frame(frame)
#time.sleep(10)
st=['0', '_', '0', '_', '0', '_', '0']
for i in range(t_day):
    st[0]=str(i)
    d1=br.find_element_by_id("".join(st))
    d1.send_keys("9.50")   

e_submit=br.find_element_by_id('submitdata')
e_submit.click()
    

