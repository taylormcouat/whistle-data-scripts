from datetime import datetime, timedelta

def get_day_number(date):
    epoch_start = datetime(1970, 1, 1)
    delta = date - epoch_start
    return delta.days

def get_date_from_day_number(day_number):
    epoch_start = datetime(1970, 1, 1)
    target_date = epoch_start + timedelta(days=day_number)
    return target_date.strftime('%Y-%m-%d')
    