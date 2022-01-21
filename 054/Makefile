run: # run Flask server
	export FLASK_APP=hello.py &&\
	python3 -m flask run

run_%: # run Flask server
	export FLASK_APP=$*.py &&\
	python3 -m flask run
