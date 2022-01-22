
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

		# get ba wise latest records
		get_load_data_latest_records_response = get_load_data_latest_records(data)
		return render_template('/landing/lord.html', bar_graph_data = data_response, get_load_data_latest_records_response = get_load_data_latest_records_response)
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

		# get latest few hours records
		data["ba_name"] = "ERCO"
		get_trade_data_latest_records_response = get_trade_data_latest_records(data)
		return render_template('/landing/power-market.html', bar_graph_data = data_response, get_trade_data_latest_records_response = get_trade_data_latest_records_response)
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

		# get the latest generation data log
		get_generation_data_latest_records_response = get_generation_data_latest_records(data)
		return render_template('/landing/priceforecast.html', bar_graph_data = data_response, get_generation_data_latest_records_response = get_generation_data_latest_records_response)
	except Exception as e:
		print(str(e))
		return 'OOPS !!!, failed to load the product - price page ...'
