# -*- coding: utf-8 -*-
"""
Created on Tue Apr 26 2022
@author: Carlos Rodriguez
"""

import requests
from bs4 import BeautifulSoup
import json

start_url = 'https://ordi.eu/sulearvutid?___store=en&___from_store=et'
lista=[]
data = {'Title': '',
        'Price': '',
        'Picture href': ''}
# print(page)


def parse(start_urls):
    page = requests.get(start_urls)
    soup = BeautifulSoup(page.text, 'html.parser')
    # print (soup)

    items_list = soup.find_all("li", class_=["item first", "item", "item last"])
    # print(items_list)


    for item in items_list:
        data['Title'] = item.h2.get_text()
        data['Price'] = item.find('div', class_='price-box').text.strip()
        data['Picture href'] = item.a['href']
        lista.append(data)
        #j=json.dumps(data, indent=4,sort_keys=True, separators=(',', ': '))
        #print(data)


        #print(json_object)

    try:
        next_page = soup.find("a", class_='next')['href']
        if next_page:
            print(next_page)
            parse(next_page)
    except:
        print("No more pages")


if __name__ == '__main__':
    parse(start_url)
    with open('BeautySoup.json', 'w') as file:
        json.dump(lista, file)




