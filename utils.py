import time
from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from datetime import datetime

import pandas
import pandas as pd


def save_df(dataframe: pd.DataFrame):
    timestamp = datetime.now()
    timeuid = str(timestamp).replace(" ", "_").replace(":", "").replace(".", "").replace("-", "")
    slug = 'resources/'+timeuid+".csv"
    print(slug, 'slug')
    dataframe.to_csv(slug)
    return slug

def scrape_comments(url: str, loads: int):
    data = []

    with Chrome(executable_path=r'C:\Program Files\chromedriver.exe') as driver:
        wait = WebDriverWait(driver, 15)
        driver.get(url)

        for item in range(loads):
            wait.until(EC.visibility_of_element_located((By.TAG_NAME, "body"))).send_keys(Keys.END)
            time.sleep(15)

        for comment in wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, "#content"))):
            data.append(comment.text)

    df = pd.DataFrame(data, columns=['comment'])
    location = save_df(df)
    print("Scrape of Video finished and saved under ", location)
    return location
