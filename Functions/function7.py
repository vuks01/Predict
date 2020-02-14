def stop_words_remover(df):
    Tweets_new = []  #empty list to store tweets
    Tweets = list(df['Tweets']) #store tweets in the list
    Tweets_Split = [] #Empty List for appending lists of words for each tweet
    for Tweet in Tweets: #Loop to go through each an every Tweet in list
        Tweets_Split.append(Tweet.lower().split()) # Append the split words to empty list created above
        for Tweets in Tweets_Split: # Loop to through each tweet in split tweets list
            x = Tweets
            for item in x: # Go through each item in each tweet
                if item in stop_words_dict['stopwords']: # Chech if item is in stopwords dictionary
                    x.remove(item) # if it is remove the item from list of split words per tweets
        Tweets_new.append(x)      
    df['Without Stop Words'] = Tweets_new # Insert list of lists where sublists contain splitwords without stopwords into dataframe
    return df