import pandas as pd
from germansentiment import SentimentModel

class SentimentAnalyser(object):

    @staticmethod
    def analyze_comment_section(dataframe: pd.DataFrame):
        model = SentimentModel()
        dataframe['sentiment'] = model.predict_sentiment(dataframe['comment'])
        return dataframe
