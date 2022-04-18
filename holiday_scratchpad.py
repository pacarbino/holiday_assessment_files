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

print(html)
soup = bsoup(html, 'html.parser')

# print(soup)
class Holiday:
    """Holiday Class:
    Holiday(name, date)

    __init__(self, name, date)
        Initialize self

    get_Holiday_name(self)

    get_Holiday_date(self)

    __str__(self):
        String output of Holiday
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

halloween = Holiday("Halloween", "2022-10-31")

print(holiday2.get_Holiday_name())
print(holiday2.get_Holiday_date())

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
    

HolidayList.addHoliday(holiday1)  ###TEST VVV
HolidayList.addHoliday(holiday2)
HolidayList.addHoliday(halloween)

def numHolidays():
        # Return the total number of holidays in innerHolidays
        return len(innerHolidays)
print(numHolidays())

def findHoliday(HolidayName, Date):
        # Find Holiday in innerHolidays
        print(f"Searching for {HolidayName} : {Date}.")
        if Holiday(HolidayName, Date):
            print(f"{HolidayName} : {Date} has been located!")
            return Holiday(HolidayName, Date)
        else:
            print(f"{HolidayName} : {Date} does not appear to be on our list.")

findHoliday("Festivus", "2022-21-23")
print(findHoliday("Festivus", "2022-21-23"))

# def removeHoliday(HolidayName, Date):  ##not working at all...
#     # Find Holiday in innerHolidays by searching the name and date combination.
#     print(f"Searching for {HolidayName} : {Date}.")
#     if Holiday(HolidayName, Date):
#         print(f"{HolidayName} : {Date} has been located!")
#     # remove the Holiday from innerHolidays
#         del Holiday(HolidayName, Date)
#     # inform user you deleted the holiday
#         print(f"{HolidayName} : {Date} has been deleted!")
#     else:
#         print(f"{HolidayName} : {Date} does not appear to be on our list.")

# removeHoliday("Halloween", "2022-10-31")

print(len(innerHolidays))
# help(Holiday)