from datetime import datetime

def get_days_from_today(date): 
    date = datetime.strptime(date, "%Y-%m-%d")
    date_day = date.day
    today = datetime.today()
    today_day = today.day
    diff = date_day - today_day
    return diff

print(get_days_from_today("2021-10-09"))