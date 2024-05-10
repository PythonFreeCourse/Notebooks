import random
from datetime import datetime, timedelta
import pytest
import builtins


def no_vinnigrete(date1: str, date2: str) -> str:
    '''
    Asks the user for two dates and returns a random date between them.
    If the random date is a Monday, it returns a message saying that there is no vinegret sauce for you.
    :return: str, random date or message
    '''

    rand_date = get_random_date(date1, date2)

    if datetime.strptime(rand_date, "%Y-%m-%d").weekday() == 0:  # 0 is monday
        return f'\nthis date:{rand_date} is a monday! no vinegret sauce for you!'
    return f'Random date : {rand_date}'


def get_random_date(date1: str, date2: str) -> str:
    '''
    returns a random date between date1 and date2
    :param date1: str, format: 'YYYY-MM-DD'
    :return str, format: 'YYYY-MM-DD'
    '''
    try:
        date1 = datetime.strptime(date1, "%Y-%m-%d")
        date2 = datetime.strptime(date2, "%Y-%m-%d")
    except ValueError:
        raise ValueError('Invalid date format, please use "YYYY-MM-DD"')

    min_date, max_date = sorted([date1, date2])
    delta = max_date - min_date
    random_date = min_date + timedelta(days=random.randint(0, delta.days))
    return random_date.strftime("%Y-%m-%d")


def test():

    start_date = datetime.strptime('2020-12-31', '%Y-%m-%d')
    end_date = datetime.strptime('2025-01-01', '%Y-%m-%d')
    rand_test = get_random_date('2020-12-31', '2025-01-01')
    rand_test = datetime.strptime(rand_test, '%Y-%m-%d')

    assert rand_test >= start_date and rand_test <= end_date
    assert get_random_date('2025-01-01', '2025-01-01') == '2025-01-01'
    assert no_vinnigrete('2024-05-06', '2024-05-06') == '\nthis date:2024-05-06 is a monday! no vinegret sauce for you!'
    assert no_vinnigrete('2024-05-06', '2024-05-06')
    
    with pytest.raises(ValueError):     # I tryed pytest just for fun
        get_random_date('2025-01-01', '20251-01')

    print('All test cases passed !\n')


if __name__ == '__main__':
    test()
    print('Enter two dates in format "YYYY-MM-DD"')
    date1 = input('Enter date1: ')
    date2 = input('Enter date2: ')
    rand_date = no_vinnigrete(date1, date2)
    print(rand_date)
