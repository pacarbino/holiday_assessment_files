import datetime
import json
from bs4 import BeautifulSoup as bsoup
import requests
from dataclasses import dataclass

def get_html(url):
    response = requests.get(url)
    return response.text
    print(response)
    print(response.status_code)

html = get_html("https://www.timeanddate.com/holidays/us/")

# print(html)
# soup = bsoup(html, 'html.parser')

# print(soup)
class Holiday:
    """Holiday Class:
    """
    
    def __init__(self, name, date):
        #Your Code Here        
        self.__name = name
        self.__date = date

    def get_Holiday_name(self):
        return self.__name

    def get_Holiday_date(self):
        return self.__date

    def __str__(self):
        # String output
        # Holiday output when printed.
        return f"{self.__name} : {self.__date}"


holiday1 = Holiday("Festivus","22022-12-23")
print(holiday1)
print(type(holiday1) == Holiday)

innerHolidays = []

holiday2 = Holiday("Chrimbus", "2022-12-25")

class HolidayList:
    def __init__(self):
       self.innerHolidays = []
   
    def addHoliday(holidayObj):
        # Make sure holidayObj is an Holiday Object by checking the type
        print(f"Checking to see if '{holidayObj}' is a valid Holiday:")
        if type(holidayObj) == Holiday:
        # Use innerHolidays.append(holidayObj) to add holiday
            print(f"'{holidayObj}' has been validated!")
            innerHolidays.append(holidayObj) ### Works!!
        # print to the user that you added a holiday
            print(f"'{holidayObj}' has been added to the Holiday List!") ### Works!!
        else:
            print(f"'{holidayObj}' isn't working... Please make sure that you're adding a Holiday Object and not something else.") ### Works!!
    

HolidayList.addHoliday(holiday1)
HolidayList.addHoliday(holiday2)

def findHoliday(HolidayName, Date):
        # Find Holiday in innerHolidays
    for holiday in innerHolidays:


def numHolidays():
        # Return the total number of holidays in innerHolidays
        return len(innerHolidays)
print(numHolidays())

def findHoliday(HolidayName, Date): ### Does not work...
        # Find Holiday in innerHolidays
        print(f"Searching for {HolidayName} : {Date}.")
        x = Holiday(HolidayName, Date)
        if x in innerHolidays:
            foundHoliday = x 
            print(f"{foundHoliday} has been located!")
            return foundHoliday

findHoliday("Festivus", "2022-21-23")

print(innerHolidays[0])
# help(Holiday)