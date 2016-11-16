import time
import datetime
import sqlite3

conn1 = sqlite3.connect('diary.db')
c = conn1.cursor()
c.execute('''CREATE TABLE meets(meet_id real PRIMARY KEY NOT NULL, venue text, srttime text, duration real,purpose text)''')	#creating the DB for meeting
c.execute('''CREATE TABLE invited(meet_id real, uid real,duration real)''')
invitees = input("Enter the number of people invite\t")																								#Enter the total number of invitees
meet_id= input("Enter the meet_id\t")
venue = raw_input("Enter the venue")																								#Enter the venue of the meeting taking place
#dip = str(raw_input('date'))
yyyy = input("Enter the year\t")
mm = input("Enter the month\t")
dd = input("Enter the days\t")
hh = input("Enter the hour\t")
minutes = input("Enter the minutes\t")
strtime = str(datetime.datetime(yyyy, mm, dd, hh, minutes))
duration =input()
purpose = raw_input()
c.execute("INSERT INTO meets VALUES(?,?,?,?,?)",(meet_id,venue,strtime,duration,purpose))
#c.execute("DROP TABLE diary.db.meets")
#c.execute("DROP TABLE diary.db.invited")
while(invitees):
	invitees = invitees-1
	iid = input("Enter the participating executive's id\t")																				#Enter the invitee's ids giving space 1 by 1
	c.execute("INSERT INTO invited VALUES(?,?,?)",(meet_id,iid,duration))
for i in c.execute('SELECT designation FROM executive JOIN invited WHERE uid = unid'):
	print i
#def check_availability():
#	for i in strtime:
#		if(i!=NULL):
#			print "Appology Exec Not available"
