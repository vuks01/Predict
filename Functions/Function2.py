import numpy as np
def five_num_summary(items):
    
    """ calculate the max, median, min, first quantile(q1) and third quartile(q300 values
        Args:
            takes in a list object containing numerical values floats and int number to calculate and return the max, median, min, first quantile and the third quantile.
            
        returns:
            it returns a dictionary with the keys and their values as calculated
            
        Examples:
            five_num_summary(gauteng) == {
                'max': 39660.0,
                'median': 24403.5,
                'min': 8842.0,
                'q1': 18653.0,
                'q3': 36372.0
            }
    """

    return {"max": np.max(items), "median": np.median(items), "min": np.min(items), "q1": np.percentile(items,25), "q3": np.percentile(items,75)}

    