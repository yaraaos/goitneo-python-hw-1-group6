from datetime import datetime, timedelta

def get_birthdays_per_week(users):
    
    today = datetime.today().date()
    weekdays = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
    birthdays_per_week = {weekday: [] for weekday in weekdays}
    
    for user in users:
        name = user['name']
        birthday = user['birthday'].date()
        birthday_this_year = birthday.replace(year=today.year)
        
        if birthday_this_year < today:
            birthday_this_year = birthday_this_year.replace(year=birthday_this_year + 1)
        
        if (birthday_this_year - today) <= timedelta(days=7):
            delta_days = (birthday_this_year - today).days
            birthday_weekday = weekdays[(today.weekday() + delta_days)% 7]

            if birthday_weekday in ['Saturday', 'Sunday']: 
                delta_days += 7 - (today.weekday() + delta_days) % 7 
                birthday_weekday = 'Monday'
               

            birthdays_per_week[birthday_weekday].append(name)

    for weekday, names in birthdays_per_week.items():
        if names:
            print(f"{weekday}: {', '.join(names)}")      


