from datetime import datetime
import os
import time
from datetime import date

def alarm(day,hr,min):
	now = datetime.now()
	print(now)
	if (day == 'p.m.'):
		day = int(now.strftime("%d"))
	elif (day =='a.m.'):
		day = int(now.strftime("%d"))+1
	print("Today's date:", day)
	alarm_time = datetime(2019, 8, day, hr, min, 00, 999999)
	print (alarm_time)
	time.sleep((alarm_time - now).total_seconds())
	os.system("start C:/Users/eshwar/Documents/python_tests/patience.mp3")
	return 'set successful'
