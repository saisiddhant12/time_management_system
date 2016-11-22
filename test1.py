import sqlite3
import datetime
import time

u = []
conn1 = sqlite3.connect('diary.db')
c = conn1.cursor()

time = raw_input("Enter time to be searched in YYYY-MM-DD HH:MM:SS format")
z = c.execute('SELECT * FROM meets WHERE strtime = (?)',(time,))
for row in z:
	u.append(row[1])

l = len(u)	
for i in range(l):
	print "No common slot: Employee No: ",u[i],"is not available for the day"