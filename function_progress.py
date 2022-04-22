import datetime
from datetime import timedelta
from datetime import datetime as dt
import itertools
import json
from bs4 import BeautifulSoup as bs
import requests
from dataclasses import dataclass


# -------------------------------------------
# Modify the holiday class to 
# 1. Only accept Datetime objects for date.
# 2. You may need to add additional functions
# 3. You may drop the init if you are using @dataclasses
# --------------------------------------------
##################################################################################################
class Holiday:
    """Holiday Class"""

    def __init__(self, name, date): ##call constructor to turn string date into datetime object.
        #Your Code Here 
        self.name = name
        self.date = dt.strptime(date,'%Y-%m-%d')#.strftime('%B %d, %Y')

    def get_Holiday_name(self):
        return self.name

    def get_Holiday_date(self):
        return self.date

    def __str__(self): ##make sure date is in the right format.
        # String output
        # Holiday output when printed.
        # return f"{self.__name} : {self.__date}"
        return f"{{'name:' '{self.name}', 'date:' '{self.date}'}}"
#############################################################################################          
           
# -------------------------------------------
# The HolidayList class acts as a wrapper and container
# For the list of holidays
# Each method has pseudo-code instructions
# --------------------------------------------
#############################################################################################
class HolidayList:
    ## __init__:
    def __init__(self):
        self.innerHolidays = []
       
    ## addHoliday:
    def addHoliday(self, holidayObj): ## WORKS!!        ####### invalid entry breaks interface, needs fixing!!!!!!!!!!!!!
        # Make sure holidayObj is an Holiday Object by checking the type
        print(f"Checking to see if '{holidayObj}' is a valid Holiday:")
        if type(holidayObj) == Holiday:
            if str(holidayObj) in self.innerHolidays:
                print(f"Looks like '{holidayObj}' is already on the list!")
            # Use innerHolidays.append(holidayObj) to add holiday
            else:
                print(f"'{holidayObj}' has been validated!")
                # self.innerHolidays.append(str(holidayObj))
                self.innerHolidays.append(holidayObj)
                print(f"'{holidayObj}' has been added to the Holiday List!")
        else:
            print(f"'{holidayObj}' isn't working... Please make sure that you're adding a Holiday Object and not something else.")
    
    ## findHoliday: 
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

    def filterHolidaysByWeek(self, year, weekNumber):
        filteredYear = list(filter(lambda holiday: holiday.date.year == int(year), self.innerHolidays))
        filteredWeek = list(filter(lambda holiday: holiday.date.isocalendar().week == int(weekNumber), filteredYear))
        return filteredWeek

    def displayHolidayList(self, displayList):
        for holiday in displayList:
            print(holiday)



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
            if str(newHoliday) not in self.innerHolidays:
                # print(print(f"Looks like '{newHoliday}' is already on the list!"))
            # self.addHoliday(newHoliday) ##old code line, appending directly instead of using 'addHoliday()' seems to be more efficient.
            # else:
                # self.innerHolidays.append(str(newHoliday))
                self.innerHolidays.append(newHoliday)
                # print(f"'{newHoliday}' has been added to the Holiday List!")
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
        for holiday in self.innerHolidays:
            if vars(holiday) == vars(holidayObj):
                self.innerHolidays.remove(holiday)
                print(f'{holiday.name} removed!')


        # if str(holidayObj) in self.innerHolidays:
        #     print(f'{holidayObj} found: Removing {holidayObj} from list:')
        #     # remove the Holiday from innerHolidays
        #     self.innerHolidays.remove(str(holidayObj))
        #     # inform user you deleted the holiday
        #     print(f'{holidayObj} removed!')
            # else:
            #     print(f'{holiday.name} does not appear to be on our list.')

    ## save_to_json:
    def save_to_json(self, filelocation):
        # Write out json file to selected file.
        with open(filelocation, 'w') as f:
            data = {'holidays':[{"name":holiday.name, "date": holiday.date} for holiday in self.innerHolidays]}
            json.dump(data, f, default = str)
        print("Your data has been saved!!")
        # jsonString = json.dumps(self.innerHolidays)
        # jsonFile = open(filelocation, "w")
        # jsonFile.write(jsonString)
        # jsonFile.close()
    
    ## web scraper:  ### ADD YEAR AS PARAMETER  '%b %-d' current format, need year '%Y'
    # Scrape Holidays from https://www.timeanddate.com/holidays/us/ 
    # def holidayScraper(self, url, year):     
    #     new_url = f'{url}{year}'
    #     def get_html(new_url): 
    #         response = requests.get(new_url)
    #         return response.text
    #     html = get_html(new_url)    
    #     soup = bs(html, 'html.parser')
    #     holidaySoup = soup.find('tbody')     
    #     rows = holidaySoup.find_all('tr')
    #     for holiday in rows:
    #         holidayInfo = holiday.get_text("|").split("|")
    #         # print(holidayInfo)
    #         for holiday in holidayInfo[1:]:
    #             if len(holiday) < 3:
    #                 continue
    #             name = holidayInfo[2]
    #             date = f'{holidayInfo[0]}, {year}'
                
    #         correctDate = dt.strptime(date,'%b %d, %Y').strftime('%Y-%m-%d')
    #         holidayObj = Holiday(name, correctDate) 
    #         # Check to see if name and date of holiday is in innerHolidays array
    #         if holidayObj not in self.innerHolidays:
    #             # print(f"Looks like '{holidayObj}' is already on the list!")
    #             # Use innerHolidays.append(holidayObj) to add holiday
    #             # Add non-duplicates to innerHolidays
    #             # self.innerHolidays.append(str(holidayObj))
    #             self.innerHolidays.append(holidayObj)
    #             # print(holidayObj)
    #             # print(type(holidayObj))
    #             # print(f"'{holidayObj}' has been added to the Holiday List!")

    def holidayScraper(self, url, year):     
        new_url = f'{url}{year}'
        def get_html(new_url): 
            response = requests.get(new_url)
            return response.text
        html = get_html(new_url)    
        soup = bs(html, 'html.parser')
        holidaySoup = soup.find('tbody')     
        rows = holidaySoup.find_all('tr')
        for holiday in rows:
            # holidayInfo = holiday.get_text("|").split("|")
            # print(holidayInfo)
            date = holiday.find('th')
            name = holiday.find('a')
            if date != None and name != None:
                date = f"{holiday.find('th').text}, {year}" 
                name = holiday.find('a').text
            # for holiday in holidayInfo[1:]:
            #     if len(holiday) < 3:
            #         continue
            #     name = holidayInfo[2]
            #     date = f'{holidayInfo[0]}, {year}'
                
                correctDate = dt.strptime(date,'%b %d, %Y').strftime('%Y-%m-%d')
                holidayObj = Holiday(name, correctDate) 
            # Check to see if name and date of holiday is in innerHolidays array
            # if holidayObj not in self.innerHolidays:
                # print(f"Looks like '{holidayObj}' is already on the list!")
                # Use innerHolidays.append(holidayObj) to add holiday
                # Add non-duplicates to innerHolidays
                # self.innerHolidays.append(str(holidayObj))
                self.innerHolidays.append(holidayObj)
                # print(holidayObj)
                # print(type(holidayObj))
                # print(f"'{holidayObj}' has been added to the Holiday List!"
######################################################################################################################
    
#         # Remember, 2 previous years, current year, and 2  years into the future. You can scrape multiple years by adding year to the timeanddate URL. For example https://www.timeanddate.com/holidays/us/2022
#         # Handle any exceptions.     



mainHolidayList = HolidayList() 
######TESTING#######

def choose():
        options = ['1', '2', '3', '4', '5']
        print('''
        =============================================
        Hello! Welcome to the Holiday List Interface.
        =============================================

        Menu:

        1) Add Holiday
        2) Remove Holiday
        3) Save Holiday List
        4) View Holidays by Week
        5) Exit
        ''')
        choice = input("What would you like to do? (Select 1-5 for Menu Choice): ")
        if choice in options:

            ## add holiday
            if choice == '1':
                print("You have selected 'Add Holiday'")
                name = input("What is the name of the holiday you'd like to add?: " )               
                # date = input("what is the year of the holiday you'd like to add? (Please write date in 'YYYY-MM-DD' format): ")
                month = input("what is the month of the holiday you'd like to add? (Please write date in 'MM' format): ")
                day = input("what is the day of the holiday you'd like to add? (Please write date in 'DD' format): ")
                year = input("what is the year of the holiday you'd like to add? (Please write date in 'YYYY' format): ")
                date = f"{year}-{month}-{day}"
                holidayObj = Holiday(name, date)
                mainHolidayList.addHoliday(holidayObj)
                choose()

            ## remove holiday
            if choice == '2':
                print("You have selected 'Remove Holiday'")
                name = input("What is the name of the holiday you'd like to remove?: " )
                # date = input("what is the date of the holiday you'd like to remove? (Please write date in 'YYYY-MM-DD' format): ")
                month = input("what is the month of the holiday you'd like to remove? (Please write date in 'MM' format): ")
                day = input("what is the day of the holiday you'd like to remove? (Please write date in 'DD' format): ")
                year = input("what is the year of the holiday you'd like to remove? (Please write date in 'YYYY' format): ")
                date = f"{year}-{month}-{day}"

                mainHolidayList.removeHoliday(name, date)
                choose()

            ## save holiday list
            if choice == '3':
                print("You have selected 'Save Holiday List'")
                fileLocation = input("What would you like the name of the file location to be?: ")
                print("Okay, saving file now...")
                mainHolidayList.save_to_json(f'{fileLocation}.json', mainHolidayList.innerHolidays)
                print("File saved!")
                choose()

            if choice == '4':
                print("You have selected to view holidays by Week")
                yearChoice = input("What year would you like to view? [Please enter year in 'YYYY' format]: ")
                weekChoice = input("What week number would you like to view? [Please enter week in 'NN' format from 1-52]: ")
                print(f"You have selected '{weekChoice}, {yearChoice}'")
                filteredHolidays = mainHolidayList.filterHolidaysByWeek(yearChoice, weekChoice)
                mainHolidayList.displayHolidayList(filteredHolidays)
                choose()

            if choice == '5':
                answer = input("Are you sure you want to exit? [Y or N]: ").upper()
                if answer == 'Y':
                    print("So sad to see you go!")
                    exit = True
                    return exit
                elif answer == 'N':
                    print("Oh, okay, let's go back to the main menu:")
                    choose()

        else:
            print("Please pick a number from 1-5 to represent your choice: ")
            choose()

def menu():
    exit = False
    while exit == False:        
        exit = choose()
    
def main():
#     # Large Pseudo Code steps
#     # -------------------------------------
#     # 1. Initialize HolidayList Object  (Done Above)
#     # 2. Load JSON file via HolidayList read_json function
    mainHolidayList.read_json('holiday_startercode.txt')
#     # 3. Scrape additional holidays using your HolidayList scrapeHolidays function.
    mainHolidayList.holidayScraper('https://www.timeanddate.com/holidays/us/', '2020')
    mainHolidayList.holidayScraper('https://www.timeanddate.com/holidays/us/', '2021')
    mainHolidayList.holidayScraper('https://www.timeanddate.com/holidays/us/', '2022')
    mainHolidayList.holidayScraper('https://www.timeanddate.com/holidays/us/', '2023')
    mainHolidayList.holidayScraper('https://www.timeanddate.com/holidays/us/', '2024')
        ## write json file
    # mainHolidayList.save_to_json('holidays.txt', mainHolidayList.innerHolidays)
    # mainHolidayList.save_to_json('holidays.json', mainHolidayList.innerHolidays)
    mainHolidayList.save_to_json('holidays.json')
#     # 3. Create while loop for user to keep adding or working with the Calender
    menu()
    
#     # 4. Display User Menu (Print the menu)
#     # 5. Take user input for their action based on Menu and check the user input for errors
#     # 6. Run appropriate method from the HolidayList object depending on what the user input is
#     # 7. Ask the User if they would like to Continue, if not, end the while loop, ending the program.  If they do wish to continue, keep the program going. 
main()

# if __name__ == "__main__":
#     main();







        
### TO DO:

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





