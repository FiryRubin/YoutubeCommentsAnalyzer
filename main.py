import time
from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pandas as pd

from utils import *

my_location = scrape_comments(url="https://www.youtube.com/watch?v=_bDXXWQxK38", loads=2)
my_file = pd.read_csv(my_location)
print(my_file)
