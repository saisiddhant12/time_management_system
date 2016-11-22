import sqlite3
import datetime
import time
import smtplib
import getpass

server = smtplib.SMTP('smtp.gmail.com', 587)
server.starttls()
username = 'saipsiddhant@gmail.com'
password = 'findme123'
server.login(username, password)
conn =  sqlite3.connect("diary.db")
c = conn.cursor()
exid = input("Enter the id you want to update\t")
yyyy = input("Enter the year\t")
mm = input("Enter the month\t")
dd = input("Enter the days\t")
hh = input("Enter the hour\t")
minutes = input("Enter the minutes\t")
str1 = str(datetime.datetime(yyyy, mm, dd, hh, minutes))
#str1 = raw_input("Enter start date in YYYY-MM-DD \t")
duration1 = input("Enter the revised duration\t")
endtime1 = str(datetime.datetime(yyyy, mm, dd, hh+duration1, minutes))
c.execute("UPDATE meets SET strtime=(?), endtime = (?) WHERE meet_id= (?)",(str1,endtime1,exid))
conn.commit()

z = c.execute('SELECT * from meets WHERE meet_id = (?)',(exid,))
for row in z:
	print row
	receiver = row[7].strip('u')
	msg = "Your meet is updated to "+row[3].strip('u')+" at "+row[2].strip('u')
	server.sendmail(username, receiver, msg)
server.quit()
conn.close()