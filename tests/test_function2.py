from Functions import Function2

def test_five_num_summary(items):

      """
    Make sure that five_num_summary works correctly
    """

    assert Function2.five_num_summary([8, 3, 2, 7, 4]) == {'max': 8, 'median': 4.0, 'min': 2, 'q1': 3.0, 'q3': 7.0}, 'incorrect'
    assert Function2.five_num_summary([12,35,23,678,67,90,78]) == {'max': 678, 'median': 67.0, 'min': 12, 'q1': 29.0, 'q3': 84.0}, 'incorrect'
    assert Function2.five_num_summary([123,34,56,334,100,506,67,234,23,76,564,32]) == {'max': 564, 'median': 88.0, 'min': 23, 'q1': 50.5, 'q3': 259.0}, 'incorrect'