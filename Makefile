venv:
	python -m venv ./build

install:
	build/bin/python -m pip install --upgrade pip
	build/bin/python -m pip install -r requirements.txt
	build/bin/python -m pip install -e .

test: venv install
	build/bin/coverage run -m unittest discover
