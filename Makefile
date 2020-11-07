dev:
	uvicorn main:app --reload --port 8001

lint: env/bin/flake8 # Lints code using flake8
	env/bin/flake8 *.py
