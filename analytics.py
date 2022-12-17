import pandas as pd
from sentimentAnalyser import SentimentAnalyser as sa


class Analytics(object):

    @staticmethod
    def general_sentiment_of_comments(dataframe: pd.DataFrame):
        # analyse sentiment
        dataframe = sa.analyze_comment_section(dataframe)

        # count sentiments
        total = len(dataframe)

        positive = 0
        negative = 0
        neutral = 0

        for x in dataframe['sentiment']:
            if x == 'neutral':
                neutral += 1
            elif x == 'positive':
                positive += 1
            elif x == 'negative':
                negative += 1

        positive_share = round((positive / total) * 100, 2)
        negative_share = round((negative / total) * 100, 2)
        neutral_share = round((neutral / total) * 100, 2)

        # print results
        print("------Analytics Report------")
        print(len(dataframe), " comments scraped")
        print(positive, ": positive comments -", positive_share, "%")
        print(neutral, ": neutral comments -", neutral_share, "%")
        print(negative, ": negative comments -", negative_share, "%")