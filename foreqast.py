
# include all the required libraries
# import flask module related package
from flask import Flask, render_template, url_for, redirect, request, jsonify, session, flash, json

# import ORM / DB related packages
from sqlalchemy import create_engine, Table, MetaData, select, insert, update, delete, and_, or_, func

# for .env variable
import os
from dotenv import load_dotenv

# initialize flask web app
app = Flask(__name__)
app.debug = True
app.secret_key = "foreqast"

@app.route('/', methods = ['GET'])
def landing():
	try:
		return render_template('/landing/index.html')
	except Exception as e:
		return 'OOPS !!!, failed to load the landing page ...'

# exec start i.e start application on port 5000 
if __name__ == '__main__':
	app.run(port = 5000)
