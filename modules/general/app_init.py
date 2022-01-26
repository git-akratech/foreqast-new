
# include all the required libraries
# import flask module related package
from flask import Flask, render_template, url_for, redirect, request, jsonify, session, flash, json

# import ORM / DB related packages
from sqlalchemy import create_engine, Table, MetaData, select, insert, update, delete, and_, or_, func
from sqlalchemy.orm import sessionmaker

# date time related packages
from datetime import datetime, timedelta, date
import time
from time import strftime
from pytz import timezone

# import encryption and decryption related packages
from passlib.hash import sha256_crypt

import random
from random import choice

from string import ascii_uppercase, digits, ascii_lowercase

# import for reading files
import codecs

# import related to sendgrid emailing
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail

# for .env variable
import os
from dotenv import load_dotenv

# ENV variables here
load_dotenv()
DATABASE_USERNAME = os.environ.get("DATABASE_USERNAME")
DATABASE_PASSWORD = os.environ.get("DATABASE_PASSWORD")
DATABASE_HOSTNAME = os.environ.get("DATABASE_HOSTNAME")
DATABASE_NAME = os.environ.get("DATABASE_NAME")
SENDGRID_API_KEY = os.environ.get("SENDGRID_API_KEY")

def init_engine(app):
	app._engine = create_engine('mysql://' + DATABASE_USERNAME + ':' + DATABASE_PASSWORD + '@' + DATABASE_HOSTNAME + '/' + DATABASE_NAME, echo = False, pool_size = 50, max_overflow = 16, pool_recycle = 300)

# initialize flask web app
app = Flask(__name__)
app.debug = True
app.secret_key = "foreqast"

# call for the app engine
init_engine(app)
