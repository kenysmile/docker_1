
import sqlite3 as sql



#
def insertUser(username,password):
    con = sql.connect("database.db")
    cur = con.cursor()
    cur.execute("INSERT INTO Log (username,password) VALUES (?,?)", (username,password))
    con.commit()
    con.close()

def retrieveUsers(x):
	con = sql.connect("database.db")
	cur = con.cursor()
	cur.execute("SELECT username, password FROM Log")
	users = cur.fetchall()
	con.close()
	return users

#
# def search(username, password):
# 	con = sql.connect("database.db")
# 	cur = con.cursor()
# 	cur.execute("SELECT username FROM Log WHERE username=? AND password=?", (username,password))
# 	con.commit()
# 	con.close()
	# rows = cur.fetchall()
	# for row in rows:
	# 	print(row)

#
# #print(insertUser('tuan', 'ntt'))
# print(retrieveUsers())

