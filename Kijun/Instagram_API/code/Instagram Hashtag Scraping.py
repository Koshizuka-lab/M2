# -*- coding: utf-8 -*-
# ---
# jupyter:
#   jupytext:
#     text_representation:
#       extension: .py
#       format_name: light
#       format_version: '1.4'
#       jupytext_version: 1.1.0
#   kernelspec:
#     display_name: Python 3
#     language: python
#     name: python3
# ---

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
import pandas as pd
import datetime
import time


# +
# Instagram Account Information
# ID = "jdsc_ds_team"
# PW = "jdscjdsc"
# -

# Definition of scraping function
def scraping(tag_list):
    
    # Define dataframe to store hashtag information
    tag_df = pd.DataFrame(columns=["Date","Hashtag","Number of Posts","Freq(mins)"])
    
    chrome_options = Options()
    chrome_options.add_argument('--headless')
    chrome_options.add_argument('--no-sandbox')
    chrome_options.add_argument('--disable-dev-shm-usage')
    
    for tag in tag_list:
        # Directory of ChromeDriver 
        driver = webdriver.Chrome("/usr/local/bin/chromedriver")
        driver.get("https://www.instagram.com/explore/tags/"+str(tag))
        soup = BeautifulSoup(driver.page_source,"lxml")
        
        tagname = tag
        
        # Extract total number of posts
        nposts = soup.find("span",{"class":"g47SY"}).text
        print(tagname) # check the target keyword
        print("number of posts:",nposts) # check the total number of posts
        
        # Extract all post links from "explore tags" page
        # NOTE : Class name may change in the website code
        # Needed to extract post frequency of recent posts
        myli = []
        for a in soup.find_all("a",href=True):
             myli.append(a["href"])
                
        # Keep link of only 1st and 9th most recent post
        newmyli = [x for x in myli if x.startswith("/p")]
        
        del newmyli[:9]
        del newmyli[9:]
        del newmyli[1:8]
        
        timediff = []
        
        # EXtract the posting time of 1st and 9th most recent
        for j in range(len(newmyli)):
            driver.get('https://www.instagram.com'+str(newmyli[j]))
            soup = BeautifulSoup(driver.page_source,"lxml")
 
            for i in soup.findAll('time'):
                if i.has_attr('datetime'):
                    timediff.append(i['datetime'])
                    
        # Calculate time difference between posts
        # For obtaining posting frequency
        datetimeFormat = '%Y-%m-%dT%H:%M:%S.%fZ'
        diff = datetime.datetime.strptime(timediff[0], datetimeFormat)\
                - datetime.datetime.strptime(timediff[1], datetimeFormat)
        pfreq = int(diff.total_seconds()/(9*60))
        print("frequency of posts:",pfreq)
        
        # Set Time
        date = datetime.datetime.now().strftime("%Y-%m-%d %H:%M")
        
        # Add hashtag info to dataframe
        s = pd.Series([date, tagname, nposts, pfreq],index=tag_df.columns)
        tag_df = tag_df.append(s,ignore_index=True)
        
        driver.quit()
        
        # Wait 2 seconds
        time.sleep(2)
    
    # Add information to csv file
    tag_df.to_csv("/data/test.csv",encoding="utf-8",mode="a",header=False)


# Define tag_list
tag_list = [
            "石原さとみ",
            "嵐",
            "菅田将暉",
            "ローラ",
            ]


# Testing
while(True):
    if datetime.datetime.now().minute%10 != 9:
        time.sleep(58)
        continue
    while datetime.datetime.now().second != 59:
        time.sleep(1)
    time.sleep(1)
    
    print("Scraping starts!",datetime.datetime.now())

    scraping(tag_list)
