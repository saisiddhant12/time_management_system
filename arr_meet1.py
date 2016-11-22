import time
import datetime
import sqlite3
import smtplib
import getpass

server = smtplib.SMTP('smtp.gmail.com', 587)
server.starttls()

conn1 = sqlite3.connect('diary.db')
c = conn1.cursor()

#c.execute('''CREATE TABLE meets(meet_id real NOT NULL,uid real, venue text, strtime text, duration INT,endtime text,purpose text, mail text)''')	#creating the DB for meeting

meet_id= input("Enter the meet_id\t")
invitees = input("Enter the number of people invite\t")																	#Enter the total number of invitees
yyyy = input("Enter the year\t")
mm = input("Enter the month\t")
dd = input("Enter the days\t")
hh = input("Enter the hour\t")
minutes = input("Enter the minutes\t")
dip = raw_input("Enter start date in YYYY-MM-DD \t")
#dip1 = raw_input("Enter end date in YYYY-MM-DD \t")
duration =input("Enter the meeting hours\t")
venue = raw_input("Enter the venue\t")																			#Enter the venue of the meeting taking place
purpose = raw_input("Project on \t")
username = 'saipsiddhant@gmail.com'
password = 'findme123'
server.login(username, password)

while(invitees):
	invitees = invitees - 1
	uid = input("Enter the invitee's id\t")
	strtime = str(datetime.datetime(yyyy, mm, dd, hh, minutes))
	endtime = str(datetime.datetime(yyyy, mm, dd,hh+duration,minutes))
	#strtime = datetime.date(dip)
	#endtime = datetime.date(dip1)
	mail = raw_input("Enter the executive's mail ID\t")
	c.execute("INSERT INTO meets VALUES(?,?,?,(?),?,(?),?,?)",(meet_id,uid,venue,strtime,duration,endtime,purpose,mail))	
	print "Welcome Master\n"
	recepient = mail
	msg = "You have a meeting on "+dip+" at "+venue
	server.sendmail(username, recepient, msg)
conn1.commit()
server.quit()
for row in c.execute("SELECT * from meets"):
	print row
conn1.close()