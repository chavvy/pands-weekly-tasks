#Weekly Task 05
#find what the current day is
#specify whether its a weekday or not

from datetime import datetime

#getting the current day as an integer using datetime
#the values follow that 0-4 is monday to friday, and 5-6 is saturday and sunday
current_day = datetime.now().weekday()

#logic for whether its a weekday or weekend
if current_day < 5:
    print("Yes, unfortunately today is a weekday.")
else:
    print("It is the weekend, yay!")