
# include all the required libraries
# import flask module related package
from flask import Flask, render_template, url_for, redirect, request, jsonify, session, flash, json

# import ORM / DB related packages
from sqlalchemy import create_engine, Table, MetaData, select, insert, update, delete, and_, or_, func

# for .env variable
import os
from dotenv import load_dotenv

# ENV variables here
DATABASE_USERNAME = "admin"
DATABASE_PASSWORD = "%Monday123%"
DATABASE_HOSTNAME = "database-1.c8uq1bsrptts.ap-south-1.rds.amazonaws.com"
DATABASE_NAME = "akra_scraper"

def init_engine(app):
	app._engine = create_engine('mysql://' + DATABASE_USERNAME + ':' + DATABASE_PASSWORD + '@' + DATABASE_HOSTNAME + '/' + DATABASE_NAME, echo = False, pool_size = 50, max_overflow = 16, pool_recycle = 300)

# initialize flask web app
app = Flask(__name__)
app.debug = True
app.secret_key = "foreqast"

# call for the app engine
init_engine(app)
