dev:
	uvicorn main:app

lint: env/bin/flake8 # Lints code using flake8
	env/bin/flake8 *.py
