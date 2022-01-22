run: # run Flask server
	export FLASK_APP=hello.py &&\
	export FLASK_ENV=development &&\
	export FLASK_DEBUG=1 &&\
	python3 -m flask run

run_%: # run Flask server
	export FLASK_APP=$*.py &&\
	export FLASK_ENV=development &&\
	export FLASK_DEBUG=1 &&\
	python3 -m flask run
