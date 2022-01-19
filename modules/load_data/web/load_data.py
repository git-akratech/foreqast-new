
# get the load data for last 15 days ba_wise
@app.route('/get_ba_wise_load_data_for_last_15_days', methods = ['POST'])
def get_ba_wise_load_data_for_last_15_days():
	response = {"status" : False, "message" : "", "data" : {}}
	try:
		# get the request data
		data = request.get_json()[0]
		ba_name = data['ba_name']

		# select data query
		data_list = []
		select_query = "select date_format(`timestamp`, '%%Y-%%m-%%d') as running_date, round(avg(load_MW), 2) as load_data, ba_name from foreqast_load_data group by date_format(`timestamp`, '%%Y-%%m-%%d') having ba_name = '{ba_name}' and running_date between '2021-12-27' and '2022-01-10'".format(ba_name = ba_name)

		result = app._engine.execute(select_query)
		
		if result.rowcount > 0:
			for row in result:
				data_list.append(dict(row.items()))
			response['status'] = True
			response['data'] = data_list
		else:
			response['message'] = "For this filter, no data available ..."

		# return common response
		return jsonify(response)
	except Exception as e:
		print(str(e))
		response["message"] = "Error while getting avg load data ..."
		return jsonify(response)