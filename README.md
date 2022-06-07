# ForeQast -> this setup is on aws with ubuntu 18.04 LTS system

# Create python virtual envirnoment
	>> sudo apt install python3-venv
	>> python3 -m venv venv_foreqast

# For MySQL client use below commands
	>> sudo apt-get install python3-dev default-libmysqlclient-dev build-essential

# Activate virtual envirnoment
	>> source venv_foreqast/bin/activate

# Deactivate virtual envirnoment
	>> deactivate

# Clone codebase - github repository
	>> git clone https://github.com/git-akratech/foreqast-new.git 

# Install requirements.txt via activating virtual envirnoment
	>> source venv_foreqast/bin/activate
	# Goto soruce directory 
		>> cd foreqast-new/
	>> pip3 install -r requirements.txt

# Create .env file and update envirnoment specific key
	>> touch .env
	>> nano .env

# Build the application server
	>> python3 main.py

# Cross check application is running or not
	>> python3 foreqast.py

# Finally run the server using nohup deamon
	>> nohup python3 foreqast.py &

# For checking log
	>> cat nohup.out
	>> tail -f nohup.out
