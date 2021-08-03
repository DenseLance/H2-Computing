import time
from datetime import datetime

datetime1 = datetime.today()
time.sleep(5) # datetime2 - datetime1 = 5 seconds
datetime2 = datetime.today()
print("Datetime 1:", datetime.strftime(datetime1, "%d/%m/%Y %H:%M:%S"))
print("Datetime 2:", datetime.strftime(datetime2, "%d/%m/%Y %H:%M:%S"))
print("Time difference between datetime1 and datetime2:", datetime2 - datetime1)
print("Time difference between datetime1 and datetime2 is 5 seconds:", (datetime2 - datetime1).seconds == 5)

date_in_str = "2020-07-29 08:30:00"
datetime3 = datetime.strptime(date_in_str, "%Y-%m-%d %H:%M:%S")
print("Datetime 3:", datetime.strftime(datetime3, "%d/%m/%Y %H:%M:%S"))
print("Time difference between datetime1 and datetime3:", datetime3 - datetime1)
print("Time difference between datetime1 and datetime2 in days:", (datetime3 - datetime1).days)
