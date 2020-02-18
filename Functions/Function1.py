import numpy as np
def dictionary_of_metrics(items):
    
    """ Calculates the mean, median, std, variance (var), minimum (min) and maximum(max) input values
        Args:
            takes in a list object containing numerical values floats and int number to calculate and return the mean, median, std, variance (var), minimum (min) and maximum(max).
            
        Returns:
             returns a dictionary with the keys and their values as calculated
    """
    return {'mean': round(np.mean(items),2), 'median': round(np.median(items),2), 'var': round(np.var(items,ddof=1),2), 'std': round(np.std(items,ddof=1),2), 'min':round(np.min(items),2), 'max': round(np.max(items),2)}