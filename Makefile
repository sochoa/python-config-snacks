venv:
	python -m venv ./build

install:
	build/bin/python -m pip install --upgrade pip
	build/bin/python -m pip install -r requirements.txt
	build/bin/python -m pip install -e .

lint:
	build/bin/pylint -E config_snacks

test: venv install lint
	build/bin/coverage run -m unittest discover
	build/bin/coverage report -m
