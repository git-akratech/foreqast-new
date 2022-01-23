
# create orm access for the foreqast_user table
sql_metadata = MetaData()
db_table_foreqast_user = Table('foreqast_user', sql_metadata, autoload = True, autoload_with = app._engine)

# common method for signup i.e add new user into the system
def foreqast_sign_up_info(request_data):
	response = {"status" : False, "message" : ""}
	try:
		# dump the data using engine
		add_new_user_query = insert(
				db_table_foreqast_user
			).values(
				request_data
			)

		# execute the query
		insert_query_result = app._engine.execute(add_new_user_query)

		response['status'] = True
		response['message'] = "Successfully added new user ..."
		return response
	except Exception as e:
		print(str(e))
		response["message"] = "Unable to create new account, please contact administrator ..."
		return response
