
# import code packaging related package
import sys
from shutil import copyfile
import os

# intgate all custom modules
def integrate_code_base():
	try:
		# integrate application build related files
		fin = open('modules/general/app_init.py', 'r')
		general_app_init = fin.read()

		# landing page related routing
		fin = open('modules/landing/web/landing.py', 'r')
		landing_web_landing = fin.read()

		fin = open('modules/load_data/common/load_data.py', 'r')
		load_data_common_load_data = fin.read()

		fin = open('modules/load_data/web/load_data.py', 'r')
		load_data_web_load_data = fin.read()

		fin = open('modules/trade_data/common/trade_data.py', 'r')
		trade_data_common_trade_data = fin.read()

		fin = open('modules/trade_data/web/trade_data.py', 'r')
		trade_data_web_trade_data = fin.read()

		fin = open('modules/generation_data/common/generation_data.py', 'r')
		generation_data_common_generation_data = fin.read()

		fin = open('modules/generation_data/web/generation_data.py', 'r')
		generation_data_web_generation_data = fin.read()

		fin = open('modules/general/app_run.py', 'r')
		general_app_run = fin.read()

		# integrated all files variables data into the one variable
		combined_file = general_app_init + landing_web_landing + load_data_web_load_data + load_data_common_load_data + trade_data_common_trade_data + trade_data_web_trade_data + generation_data_common_generation_data + generation_data_web_generation_data + general_app_run

		# write entire integrated files in final file
		fout = open('foreqast.py', 'w')
		fout.write(combined_file)
		fout.close()

		return True
	except Exception as e:
		print("Exception while integrating code base : ", str(e))
		return False

# call for the integrate code base
if __name__ == '__main__':
	integrate_code_base()
