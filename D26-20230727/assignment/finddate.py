from datetime import datetime
from datetime import timedelta
today=datetime.today()
date=today.date()
print(date)
n=int(input("num "))
c=date+timedelta(days=n)
print(c)