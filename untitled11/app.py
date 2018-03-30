from flask import Flask, render_template, session, request, redirect, url_for, jsonify
import sqlite3 as sql
import sqlite3
import sys
import model as dbHandler
import hashlib
from werkzeug.security import generate_password_hash, check_password_hash
import sqlite3

app = Flask(__name__)


     #   try:
     #       cursor.execute('INSERT INTO users (username, password) VALUES (?, ?)', (self.username, self.password))
     #   except:
     #       cursor.execute('CREATE TABLE users (, username TEXT, password TEXT)')
     #       raise UserNotFoundError('The table `users` did not exist, but it was created. Run the registration again.')
     #   finally:
     #       connection.commit()
     #       connection.close()

# @app.route('/login', methods=['POST'])
# def login_user():
#     username = request.form['username']
#     password = request.form['password']
#
#     user = (username)
#
#     if user and check_password_hash(user.password, password):
#         return jsonify(
#             {'message': 'Password is correct'})  # You'll want to return a token that verifies the user in the future
#     return jsonify({'error': 'User or password are incorrect'}), 401

# @app.route("/home")
# def index():
# 	return "Hello World"

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

@app.route("/home/")
def home():
	return "Hello World"

@app.route('/', methods=['GET', 'POST'])
def login():
    error = None
    a = []
    con = sql.connect("database.db")
    cur = con.cursor()
    cur.execute("SELECT username FROM Log")
    users = cur.fetchall()
    for user in users:
        a.append([user])

    cur.execute("SELECT password FROM Log")
    pas = cur.fetchall()



    if request.method == 'POST':
        if request.form['username'] == user:
            return redirect(url_for('home'))
        else:

            error = 'Invalid.Please try again'
    #     else:
    #         return redirect(url_for('home'))
    return render_template('login.html', error = error)


# @app.route("/home/")
# def home():
# 	return "Hello World"
#
# @app.route('/', methods=['GET', 'POST'])
# def login():
#     error = None
#     if request.method == 'POST':
#         if request.form['username'] != 'admin' or request.form['password'] != 'admin':
#             error = 'Invalid.Please try again'
#         else:
#             return redirect(url_for('home'))
#     return render_template('login.html', error = error)


if __name__ == '__main__':
    app.run(debug=True)