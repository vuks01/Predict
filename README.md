dictionary_of_metrics 
Function calculates the mean, median, variance, standard deviation, minimum and maximum of of list of items. Given list contains only numerical entries, and will use numpy functions to do this.
https://github.com/vuks01/Predict/blob/master/Functions/Function1.py

five_num_summary
Function takes in a list of integers and returns a dictionary of the five number(maximum,median,minimum,first quartile, third quartile). Will use numpy functions to do this.
https://github.com/vuks01/Predict/blob/master/Functions/Function2.py

date_parser
Function takes as input a list of datetime strings and returns only the date in 'yyyy-mm-dd' format.
https://github.com/vuks01/Predict/blob/master/Functions/Function3.py

extract_municipality_hashtags
Function takes in a pandas dataframe and returns a modified dataframe that includes two new columns that contain information about the municipality and hashtag of the tweet. Pandas and numpy are used in this function.
https://github.com/vuks01/Predict/blob/master/Functions/Function4.py

number_of_tweets_per_day
Function calculates the number of tweets that were posted per day. It takes a pandas dataframe as input. Function returns a new dataframe, grouped by day, with the number of tweets for that day.
https://github.com/vuks01/Predict/blob/master/Functions/Function5.py

word_splitter
Function splits the sentences in a dataframe's column into a list of the separate words. The created list is placed in a column named 'Split Tweets'. Function takes a pandas dataframe as an input. The dataframe should contain a column, named 'Tweets'. The function modifies the input dataframe directly.
https://github.com/vuks01/Predict/blob/master/Functions/Function6.py

stop_words_remover
Function removes english stop words from a tweet. Function takes a pandas dataframe as input. The resulting tokenised list of tweets without the stop words are placed a column  named "Without Stop Words". The function should modifies the input dataframe
https://github.com/vuks01/Predict/blob/master/Functions/function7.py
