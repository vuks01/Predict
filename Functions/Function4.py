def extract_municipality_hashtags(df):
    
    """Return modified dataframe that has new columns that contain information 
    about the municipality and hashtag included in each tweet.

    Args:
        df(dataframe): datatframe containing tweets and dates.

    Returns:
        dataframe: modified with two new columns that contain information about the municipality and hashtag included in each tweet.

    """
    import numpy as np
    import pandas as pd 
    mun_dict = {
    '@CityofCTAlerts' : 'Cape Town',
    '@CityPowerJhb' : 'Johannesburg',
    '@eThekwiniM' : 'eThekwini' ,
    '@EMMInfo' : 'Ekurhuleni',
    '@centlecutility' : 'Mangaung',
    '@NMBmunicipality' : 'Nelson Mandela Bay',
    '@CityTshwane' : 'Tshwane'
    }
    
    muni = list(mun_dict.keys())
    df1 = df.copy()
    cities = []
    hashtags = []
    
    Tweets = list(df1['Tweets'])                   #Place Tweets in List
    Tweets_Split = []                              #Empty List for appending lists of words for each tweet
    for Tweet in Tweets:                           #Loop to go through every Tweet in list
        Tweets_Split.append(Tweet.lower().split()) #Append the split words to empty list created above
    
    for tweet in Tweets_Split:                     #Go to each tweet in the split words list
        city1 = ''                                 #Create empty string to store city names
        hashs = []                                 #Create list to store Hastags per tweet
        for words in tweet:                        #Go to each word in the tweet
            if words in muni:                      #if word is in Municipality Dict Keys 
                city1 = str(mun_dict[words])       # Then Store the City for the key
            if '#' in words:                       # if word contains a Hashtag
                words = words.lower()              # Store Word as lower case
                hashs.append(words)                # append word to list of hashs for that tweet
        cities.append(city1)                       # Store city Name and append to list for each tweet
        hashtags.append(hashs)                     # Store hastags per tweet and append to list
    
    cities = [np.nan if x == '' else x for x in cities] # Replace empty string with np.nan
    df1['municipality'] = cities                        # Insert the name of cities into a new column called 'municipality
    df1['hashtags'] = hashtags                          #Insert the hashtags found into a new column called 'hashtags
    df1['hashtags'] = df1['hashtags'].apply(lambda y: np.nan if len(y)==0 else y) # Replace empty lists(no hashtags) with np.nan
    
    return df1 