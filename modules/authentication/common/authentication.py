
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

# common method for login user
def foreqast_login_info(data):
	response = {
		'status' : False,
		'message' : ''
	}
	try:
		# get the user by email ID
		select_user_query = select([
				db_table_foreqast_user.c.user_id,
				db_table_foreqast_user.c.email_id,
				db_table_foreqast_user.c.full_name,
				db_table_foreqast_user.c.password.label('existing_hash_password')
			]).select_from(
				db_table_foreqast_user
			).where(
				db_table_foreqast_user.c.email_id == data['user_email']
			)

		# execute the query
		select_query_result = app._engine.execute(select_user_query)
		user_count = select_query_result.rowcount
		if user_count == 0:
			response['status'] = False
			response['message'] = "This email is not registed into the system, please contact administrator ..."
			return response	
		if user_count == 1:
			response['message'] = "Unique user found in the system, carry forward the login process ..."
		elif user_count > 1:
			response['status'] = False
			response['message'] = "This email is registed multiple times in system, please contact administrator ..."
			return response
		else:
			response['status'] = False
			response['message'] = "No user found ..."
			return response

		# fetch the query result data
		system_data = select_query_result.fetchone()

		if sha256_crypt.verify(str(data['user_password']), system_data['existing_hash_password']):
			response['status'] = True
			response['data'] = system_data
			response['message'] = "Successfully logged in ..."
		else:
			response['status'] = False
			response['message'] = "Wrong password ..."
	except Exception as e:
		print(str(e))
		response['message'] = "Error while getting user details, please contact administrator ..."
	return response


# common method for getting all userd from the system
def foreqast_get_user_list_info():
	response = {
		'status' : False,
		'message' : '',
		'data' : []
	}
	try:
		# get the user by email ID
		select_user_query = select([
				db_table_foreqast_user.c.user_id,
				db_table_foreqast_user.c.email_id,
				db_table_foreqast_user.c.full_name,
			]).select_from(
				db_table_foreqast_user
			)

		# execute the query
		select_query_result = app._engine.execute(select_user_query)
		user_list = []
		for row in select_query_result:
			user_list.append(dict(row.items()))

		response['data'] = user_list
		response['message'] = "Successfully retrieved user list .."
		response['status'] = True
		return response
	except Exception as e:
		print(str(e))
		response['message'] = "Error while getting user list, please contact administrator ..."
	return response

