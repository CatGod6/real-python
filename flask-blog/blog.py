from flask import Flask, render_template, request, session, flash, redirect, url_for, g
import sqlite3

#Let's config the database.

DATABASE = 'blog.db'

app = Flask(__name__)

app.config.from_object(__name__)

def connect_db():
	return sqlite3.connect(app.config["DATABASE"])

if __name__ == "__name__" :
	app.run(debug==True)