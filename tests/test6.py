from Functions import Function6

def  test_word_splitter()
    """
    Make sure that word_splitter works correctly
    """

    assert function6.word_splitter(df1['Split Tweets'][1]) == ['@saucy_mamiie', 'pls', 'log', 'a', 'call', 'on', '0860037566'] 'incorrect'
    assert function6.word_splitter(df1['Split Tweets'][100]) == ['#eskomnorthwest', '#mediastatement', ':', 'notice', 'of', 'supply', 'interruption', 'in', 'lichtenburg', 'area', 'https://t.co/7hfwvxllit'] 'incorrect'
    assert function6.word_splitter(df1['Split Tweets'][125]) == ['@wordsalchemy', 'please', 'report', 'to', 'customer', 'services', 'on', '08600', '37566'] 'incorrect'