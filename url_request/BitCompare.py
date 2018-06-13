import re, bs4,requests, time , openpyxl
import nltk   
from urllib import urlopen
import os
os.chdir(r'C:\\Users\pc\\Desktop')
#from pyquery import PyQuery
i=1
j=1

wb = openpyxl.load_workbook('bitcoin.xlsx','w')
sheet=wb.get_sheet_by_name('Sheet1')


while(i!=5):
    res=requests.get("https://www.coingecko.com/en/price_charts/bitcoin/inr")
    #res=requests.get("https://www.coinbase.com/charts?locale=en")
    res.raise_for_status()
    sst=bs4.BeautifulSoup(res.text[0:],"lxml")
    result=sst.select('#wrapper > div.container > div.coingecko.row > div > div.coin-details.row > div.col-md-5.market-value > div.coin-value > span.currency-exchangable')
    #result=sst.select('#chart_react > div > div.PriceChart__Container-klmtfG.fkKUHd.Panel__Container-hCUKEb.kyJbgA > div:nth-child(2) > div.PriceChart__PriceContainer-fkPIYJ.hvlhsT.Flex__Flex-fVJVYW.hQXxaf > div > div.BigAmount__Number-fWXHBq.gBskIE.Flex__Flex-fVJVYW.iDqRrV > span > span:nth-child(1)')
    val=(str(result[0])[64:75])
    sheet.cell(row=1, column=2).value=val
    time.sleep(6)
    i=i+1
    j=j+1


wb.save('bitcoin.xlsx')
