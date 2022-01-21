
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
