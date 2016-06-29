#This is the blog.py controller

from flask import Flask, render_template, request, session, flash, redirect, url_for, g
import sqlite3
from functools import wraps
#Let's config the database.

DATABASE = 'blog.db'
USERNAME = 'admin'
PASSWORD = 'admin'
SECRET_KEY= 'bxd9+x08uxfxb7xbdx92hbxd2I~xbdx91xe4xd1xf4b4xxe6Nxbb'

#This is where the magic happens V

app = Flask(__name__)

app.config["DEBUG"] = True

app.config.from_object(__name__)

#Connects to database
def connect_db():
	return sqlite3.connect(app.config['DATABASE'])

#Makes the user aware that you HAVE to login
def login_required(test):
	@wraps(test)
	def wrap(*args, **kwargs):
		if 'logged_in' in session:
			return test(*args, **kwargs)
		else: 
			flash("You need to login first!")
			return redirect(url_for('login'))
	return wrap

#routes to the login page and checks if credentials are right
@app.route('/', methods=['GET', 'POST'])
def login():
	error = None
	if request.method == 'POST':
		if request.form['username'] != app.config['USERNAME'] or \
		       request.form['password'] != app.config['PASSWORD']:
		       error = 'Invalid Credentials. Please try again'
		else:
		   	session['logged_in'] = True 
		   	return redirect(url_for('main'))
	return render_template('login.html', error=error)

@app.route('/main')
@login_required
def main():
	return render_template('main.html')

#routes to the logout page and gives the user a message
@app.route('/logout')
def logout():
	session.pop('logged_in', None)
	flash('You were logged out!')
	return redirect(url_for('login'))

#Initiates the website in DEBUGGER mode
if __name__ == "__main__" :
	app.run()