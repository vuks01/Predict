from Functions import Function5

def test_number_of_tweets_per_day():

 """
    Make sure that number_of_tweets_per_day works correctly
    """
    assert Function5.number_of_tweets_per_day(number_of_tweets_per_day(twitter_df.copy().iloc[1:2])) == Tweets 1 Date 2019-11-29, 'incorrect'
    assert Function5.number_of_tweets_per_day(number_of_tweets_per_day(twitter_df.copy().iloc[1:4])) == Tweets 3 Date 2019-11-29, 'incorrect'
    assert Function5.number_of_tweets_per_day(number_of_tweets_per_day(twitter_df.copy().iloc[:4])) ==  Tweets 1 Date 2019-11-29, 'incorrect'

