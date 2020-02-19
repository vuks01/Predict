from Functions import Function7

def test_stop_words_remover():

    """
    Make sure that stop_words_remover works correctly
    
    """

    assert Function7.stop_words_remover(twitter_df.copy()).loc[0, "Without Stop Words"] == ['@bongadlulane', 'send', 'email', 'mediadesk@eskom.co.za'], 'incorrect'
    assert Function7.stop_words_remover(twitter_df.copy()).loc[100, "Without Stop Words"] == ['#eskomnorthwest', '#mediastatement', ':', 'notice', 'supply', 'interruption', 'lichtenburg', 'area', 'https://t.co/7hfwvxllit'], 'incorrect'
    assert Function7.stop_words_remover(twitter_df.copy()).loc[10, "Without Stop Words"] == ['rt','@exposcience:','#fridaythoughts','norman','mashiri','dr','joseph','shabalala','school','received','top','ict','project','award','@siemensafrica','p…'], 'incorrect'