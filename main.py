import pandas as pd

from utils import *
from sentimentAnalyser import SentimentAnalyser as sa
from analytics import Analytics as anal

# example files
my_location1 = "resources/20221217_235007657780.csv"
# my_location2 = scrape_comments(url="https://www.youtube.com/watch?v=iEvbOQXdYAE", loads=2)
my_location3 = "resources/20221218_001419741920.csv"
sevwswild13 = "resources/20221218_002108464958.csv"

my_file = pd.read_csv(sevwswild13)
anal.general_sentiment_of_comments(my_file)


