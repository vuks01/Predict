def number_of_tweets_per_day(df):
    
    """Returns number of tweets posted per day.

    Args:
        pandas dataframe

    Returns:
        new dataframe, grouped by day, with the number of tweets per day

    """

    import pandas as pd
    # Making a copy of the DataFrame
    df1 = df.copy()
    # Extracting a column of dates and turning it into a list
    dates = list(df1['Date'])
    # Intializing an empty list to store dates without time
    date_only = []
    # Iterating over dates to get dates only
    for date in dates:
        date_only.append(date[:10])
    # Creating an empty list
    data = pd.DataFrame()
    #inputing data into the empty DataFrame and creating columns
    data['Date'] = date_only
    data['Tweets'] = 1
    #Grouping by date and getting the some of tweets per day
    data = data.groupby(['Date']).sum()
    return data


