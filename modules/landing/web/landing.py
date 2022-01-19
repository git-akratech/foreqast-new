
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
