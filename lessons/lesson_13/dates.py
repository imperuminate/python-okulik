import datetime


now = datetime.datetime.now()
print(now)

today_midnight = datetime.datetime.now().replace(hour=0, minute=0, second=0, microsecond=0)
print(today_midnight)

print(now - today_midnight)

after_10_hours = now + datetime.timedelta(hours=10)
print(after_10_hours)