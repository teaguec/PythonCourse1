long_month = ['jan', 'mar', 'may', 'jul', 'aug', 'oct', 'dec']
mid_month = ['apr', 'jun', 'sep', 'nov']


def num_days(month):

    if month in long_month:
        print('number of days in',month,'is',31)
    elif month in mid_month:
        print('number of days in',month,'is',30)
    elif month == 'feb':
        print('number of days in',month,'is',28)
    else:
        print('invalid month')


num_days(input("input month"))
# optimize/shorten the code in the function
# try to reduce the number of conditionals 