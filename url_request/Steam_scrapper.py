import requests
import lxml.html
from pprint import pprint



html = requests.get('https://store.steampowered.com/explore/new/')
doc = lxml.html.fromstring(html.content)
new_releases = doc.xpath('//div[@id="tab_newreleases_content"]')[0]
#print new_releases


titles = new_releases.xpath('.//div[@class="tab_item_name"]/text()')
#print titles
prices = new_releases.xpath('.//div[@class="discount_final_price"]/text()')

tags = [tag.text_content() for tag in new_releases.xpath('.//div[@class="tab_item_top_tags"]')]
tags = [tag.split(', ') for tag in tags]

platforms_div = new_releases.xpath('.//div[@class="tab_item_details"]')
total_platforms = []

for game in platforms_div:
    temp = game.xpath('.//span[contains(@class, "platform_img")]')
    platforms = [t.get('class').split(' ')[-1] for t in temp]
    if 'hmd_separator' in platforms:
        platforms.remove('hmd_separator')
    total_platforms.append(platforms)
output = []
for info in zip(titles,prices, tags, total_platforms):
    resp = {}
    resp['platforms'] = info[3]
    resp['tags'] = info[2]
    resp['price'] = info[1]
    resp['title'] = info[0]
    output.append(resp)

pprint( output)
