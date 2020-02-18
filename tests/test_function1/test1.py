from Functions import Function1

def  test_dictionary_of_metrics()
    """
    Make sure that dictionary_of_metrics works correctly
    """

    assert function1.dictionary_of_metrics(39660, 36024, 32127, 39488, 18422) == {'mean': 33144.2, 'median': 36024.0, 'var': 77192641.2, 'std': 8785.93, 'min': 18422, 'max': 39660} 'incorrect'
    assert function1.dictionary_of_metrics([28365, 26303, 11976, 33515, 16218]) == {'mean': 23275.4, 'median': 26303.0, 'var': 79350783.3, 'std': 8907.91, 'min': 11976, 'max': 33515} 'incorrect'
    assert function1.dictionary_of_metrics([51860, 68121, 49881, 42034, 54646]) == {'mean': 53308.4, 'median': 51860.0, 'var': 90539830.3, 'std': 9515.24, 'min': 42034, 'max': 68121} 'incorrect'