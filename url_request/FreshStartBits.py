import re, bs4,requests
import nltk   
from urllib import urlopen
#from pyquery import PyQuery

res=requests.get("https://www.zebpay.com/")
res.raise_for_status()
sst=bs4.BeautifulSoup(res.text[0:],"html.parser")
#result=sst.select('#main-wrapper.hometriston > header#top.header.app > div.overlay > nav.navbar navbar-fixed-top.is-scrolling > div.container > div.row > div.col-md-12 > div.navbar-header > div#bitlabel > a.bitcoin-buy-price > span#buy')
result=sst.select('#main-wrapper.hometriston > header#top.header.app > div.overlay > nav.navbar.navbar-fixed-top > div.container > div.row > div.col-md-12 > div.navbar-header > div#bitlabel > a.bitcoin-buy-price > span#buy')
print(result)
