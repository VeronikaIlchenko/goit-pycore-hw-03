from datetime import datetime, timedelta

users = [
    {"name": "Bill Gates", "birthday": "1955.10.28"},
    {"name": "Jan Koum", "birthday": "1976.02.24"},
    {"name": "Kim Kardashian", "birthday": "1980.10.21"},
    {"name": "Jill Valentine", "birthday": "1974.11.30"},
    {"name": "Birthday Boy", "birthday": "2000.03.01"},
    {"name": "Next Week Friend", "birthday": "1995.03.04"},
    {"name": "Late Friend", "birthday": "1992.02.28"}
]

def get_upcoming_birthdays(users):
    today = datetime.now().date()
    upcoming_birthdays = [] 
    for user in users:
        birthday = datetime.strptime(user['birthday'], "%Y.%m.%d").date()
        birthday_this_year = birthday.replace(year=today.year)
        days_until = (birthday_this_year - today).days

        if 0 <= days_until <= 7:
           day_of_week = birthday_this_year.weekday()
           congratulation_date = birthday_this_year
           if day_of_week == 5: # Субота
            congratulation_date += timedelta(days=2)
           elif day_of_week == 6: # Неділя
            congratulation_date += timedelta(days=1)
            upcoming_birthdays.append({
                "name": user["name"],
                "congratulation_date": congratulation_date.strftime("%Y.%m.%d")
            })
            
    return upcoming_birthdays

result = get_upcoming_birthdays(users)
print("Список привітань на цьому тижні:", result)