
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

# Handle landing page routing
@app.route('/', methods = ['GET'])
def landing():
	try:
		return render_template('/landing/index.html')
	except Exception as e:
		print(str(e))
		return 'OOPS !!!, failed to load the landing page ...'

# Handle login page routing
@app.route('/foreqast_login', methods = ['GET'])
def foreqast_login():
	try:
		return render_template('/landing/log-in.html')
	except Exception as e:
		print(str(e))
		return 'OOPS !!!, failed to load the login page ...'

# handling signup page routing
@app.route('/foreqast_sign_up', methods = ['GET'])
def foreqast_sign_up():
	try:
		return render_template('/landing/sign-up.html')
	except Exception as e:
		print(str(e))
		return 'OOPS !!!, failed to load the sign-up page ...'

# handle artical details page routing
@app.route('/foreqast_article_detail', methods = ['GET'])
def foreqast_article_detail():
	try:
		return render_template('/landing/article-details.html')
	except Exception as e:
		print(str(e))
		return 'OOPS !!!, failed to load the artical detail page ...'

# handle terms and conditions page routing
@app.route('/foreqast_terms_and_conditions', methods = ['GET'])
def foreqast_terms_and_conditions():
	try:
		return render_template('/landing/terms-conditions.html')
	except Exception as e:
		print(str(e))
		return 'OOPS !!!, failed to load the terms and conditions page ...'

# handle privacy policy page routing
@app.route('/foreqast_privacy_policy', methods = ['GET'])
def foreqast_privacy_policy():
	try:
		return render_template('/landing/privacy-policy.html')
	except Exception as e:
		print(str(e))
		return 'OOPS !!!, failed to load the privacy policy page ...'

# handle foreqast product load render page
@app.route('/foreqast_load', methods = ['GET']) 
def foreqast_load():
	try:
		# get initial load data from loading the graph
		data = {
			"from_date" : "2021-12-22",
			"to_date" : "2022-01-10",
			"ba_name" : "PJM"
		}
		data_response = get_load_data_by_avg_with_date_range(data)
		return render_template('/landing/lord.html', bar_graph_data = data_response)
	except Exception as e:
		print(str(e))
		return 'OOPS !!!, failed to load the product - load page ...'

# handle foreqast power market render page
@app.route('/foreqast_power_market', methods = ['GET']) 
def foreqast_power_market():
	try:
		# get initial trade data from loading the graph
		data = {
			"from_date" : "2021-12-22",
			"to_date" : "2022-01-10",
			"ba_name" : "PJM"
		}
		data_response = get_trade_data_by_avg_with_date_range(data)
		return render_template('/landing/power-market.html', bar_graph_data = data_response)
	except Exception as e:
		print(str(e))
		return 'OOPS !!!, failed to load the product - power page ...'

# handle foreqast product power render page
@app.route('/foreqast_price', methods = ['GET']) 
def foreqast_price():
	try:
		# get initial generation data from loading the graph
		data = {
			"from_date" : "2021-12-22",
			"to_date" : "2022-01-10",
			"ba_name" : "PJM"
		}
		data_response = get_generation_data_by_avg_with_date_range(data)
		return render_template('/landing/priceforecast.html', bar_graph_data = data_response)
	except Exception as e:
		print(str(e))
		return 'OOPS !!!, failed to load the product - price page ...'

# get the load data for ba and date range filter
@app.route('/get_ba_wise_avg_load_data_for_date_range', methods = ['POST'])
def get_ba_wise_avg_load_data_for_date_range():
	response = {"status" : False, "message" : "", "data" : {}}
	try:
		# get the request data
		data = request.get_json()[0]

		# extract and validate the data
		ba_name = data['ba_name']
		from_date = data['from_date']
		to_date = data['to_date']

		# create request data object
		request_data = {
			"ba_name" : ba_name,
			"from_date" : from_date,
			"to_date" : to_date
		}

		#call to the common method
		response = get_load_data_by_avg_with_date_range(request_data)

		# return the response
		return jsonify(response)
	except Exception as e:
		print(str(e))
		response["message"] = "Error while getting avg load data ..."
		return jsonify(response)
# create ORM table
sql_metadata = MetaData()
db_table_foreqast_load_data = Table('foreqast_load_data', sql_metadata, autoload = True, autoload_with = app._engine)

# get the load data from date range with avg data
def get_load_data_by_avg_with_date_range(data):
	response = {"status" : False, "message" : "", "data" : {}}
	try:
		# get the object data
		from_date = data['from_date']
		to_date = data['to_date']
		ba_name = data['ba_name']

		# select data query
		data_list = []
		select_query = "select date_format(`timestamp`, '%%Y-%%m-%%d') as running_date, round(avg(load_MW), 2) as load_data, ba_name from foreqast_load_data group by ba_name, date_format(`timestamp`, '%%Y-%%m-%%d') having ba_name = '{ba_name}' and running_date between '{from_date}' and '{to_date}'".format(ba_name = ba_name, from_date = from_date, to_date = to_date)

		# execute the query
		load_result = app._engine.execute(select_query)

		# check for the result
		if load_result.rowcount > 0:
			for row in load_result:
				data_list.append(dict(row.items()))
			response['status'] = True
			response['data'] = data_list
		else:
			response['message'] = "For this filter, no data available ..."

		# return common response
		return response
	except Exception as e:
		print(str(e))
		response["message"] = "Error while getting avg load data ..."
		return response


# create ORM table
sql_metadata = MetaData()
db_table_foreqast_load_data = Table('foreqast_trade_data', sql_metadata, autoload = True, autoload_with = app._engine)

# get the load data from date range with avg data
def get_trade_data_by_avg_with_date_range(data):
	response = {"status" : False, "message" : "", "data" : {}}
	try:
		# get the object data
		from_date = data['from_date']
		to_date = data['to_date']
		ba_name = data['ba_name']

		# select data query
		data_list = []
		select_query = "select date_format(`timestamp`, '%%Y-%%m-%%d') as running_date, round(avg(net_exp_MW), 2) as trade_data, ba_name from foreqast_trade_data group by ba_name, date_format(`timestamp`, '%%Y-%%m-%%d') having ba_name = '{ba_name}' and running_date between '{from_date}' and '{to_date}'".format(ba_name = ba_name, from_date = from_date, to_date = to_date)

		# execute the query
		load_result = app._engine.execute(select_query)

		# check for the result
		if load_result.rowcount > 0:
			for row in load_result:
				data_list.append(dict(row.items()))
			response['status'] = True
			response['data'] = data_list
		else:
			response['message'] = "For this filter, no data available ..."

		# return common response
		return response
	except Exception as e:
		print(str(e))
		response["message"] = "Error while getting avg trade data ..."
		return response

# get the trade data for ba and date range filter
@app.route('/get_ba_wise_avg_trade_data_for_date_range', methods = ['POST'])
def get_ba_wise_avg_trade_data_for_date_range():
	response = {"status" : False, "message" : "", "data" : {}}
	try:
		# get the request data
		data = request.get_json()[0]

		# extract and validate the data
		ba_name = data['ba_name']
		from_date = data['from_date']
		to_date = data['to_date']

		# create request data object
		request_data = {
			"ba_name" : ba_name,
			"from_date" : from_date,
			"to_date" : to_date
		}

		#call to the common method
		response = get_trade_data_by_avg_with_date_range(request_data)

		# return the response
		return jsonify(response)
	except Exception as e:
		print(str(e))
		response["message"] = "Error while getting avg trade data ..."
		return jsonify(response)

# create ORM table
sql_metadata = MetaData()
db_table_foreqast_load_data = Table('foreqast_generation_data', sql_metadata, autoload = True, autoload_with = app._engine)

# get the load data from date range with avg data
def get_generation_data_by_avg_with_date_range(data):
	response = {"status" : False, "message" : "", "data" : {}}
	try:
		# get the object data
		from_date = data['from_date']
		to_date = data['to_date']
		ba_name = data['ba_name']

		# select data query
		data_list = []
		select_query = "select date_format(`timestamp`, '%%Y-%%m-%%d') as running_date, round(avg(gen_MW), 2) as generation_data, ba_name from foreqast_generation_data group by ba_name, date_format(`timestamp`, '%%Y-%%m-%%d') having ba_name = '{ba_name}' and running_date between '{from_date}' and '{to_date}'".format(ba_name = ba_name, from_date = from_date, to_date = to_date)

		# execute the query
		load_result = app._engine.execute(select_query)

		# check for the result
		if load_result.rowcount > 0:
			for row in load_result:
				data_list.append(dict(row.items()))
			response['status'] = True
			response['data'] = data_list
		else:
			response['message'] = "For this filter, no data available ..."

		# return common response
		return response
	except Exception as e:
		print(str(e))
		response["message"] = "Error while getting avg generation data ..."
		return response


# get the generation data for ba and date range filter
@app.route('/get_ba_wise_avg_generation_data_for_date_range', methods = ['POST'])
def get_ba_wise_avg_generation_data_for_date_range():
	response = {"status" : False, "message" : "", "data" : {}}
	try:
		# get the request data
		data = request.get_json()[0]

		# extract and validate the data
		ba_name = data['ba_name']
		from_date = data['from_date']
		to_date = data['to_date']

		# create request data object
		request_data = {
			"ba_name" : ba_name,
			"from_date" : from_date,
			"to_date" : to_date
		}

		#call to the common method
		response = get_generation_data_by_avg_with_date_range(request_data)

		# return the response
		return jsonify(response)
	except Exception as e:
		print(str(e))
		response["message"] = "Error while getting avg generation data ..."
		return jsonify(response)

# exec start i.e start application on port 5000 
if __name__ == '__main__':
	app.run(port = 5000)
