MAIN=./src/imgcipher_interface.py

.ONESHELL:

.PHONY: install clean run
install:
	python -m venv env
	source ./env/bin/activate
	pip install -r requirements.txt

run:
	source ./env/bin/activate
	python $(MAIN)

clean:
	rm -rf env __pycache__
