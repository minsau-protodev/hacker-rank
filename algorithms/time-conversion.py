from datetime import datetime


def timeConversion(s):
    today_str = datetime.now().strftime("%d/%m/%y")
    full_date = f'{today_str} {s}'
    formatted = datetime.strptime(full_date, '%d/%m/%y %I:%M:%S%p')
    return formatted.strftime('%H:%M:%S')


result = timeConversion('07:05:45PM')
print(result)
