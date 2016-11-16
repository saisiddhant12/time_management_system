import sqlite3

conn1 = sqlite3.connect('diary.db')
c = conn1.cursor()


a = input("Enter 1 for determining time spent by executive on a meeting, 2 for purpose duration and number of meetings")

if a == 1:
	exid = input("Enter the executive ID")
	c.execute("SELECT SUM(duration) AS total_duration from diary.db.invited where uid=exid")

if a == 2:
	project = raw_input("Enter the project's name")
	c.execute("SELECT sum(duration) AS pduration from diary.db.meets ")