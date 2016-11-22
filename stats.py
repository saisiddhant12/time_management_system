import sqlite3

conn1 = sqlite3.connect('diary.db')
c = conn1.cursor()


a = input("Enter 1 for determining time spent by executive on a meeting, 2 for man-hours on a project & no of meetings per project")

if a == 1:
	exid = input("Enter the executive ID")
	c.execute("SELECT SUM(duration) from meets where uid=(?)",(exid,))
	data = c.fetchone()[0]
	print data

if a == 2:
	project = raw_input("Enter the project's name")
	c.execute("SELECT sum(duration) AS pduration from meets where purpose=(?)",(project,))										#man-hours
	data1 = c.fetchone()[0]
	print data1
	c.execute("SELECT COUNT(DISTINCT meet_id) from meets where purpose=(?)",(project,))											#no_of_meets
	data2 = c.fetchone()[0]
	print data2

conn1.close()