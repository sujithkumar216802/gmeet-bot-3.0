import os
import sqlite3
from datetime import datetime as d
import time
connection = sqlite3.connect('database.db')
def getTiming(day):
    val = connection.execute('SELECT * FROM TIMING WHERE DAY = {};'.format(day))
    ret = []
    for x in val:
        obj = {}
        obj['day'] = x[0]
        obj['start_time'] = x[1]
        obj['end_time'] = x[2]
        obj['subject'] = x[3]
        ret.append(x[2])
    return ret

while True:
    date = d.now()
    if date.strftime("%H:%M") in getTiming(1):
        print("im available in database")
    else:
        print(".")
    time.sleep(30)
print(getTiming(1))

