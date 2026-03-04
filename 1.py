from datetime import datetime

def get_days_from_today(date): 
    try:
        date = datetime.strptime(date, "%Y-%m-%d")
        today = datetime.today()
        diff = date - today
        return diff
    except ValueError:
        return "Неправильний формат дати! Використовуйте РРРР-ММ-ДД."

print(get_days_from_today("3"))