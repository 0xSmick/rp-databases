import random
import sqlite3

conn = sqlite3.connect("num.db")
c = conn.cursor()

c.execute("DROP TABLE if exists numbers")
c.execute("CREATE TABLE numbers(num int)")

for i in range(100):
	c.execute("INSERT INTO numbers VALUES(?)",(random.randint(0,100),))


while True:
	x = raw_input("Pick 1:avg, 2:max, 3:min, 4:sum 5:exit")

	if x in set(["1","2","3","4"]):
		operation = {1: "avg", 2:"max", 3:"min", 4:"sum"}[int(x)]
		c.execute("SELECT {}(num) from numbers".format(operation))

		get = c.fetchone()

		print operation + ": %f" % get[0]

	elif x == "5":
		print "Exit"
		break



