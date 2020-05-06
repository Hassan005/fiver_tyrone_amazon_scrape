#!/usr/bin/env python
# coding: utf-8

# In[178]:


from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup as soup
from selenium import webdriver
import time
import re
from selenium.webdriver.chrome.options import Options

chrome_options = Options()
#chrome_options.add_argument("--disable-extensions")
#chrome_options.add_argument("--disable-gpu")
#chrome_options.add_argument("--no-sandbox") # linux only
chrome_options.add_argument("--headless")
chromedriver_location = "H:/setups/selenium/chromedriver"
driver = webdriver.Chrome(executable_path=chromedriver_location,options=chrome_options)
driver.get("https://www.amazon.com.au/hz/wishlist/ls/3N4RUAN4EQLFC")
time.sleep(5)
SCROLL_PAUSE_TIME = 5

# Get scroll height
last_height = driver.execute_script("return document.body.scrollHeight")

while True:
    # Scroll down to bottom
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

    # Wait to load page
    time.sleep(SCROLL_PAUSE_TIME)

    # Calculate new scroll height and compare with last scroll height
    new_height = driver.execute_script("return document.body.scrollHeight")
    if new_height == last_height:
        break
    last_height = new_height
b= [i for i in soup(driver.page_source, 'html.parser').find_all('li',class_="a-spacing-none g-item-sortable")]
free_delivery="N"
item_list=[]

for i in b:
    #to get attrs of list tag
    
    check_for_data=i.h3.find('a')
#     print(check_for_data)
    if (check_for_data!=None):
#         print(check_for_data.text)
        title=i.h3.a.text
        spid=i.attrs["data-reposition-action-params"]
        product_id=spid[24:34]
        p=i.find('span',class_="a-color-price itemUsedAndNewPrice")
        price=p.text[1:]
        price=float(price)
        
        if (price>39):
            free_delivery="Y"
        products ={
          "title":title,
          "product_id":product_id ,
          "price":price ,
          "free_delivery":free_delivery
        }
        item_list.append(products)
print(item_list)    

