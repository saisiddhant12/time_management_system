import time
import datetime
import sqlite3
conn = sqlite3.connect('diary.db')
c = conn.cursor()
#c.execute('''CREATE TABLE engg (uid real, jobs text, jtime time)''')

uid = input("Enter Your Executive ID")
jobs = raw_input("Enter the important jobs")
yyyy = input("Enter the year\t")
mm = input("Enter the month\t")
dd = input("Enter the days\t")
hh = input("Enter the hour\t")
minutes = input("Enter the minutes")
jtime = str(datetime.datetime(yyyy, mm, dd, hh, minutes))

c.execute("INSERT INTO engg VALUES (?,?,?)",(uid,jobs,jtime))			
conn.commit()

for row in c.execute('SELECT * FROM engg '):																	#Displays the database
	print(row)
conn.close()