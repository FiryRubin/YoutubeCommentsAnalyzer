import time
from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

from datetime import datetime

import pandas as pd


def save_df(dataframe: pd.DataFrame):
    timestamp = datetime.now()
    timeuid = str(timestamp).replace(" ", "_").replace(":", "").replace(".", "").replace("-", "")
    slug = 'resources/'+timeuid+".csv"
    print(slug, 'slug')
    dataframe.to_csv(slug)
    return slug


def scrape_comments(url: str, loads: int):
    data=[]

    service = Service(ChromeDriverManager().install())
    with Chrome(service=service) as driver:
        wait = WebDriverWait(driver,15)
        driver.get(url)

        time.sleep(2)

        consent_button_xpath = "//button[@aria-label='Verwendung von Cookies und anderen Daten zu den beschriebenen Zwecken ablehnen']"
        consent = WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.XPATH, consent_button_xpath)))
        if consent != None:
            consent_button = driver.find_element(by=By.XPATH, value=consent_button_xpath)
            consent_button.click()

        time.sleep(2)

        pause_button = driver.find_element(by=By.CSS_SELECTOR, value="video")
        pause_button.click()
        
        time.sleep(2)

        for item in range(loads): 
            wait.until(EC.visibility_of_element_located((By.TAG_NAME, "body"))).send_keys(Keys.END)
            time.sleep(2)

        for comment in wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, "#content"))):
            data.append(comment.text)


    df = pd.DataFrame(data, columns=['comment'])
    df = clean_scraped_df(df)
    location = save_df(df)
    print("Scrape of Video finished and saved under ", location)
    return location


def clean_scraped_df(dataframe: pd.DataFrame):
    if dataframe.size > 10:
        return dataframe[3:len(dataframe) - 7]
    else:
        print("Warning - Data has not been cleand do to insufficient length")
        return dataframe
