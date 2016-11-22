import time
import datetime
import sqlite3


conn = sqlite3.connect('diary.db')
c = conn.cursor()
#c.execute('''CREATE TABLE executive (unid INTEGER PRIMARY KEY,name text,designation text, abs text)''')

no_of_exec = input("No of executives\t")																								 #enter the total number of executives

while(no_of_exec):
	no_of_exec = no_of_exec-1
	eid = input("Enter the eid of executives")																#enter the assigned UID to the executive   Enter 0 to directly view the table
	nam = raw_input("Enter the name of the executive")															#enter the name of the executive
	des = raw_input("Enter the mail ID")											
	c.execute("INSERT INTO executive (unid,name,designation) VALUES (?,?,?)",(eid,nam,des))												#Inserting credentials into database
	
	a = input("Enter 1 for taking a leave")

	if a == 1:
		yyyy = input("Enter the year\t")
		mm = input("Enter the month\t")
		dd = input("Enter the days\t")
		leave = str(datetime.datetime(yyyy, mm, dd))												#enter the leave date and duration
		c.execute("UPDATE executive SET abs=(?) WHERE unid = (?)",(leave,eid))
conn.commit()

#c.execute("DROP TABLE diary.db.executive")

for row in c.execute('SELECT * FROM executive '):																	#Displays the database
	print(row)
conn.close()