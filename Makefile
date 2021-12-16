help:
	echo "Run 'make pip' to install test requirements or 'make test' to test"

test: pip pytest_test linting_test

pip: pip_upgrade pip_requirements

pip_upgrade:
	python -m pip install --upgrade pip

pip_requirements:
	python -m pip install -U -r requirements-dev.txt

pytest_test:
	pytest --html=reports/unittests.html --self-contained-html --cov=file_type_guesser --cov-report html:reports/coverage tests/

linting_test:
	flake8 . --count --select=E9,F63,F7,F82 --show-source --statistics
	flake8 . --count --exit-zero --max-complexity=10 --max-line-length=100 --statistics

cc_test:
	flake8 . --count --select= --radon-max-cc 12 --radon-no-assert --show-source --statistics

radon_cc:
	radon cc file_type_guesser -a
