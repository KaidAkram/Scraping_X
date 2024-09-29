from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By 
from selenium.webdriver.support.wait import WebDriverWait
import time
from selenium.common.exceptions import NoSuchElementException, StaleElementReferenceException
import pandas as pd
import emoji
import requests
import os
from selenium.webdriver.chrome.options import Options



chrome_options = Options()
chrome_options.add_argument("--headless")  # Run browser in headless mode
chrome_options.add_argument("--disable-gpu")  # Disable GPU for compatibility
chrome_options.add_argument("--window-size=1920x1080")
titlesoftweets =[]
dates = []
tweet_containers = []


def Scrapping_account(account):
    def contains_only_emoji(text):
        return all(char in emoji.EMOJI_DATA for char in text)
    
    driver = webdriver.Chrome()
    driver.get(account)
    time.sleep(5)
    scroll_position = 0
    last_height = driver.execute_script("return document.body.scrollHeight;")
    a= last_height
    new_height = 0
    scrolling = last_height/20
    while True:
        time.sleep(1.5) 
        driver.execute_script(f"window.scrollTo(0, {scroll_position});")
        tweet_containers = driver.find_elements(By.CSS_SELECTOR, '[data-testid="tweet"]')
        for container in tweet_containers:
            try:
                    
                # Find elements and extract text
                        date = container.find_element(By.TAG_NAME , 'time')
                        date_text = date.text
                        try:
                            tweet = container.find_element(By.CSS_SELECTOR, '[data-testid="tweetText"]')
                            tweet_text = tweet.text
                            if not tweet_text.strip() and contains_only_emoji(tweet_text):
                                tweet_text = "Emoji only"  # Replace with a specific placeholder
                        except NoSuchElementException:
                            tweet_text = 'No tweet text'
                            
                        titlesoftweets.append(tweet_text)
                        dates.append(date_text)     
            except Exception as e:
                print(e)
        scroll_position += scrolling
        print(scroll_position)
        print(last_height)
        print(a)
        
        if int(last_height) == int(scroll_position):
            print('no more tweets')
            driver.quit()
            break
        
        last_height = new_height #update the body height
          
        
    data ={
        'tweets' : titlesoftweets,
        'date' : dates ,
    
    }
    print(len(data['tweets']))
    return data





