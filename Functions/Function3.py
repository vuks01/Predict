def date_parser(dates):
    
    """Returns date in the format of yyyy-mm-dd

    Args:
       list of datetime strings

    Returns:
         list of strings where each element now only contains only the date in yyyy-mm-dd format 
    """
    dates_only =[]
    for i in dates:               #iterate through the date given in the argument
        date = i[0:10]            #the date is only the first 9 items of the string being evaluated
        dates_only.append(date)   #append the empty list with the date
    return dates_only