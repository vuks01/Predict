def word_splitter(df):
    
    """splits the sentences in a dataframe's column into a list of the separate words
        Args:
            It should take a pandas dataframe that contain a column, named 'Tweets' as an input. Split the tweets and also change the case to lowercase

        Returns:
             function modifiesthe input dataframe directly and return the modified dataframe.
        Example:
            0        @BongaDlulane Please send an email to mediades...        2019-11-29 12:50:54        [@bongadlulane, please, send, an, email, to, m...
            1        @saucy_mamiie Pls log a call on 0860037566               2019-11-29 12:46:53        [@saucy_mamiie, pls, log, a, call, on, 0860037...
            2        @BongaDlulane Query escalated to media desk.             2019-11-29 12:46:10        [@bongadlulane, query, escalated, to, media, d...
            3        Before leaving the office this afternoon, head...        2019-11-29 12:33:36        [before, leaving, the, office, this, afternoon...
            4        #ESKOMFREESTATE #MEDIASTATEMENT : ESKOM SUSPEN...        2019-11-29 12:17:43        [#eskomfreestate, #mediastatement, :, eskom, s...
            
         """

    import pandas as pd
    
    df1 = df.copy() # Make Copy Of Dataframe
    Tweets = list(df1['Tweets']) # Place Tweets in List
    Tweets_Split = [] # Empty List for appending lists of words for each tweet
    for Tweet in Tweets: # Loop to go through every Tweet in list
        Tweets_Split.append(Tweet.lower().split()) # Append the split words to empty list created above
    df1['Split Tweets'] = Tweets_Split # Insert list of lists where sublists contain splitwords into dataframe
    return df1