

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


# table = soup.find('section', attrs = {'class':'table-data__table'})
# print(table)
# for row in table.find_all('th'):
holidays = []
dateSoup = soup.find('tbody')
# print(dateSoup)

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
# for i in dates: 
# print(holidayDates)
print(holidays)

# for item in dateSoup.find_all('tr', attrs = {'class':'showrow'}):
#     holiday = {}
#     holiday['date'] = item.find('th').text
#     holidays.append(holiday)
# print(holidays)    
    