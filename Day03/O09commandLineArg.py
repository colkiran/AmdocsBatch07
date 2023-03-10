
import sys

print(sys.argv)

print("-" * 40)

from datetime import datetime, date

print(datetime.now())   # current date and time

print("Date :", date.today())

today = date.today()
print(today.strftime("%d/%m/%Y"))

print(today.strftime("%B / %d / %Y"))

print(today.strftime("%b / %d / %Y"))

print("-" * 40)
# time
time = datetime.now()
curtime = time.strftime("%H:%M:%S")
print(curtime)

print("-" * 40)
import pytz

ty_NY = pytz.timezone('America/New_York')
datetime_NY = datetime.now(ty_NY)
print("Newyork :", datetime_NY.strftime("%H:%M:%S"))

ty_Ldn = pytz.timezone('Europe/London')
datetime_Ldn = datetime.now(ty_Ldn)
print("London :", datetime_Ldn.strftime("%H:%M:%S"))

