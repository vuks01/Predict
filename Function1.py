import numpy as np
def dictionary_of_metrics(items):
    """ calculate the mean, median, std, variance (var), minimum (min) and maximum(max) input values
        Args:
            takes in a list object containing numerical values floats and int number to calculate and return the mean, median, std, variance (var), minimum (min) and maximum(max).
            
        returns:
            it returns a dictionary with the keys and their values as calculated
            
        Examples:
            five_num_summary(gauteng) == {
                'mean': 26244.42
                'median': 24403.5
                'std': 10400.01
                'var': 108160153.17,
                'min': 8842,
                'max': 39660,
            }
    """
    return {'mean': round(np.mean(items),2), 'median': round(np.median(items),2), 'var': round(np.var(items,ddof=1),2), 'std': round(np.std(items,ddof=1),2), 'min':round(np.min(items),2), 'max': round(np.max(items),2)}