

################################################################################################################

import datetime
import json
from bs4 import BeautifulSoup as bs
import requests
from dataclasses import dataclass

def get_html(url):
    response = requests.get(url)
    return response.text
    print(response)
    print(response.status_code)

html = get_html("https://www.timeanddate.com/holidays/us/")

# print(html)
soup = bs(html, 'html.parser')

# print(soup.prettify())



holidays = []
dateSoup = soup.find('tbody')
# print(dateSoup)
### vvvvvvvvvvvvvvvvvvvvvSORT OF WORK, DON'T MESS UP!!vvvvvvvvvvvvvvvv#########
names = dateSoup.find_all('a')
for name in names:
    holidayNames = {}
    holidayNames['name'] = name.get_text()
    holidays.append(holidayNames)
    # print(holidayNames)
dates = dateSoup.find_all('th', attrs = {'class':'nw'})
for date in dates:
    holidayDates = {}
    holidayDates['date'] = date.get_text()
    holidays.append(holidayDates)
    # print(holidayDates)
### ^^^^^^^^^^^^^^^^^^^^^^SORT OF WORK, DON'T MESS UP!!#########^^^^^^^^^^^^^
# print(holidays)


rows = dateSoup.find_all('tr')
print(type(rows))
print(rows[0])
print(rows[1])
print(rows[2])
print(rows[3])
print(rows[4])
print(rows[5])
print(rows[6])
print(rows[7])
print(rows[8])
print(rows[9])
print(rows[10])
print(rows[11])
print(rows[12])