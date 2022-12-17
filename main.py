import time
from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pandas as pd

from utils import *

# example files
my_location2 = "resources/20221217_231912121477.csv"

my_location = scrape_comments(url="https://www.youtube.com/watch?v=iEvbOQXdYAE", loads=2)

my_file = pd.read_csv(my_location)
print(my_file)
