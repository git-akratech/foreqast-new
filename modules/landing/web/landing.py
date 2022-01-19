
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
