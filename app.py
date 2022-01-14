# import flask module related package
from flask import Flask, render_template, url_for, redirect, request, jsonify, session, flash, json

# initialize flask web app
app = Flask(__name__)
app.debug = True
app.secret_key = "akra-tech"


@app.route('/')
def index():
	return render_template('index.html')

@app.route('/login')
def login():
	return render_template('log-in.html')

@app.route('/sign_up')
def sign_up():
	return "Coming up ..."


# exec start i.e start application on port 5000 
if __name__ == '__main__':
	app.run(port = 5000)