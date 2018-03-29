from flask import Flask, render_template, session, request, redirect, url_for
import sqlite3 as sql
import sqlite3
app = Flask(__name__)
import sys
import model as dbHandler
import hashlib


# def check_password(hashed_password, user_password):
# 	return hashed_password == hashlib.md5(user_password.encode()).hexdigest()
#
#
# def validate(username, password):
#     con = sqlite3.connect('database.db')
#     completion = False
#     with con:x`x`
#                 cur = con.cursor()
#                 cur.execute("SELECT * FROM Log")
#                 rows = cur.fetchall()
#                 for row in rows:
#                     dbUser = row[0]
#                     dbPass = row[1]
#                     if dbUser==username:
#                         completion=check_password(dbPass, password)
# 		return completion


@app.route("/home")
def index():
	return "Hello World"

# @app.route('/', methods=['POST', 'GET'])
# def home():
# 	if request.method=='POST':
#    		username = request.form['username']
#    		password = request.form['password']
#    		dbHandler.insertUser(username, password)
#    		users = dbHandler.retrieveUsers()
# 		return render_template('index.html', users=users)
#    	else:
#    		return render_template('index.html')
#
# @app.route('/', methods=['POST', 'GET'])
# def home():
# 	if request.method == 'POST':

@app.route("/home/")
def home():
	return "Hello World"

@app.route('/login', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        if request.form['username'] != 'admin' or request.form['password'] != 'admin':
            error = 'Invalid.Please try again'
        else:
            return redirect(url_for('home'))
    return render_template('login.html', error = error)


if __name__ == '__main__':
    app.run(debug=True)