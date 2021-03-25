#importing modules
from selenium import webdriver
import datetime
import time
import argparse
import os

#Welcome Script
print("Welcome to python data scrape script!")
print("Intially it scraper the data for Gurgaon Region only (will be extended for all regions in v2)")
print("-------------------------------------")

days = int(input("Starting from today, how many days prices do you want? Enter b/w [0-50]: "))
url = 'https://www.mypetrolprice.com/40/Petrol-price-in-Gurgaon?FuelType=0&LocationId=40'
# Define Chrome options to open the window in maximized mode
options = webdriver.ChromeOptions()
options.add_argument("--start-maximized")

# Initialize the Chrome webdriver and open the URL
driver = webdriver.Chrome(r"C:\Users\samyjain\Downloads\chromedriver.exe")
driver.get(url)

# Define a pause time in between scrolls
pause_time = 2

# Get scroll height
last_height = driver.execute_script("return document.body.scrollHeight")

while True:
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(pause_time)
    new_height = driver.execute_script("return document.body.scrollHeight")
    if new_height == last_height: # which means end of page
        break
    last_height = new_height

# Creating a price_list dictionary
prices_list = {}
count = 0
while True and count <= days:
    price = driver.find_elements_by_class_name('PriceDiv')
    date = driver.find_elements_by_class_name('DateDiv')
    for i, j in zip(date, price):
        prices_list[" ".join((i.text).split("\n"))] = (j.text).strip().split("  ")
        count+=1
    next_frame = driver.find_element_by_id('BC_GV_CustomGridPager_NextButton')
    next_frame.click()

flag=True
while(flag!=False):
    count = 0
    todo = input("The data has been generated, if you want to display press display or d, or if you want to export it as csv press csv or c: ")
    print("-------------------------------------")
    if todo.lower() == "csv" or todo.lower() == "c":
        flag=False
        import pandas as pd
        price_df = pd.DataFrame(list(prices_list.keys()),columns=["Date"])
        price_df['Price (in INR)'] = [i[0].strip("₹ ") for i in list(prices_list.values())]
        price_df['Inflation'] = [i[1].strip("▼").strip("▲") for i in list(prices_list.values())]
        start_date = "".join(price_df.Date[-1:].values)
        end_date = "".join(price_df.Date[0:1].values)
        filename = f"Petrol data for {start_date}-{end_date}.csv"
        price_df.head(days).to_csv(filename, index=False)
        print(f"File saved as {filename}")
    elif todo.lower() == "display" or todo.lower() == "d":
        flag=False
        print("The petrol price list are as follows:")
        print("Date       : Price   Inflation")
        for date in prices_list:
            if(count<=days):
                print(f"{date}: {prices_list[date][0]} {prices_list[date][1]}")
            count+=1
    else:
        print("Wrong selection, please try again")
print("-------------------------------------")
print("Thank you for using python petrol data scrape script!")