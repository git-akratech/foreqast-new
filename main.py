

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

		fin = open('modules/general/app_run.py', 'r')
		general_app_run = fin.read()

		# integrated all files variables data into the one variable
		combined_file = general_app_init + landing_web_landing + load_data_common_load_data + general_app_run

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
