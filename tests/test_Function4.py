from Functions import Function4

def test_extract_municipality_hashtags():

    """
    Make sure that extract_municipality_hashtags works correctly
    """
    assert Function4.extract_municipality_hashtags(twitter_df.copy()).iloc[[0]] == 0 Tweets: @BongaDlulane Please send an email to mediades... Date: 2019-11-29 12:50:54 municipality: NaN hashtags: NaN , 'incorrect'
    assert Function4.extract_municipality_hashtags(twitter_df.copy()).iloc[[1]] == 1 Tweets: @saucy_mamiie Pls log a call on 0860037566  Date: 2019-11-29 12:46:53  municipality: NaN hashtags: NaN , 'incorrect'
    assert Function4.extract_municipality_hashtags(twitter_df.copy()).iloc[[4]] == 4 Tweets: '#ESKOMFREESTATE #MEDIASTATEMENT : ESKOM SUSPEN...' Date: 2019-11-29 12:17:43  municipality: NaN hashtags: '[#eskomfreestate, #mediastatement]' , 'incorrect'