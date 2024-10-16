from datetime import datetime 

def get_days_from_today(date):
    date = datetime.strptime(date, "%Y-%m-%d")
    current_date = datetime.today().date()
    delta = current_date - date.date()
    return delta.days


print(get_days_from_today("2024-10-10"))