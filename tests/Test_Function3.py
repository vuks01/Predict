from Functions import Function3

def date_parser():
    """
        the output should be a list of string where each elements in the returned list contain only the date in the 'yyyy-mm-dd' format.
    """

    assert Function3.date_parser(['2019-11-29 12:50:54', '2019-11-29 12:46:53', '2020-01-29 12:46:10']) == ['2019-11-29', '2019-11-29', '2020-01-29'], 'incorrect'
    assert Function3.date_parser(['2019-11-29 12:50:54', '2019-11-29 12:46:53', '2019-12-29 12:46:10', '2020-02-18 14:02:55']) == ['2019-11-29', '2019-11-29', '2019-12-29', '2020-02-18'], 'incorrect'
    assert Function3.date_parser(['2019-11-29 12:46:53', '2019-11-29 12:46:10', '2020-01-29 12:46:10', '2020-01-29 12:17:43']) == ['2019-11-29', '2019-11-29', '2020-01-29', '2020-01-29'], 'incorrect'