
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

# get the trade data for latest records
def get_trade_data_latest_records(data):
	response = {"status" : False, "message" : "", "data" : {}}
	try:
		# get the object data
		ba_name = data['ba_name']

		# select data query
		data_list = []
		select_query = "select date_format(`timestamp`, '%%Y-%%m-%%d %%H:%%m') as running_date, round(net_exp_MW, 2) as trade_data, ba_name from foreqast_trade_data group by ba_name, date_format(`timestamp`, '%%Y-%%m-%%d %%H:%%m') having ba_name = '{ba_name}' order by running_date desc limit 0, 24".format(ba_name = ba_name)

		# execute the query
		trade_result = app._engine.execute(select_query)

		# check for the result
		if trade_result.rowcount > 0:
			for row in trade_result:
				data_list.append(dict(row.items()))
			response['status'] = True
			response['data'] = data_list
		else:
			response['message'] = "For this filter, no data available ..."

		# return common response
		return response
	except Exception as e:
		print(str(e))
		response["message"] = "Error while getting latest trade data ..."
		return response
