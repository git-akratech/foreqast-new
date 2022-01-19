
@app.route('/', methods = ['GET'])
def landing():
	try:
		return render_template('/landing/index.html')
	except Exception as e:
		return 'OOPS !!!, failed to load the landing page ...'
