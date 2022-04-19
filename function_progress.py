import datetime
from datetime import timedelta
from datetime import datetime as dt
import itertools
import json
from bs4 import BeautifulSoup
import requests
from dataclasses import dataclass


# -------------------------------------------
# Modify the holiday class to 
# 1. Only accept Datetime objects for date.
# 2. You may need to add additional functions
# 3. You may drop the init if you are using @dataclasses
# --------------------------------------------

class Holiday:
    """Holiday Class"""

    def __init__(self, name, date): ##call constructor to turn string date into datetime object.
        #Your Code Here 
        # if type(dateFormat) != datetime.datetime:
        #     print("Please enter a valid date in the format: 'yyyy-mm-dd'.")
        self.__name = name
        self.__date = dt.strptime(date,'%Y-%m-%d').strftime('%B %d, %Y')

    def get_Holiday_name(self):
        return self.__name

    def get_Holiday_date(self):
        return self.__date

    def __str__(self): ##make sure date is in the right format.
        # String output
        # Holiday output when printed.
        return f"{self.__name} : {self.__date}"
          
           
# -------------------------------------------
# The HolidayList class acts as a wrapper and container
# For the list of holidays
# Each method has pseudo-code instructions
# --------------------------------------------
class HolidayList:
    ## __init__:
    def __init__(self):
        self.innerHolidays = []
   
    
    ## addHoliday:
    def addHoliday(self, holidayObj): ## WORKS!!
        # Make sure holidayObj is an Holiday Object by checking the type
        print(f"Checking to see if '{holidayObj}' is a valid Holiday:")
        if type(holidayObj) == Holiday:
            if str(holidayObj) in self.innerHolidays:
                print(f"Looks like {holidayObj} is already on the list!")
            # Use innerHolidays.append(holidayObj) to add holiday
            else:
                print(f"'{holidayObj}' has been validated!")
                self.innerHolidays.append(str(holidayObj))
                print(f"'{holidayObj}' has been added to the Holiday List!") 
        else:
            print(f"'{holidayObj}' isn't working... Please make sure that you're adding a Holiday Object and not something else.")
    
    ## findHoliday:  ## NOT WORKING, COME BACK LATER!!!!!!!!!*****************************************
    def findHoliday(self, HolidayName, date):
        holidayObj = Holiday(HolidayName, date)
        print(f'Searching for {holidayObj}:')
        if str(holidayObj) in self.innerHolidays:
            # Find Holiday in innerHolidays
            print(f'{holidayObj} found!')
            # Return Holiday
            return holidayObj
        else:
            print(f"'{holidayObj}' does not appear to be on our list... Please check your input or try adding it.")

    ## read_json: ##  WORKS!!!
    def read_json(self, filelocation):  ##  WORKS!!!
        # Read in things from json file location
        f = open(filelocation)
        holidayInfo = json.load(f)
        # print(holidayInfo) ## test
        for x in list(holidayInfo.values())[0]:
            # print(list(x.values())) ## test
            name = list(x.values())[0]
            date = list(x.values())[1]
            newHoliday = Holiday(name, date)
            self.addHoliday(newHoliday)
        f.close()

    ## numHolidays: ## WORKS!!
    def numHolidays(self):
        # Return the total number of holidays in innerHolidays
        return len(self.innerHolidays)

    ## removeHoliday: ##WORKS!!
    def removeHoliday(self, HolidayName, Date):
        holidayObj = Holiday(HolidayName, Date)
        print(f'Searching for {holidayObj}:')
    # Find Holiday in innerHolidays by searching the name and date combination.
        if str(holidayObj) in self.innerHolidays:
            print(f'{holidayObj} found: Removing {holidayObj} from list:')
            # remove the Holiday from innerHolidays
            self.innerHolidays.remove(str(holidayObj))
            # inform user you deleted the holiday
            print(f'{holidayObj} removed!')
            



######TESTING#######

mainHolidayList = HolidayList() ### MUST ADD INSTANCE OF CLASS!!! (mainHolidayList is an instance of HolidayList. Without that, you have plans, but no actual object with any of the properties.)

######TESTING#######
## test Holiday class: ## Holiday class WORKS
xmas = Holiday('Christmas', '2022-12-25') ### these will be made internally with json import
halloween = Holiday('Halloween', '2022-10-31')
print(halloween)
print(Holiday.get_Holiday_date(halloween))
print(Holiday.get_Holiday_name(xmas))
halloween2 = Holiday('Halloween', '2022-10-31')
## test(HolidayList class): ## HolidayList class WORKS
print(len(mainHolidayList.innerHolidays))
mainHolidayList.addHoliday(halloween)
mainHolidayList.addHoliday(xmas)
print(len(mainHolidayList.innerHolidays))
print('****TEST FLAG****')
mainHolidayList.addHoliday(halloween2) ##FIXED!! append str(holidayObj), not holidayObj.
print('****TEST FLAG****')
print(len(mainHolidayList.innerHolidays))
festivus = Holiday('Festivus', '2022-12-23')
mainHolidayList.addHoliday(festivus)
print(len(mainHolidayList.innerHolidays))

## test mainHolidayList.findHoliday: ## mainHolidayList.findHoliday 
print('****TEST FLAG****')
mainHolidayList.findHoliday('Festivus', '2022-12-23') ### working!! (added str(holidayObj))
print('****TEST FLAG****')
##test mainHolidayList.read_json: ## mainHolidayList.read_json WORKS!!
mainHolidayList.read_json('holiday_startercode.txt')

## test mainHolidayList.numHolidays(): mainHolidayList.numHolidays() WORKS!!
print(mainHolidayList.numHolidays())

for x in mainHolidayList.innerHolidays:
    print(x)

for index, holiday in enumerate(mainHolidayList.innerHolidays):
    print(f'{index}: {holiday}')

## test removeHoliday:
mainHolidayList.removeHoliday('Halloween', '2022-10-31')

for index, holiday in enumerate(mainHolidayList.innerHolidays):
    print(f'{index}: {holiday}')




#     def save_to_json(filelocation):
#         # Write out json file to selected file.
        
#     def scrapeHolidays():
#         # Scrape Holidays from https://www.timeanddate.com/holidays/us/ 
#         # Remember, 2 previous years, current year, and 2  years into the future. You can scrape multiple years by adding year to the timeanddate URL. For example https://www.timeanddate.com/holidays/us/2022
#         # Check to see if name and date of holiday is in innerHolidays array
#         # Add non-duplicates to innerHolidays
#         # Handle any exceptions.     

#     def numHolidays():
#         # Return the total number of holidays in innerHolidays
    
#     def filter_holidays_by_week(year, week_number):
#         # Use a Lambda function to filter by week number and save this as holidays, use the filter on innerHolidays
#         # Week number is part of the the Datetime object
#         # Cast filter results as list
#         # return your holidays

#     def displayHolidaysInWeek(holidayList):
#         # Use your filter_holidays_by_week to get list of holidays within a week as a parameter
#         # Output formated holidays in the week. 
#         # * Remember to use the holiday __str__ method.

#     def getWeather(weekNum):
#         # Convert weekNum to range between two days
#         # Use Try / Except to catch problems
#         # Query API for weather in that week range
#         # Format weather information and return weather string.

#     def viewCurrentWeek():
#         # Use the Datetime Module to look up current week and year
#         # Use your filter_holidays_by_week function to get the list of holidays 
#         # for the current week/year
#         # Use your displayHolidaysInWeek function to display the holidays in the week
#         # Ask user if they want to get the weather
#         # If yes, use your getWeather function and display results



# def main():
#     # Large Pseudo Code steps
#     # -------------------------------------
#     # 1. Initialize HolidayList Object
#     # 2. Load JSON file via HolidayList read_json function
#     # 3. Scrape additional holidays using your HolidayList scrapeHolidays function.
#     # 3. Create while loop for user to keep adding or working with the Calender
#     # 4. Display User Menu (Print the menu)
#     # 5. Take user input for their action based on Menu and check the user input for errors
#     # 6. Run appropriate method from the HolidayList object depending on what the user input is
#     # 7. Ask the User if they would like to Continue, if not, end the while loop, ending the program.  If they do wish to continue, keep the program going. 


# if __name__ == "__main__":
#     main();


# # Additional Hints:
# # ---------------------------------------------
# # You may need additional helper functions both in and out of the classes, add functions as you need to.
# #
# # No one function should be more then 50 lines of code, if you need more then 50 lines of code
# # excluding comments, break the function into multiple functions.
# #
# # You can store your raw menu text, and other blocks of texts as raw text files 
# # and use placeholder values with the format option.
# # Example:
# # In the file test.txt is "My name is {fname}, I'm {age}"
# # Then you later can read the file into a string "filetxt"
# # and substitute the placeholders 
# # for example: filetxt.format(fname = "John", age = 36)
# # This will make your code far more readable, by seperating text from code.





