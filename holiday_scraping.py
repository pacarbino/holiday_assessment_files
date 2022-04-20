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
dates = dateSoup.find_all('th', attrs = {'class':'nw'})

# for i in dates: 
print(dates)
# for item in dateSoup.find_all('tr', attrs = {'class':'showrow'}):
#     holiday = {}
#     holiday['date'] = item.find('th').text
#     holidays.append(holiday)
# print(holidays)    
    

###########################################################################################
# class Holiday:
#     """Holiday Class"""
#     def __init__(self, name, date):
#         #Your Code Here        
#         self.__name = name
#         self.__date = date
    

#     def __str__(self):
#         # String output
#         # Holiday output when printed.
#         return f"{self.__name} : {self.__date}"


# holiday1 = Holiday("Festivus","22022-12-23")
# print(holiday1)
# print(type(holiday1) == Holiday)

# innerHolidays = []

# holiday2 = "Chrimbus : 2022-12-25"

# class HolidayList:
#     def __init__(self):
#        self.innerHolidays = []
   
#     def addHoliday(holidayObj):
#         # Make sure holidayObj is an Holiday Object by checking the type
#         if type(holidayObj) == Holiday:
#         # Use innerHolidays.append(holidayObj) to add holiday
#             innerHolidays.append(holidayObj) ### ???
#         # print to the user that you added a holiday
#             print(f"\"{holidayObj}\" has been added to the Holiday List!")
#         else:
#             print(f"\"{holidayObj}\" isn't working... Please make sure that you're adding a Holiday Object and not something else.")

# HolidayList.addHoliday(holiday1)
# HolidayList.addHoliday(holiday2)

# def findHoliday(HolidayName, Date):
#         # Find Holiday in innerHolidays
#         foundHoliday = HolidayList.find(HolidayName, Date)
#         return foundHoliday

# def numHolidays():
#         # Return the total number of holidays in innerHolidays
#         return len(innerHolidays)
# print(numHolidays())