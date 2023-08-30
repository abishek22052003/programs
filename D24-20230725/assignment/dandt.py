from datetime import date
# finding date
dandt=date(2023,7,27)
print(dandt)

#finding today date
# dandt=date.today()
# print("today date is",dandt)

#printing day and month AND YEAR
# dandd=date.today().day
# dandm=date.today().month
# dandy=date.today().year
# print(dandm)
# print(dandd)
# print(dandy)

#finding the time
from datetime import time
# dandt=time(11,22,11)
# print(dandt)

# finding the time
# from datetime import time
# dandt=time()
# print(dandt)

# from datetime import datetime
# dandt=datetime(2023,7,25,12,30,29)
# print(dandt)

# from datetime import datetime
# dandt=datetime.now()
# print(dandt)

#finding date
# from datetime import datetime
# now=datetime.now()
# dandt=now.strftime("%y-%m-%d")
# print(dandt)
# from datetime import datetime
# now=datetime.now()
# dandt=now.strftime("%Y")
# print(dandt)
# from datetime import datetime
# now=datetime.now()
# dandt=now.strftime("%D")
# print(dandt)

#finding time
# from datetime import datetime
# now=datetime.now()
# dandt=now.strftime("%H:%M:%S")
# print(dandt)


# import pytz
# print(pytz.all_timezones)

from datetime import datetime
from pytz import timezone
format="%y-%m-%d,%H:%M:%S"
now_utc=datetime.now(timezone("UTC"))
now_asia=now_utc.astimezone(timezone("Asia/kolkata"))
print(now_asia.strftime(format))

# from datetime import datetime
# import pytz
# time=datetime.now(pytz.timezone("Asia/Kolkata"))
# print(time)



