# time module – low-level time operations.
# datetime module – high-level operations (dates, times, timestamps).
# calendar module – calendar-based functions.
# dateutil module – third-party for easier manipulation.

# 🔹 1. time Module
import time

# Common Methods:
# Method	Description
# time.time()	        Returns current time in seconds since the epoch
# time.sleep(seconds)	Suspends execution for a number of seconds
# time.ctime()	        Returns current time as a readable string
# time.gmtime()	        Returns UTC time in a struct_time
# time.localtime()	    Returns local time in a struct_time
# time.strftime(format, time_struct)	Converts time struct to string
# time.strptime(string, format)	    Parses string to time struct

# Example:
print(time.time())  # Example: 1718381383.341388
print(time.ctime())  # Example: 'Sat Jun 15 00:39:43 2025'

# 🔹 2. datetime Module
from datetime import datetime, date, time, timedelta

# Working with Current Time:
now = datetime.now()
print(now)  # Example: 2025-06-15 00:40:00.123456
print(now.date())  # Example: 2025-06-15
print(now.time())  # Example: 00:40:00.123456

# Creating Dates & Times:
d = date(2025, 6, 15)
t = time(12, 30, 45)

# Formatting and Parsing:
formatted = now.strftime("%Y-%m-%d %H:%M:%S")
parsed = datetime.strptime("2025-06-15", "%Y-%m-%d")

# Date Arithmetic:
today = date.today()
tomorrow = today + timedelta(days=1)
yesterday = today - timedelta(days=1)

# 🔹 3. calendar Module
import calendar

# Example Usage:
print(calendar.month(2025, 6))
print(calendar.isleap(2024))  # True

# 🔹 4. Time Operations Examples

# 1. Timer Example:
start = time.time()
# some code
time.sleep(2)
end = time.time()
print("Execution time:", end - start)

# 2. Countdown Timer:
for i in range(5, 0, -1):
    print(i)
    time.sleep(1)

# 3. Difference Between Dates:
d1 = datetime(2025, 6, 15)
d2 = datetime(2025, 7, 1)
delta = d2 - d1
print(delta.days)  # 16
