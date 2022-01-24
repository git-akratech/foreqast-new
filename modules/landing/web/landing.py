
# Handle landing page routing
@app.route('/', methods = ['GET'])
def landing():
	try:
		return render_template('/landing/index.html')
	except Exception as e:
		print(str(e))
		return 'OOPS !!!, failed to load the landing page ...'

# Handle login page routing
@app.route('/foreqast_login', methods = ['GET','POST'])
def foreqast_login():
	try:
		if request.method == "GET":
			return render_template('/landing/log-in.html')
		elif request.method == "POST":
			# get the request data and convert into the requred format
			# get the request data
			data = request.form.to_dict()

			# pass to the common method
			login_user_response = foreqast_login_info(data)
			if login_user_response['status']:
				# create a DB session connection
				Session = sessionmaker(bind = app._engine)
				application_session = Session()

				# create a flask app session
				session['logged_in'] = True
				session['user_id'] = login_user_response['data']['user_id']
				session['full_name'] = login_user_response['data']['full_name']
				session['email_id'] = login_user_response['data']['email_id']

				# on successful login create a user session and nevigate to the dashboard page
				return  redirect(url_for('landing_login'))
			else:
				flash(login_user_response['message'], 'error')
				return redirect(url_for('foreqast_login'))
	except Exception as e:
		print(str(e))
		return 'OOPS !!!, failed to load the login page ...'

@app.route('/landing_login')
def landing_login():
	if 'logged_in' in session and session['logged_in'] == True:
		user_list = foreqast_get_user_list_info()['data']
		return render_template('admin/users.html', user_list = user_list)
	else:
		flash("Your session had been expired, please login again ...", 'error')
		return redirect(url_for('foreqast_login'))

# handling signup page routing
@app.route('/foreqast_sign_up', methods = ['GET', 'POST'])
def foreqast_sign_up():
	try:
		if request.method == "GET":
			return render_template('/landing/sign-up.html')
		elif request.method == "POST":
			# prepare data for adding new user into the system

			# get teh request data and convert it into the dict
			data = request.form.to_dict()

			#prepare request data
			request_data = {}

			# generate hash password
			hash_password = sha256_crypt.hash(str(data['user_password']))

			# generate random user id
			request_data['user_id'] = ''.join(choice(ascii_uppercase) for i in range(3)) + ''.join(choice(digits) for i in range(4))
			request_data['full_name'] = str(data['user_name']).strip()
			request_data['email_id'] = str(data['user_email']).strip()
			request_data['password'] = hash_password
			# mysql default date format
			request_data['registered_on'] = datetime.now(timezone('Asia/Kolkata')).strftime('%Y-%m-%d %H:%M')

			# pass request data object to the common method
			response = foreqast_sign_up_info(request_data)
			if response['status']:
				flash(response["message"], "success")
			else:
				flash(response["message"], "error")

			return redirect(url_for('foreqast_login'))
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

@app.route('/foreqast_user_logout')
def foreqast_user_logout():
	try:
		# clear all session vaiable
		session['logged_in'] = False
		session.clear()
		flash("Successfully logged out ...", "success")
		return redirect(url_for('foreqast_login'))
	except Exception as e:
		print(str(e))
		flash("Falied to logout, please contact administrator ...", "error")
		return redirect(url_for('foreqast_login'))
